/* ── PROFESSIONAL FLOATING SCIENTIFIC CALCULATOR ENGINE ── */

(function () {
    let calcPopup = null;
    let isDeg = true;
    let lastAns = 0;

    function initCalculator() {
        if (document.getElementById('calc-popup')) return;

        // Create Calculator Modal HTML
        const modalHTML = `
        <div id="calc-popup" class="calc-popup">
            <div class="calc-header" id="calc-header">
                <h3><i class="fas fa-calculator"></i> Scientific Calculator</h3>
                <button class="calc-close" id="calc-close-btn" aria-label="Close calculator">&times;</button>
            </div>
            <div class="calc-display-container">
                <div class="calc-history" id="calc-history"></div>
                <input type="text" class="calc-input" id="calc-input" value="0" readonly>
            </div>
            <div class="calc-keypad">
                <button class="calc-btn fn-btn" data-action="deg" id="calc-deg-btn">DEG</button>
                <button class="calc-btn fn-btn" data-action="sin">sin</button>
                <button class="calc-btn fn-btn" data-action="cos">cos</button>
                <button class="calc-btn fn-btn" data-action="tan">tan</button>
                <button class="calc-btn clear-btn" data-action="clear">C</button>

                <button class="calc-btn fn-btn" data-action="pow">x^y</button>
                <button class="calc-btn fn-btn" data-action="sqrt">√</button>
                <button class="calc-btn fn-btn" data-action="log">log</button>
                <button class="calc-btn fn-btn" data-action="ln">ln</button>
                <button class="calc-btn clear-btn" data-action="backspace"><i class="fas fa-backspace"></i></button>

                <button class="calc-btn fn-btn" data-action="pi">π</button>
                <button class="calc-btn fn-btn" data-action="e">e</button>
                <button class="calc-btn fn-btn" data-action="(">(</button>
                <button class="calc-btn fn-btn" data-action=")">)</button>
                <button class="calc-btn op-btn" data-action="/">÷</button>

                <button class="calc-btn fn-btn" data-action="fact">n!</button>
                <button class="calc-btn" data-val="7">7</button>
                <button class="calc-btn" data-val="8">8</button>
                <button class="calc-btn" data-val="9">9</button>
                <button class="calc-btn op-btn" data-action="*">&times;</button>

                <button class="calc-btn fn-btn" data-action="recip">1/x</button>
                <button class="calc-btn" data-val="4">4</button>
                <button class="calc-btn" data-val="5">5</button>
                <button class="calc-btn" data-val="6">6</button>
                <button class="calc-btn op-btn" data-action="-">-</button>

                <button class="calc-btn fn-btn" data-action="ans">Ans</button>
                <button class="calc-btn" data-val="1">1</button>
                <button class="calc-btn" data-val="2">2</button>
                <button class="calc-btn" data-val="3">3</button>
                <button class="calc-btn op-btn" data-action="+">+</button>

                <button class="calc-btn fn-btn" data-action="pm">&plusmn;</button>
                <button class="calc-btn" data-val="0">0</button>
                <button class="calc-btn" data-val=".">.</button>
                <button class="calc-btn equals-btn" data-action="equals">=</button>
            </div>
        </div>
        `;

        document.body.insertAdjacentHTML('beforeend', modalHTML);
        calcPopup = document.getElementById('calc-popup');

        setupEventListeners();
        makeDraggable();
    }

    function setupEventListeners() {
        const closeBtn = document.getElementById('calc-close-btn');
        if (closeBtn) closeBtn.addEventListener('click', toggleCalculator);

        // Bind toggle buttons on page
        document.querySelectorAll('#calc-mode-btn, .calc-mode-toggle').forEach(btn => {
            btn.addEventListener('click', toggleCalculator);
        });

        const keypad = calcPopup.querySelector('.calc-keypad');
        keypad.addEventListener('click', (e) => {
            const btn = e.target.closest('.calc-btn');
            if (!btn) return;

            const val = btn.dataset.val;
            const action = btn.dataset.action;

            if (val !== undefined) {
                appendInput(val);
            } else if (action) {
                handleAction(action);
            }
        });

        // Keyboard navigation
        window.addEventListener('keydown', (e) => {
            if (!calcPopup || !calcPopup.classList.contains('active')) return;

            if (e.key >= '0' && e.key <= '9') appendInput(e.key);
            else if (e.key === '.') appendInput('.');
            else if (e.key === '+') handleAction('+');
            else if (e.key === '-') handleAction('-');
            else if (e.key === '*') handleAction('*');
            else if (e.key === '/') handleAction('/');
            else if (e.key === '(') handleAction('(');
            else if (e.key === ')') handleAction(')');
            else if (e.key === 'Enter' || e.key === '=') handleAction('equals');
            else if (e.key === 'Backspace') handleAction('backspace');
            else if (e.key === 'Escape') toggleCalculator();
        });
    }

    let inputStr = "0";
    let isNewInput = true;

    function appendInput(val) {
        const inputEl = document.getElementById('calc-input');
        if (isNewInput || inputStr === "0") {
            inputStr = val === '.' ? "0." : val;
            isNewInput = false;
        } else {
            inputStr += val;
        }
        inputEl.value = inputStr;
    }

    function handleAction(action) {
        const inputEl = document.getElementById('calc-input');
        const historyEl = document.getElementById('calc-history');

        switch (action) {
            case 'clear':
                inputStr = "0";
                historyEl.textContent = "";
                isNewInput = true;
                break;

            case 'backspace':
                if (!isNewInput && inputStr.length > 0) {
                    inputStr = inputStr.slice(0, -1);
                    if (inputStr === "" || inputStr === "-") inputStr = "0";
                }
                break;

            case '+': case '-': case '*': case '/':
                if (isNewInput && historyEl.textContent !== "") {
                    historyEl.textContent = inputEl.value + " " + getSymbol(action) + " ";
                } else {
                    historyEl.textContent = inputStr + " " + getSymbol(action) + " ";
                }
                inputStr = "0";
                isNewInput = true;
                break;

            case 'pow':
                historyEl.textContent = inputStr + " ^ ";
                inputStr = "0";
                isNewInput = true;
                break;

            case 'sin': case 'cos': case 'tan': case 'log': case 'ln': case 'sqrt':
                evaluateSingleFn(action);
                break;

            case 'fact':
                evaluateFactorial();
                break;

            case 'recip':
                evaluateReciprocal();
                break;

            case 'pm':
                if (inputStr !== "0") {
                    inputStr = inputStr.startsWith('-') ? inputStr.slice(1) : '-' + inputStr;
                }
                break;

            case 'pi':
                inputStr = Math.PI.toString();
                isNewInput = false;
                break;

            case 'e':
                inputStr = Math.E.toString();
                isNewInput = false;
                break;

            case 'ans':
                inputStr = lastAns.toString();
                isNewInput = false;
                break;

            case 'deg':
                isDeg = !isDeg;
                document.getElementById('calc-deg-btn').textContent = isDeg ? "DEG" : "RAD";
                break;

            case '(': case ')':
                appendInput(action);
                break;

            case 'equals':
                calculateResult();
                break;
        }

        inputEl.value = inputStr;
    }

    function getSymbol(op) {
        if (op === '*') return '×';
        if (op === '/') return '÷';
        return op;
    }

    function evaluateSingleFn(fn) {
        let val = parseFloat(inputStr);
        if (isNaN(val)) return;

        let res = 0;
        let expr = "";

        if (fn === 'sin') {
            const rad = isDeg ? (val * Math.PI) / 180 : val;
            res = Math.sin(rad);
            expr = `sin(${val}${isDeg ? '°' : ''})`;
        } else if (fn === 'cos') {
            const rad = isDeg ? (val * Math.PI) / 180 : val;
            res = Math.cos(rad);
            expr = `cos(${val}${isDeg ? '°' : ''})`;
        } else if (fn === 'tan') {
            const rad = isDeg ? (val * Math.PI) / 180 : val;
            res = Math.tan(rad);
            expr = `tan(${val}${isDeg ? '°' : ''})`;
        } else if (fn === 'log') {
            res = Math.log10(val);
            expr = `log10(${val})`;
        } else if (fn === 'ln') {
            res = Math.log(val);
            expr = `ln(${val})`;
        } else if (fn === 'sqrt') {
            res = Math.sqrt(val);
            expr = `√(${val})`;
        }

        res = parseFloat(res.toFixed(8));
        document.getElementById('calc-history').textContent = `${expr} =`;
        inputStr = res.toString();
        lastAns = res;
        isNewInput = true;
    }

    function evaluateFactorial() {
        let n = parseInt(inputStr);
        if (isNaN(n) || n < 0) return;
        if (n > 170) {
            inputStr = "Infinity";
            isNewInput = true;
            return;
        }
        let fact = 1;
        for (let i = 2; i <= n; i++) fact *= i;
        document.getElementById('calc-history').textContent = `${n}! =`;
        inputStr = fact.toString();
        lastAns = fact;
        isNewInput = true;
    }

    function evaluateReciprocal() {
        let val = parseFloat(inputStr);
        if (isNaN(val) || val === 0) return;
        let res = 1 / val;
        res = parseFloat(res.toFixed(8));
        document.getElementById('calc-history').textContent = `1/(${val}) =`;
        inputStr = res.toString();
        lastAns = res;
        isNewInput = true;
    }

    function calculateResult() {
        const historyEl = document.getElementById('calc-history');
        const histText = historyEl.textContent;

        let fullExpr = "";
        if (histText.includes('^')) {
            const parts = histText.split('^');
            const base = parseFloat(parts[0]);
            const exp = parseFloat(inputStr);
            const res = Math.pow(base, exp);
            historyEl.textContent = `${base} ^ ${exp} =`;
            inputStr = parseFloat(res.toFixed(8)).toString();
            lastAns = parseFloat(inputStr);
            isNewInput = true;
            return;
        }

        if (histText && !histText.includes('=')) {
            let sanitizedHist = histText.replace(/×/g, '*').replace(/÷/g, '/');
            fullExpr = sanitizedHist + inputStr;
        } else {
            fullExpr = inputStr;
        }

        try {
            // Safe evaluation of mathematical arithmetic
            let evalExpr = fullExpr.replace(/π/g, Math.PI).replace(/e/g, Math.E);
            let res = Function('"use strict"; return (' + evalExpr + ')')();
            if (typeof res === 'number' && !isNaN(res)) {
                res = parseFloat(res.toFixed(8));
                historyEl.textContent = `${fullExpr} =`;
                inputStr = res.toString();
                lastAns = res;
                isNewInput = true;
            }
        } catch (err) {
            inputStr = "Error";
            isNewInput = true;
        }
    }

    function toggleCalculator() {
        if (!calcPopup) initCalculator();
        calcPopup.classList.toggle('active');
    }
    window.toggleCalculator = toggleCalculator;
    window.openCalculator = toggleCalculator;

    document.addEventListener('click', (e) => {
        if (e.target.closest('#calc-mode-btn, .calc-mode-toggle')) {
            toggleCalculator();
        }
    });

    function makeDraggable() {
        const header = document.getElementById('calc-header');
        if (!header) return;

        let isDragging = false;
        let offsetX = 0, offsetY = 0;

        header.addEventListener('mousedown', (e) => {
            isDragging = true;
            offsetX = e.clientX - calcPopup.offsetLeft;
            offsetY = e.clientY - calcPopup.offsetTop;
            header.style.cursor = 'grabbing';
        });

        window.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            calcPopup.style.left = `${e.clientX - offsetX}px`;
            calcPopup.style.top = `${e.clientY - offsetY}px`;
        });

        window.addEventListener('mouseup', () => {
            isDragging = false;
            if (header) header.style.cursor = 'move';
        });
    }

    // Auto init on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initCalculator);
    } else {
        initCalculator();
    }
})();
