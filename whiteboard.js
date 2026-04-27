/**
 * ── TEACHER'S FLOATING POPUP WHITEBOARD ──
 * Optimized for simultaneous viewing of content and writing.
 */

(function() {
    // 1. Create Popup HTML Structure
    const popupHTML = `
        <div id="whiteboard-popup" class="whiteboard-popup">
            <div class="popup-header" id="popup-drag-handle">
                <h3><i class="fas fa-chalkboard"></i> Teacher's Canvas</h3>
                <button class="popup-close" id="popup-close-btn"><i class="fas fa-times"></i></button>
            </div>
            
            <div class="popup-canvas-container" id="popup-canvas-wrap">
                <canvas id="popup-canvas"></canvas>
            </div>
            
            <div class="popup-toolbar">
                <button class="popup-tool-btn active" id="pop-pen" title="Pen"><i class="fas fa-pen"></i></button>
                <button class="popup-tool-btn" id="pop-eraser" title="Eraser"><i class="fas fa-eraser"></i></button>
                <button class="popup-tool-btn" id="pop-clear" title="Clear All"><i class="fas fa-trash-alt"></i></button>
                
                <div style="width:1px; height:24px; background:#DDD8CF; margin:0 5px;"></div>
                
                <div class="popup-color-dot active" style="background: #000000;" data-color="#000000"></div>
                <div class="popup-color-dot" style="background: #9B2335;" data-color="#9B2335"></div>
                <div class="popup-color-dot" style="background: #3D6B5A;" data-color="#3D6B5A"></div>
                <div class="popup-color-dot" style="background: #1D6FA4;" data-color="#1D6FA4"></div>
                
                <div style="width:1px; height:24px; background:#DDD8CF; margin:0 5px;"></div>
                
                <input type="range" min="1" max="30" value="3" class="popup-size-slider" id="pop-size">
                
                <button class="popup-tool-btn" id="pop-save" title="Save Image" style="margin-left:auto;">
                    <i class="fas fa-download"></i>
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

    // Inject toggle button into header
    function injectButton() {
        const header = document.querySelector('.book-header');
        if (header && !document.getElementById('draw-mode-btn')) {
            header.insertAdjacentHTML('beforeend', `
                <button class="draw-mode-toggle" id="draw-mode-btn">
                    <i class="fas fa-chalkboard"></i> Open Whiteboard
                </button>
            `);
        }
    }
    injectButton();

    let isDrawing = false;
    let currentTool = 'pen';
    let currentColor = '#000000';
    let currentSize = 3;
    let lastX = 0, lastY = 0;

    // 3. Canvas Initialization
    function initCanvas() {
        // Set internal resolution to match displayed size
        canvas.width = container.clientWidth;
        canvas.height = container.clientHeight;
        
        ctx.lineJoin = 'round';
        ctx.lineCap = 'round';
        ctx.fillStyle = "#ffffff";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        applyBrush();
    }

    function applyBrush() {
        if (currentTool === 'eraser') {
            ctx.globalCompositeOperation = 'destination-out';
            ctx.lineWidth = currentSize * 6;
        } else {
            ctx.globalCompositeOperation = 'source-over';
            ctx.strokeStyle = currentColor;
            ctx.lineWidth = currentSize;
        }
    }

    // 4. Drawing Logic
    function getPos(e) {
        const rect = canvas.getBoundingClientRect();
        if (e.touches && e.touches.length > 0) {
            return { 
                x: e.touches[0].clientX - rect.left, 
                y: e.touches[0].clientY - rect.top 
            };
        }
        return { 
            x: e.clientX - rect.left, 
            y: e.clientY - rect.top 
        };
    }

    function startDraw(e) {
        isDrawing = true;
        const pos = getPos(e);
        lastX = pos.x;
        lastY = pos.y;
        
        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
    }

    function draw(e) {
        if (!isDrawing) return;
        if (e.cancelable) e.preventDefault();

        const pos = getPos(e);
        ctx.lineTo(pos.x, pos.y);
        ctx.stroke();
        [lastX, lastY] = [pos.x, pos.y];
    }

    function stopDraw() {
        isDrawing = false;
    }

    // 5. Dragging Logic
    let isDragging = false;
    let dragStartX, dragStartY;

    dragHandle.addEventListener('mousedown', (e) => {
        isDragging = true;
        dragStartX = e.clientX - popup.offsetLeft;
        dragStartY = e.clientY - popup.offsetTop;
    });

    window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        popup.style.left = (e.clientX - dragStartX) + 'px';
        popup.style.top = (e.clientY - dragStartY) + 'px';
        popup.style.right = 'auto'; // Break the initial "right: 40px"
    });

    window.addEventListener('mouseup', () => isDragging = false);

    // 6. UI Event Listeners
    canvas.addEventListener('mousedown', startDraw);
    canvas.addEventListener('mousemove', draw);
    window.addEventListener('mouseup', stopDraw);

    canvas.addEventListener('touchstart', startDraw, { passive: false });
    canvas.addEventListener('touchmove', draw, { passive: false });
    canvas.addEventListener('touchend', stopDraw);

    // Toggle Button
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
        document.getElementById('draw-mode-btn').click();
    });

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
        if (confirm('Clear the whiteboard?')) {
            ctx.fillStyle = "#ffffff";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
        }
    });

    document.getElementById('pop-save').addEventListener('click', () => {
        const link = document.createElement('a');
        link.download = 'whiteboard-notes.png';
        link.href = canvas.toDataURL();
        link.click();
    });

})();
