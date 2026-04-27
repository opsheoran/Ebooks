/**
 * ── TEACHER'S TRANSPARENT OVERLAY WHITEBOARD ──
 */

(function() {
    // 1. Create Overlay HTML Structure
    const overlayHTML = `
        <div id="whiteboard-overlay" class="whiteboard-overlay">
            <canvas id="overlay-canvas"></canvas>
            
            <div class="overlay-toolbar">
                <button class="overlay-tool-btn active" id="overlay-pen" title="Pen"><i class="fas fa-pen"></i></button>
                <button class="overlay-tool-btn" id="overlay-eraser" title="Eraser"><i class="fas fa-eraser"></i></button>
                <button class="overlay-tool-btn" id="overlay-clear" title="Clear All"><i class="fas fa-trash-alt"></i></button>
                
                <hr style="opacity:0.2">
                
                <div class="overlay-color-dot active" style="background: #000000;" data-color="#000000"></div>
                <div class="overlay-color-dot" style="background: #9B2335;" data-color="#9B2335"></div>
                <div class="overlay-color-dot" style="background: #3D6B5A;" data-color="#3D6B5A"></div>
                <div class="overlay-color-dot" style="background: #1D6FA4;" data-color="#1D6FA4"></div>
                <div class="overlay-color-dot" style="background: #ffffff;" data-color="#ffffff"></div>
                
                <hr style="opacity:0.2">
                
                <input type="range" min="1" max="40" value="4" class="overlay-size-slider" id="overlay-size">
                
                <button class="overlay-tool-btn" id="overlay-close" title="Exit Draw Mode" style="background:#9B2335; margin-top:10px;">
                    <i class="fas fa-times"></i>
                </button>
            </div>
        </div>
    `;

    document.body.insertAdjacentHTML('beforeend', overlayHTML);

    // 2. State & Elements
    const overlay = document.getElementById('whiteboard-overlay');
    const canvas = document.getElementById('overlay-canvas');
    const ctx = canvas.getContext('2d');
    const toggleBtnTemplate = `
        <button class="draw-mode-toggle" id="draw-mode-btn">
            <i class="fas fa-edit"></i> Draw Mode
        </button>
    `;

    // Inject toggle button into header
    const header = document.querySelector('.book-header');
    if (header) {
        header.insertAdjacentHTML('beforeend', toggleBtnTemplate);
    }

    let isDrawing = false;
    let lastX = 0;
    let lastY = 0;
    let currentTool = 'pen';
    let currentColor = '#000000';
    let currentSize = 4;

    // 3. Functions
    function initCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        ctx.lineJoin = 'round';
        ctx.lineCap = 'round';
    }

    function getPos(e) {
        let x, y;
        if (e.type.includes('touch')) {
            x = e.touches[0].clientX;
            y = e.touches[0].clientY;
        } else {
            x = e.clientX;
            y = e.clientY;
        }
        return { x, y };
    }

    function startDrawing(e) {
        if (!overlay.classList.contains('active')) return;
        isDrawing = true;
        const pos = getPos(e);
        [lastX, lastY] = [pos.x, pos.y];
    }

    function draw(e) {
        if (!isDrawing) return;
        e.preventDefault();
        const pos = getPos(e);

        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(pos.x, pos.y);

        if (currentTool === 'eraser') {
            ctx.globalCompositeOperation = 'destination-out';
            ctx.lineWidth = currentSize * 4;
        } else {
            ctx.globalCompositeOperation = 'source-over';
            ctx.strokeStyle = currentColor;
            ctx.lineWidth = currentSize;
        }

        ctx.stroke();
        [lastX, lastY] = [pos.x, pos.y];
    }

    function stopDrawing() {
        isDrawing = false;
        ctx.beginPath();
    }

    // 4. Event Listeners
    window.addEventListener('resize', initCanvas);
    initCanvas();

    canvas.addEventListener('mousedown', startDrawing);
    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('mouseup', stopDrawing);
    canvas.addEventListener('mouseout', stopDrawing);

    canvas.addEventListener('touchstart', startDrawing, { passive: false });
    canvas.addEventListener('touchmove', draw, { passive: false });
    canvas.addEventListener('touchend', stopDrawing);

    // 5. Tool Controls
    document.getElementById('draw-mode-btn').addEventListener('click', function() {
        this.classList.toggle('active');
        overlay.classList.toggle('active');
        if (overlay.classList.contains('active')) {
            this.innerHTML = '<i class="fas fa-times"></i> Exit Draw';
            document.body.style.overflow = 'hidden'; // Prevent scrolling while drawing
        } else {
            this.innerHTML = '<i class="fas fa-edit"></i> Draw Mode';
            document.body.style.overflow = '';
        }
    });

    document.getElementById('overlay-close').addEventListener('click', () => {
        document.getElementById('draw-mode-btn').click();
    });

    document.getElementById('overlay-pen').addEventListener('click', function() {
        currentTool = 'pen';
        setActiveTool(this);
    });

    document.getElementById('overlay-eraser').addEventListener('click', function() {
        currentTool = 'eraser';
        setActiveTool(this);
    });

    function setActiveTool(btn) {
        document.querySelectorAll('.overlay-tool-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    }

    document.querySelectorAll('.overlay-color-dot').forEach(dot => {
        dot.addEventListener('click', function() {
            currentColor = this.getAttribute('data-color');
            document.querySelectorAll('.overlay-color-dot').forEach(d => d.classList.remove('active'));
            this.classList.add('active');
            currentTool = 'pen';
            setActiveTool(document.getElementById('overlay-pen'));
        });
    });

    document.getElementById('overlay-size').addEventListener('input', function() {
        currentSize = this.value;
    });

    document.getElementById('overlay-clear').addEventListener('click', () => {
        if (confirm('Clear drawings?')) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        }
    });

})();
