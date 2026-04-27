/**
 * ── TEACHER'S TRANSPARENT OVERLAY WHITEBOARD (Professional Pen-Tablet Edition) ──
 * Optimized for Wacom/Writing Pads and Real-Time persistence.
 */

(function() {
    // 1. Create Overlay HTML Structure
    const overlayHTML = `
        <div id="whiteboard-overlay" class="whiteboard-overlay">
            <canvas id="overlay-canvas"></canvas>
            
            <div class="overlay-toolbar">
                <button class="overlay-tool-btn active" id="overlay-pen" title="Pen (P)"><i class="fas fa-pen"></i></button>
                <button class="overlay-tool-btn" id="overlay-eraser" title="Eraser (E)"><i class="fas fa-eraser"></i></button>
                <button class="overlay-tool-btn" id="overlay-scroll" title="Scroll Mode (S)"><i class="fas fa-arrows-alt"></i></button>
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
            
            <div id="scroll-hint" style="position:fixed; bottom:20px; left:50%; transform:translateX(-50%); background:rgba(27,42,74,0.9); color:white; padding:8px 16px; border-radius:20px; font-size:0.8rem; pointer-events:none; display:none; z-index:10000;">
                <i class="fas fa-info-circle"></i> Scroll Mode Active: Use pen/mouse to drag the page.
            </div>
        </div>
    `;

    document.body.insertAdjacentHTML('beforeend', overlayHTML);

    // 2. Elements & State
    const overlay = document.getElementById('whiteboard-overlay');
    const canvas = document.getElementById('overlay-canvas');
    const ctx = canvas.getContext('2d', { alpha: true, desynchronized: true });
    const scrollHint = document.getElementById('scroll-hint');
    
    let isDrawing = false;
    let isScrolling = false;
    let currentTool = 'pen'; // 'pen', 'eraser', 'scroll'
    let currentColor = '#000000';
    let currentSize = 4;
    let lastX = 0, lastY = 0;

    // 3. Canvas Initialization
    function initCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        ctx.lineJoin = 'round';
        ctx.lineCap = 'round';
        applyBrushSettings();
    }

    function applyBrushSettings() {
        if (currentTool === 'eraser') {
            ctx.globalCompositeOperation = 'destination-out';
            ctx.lineWidth = currentSize * 5;
        } else {
            ctx.globalCompositeOperation = 'source-over';
            ctx.strokeStyle = currentColor;
            ctx.lineWidth = currentSize;
        }
    }

    // 4. Input Handling (Optimized for Writing Pads)
    function getPos(e) {
        const rect = canvas.getBoundingClientRect();
        if (e.touches && e.touches.length > 0) {
            return { x: e.touches[0].clientX - rect.left, y: e.touches[0].clientY - rect.top };
        }
        return { x: e.clientX - rect.left, y: e.clientY - rect.top };
    }

    function startAction(e) {
        if (!overlay.classList.contains('active')) return;
        
        const pos = getPos(e);
        lastX = pos.x;
        lastY = pos.y;

        if (currentTool === 'scroll') {
            isScrolling = true;
        } else {
            isDrawing = true;
            // Draw a dot immediately for pen taps
            ctx.beginPath();
            ctx.arc(lastX, lastY, ctx.lineWidth / 2, 0, Math.PI * 2);
            ctx.fill();
            ctx.beginPath();
            ctx.moveTo(lastX, lastY);
        }
    }

    function handleMove(e) {
        if (!isDrawing && !isScrolling) return;
        if (e.cancelable) e.preventDefault();

        const pos = getPos(e);

        if (isScrolling) {
            const dy = lastY - pos.y;
            window.scrollBy(0, dy);
            lastX = pos.x;
            lastY = pos.y;
        } else if (isDrawing) {
            ctx.lineTo(pos.x, pos.y);
            ctx.stroke();
            lastX = pos.x;
            lastY = pos.y;
        }
    }

    function stopAction() {
        isDrawing = false;
        isScrolling = false;
        ctx.beginPath();
    }

    // 5. Tool Switching
    function setTool(tool) {
        currentTool = tool;
        isScrolling = false;
        isDrawing = false;
        
        document.querySelectorAll('.overlay-tool-btn').forEach(b => b.classList.remove('active'));
        document.getElementById(`overlay-${tool}`).classList.add('active');
        
        if (tool === 'scroll') {
            canvas.style.cursor = 'grab';
            scrollHint.style.display = 'block';
        } else {
            canvas.style.cursor = 'crosshair';
            scrollHint.style.display = 'none';
        }
        applyBrushSettings();
    }

    // 6. Listeners
    window.addEventListener('resize', initCanvas);
    initCanvas();

    canvas.addEventListener('mousedown', startAction);
    window.addEventListener('mousemove', handleMove);
    window.addEventListener('mouseup', stopAction);

    canvas.addEventListener('touchstart', startAction, { passive: false });
    canvas.addEventListener('touchmove', handleMove, { passive: false });
    canvas.addEventListener('touchend', stopAction);

    // Header Button Logic
    document.addEventListener('click', (e) => {
        if (e.target.id === 'draw-mode-btn' || e.target.closest('#draw-mode-btn')) {
            const btn = document.getElementById('draw-mode-btn');
            const isActive = overlay.classList.toggle('active');
            btn.classList.toggle('active');
            
            if (isActive) {
                btn.innerHTML = '<i class="fas fa-times"></i> Exit Draw';
                setTool('pen');
            } else {
                btn.innerHTML = '<i class="fas fa-edit"></i> Draw Mode';
                setTool('scroll'); // Reset cursor
                overlay.classList.remove('active');
            }
        }
    });

    // Toolbar Listeners
    document.getElementById('overlay-pen').addEventListener('click', () => setTool('pen'));
    document.getElementById('overlay-eraser').addEventListener('click', () => setTool('eraser'));
    document.getElementById('overlay-scroll').addEventListener('click', () => setTool('scroll'));
    
    document.getElementById('overlay-clear').addEventListener('click', () => {
        if (confirm('Clear all drawings?')) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        }
    });

    document.getElementById('overlay-close').addEventListener('click', () => {
        document.getElementById('draw-mode-btn').click();
    });

    document.querySelectorAll('.overlay-color-dot').forEach(dot => {
        dot.addEventListener('click', function() {
            currentColor = this.getAttribute('data-color');
            document.querySelectorAll('.overlay-color-dot').forEach(d => d.classList.remove('active'));
            this.classList.add('active');
            setTool('pen');
        });
    });

    document.getElementById('overlay-size').addEventListener('input', function() {
        currentSize = this.value;
        applyBrushSettings();
    });

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
        if (!overlay.classList.contains('active')) return;
        const key = e.key.toLowerCase();
        if (key === 'p') setTool('pen');
        if (key === 'e') setTool('scroll'); // Toggle scroll with S
        if (key === 's') setTool('scroll');
        if (key === 'escape') document.getElementById('draw-mode-btn').click();
    });

})();
