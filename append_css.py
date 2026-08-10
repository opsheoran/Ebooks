with open('common_style.css', 'a', encoding='utf-8') as f:
    f.write('''
/* SPA and Dual Language Toggle Logic */
.section-card { display: none; }
.section-card.active { display: block; }

.hinglish-content { display: none; }
.hinglish-active .english-content { display: none; }
.hinglish-active .hinglish-content { display: block; }

/* QUIZ STYLES (if missing) */
.question-box { margin-bottom: 30px; border-bottom: 1px dashed var(--border); padding-bottom: 20px; }
.question { font-weight: 600; margin-bottom: 10px; color: var(--navy); }
.mcq-options { list-style: none; margin-left: 0; padding-left: 0; }
.mcq-options li { margin-bottom: 5px; }
.toggle-btn { background: var(--navy); color: #fff; border: none; padding: 7px 18px; border-radius: 20px; cursor: pointer; font-family: 'DM Sans', sans-serif; font-size: .82rem; font-weight: 500; margin: 10px 0; transition: all .25s; }      
.toggle-btn:hover { background: var(--navy-light); }
.answer { display: none; background: #F0FBF5; border-left: 4px solid var(--sage); padding: 16px 20px; margin: 10px 0; border-radius: 0 8px 8px 0; color: var(--text-dark); font-size: .97rem; }
.answer.show { display: block; }

.lang-toggle-btn { position: sticky; top: 90px; float: right; background: var(--gold); color: var(--navy); border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-family: 'DM Sans', sans-serif; font-weight: 600; z-index: 100; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
''')
