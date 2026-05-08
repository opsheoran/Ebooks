/**
 * ── PROFESSIONAL TEACHER'S CANVAS ──
 * High-DPI, Ultra-Smooth Ink, Notebook Paper, Rich Tools, and Resize-Safe.
 */

(function() {
    // 1. Setup HTML
    const popupHTML = `
        <div id="whiteboard-popup" class="whiteboard-popup">
            <div class="popup-header" id="popup-drag-handle">
                <h3><i class="fas fa-file-signature"></i> Teacher's Pro Canvas</h3>
                <button class="popup-close" id="popup-close-btn"><i class="fas fa-times"></i></button>
            </div>

            <div class="popup-canvas-container" id="popup-canvas-wrap">
                <canvas id="popup-canvas"></canvas>
                <textarea id="text-input-overlay" spellcheck="false" placeholder="Type here..."></textarea>
            </div>

            <div class="popup-toolbar">
                <button class="popup-tool-btn active" data-tool="pen" title="Pen (P)"><i class="fas fa-pen-nib"></i></button>
                <button class="popup-tool-btn" data-tool="highlighter" title="Highlighter (H)"><i class="fas fa-highlighter"></i></button>
                <button class="popup-tool-btn" data-tool="eraser" title="Eraser (E)"><i class="fas fa-eraser"></i></button>
                
                <div class="toolbar-divider"></div>
                
                <button class="popup-tool-btn" data-tool="line" title="Straight Line"><i class="fas fa-slash"></i></button>
                <button class="popup-tool-btn" data-tool="rect" title="Rectangle"><i class="far fa-square"></i></button>
                <button class="popup-tool-btn" data-tool="circle" title="Circle"><i class="far fa-circle"></i></button>
                <button class="popup-tool-btn" data-tool="text" title="Text Input"><i class="fas fa-font"></i></button>

                <div class="toolbar-divider"></div>

                <div class="popup-color-dot active" style="background: #000000;" data-color="#000000"></div>
                <div class="popup-color-dot" style="background: #1B2A4A;" data-color="#1B2A4A"></div> <!-- Navy -->
                <div class="popup-color-dot" style="background: #9B2335;" data-color="#9B2335"></div> <!-- Red -->
                <div class="popup-color-dot" style="background: #3D6B5A;" data-color="#3D6B5A"></div> <!-- Green -->
                <div class="popup-color-dot" style="background: #C8922A;" data-color="#C8922A"></div> <!-- Gold -->

                <div class="toolbar-divider"></div>

                <span style="font-size: 0.9rem; color: #1B2A4A; font-weight: 600;">Size</span>
                <input type="range" min="1" max="40" value="3" class="popup-size-slider" id="pop-size">

                <button class="popup-tool-btn" id="pop-undo" title="Undo (Ctrl+Z)" style="margin-left:auto;"><i class="fas fa-undo"></i></button>
                <button class="popup-tool-btn" id="pop-clear" title="Clear Board" style="color: #9B2335;"><i class="fas fa-trash-restore"></i></button>
                <button class="popup-tool-btn" id="pop-save" title="Save as PNG" style="background:#2E4270; color:#fff; border:none;">
                    <i class="fas fa-save"></i>
                </button>
            </div>
        </div>
    `;

    document.body.insertAdjacentHTML('beforeend', popupHTML);

    // 2. Elements & State
    const popup = document.getElementById('whiteboard-popup');
    const canvas = document.getElementById('popup-canvas');
    // Requesting desynchronized for lower latency ink
    const ctx = canvas.getContext('2d', { alpha: true });
    const container = document.getElementById('popup-canvas-wrap');
    const dragHandle = document.getElementById('popup-drag-handle');
    const textOverlay = document.getElementById('text-input-overlay');

    let currentTool = 'pen';
    let currentColor = '#000000';
    let currentSize = 3;
    let isDrawing = false;
    let dpr = window.devicePixelRatio || 1;

    // History for Undo
    let history = [];
    const MAX_HISTORY = 20;

    // Drawing state
    let startX = 0, startY = 0;
    let lastX = 0, lastY = 0;
    let points = [];
    let savedImageData = null; // Used for shape preview

    // 3. High-DPI Canvas Init & Resizing
    function initCanvas() {
        resizeCanvas();
        saveState(); // Initial blank state
    }

    function resizeCanvas() {
        const rect = container.getBoundingClientRect();
        
        // Save current ink before resize
        let tempCanvas = document.createElement('canvas');
        tempCanvas.width = canvas.width;
        tempCanvas.height = canvas.height;
        let tCtx = tempCanvas.getContext('2d');
        if (canvas.width > 0 && canvas.height > 0) {
            tCtx.drawImage(canvas, 0, 0);
        }

        // Scale canvas for sharp ink
        canvas.width = rect.width * dpr;
        canvas.height = rect.height * dpr;
        canvas.style.width = rect.width + 'px';
        canvas.style.height = rect.height + 'px';

        ctx.scale(dpr, dpr);
        ctx.lineJoin = 'round';
        ctx.lineCap = 'round';

        // Restore ink
        ctx.save();
        ctx.setTransform(1, 0, 0, 1, 0, 0);
        ctx.drawImage(tempCanvas, 0, 0);
        ctx.restore();
    }

    // Professional Resizer using ResizeObserver
    const resizeObserver = new ResizeObserver(() => {
        if (popup.style.display === 'flex' || popup.classList.contains('active')) {
            resizeCanvas();
        }
    });
    resizeObserver.observe(container);

    function applyBrush(isTempShape = false) {
        ctx.lineJoin = 'round';
        ctx.lineCap = 'round';

        if (currentTool === 'eraser') {
            ctx.globalCompositeOperation = 'destination-out';
            ctx.strokeStyle = "rgba(0,0,0,1)";
            ctx.lineWidth = currentSize * 8; 
        } else if (currentTool === 'highlighter') {
            ctx.globalCompositeOperation = 'source-over';
            // Convert hex to rgba for highlighter
            let hex = currentColor;
            let r = parseInt(hex.slice(1,3), 16), g = parseInt(hex.slice(3,5), 16), b = parseInt(hex.slice(5,7), 16);
            // If doing temp shape preview, don't stack opacity by drawing over and over,
            // Actually, highlighter over shapes is tricky. We'll use low opacity.
            ctx.strokeStyle = `rgba(${r},${g},${b},0.3)`;
            ctx.fillStyle = `rgba(${r},${g},${b},0.3)`;
            ctx.lineWidth = currentSize * 6;
            ctx.lineCap = 'butt'; // Flat ends for highlighter
        } else {
            ctx.globalCompositeOperation = 'source-over';
            ctx.strokeStyle = currentColor;
            ctx.fillStyle = currentColor;
            ctx.lineWidth = currentSize;
        }
    }

    function getPos(e) {
        const rect = canvas.getBoundingClientRect();
        return {
            x: e.clientX - rect.left,
            y: e.clientY - rect.top
        };
    }

    // 4. Input Events (Pointer Events for Zero Delay)
    canvas.addEventListener('pointerdown', (e) => {
        if (e.button !== 0 && e.button !== 5) return; // Only left click or pen tip/eraser
        isDrawing = true;
        canvas.setPointerCapture(e.pointerId);

        const pos = getPos(e);
        startX = pos.x;
        startY = pos.y;
        lastX = pos.x;
        lastY = pos.y;

        // Auto-switch to eraser if pen button is pressed
        if (e.pointerType === 'pen' && e.button === 5) {
            let oldTool = currentTool;
            currentTool = 'eraser';
            applyBrush();
            // Store old tool to revert on pointerup
            canvas.dataset.revertTool = oldTool;
        } else {
            applyBrush();
        }

        if (currentTool === 'pen' || currentTool === 'eraser' || currentTool === 'highlighter') {
            points = [{x: startX, y: startY}];
            ctx.beginPath();
            ctx.moveTo(startX, startY);
            ctx.lineTo(startX, startY);
            ctx.stroke();
        } else if (currentTool === 'text') {
            openTextInput(startX, startY);
            isDrawing = false;
        } else {
            // Shapes: save current canvas to restore during drag
            savedImageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
        }
    });

    canvas.addEventListener('pointermove', (e) => {
        if (!isDrawing) return;
        const pos = getPos(e);

        if (currentTool === 'pen' || currentTool === 'eraser' || currentTool === 'highlighter') {
            points.push({x: pos.x, y: pos.y});
            
            // Quadratic curve smoothing
            if (points.length >= 3) {
                const lastTwo = points.slice(-2);
                const controlPoint = lastTwo[0];
                const endPoint = {
                    x: (lastTwo[0].x + lastTwo[1].x) / 2,
                    y: (lastTwo[0].y + lastTwo[1].y) / 2,
                };
                
                ctx.beginPath();
                ctx.moveTo(lastX, lastY);
                ctx.quadraticCurveTo(controlPoint.x, controlPoint.y, endPoint.x, endPoint.y);
                ctx.stroke();
                
                lastX = endPoint.x;
                lastY = endPoint.y;
            } else {
                ctx.beginPath();
                ctx.moveTo(lastX, lastY);
                ctx.lineTo(pos.x, pos.y);
                ctx.stroke();
                lastX = pos.x;
                lastY = pos.y;
            }
        } else {
            // Shapes
            ctx.putImageData(savedImageData, 0, 0); // Restore background
            applyBrush(true);
            ctx.beginPath();
            if (currentTool === 'line') {
                ctx.moveTo(startX, startY);
                ctx.lineTo(pos.x, pos.y);
            } else if (currentTool === 'rect') {
                ctx.rect(startX, startY, pos.x - startX, pos.y - startY);
            } else if (currentTool === 'circle') {
                let radius = Math.sqrt(Math.pow(pos.x - startX, 2) + Math.pow(pos.y - startY, 2));
                ctx.arc(startX, startY, radius, 0, 2 * Math.PI);
            }
            ctx.stroke();
        }
    });

    canvas.addEventListener('pointerup', (e) => {
        if (!isDrawing) return;
        isDrawing = false;
        canvas.releasePointerCapture(e.pointerId);

        // Finalize last segment for smooth ink
        if (currentTool === 'pen' || currentTool === 'eraser' || currentTool === 'highlighter') {
            const pos = getPos(e);
            ctx.beginPath();
            ctx.moveTo(lastX, lastY);
            ctx.lineTo(pos.x, pos.y);
            ctx.stroke();
        }

        // Revert eraser auto-switch
        if (canvas.dataset.revertTool) {
            currentTool = canvas.dataset.revertTool;
            delete canvas.dataset.revertTool;
        }

        saveState();
    });

    // 5. Text Tool Implementation
    function openTextInput(x, y) {
        textOverlay.style.display = 'block';
        textOverlay.style.left = x + 'px';
        textOverlay.style.top = y + 'px';
        textOverlay.style.color = currentColor;
        textOverlay.style.fontSize = (currentSize * 8) + 'px';
        textOverlay.value = '';
        textOverlay.focus();
    }

    textOverlay.addEventListener('blur', commitText);
    textOverlay.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            commitText();
        }
    });

    function commitText() {
        if (textOverlay.style.display === 'none') return;
        textOverlay.style.display = 'none';
        
        let text = textOverlay.value.trim();
        if (!text) return;

        let x = parseInt(textOverlay.style.left);
        let y = parseInt(textOverlay.style.top);
        let fontSize = currentSize * 8;

        ctx.globalCompositeOperation = 'source-over';
        ctx.fillStyle = currentColor;
        ctx.font = `600 ${fontSize}px 'Source Serif 4', serif`;
        ctx.textBaseline = 'top';

        let lines = text.split('\\n');
        lines.forEach((line, i) => {
            ctx.fillText(line, x, y + (i * fontSize * 1.2));
        });

        saveState();
    }

    // 6. Undo/Redo State Management
    function saveState() {
        if (history.length >= MAX_HISTORY) {
            history.shift();
        }
        history.push(canvas.toDataURL());
    }

    function undo() {
        if (history.length > 1) {
            history.pop(); // Remove current
            let img = new Image();
            img.src = history[history.length - 1];
            img.onload = () => {
                ctx.clearRect(0, 0, canvas.width, canvas.height); // clear transparent
                ctx.save();
                ctx.setTransform(1, 0, 0, 1, 0, 0);
                ctx.drawImage(img, 0, 0);
                ctx.restore();
            };
        } else if (history.length === 1) {
            // Clear board
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            history = [];
            saveState();
        }
    }

    document.getElementById('pop-undo').addEventListener('click', undo);
    document.addEventListener('keydown', (e) => {
        if (e.ctrlKey && e.key === 'z') {
            if (popup.classList.contains('active') || popup.style.display === 'flex') {
                undo();
            }
        }
    });

    // 7. UI Controls Setup
    document.querySelectorAll('.popup-tool-btn[data-tool]').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.popup-tool-btn[data-tool]').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentTool = btn.dataset.tool;
        });
    });

    document.querySelectorAll('.popup-color-dot').forEach(dot => {
        dot.addEventListener('click', () => {
            document.querySelectorAll('.popup-color-dot').forEach(d => d.classList.remove('active'));
            dot.classList.add('active');
            currentColor = dot.dataset.color;
            if (currentTool === 'eraser') {
                // Auto switch back to pen if picking color while erasing
                document.querySelector('.popup-tool-btn[data-tool="pen"]').click();
            }
        });
    });

    document.getElementById('pop-size').addEventListener('input', (e) => {
        currentSize = parseInt(e.target.value);
    });

    document.getElementById('pop-clear').addEventListener('click', () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        saveState();
    });

    document.getElementById('pop-save').addEventListener('click', () => {
        // Draw background before saving to ensure it's not transparent
        let tempCanvas = document.createElement('canvas');
        tempCanvas.width = canvas.width;
        tempCanvas.height = canvas.height;
        let tCtx = tempCanvas.getContext('2d');
        
        tCtx.fillStyle = '#faf9f6'; // Match notebook paper color
        tCtx.fillRect(0, 0, tempCanvas.width, tempCanvas.height);
        tCtx.drawImage(canvas, 0, 0);

        const link = document.createElement('a');
        link.download = 'board-' + new Date().getTime() + '.png';
        link.href = tempCanvas.toDataURL('image/png');
        link.click();
    });

    // 8. Draggable Popup Logic
    let isDragging = false, dragStartX, dragStartY, popupStartLeft, popupStartTop;
    
    dragHandle.addEventListener('mousedown', (e) => {
        if(e.target.closest('button')) return;
        isDragging = true;
        dragStartX = e.clientX;
        dragStartY = e.clientY;
        const rect = popup.getBoundingClientRect();
        popupStartLeft = rect.left;
        popupStartTop = rect.top;
        popup.style.transform = 'none'; // remove translate(-50%, -50%)
        popup.style.left = popupStartLeft + 'px';
        popup.style.top = popupStartTop + 'px';
    });

    document.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        popup.style.left = (popupStartLeft + e.clientX - dragStartX) + 'px';
        popup.style.top = (popupStartTop + e.clientY - dragStartY) + 'px';
    });

    document.addEventListener('mouseup', () => { isDragging = false; });

    // 9. Toggle Logic
    document.getElementById('popup-close-btn').addEventListener('click', () => {
        popup.classList.remove('active');
        popup.style.display = 'none';
    });

    document.addEventListener('click', (e) => {
        if (e.target.closest('.draw-mode-toggle')) {
            if (!canvas.width) initCanvas(); // init on first open
            popup.style.display = 'flex';
            popup.classList.add('active');
            resizeCanvas(); // Ensure it fits the current view
        }
    });

})();