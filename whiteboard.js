/**
 * ── TEACHER'S TRANSPARENT OVERLAY WHITEBOARD (Optimized for Real-Time) ──
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

    // 2. Elements & State
    const overlay = document.getElementById('whiteboard-overlay');
    const canvas = document.getElementById('overlay-canvas');
    const ctx = canvas.getContext('2d', { alpha: true, desynchronized: true }); // 'desynchronized' reduces latency in modern browsers
    
    const header = document.querySelector('.book-header');
    if (header) {
        header.insertAdjacentHTML('beforeend', `
            <button class="draw-mode-toggle" id="draw-mode-btn">
                <i class="fas fa-edit"></i> Draw Mode
            </button>
        `);
    }

    let isDrawing = false;
    let currentTool = 'pen';
    let currentColor = '#000000';
    let currentSize = 4;
    
    // Position tracking
    let points = [];

    // 3. Optimized Drawing Logic
    function initCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        ctx.lineJoin = 'round';
        ctx.lineCap = 'round';
        updateContextSettings();
    }

    function updateContextSettings() {
        if (currentTool === 'eraser') {
            ctx.globalCompositeOperation = 'destination-out';
            ctx.lineWidth = currentSize * 4;
        } else {
            ctx.globalCompositeOperation = 'source-over';
            ctx.strokeStyle = currentColor;
            ctx.lineWidth = currentSize;
        }
    }

    function getPos(e) {
        if (e.touches && e.touches.length > 0) {
            return { x: e.touches[0].clientX, y: e.touches[0].clientY };
        }
        return { x: e.clientX, y: e.clientY };
    }

    function startDrawing(e) {
        if (!overlay.classList.contains('active')) return;
        isDrawing = true;
        const pos = getPos(e);
        points = [pos];
    }

    function draw(e) {
        if (!isDrawing) return;
        if (e.cancelable) e.preventDefault();
        
        const pos = getPos(e);
        points.push(pos);

        // Optimization: Draw only the latest segment immediately for lowest latency
        if (points.length > 1) {
            const start = points[points.length - 2];
            const end = points[points.length - 1];
            
            ctx.beginPath();
            ctx.moveTo(start.x, start.y);
            ctx.lineTo(end.x, end.y);
            ctx.stroke();
        }
    }

    function stopDrawing() {
        isDrawing = false;
        points = [];
    }

    // 4. Event Listeners
    window.addEventListener('resize', initCanvas);
    initCanvas();

    // Mouse
    canvas.addEventListener('mousedown', startDrawing);
    canvas.addEventListener('mousemove', draw);
    window.addEventListener('mouseup', stopDrawing);

    // Touch
    canvas.addEventListener('touchstart', startDrawing, { passive: false });
    canvas.addEventListener('touchmove', draw, { passive: false });
    canvas.addEventListener('touchend', stopDrawing);

    // 5. Tool Controls
    document.getElementById('draw-mode-btn').addEventListener('click', function() {
        const isActive = overlay.classList.toggle('active');
        this.classList.toggle('active');
        
        if (isActive) {
            this.innerHTML = '<i class="fas fa-times"></i> Exit Draw';
            document.body.style.overflow = 'hidden';
            updateContextSettings();
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
        updateContextSettings();
        setActiveTool(this);
    });

    document.getElementById('overlay-eraser').addEventListener('click', function() {
        currentTool = 'eraser';
        updateContextSettings();
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
            updateContextSettings();
            setActiveTool(document.getElementById('overlay-pen'));
        });
    });

    document.getElementById('overlay-size').addEventListener('input', function() {
        currentSize = this.value;
        updateContextSettings();
    });

    document.getElementById('overlay-clear').addEventListener('click', () => {
        if (confirm('Clear drawings?')) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        }
    });

})();
