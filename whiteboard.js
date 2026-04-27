/**
 * ── PROFESSIONAL TEACHER'S CANVAS ──
 * High-DPI, Ultra-Smooth Ink, and Reliable Eraser.
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
            </div>
            
            <div class="popup-toolbar">
                <button class="popup-tool-btn active" id="pop-pen" title="Pen Tool (P)"><i class="fas fa-pen-nib"></i></button>
                <button class="popup-tool-btn" id="pop-eraser" title="Eraser Tool (E)"><i class="fas fa-eraser"></i></button>
                <button class="popup-tool-btn" id="pop-clear" title="Clear Board"><i class="fas fa-trash-restore"></i></button>
                
                <div style="width:2px; height:28px; background:#DDD8CF; margin:0 8px;"></div>
                
                <div class="popup-color-dot active" style="background: #000000;" data-color="#000000"></div>
                <div class="popup-color-dot" style="background: #9B2335;" data-color="#9B2335"></div>
                <div class="popup-color-dot" style="background: #1B2A4A;" data-color="#1B2A4A"></div>
                <div class="popup-color-dot" style="background: #3D6B5A;" data-color="#3D6B5A"></div>
                
                <div style="width:2px; height:28px; background:#DDD8CF; margin:0 8px;"></div>
                
                <span class="popup-size-label">Size</span>
                <input type="range" min="1" max="40" value="4" class="popup-size-slider" id="pop-size">
                
                <button class="popup-tool-btn" id="pop-save" title="Save as PNG" style="margin-left:auto; background:var(--sage); color:#fff; border:none;">
                    <i class="fas fa-save"></i>
                </button>
            </div>
        </div>
    `;

    document.body.insertAdjacentHTML('beforeend', popupHTML);

    // 2. Elements & State
    const popup = document.getElementById('whiteboard-popup');
    const canvas = document.getElementById('popup-canvas');
    const ctx = canvas.getContext('2d', { desynchronized: true });
    const container = document.getElementById('popup-canvas-wrap');
    const dragHandle = document.getElementById('popup-drag-handle');

    let isDrawing = false;
    let currentTool = 'pen';
    let currentColor = '#000000';
    let currentSize = 4;
    
    // Smooth drawing points
    let points = [];

    // 3. High-DPI Canvas Init
    function initCanvas() {
        const dpr = window.devicePixelRatio || 1;
        const rect = container.getBoundingClientRect();
        
        // Scale canvas for sharp ink
        canvas.width = rect.width * dpr;
        canvas.height = rect.height * dpr;
        canvas.style.width = rect.width + 'px';
        canvas.style.height = rect.height + 'px';
        
        ctx.scale(dpr, dpr);
        ctx.lineJoin = 'round';
        ctx.lineCap = 'round';
        
        // Solid white background
        ctx.fillStyle = "#ffffff";
        ctx.fillRect(0, 0, rect.width, rect.height);
        
        applyBrush();
    }

    function applyBrush() {
        ctx.globalCompositeOperation = 'source-over'; // Always use source-over for reliability
        if (currentTool === 'eraser') {
            ctx.strokeStyle = "#ffffff"; // Erase with white
            ctx.lineWidth = currentSize * 8; // Larger eraser
        } else {
            ctx.strokeStyle = currentColor;
            ctx.lineWidth = currentSize;
        }
    }

    // 4. Ultra-Smooth Drawing Logic (Quadratic Curves)
    function getPos(e) {
        const rect = canvas.getBoundingClientRect();
        return {
            x: e.clientX - rect.left,
            y: e.clientY - rect.top
        };
    }

    function startDraw(e) {
        if (e.button !== undefined && e.button !== 0) return; // Only left click
        isDrawing = true;
        const pos = getPos(e);
        points = [pos];
        
        // Draw a dot immediately for taps
        ctx.beginPath();
        ctx.fillStyle = currentTool === 'eraser' ? '#ffffff' : currentColor;
        const dotSize = currentTool === 'eraser' ? currentSize * 4 : currentSize / 2;
        ctx.arc(pos.x, pos.y, dotSize, 0, Math.PI * 2);
        ctx.fill();
        
        applyBrush();
    }

    function moveDraw(e) {
        if (!isDrawing) return;
        if (e.cancelable) e.preventDefault();

        const pos = getPos(e);
        points.push(pos);

        if (points.length > 2) {
            ctx.beginPath();
            // Start at the midpoint of the first two points
            const start = points[points.length - 3];
            const mid1 = {
                x: (start.x + points[points.length - 2].x) / 2,
                y: (start.y + points[points.length - 2].y) / 2
            };
            const mid2 = {
                x: (points[points.length - 2].x + pos.x) / 2,
                y: (points[points.length - 2].y + pos.y) / 2
            };

            ctx.moveTo(mid1.x, mid1.y);
            // Curve through the middle point to the next midpoint
            ctx.quadraticCurveTo(points[points.length - 2].x, points[points.length - 2].y, mid2.x, mid2.y);
            ctx.stroke();
        }
    }

    function endDraw() {
        isDrawing = false;
        points = [];
    }

    // 5. Dragging Logic
    let isDragging = false;
    let dragStartX, dragStartY;

    dragHandle.addEventListener('mousedown', (e) => {
        if (e.target.closest('.popup-close')) return;
        isDragging = true;
        dragStartX = e.clientX - popup.offsetLeft;
        dragStartY = e.clientY - popup.offsetTop;
        popup.style.transition = 'none';
    });

    window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        popup.style.left = (e.clientX - dragStartX) + 'px';
        popup.style.top = (e.clientY - dragStartY) + 'px';
        popup.style.transform = 'none'; // Clear the initial centering transform
    });

    window.addEventListener('mouseup', () => {
        isDragging = false;
        popup.style.transition = '';
    });

    // 6. Global Event Listeners (PointerEvents for Pen/Mouse/Touch)
    canvas.addEventListener('pointerdown', startDraw);
    window.addEventListener('pointermove', moveDraw);
    window.addEventListener('pointerup', endDraw);
    canvas.addEventListener('pointerleave', endDraw);

    // Toggle Button Logic
    document.addEventListener('click', (e) => {
        const btn = e.target.closest('#draw-mode-btn');
        if (btn) {
            const isActive = popup.classList.toggle('active');
            btn.classList.toggle('active');
            if (isActive) {
                btn.innerHTML = '<i class="fas fa-times"></i> Close Whiteboard';
                initCanvas();
            } else {
                btn.innerHTML = '<i class="fas fa-chalkboard"></i> Open Whiteboard';
            }
        }
    });

    document.getElementById('popup-close-btn').addEventListener('click', () => {
        const btn = document.getElementById('draw-mode-btn');
        if (btn) btn.click();
    });

    // Toolbar Listeners
    document.getElementById('pop-pen').addEventListener('click', function() {
        currentTool = 'pen';
        setActiveTool(this);
        applyBrush();
    });

    document.getElementById('pop-eraser').addEventListener('click', function() {
        currentTool = 'eraser';
        setActiveTool(this);
        applyBrush();
    });

    function setActiveTool(btn) {
        document.querySelectorAll('.popup-tool-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    }

    document.querySelectorAll('.popup-color-dot').forEach(dot => {
        dot.addEventListener('click', function() {
            currentColor = this.getAttribute('data-color');
            document.querySelectorAll('.popup-color-dot').forEach(d => d.classList.remove('active'));
            this.classList.add('active');
            currentTool = 'pen';
            setActiveTool(document.getElementById('pop-pen'));
            applyBrush();
        });
    });

    document.getElementById('pop-size').addEventListener('input', function() {
        currentSize = this.value;
        applyBrush();
    });

    document.getElementById('pop-clear').addEventListener('click', () => {
        if (confirm('Clear the entire board?')) {
            const rect = container.getBoundingClientRect();
            ctx.fillStyle = "#ffffff";
            ctx.fillRect(0, 0, rect.width, rect.height);
        }
    });

    document.getElementById('pop-save').addEventListener('click', () => {
        const link = document.createElement('a');
        link.download = 'teacher-notes-' + new Date().getTime() + '.png';
        link.href = canvas.toDataURL('image/png');
        link.click();
    });

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
        if (!popup.classList.contains('active')) return;
        const key = e.key.toLowerCase();
        if (key === 'p') document.getElementById('pop-pen').click();
        if (key === 'e') document.getElementById('pop-eraser').click();
        if (key === 'escape') document.getElementById('popup-close-btn').click();
    });

})();
