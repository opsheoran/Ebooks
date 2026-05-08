/**
 * ── PROFESSIONAL TEACHER'S CANVAS (MULTI-PAGE) ──
 * High-DPI, Ultra-Smooth Ink, Notebook Paper, Rich Tools, Resize-Safe, and PDF Export.
 */

(function() {
    // 0. Load jsPDF dynamically for PDF Export
    if (!window.jspdf) {
        const script = document.createElement('script');
        script.src = "https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js";
        document.head.appendChild(script);
    }

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

            <!-- PAGE NAVIGATION BAR -->
            <div style="background: #e8e6df; border-top: 1px solid #DDD8CF; padding: 6px 20px; display: flex; align-items: center; justify-content: space-between; flex-shrink: 0; font-size: 0.9rem; color: #1B2A4A;">
                <div style="display: flex; gap: 10px; align-items: center;">
                    <button class="popup-tool-btn" id="pop-page-prev" title="Previous Page" style="width: 30px; height: 30px;"><i class="fas fa-chevron-left"></i></button>
                    <span id="pop-page-indicator" style="font-weight: 600; min-width: 80px; text-align: center;">Page 1 of 1</span>
                    <button class="popup-tool-btn" id="pop-page-next" title="Next Page" style="width: 30px; height: 30px;"><i class="fas fa-chevron-right"></i></button>
                    <button class="popup-tool-btn" id="pop-page-add" title="Add New Page" style="width: 30px; height: 30px; margin-left: 10px; color: #3D6B5A;"><i class="fas fa-plus"></i></button>
                    <button class="popup-tool-btn" id="pop-page-del" title="Delete Current Page" style="width: 30px; height: 30px; color: #9B2335;"><i class="fas fa-trash"></i></button>
                </div>
                <div>
                    <button class="popup-tool-btn" id="pop-save" title="Export All Pages as PDF" style="background:#2E4270; color:#fff; border:none; width:auto; padding: 0 15px; font-weight: 600; height: 30px;">
                        <i class="fas fa-file-pdf" style="margin-right: 8px;"></i> Download PDF
                    </button>
                </div>
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
                <button class="popup-tool-btn" id="pop-clear" title="Clear Board" style="color: #9B2335;"><i class="fas fa-eraser"></i> Clear</button>
            </div>
        </div>
    `;

    document.body.insertAdjacentHTML('beforeend', popupHTML);

    // 2. Elements & State
    const popup = document.getElementById('whiteboard-popup');
    const canvas = document.getElementById('popup-canvas');
    const ctx = canvas.getContext('2d', { alpha: true }); // No desynchronized to fix black bg bug
    const container = document.getElementById('popup-canvas-wrap');
    const dragHandle = document.getElementById('popup-drag-handle');
    const textOverlay = document.getElementById('text-input-overlay');

    let currentTool = 'pen';
    let currentColor = '#000000';
    let currentSize = 3;
    let isDrawing = false;
    let dpr = window.devicePixelRatio || 1;

    // Multi-page State
    let bookPages = [null]; // Array of image dataURLs
    let currentPageIndex = 0;

    // History for Undo (current page only)
    let history = [];
    const MAX_HISTORY = 20;

    // Drawing state
    let startX = 0, startY = 0;
    let lastX = 0, lastY = 0;
    let points = [];
    let savedImageData = null;

    // 3. High-DPI Canvas Init & Resizing
    function initCanvas() {
        resizeCanvas();
        saveHistoryState(); // Initial blank state
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

    const resizeObserver = new ResizeObserver(() => {
        if (popup.style.display === 'flex' || popup.classList.contains('active')) {
            resizeCanvas();
            // Important: we need to update the saved snapshot for this page 
            // after resize so it doesn't get squished if we switch pages later.
            if(canvas.width > 0) {
                bookPages[currentPageIndex] = canvas.toDataURL();
            }
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
            let hex = currentColor;
            let r = parseInt(hex.slice(1,3), 16), g = parseInt(hex.slice(3,5), 16), b = parseInt(hex.slice(5,7), 16);
            ctx.strokeStyle = `rgba(${r},${g},${b},0.3)`;
            ctx.fillStyle = `rgba(${r},${g},${b},0.3)`;
            ctx.lineWidth = currentSize * 6;
            ctx.lineCap = 'butt';
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

    // 4. Input Events
    canvas.addEventListener('pointerdown', (e) => {
        if (e.button !== 0 && e.button !== 5) return; 
        isDrawing = true;
        canvas.setPointerCapture(e.pointerId);

        const pos = getPos(e);
        startX = pos.x;
        startY = pos.y;
        lastX = pos.x;
        lastY = pos.y;

        if (e.pointerType === 'pen' && e.button === 5) {
            let oldTool = currentTool;
            currentTool = 'eraser';
            applyBrush();
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
            savedImageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
        }
    });

    canvas.addEventListener('pointermove', (e) => {
        if (!isDrawing) return;
        const pos = getPos(e);

        if (currentTool === 'pen' || currentTool === 'eraser' || currentTool === 'highlighter') {
            points.push({x: pos.x, y: pos.y});
            
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
            ctx.putImageData(savedImageData, 0, 0); 
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

        if (currentTool === 'pen' || currentTool === 'eraser' || currentTool === 'highlighter') {
            const pos = getPos(e);
            ctx.beginPath();
            ctx.moveTo(lastX, lastY);
            ctx.lineTo(pos.x, pos.y);
            ctx.stroke();
        }

        if (canvas.dataset.revertTool) {
            currentTool = canvas.dataset.revertTool;
            delete canvas.dataset.revertTool;
        }

        saveHistoryState();
    });

    // 5. Text Tool
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

        saveHistoryState();
    }

    // 6. Undo History & Page State Management
    function saveHistoryState() {
        if (history.length >= MAX_HISTORY) {
            history.shift();
        }
        let data = canvas.toDataURL();
        history.push(data);
        bookPages[currentPageIndex] = data; // Sync the multi-page array
    }

    function undo() {
        if (history.length > 1) {
            history.pop(); 
            let data = history[history.length - 1];
            bookPages[currentPageIndex] = data; // Sync the multi-page array
            loadPageData(data);
        } else if (history.length === 1) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            history = [];
            saveHistoryState();
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

    // 7. Multi-Page Logic
    function updatePageIndicator() {
        document.getElementById('pop-page-indicator').textContent = `Page ${currentPageIndex + 1} of ${bookPages.length}`;
    }

    function loadPageData(dataUrl) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        if (dataUrl) {
            let img = new Image();
            img.src = dataUrl;
            img.onload = () => {
                ctx.save();
                ctx.setTransform(1, 0, 0, 1, 0, 0);
                ctx.drawImage(img, 0, 0);
                ctx.restore();
            };
        }
    }

    function switchPage(index) {
        // Ensure current page is saved
        bookPages[currentPageIndex] = canvas.toDataURL();
        
        currentPageIndex = index;
        history = []; // Reset undo history for the new page
        
        loadPageData(bookPages[currentPageIndex]);
        
        // Push to history to allow undo to clear page
        history.push(bookPages[currentPageIndex] || canvas.toDataURL());
        
        updatePageIndicator();
    }

    document.getElementById('pop-page-prev').addEventListener('click', () => {
        if (currentPageIndex > 0) switchPage(currentPageIndex - 1);
    });

    document.getElementById('pop-page-next').addEventListener('click', () => {
        if (currentPageIndex < bookPages.length - 1) {
            switchPage(currentPageIndex + 1);
        } else {
            // Auto add page if at end
            document.getElementById('pop-page-add').click();
        }
    });

    document.getElementById('pop-page-add').addEventListener('click', () => {
        bookPages[currentPageIndex] = canvas.toDataURL(); // Save current
        bookPages.push(null); // Add blank page
        switchPage(bookPages.length - 1);
    });

    document.getElementById('pop-page-del').addEventListener('click', () => {
        if (bookPages.length === 1) {
            // If only one page, just clear it
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            saveHistoryState();
            return;
        }
        
        if (confirm("Are you sure you want to delete this page?")) {
            bookPages.splice(currentPageIndex, 1);
            if (currentPageIndex >= bookPages.length) {
                currentPageIndex = bookPages.length - 1;
            }
            switchPage(currentPageIndex);
        }
    });


    // 8. PDF Export Logic
    document.getElementById('pop-save').addEventListener('click', () => {
        if (!window.jspdf || !window.jspdf.jsPDF) {
            alert("PDF library is loading. Please try again in a few seconds.");
            return;
        }
        
        const saveBtn = document.getElementById('pop-save');
        const originalText = saveBtn.innerHTML;
        saveBtn.innerHTML = '<i class="fas fa-spinner fa-spin" style="margin-right: 8px;"></i> Exporting...';
        
        // Save active page
        bookPages[currentPageIndex] = canvas.toDataURL();

        setTimeout(() => {
            const { jsPDF } = window.jspdf;
            const pdf = new jsPDF('l', 'pt', [canvas.width / dpr, canvas.height / dpr]); // Landscape exact fit
            const pdfWidth = pdf.internal.pageSize.getWidth();
            const pdfHeight = pdf.internal.pageSize.getHeight();

            let loadPromises = bookPages.map((pageData, index) => {
                return new Promise((resolve) => {
                    let tempCanvas = document.createElement('canvas');
                    tempCanvas.width = canvas.width;
                    tempCanvas.height = canvas.height;
                    let tCtx = tempCanvas.getContext('2d');
                    
                    // Draw Paper Background
                    tCtx.fillStyle = '#faf9f6'; 
                    tCtx.fillRect(0, 0, tempCanvas.width, tempCanvas.height);
                    
                    tCtx.lineWidth = 1 * dpr;
                    tCtx.strokeStyle = 'rgba(100,150,200,0.2)';
                    for (let y = 0; y < tempCanvas.height; y += 30 * dpr) {
                        tCtx.beginPath();
                        tCtx.moveTo(0, y);
                        tCtx.lineTo(tempCanvas.width, y);
                        tCtx.stroke();
                    }
                    tCtx.lineWidth = 2 * dpr;
                    tCtx.strokeStyle = 'rgba(230,130,130,0.4)';
                    tCtx.beginPath();
                    tCtx.moveTo(79 * dpr, 0);
                    tCtx.lineTo(79 * dpr, tempCanvas.height);
                    tCtx.stroke();

                    if (!pageData) {
                        resolve(tempCanvas);
                        return;
                    }

                    let img = new Image();
                    img.src = pageData;
                    img.onload = () => {
                        tCtx.drawImage(img, 0, 0);
                        resolve(tempCanvas);
                    };
                });
            });

            Promise.all(loadPromises).then(canvases => {
                canvases.forEach((c, idx) => {
                    if (idx > 0) pdf.addPage();
                    const imgData = c.toDataURL('image/jpeg', 0.95);
                    pdf.addImage(imgData, 'JPEG', 0, 0, pdfWidth, pdfHeight);
                });
                pdf.save('Teacher_Notebook_' + new Date().getTime() + '.pdf');
                saveBtn.innerHTML = originalText;
            });
        }, 100);
    });


    // 9. UI Controls Setup
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
                document.querySelector('.popup-tool-btn[data-tool="pen"]').click();
            }
        });
    });

    document.getElementById('pop-size').addEventListener('input', (e) => {
        currentSize = parseInt(e.target.value);
    });

    document.getElementById('pop-clear').addEventListener('click', () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        saveHistoryState();
    });

    // 10. Draggable Popup Logic
    let isDragging = false, dragStartX, dragStartY, popupStartLeft, popupStartTop;
    
    dragHandle.addEventListener('mousedown', (e) => {
        if(e.target.closest('button')) return;
        isDragging = true;
        dragStartX = e.clientX;
        dragStartY = e.clientY;
        const rect = popup.getBoundingClientRect();
        popupStartLeft = rect.left;
        popupStartTop = rect.top;
        popup.style.transform = 'none'; 
        popup.style.left = popupStartLeft + 'px';
        popup.style.top = popupStartTop + 'px';
    });

    document.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        popup.style.left = (popupStartLeft + e.clientX - dragStartX) + 'px';
        popup.style.top = (popupStartTop + e.clientY - dragStartY) + 'px';
    });

    document.addEventListener('mouseup', () => { isDragging = false; });

    // 11. Toggle Logic
    document.getElementById('popup-close-btn').addEventListener('click', () => {
        popup.classList.remove('active');
        popup.style.display = 'none';
    });

    document.addEventListener('click', (e) => {
        if (e.target.closest('.draw-mode-toggle')) {
            if (!canvas.width) initCanvas(); 
            popup.style.display = 'flex';
            popup.classList.add('active');
            resizeCanvas(); 
        }
    });

})();