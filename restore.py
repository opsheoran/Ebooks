import sys

html_suffix = """</div>

    </main>

    <footer class="book-footer">
        <p>Design and developed by <strong>Prof. O.P. Sheoran</strong>, Department of Mathematics and Statistics,<br>
        CCS Haryana Agricultural University, Hisar</p>
    </footer>
</body>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const hash = window.location.hash.substring(1);
        if (hash && document.getElementById(hash)) {
            showTopic(hash);
        } else {
            const firstSec = document.querySelector('.topic-section');
            if(firstSec) showTopic(firstSec.id);
        }
    });

    let isHinglish = false;
    function toggleLanguage() {
        isHinglish = !isHinglish;
        const btnText = document.getElementById('lang-toggle-text');
        const engContents = document.querySelectorAll('.english-content');
        const hinContents = document.querySelectorAll('.hinglish-content');

        if (isHinglish) {
            btnText.innerHTML = '<i class="fas fa-language"></i> Switch Language (English)';
            engContents.forEach(el => el.style.display = 'none');
            hinContents.forEach(el => el.style.display = 'block');
        } else {
            btnText.innerHTML = '<i class="fas fa-language"></i> Switch Language (Hinglish)';
            hinContents.forEach(el => el.style.display = 'none');
            engContents.forEach(el => el.style.display = 'block');
        }
    }

    function showTopic(id) {
        document.querySelectorAll('.topic-section').forEach(el => {
            el.classList.remove('active');
        });
        document.querySelectorAll('.nav-link').forEach(el => {
            el.classList.remove('active');
        });
        
        const targetSection = document.getElementById(id);
        if (targetSection) {
            targetSection.classList.add('active');
        }
        
        const activeLink = document.querySelector(`.nav-link[href="#${id}"]`);
        if (activeLink) {
            activeLink.classList.add('active');
        }
        
        window.scrollTo(0,0);
        
        if (window.innerWidth <= 768) {
            document.getElementById('sidebar').classList.remove('open');
        }
        
        try {
            history.replaceState(null, null, '#' + id);
        } catch (e) {
            console.warn('History state update failed:', e);
        }
    }

    document.addEventListener("DOMContentLoaded", function() {
        const navItems = document.querySelectorAll('.sidebar .nav-list > .nav-item:not(.nav-sub)');
        navItems.forEach(item => {
            let nextEl = item.nextElementSibling;
            const subItems = [];
            while (nextEl && nextEl.classList.contains('nav-sub')) {
                subItems.push(nextEl);
                nextEl.style.display = 'none';
                nextEl = nextEl.nextElementSibling;
            }
            if (subItems.length > 0) {
                const link = item.querySelector('.nav-link');
                if (link) {
                    const arrow = document.createElement('span');
                    arrow.innerHTML = ' &#9660;';
                    arrow.style.fontSize = '0.8em';
                    arrow.style.float = 'right';
                    arrow.style.marginTop = '2px';
                    arrow.style.transition = 'transform 0.3s';
                    link.appendChild(arrow);
                    link.addEventListener('click', function() {
                        const isHidden = subItems[0].style.display === 'none';
                        arrow.style.transform = isHidden ? 'rotate(180deg)' : 'rotate(0deg)';
                        subItems.forEach(sub => {
                            sub.style.display = isHidden ? 'list-item' : 'none';
                        });
                    });
                }
            }
        });
    });

    function toggleSidebar() { document.getElementById('sidebar').classList.toggle('open'); }

    function toggleAnswer(id) {
        const answer = document.getElementById(id);
        const btn = event.target;
        if (answer.classList.contains('show')) {
            answer.classList.remove('show');
            btn.innerHTML = 'Show Answer ▼';
        } else {
            answer.classList.add('show');
            btn.innerHTML = 'Hide Answer ▲';
        }
    }
</script>
<script src="../whiteboard/whiteboard.js?v=2.0"></script>
</html>"""

with open('Stat-101/Unit-IV.html', 'a', encoding='utf-8') as f:
    f.write(html_suffix)

print("Restored missing footer and scripts")
