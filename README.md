[Готовый слайд2.html](https://github.com/user-attachments/files/29184633/2.html)
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Презентация проекта: Поиск отелей на Django</title>
    <!-- Базовые автономные стили структуры слайдов -->
    <style>
        html,body{width:100%;height:100%;overflow:hidden;margin:0;padding:0;background:#282a36;color:#f8f8f2;font-family:sans-serif}
        .slides-container{position:relative;width:100%;height:100%;display:flex;align-items:center;justify-content:center}
        .slide{position:absolute;opacity:0;visibility:hidden;transition:opacity .4s ease,visibility .4s;text-align:center;max-width:900px;width:90%;padding:20px;box-sizing:border-box}
        .slide.active{opacity:1;visibility:visible}
        h1,h2,h3{font-weight:700;margin-top:0}
        h1{color:#50fa7b;font-size:2.5em}
        h2{color:#8be9fd;border-bottom:2px solid #6272a4;padding-bottom:10px;font-size:2em}
        .highlight-text{color:#ff79c6;font-weight:bold}
        ul{font-size:1.1em;line-height:1.6;text-align:left;display:inline-block;margin:0 auto}
        p{font-size:1.1em;line-height:1.5}
        .controls{position:fixed;bottom:20px;right:20px;display:flex;gap:10px;z-index:1000}
        .btn{background:#44475a;color:#f8f8f2;border:none;padding:10px 15px;font-size:1.2em;border-radius:5px;cursor:pointer;user-select:none;transition:background .2s}
        .btn:hover{background:#6272a4}
        .progress-bar{position:fixed;bottom:0;left:0;height:5px;background:#50fa7b;width:0%;transition:width .3s ease;z-index:1000}
        .code-box{background:#1d1f27;color:#f8f8f2;padding:15px;border-radius:5px;text-align:left;font-family:monospace;font-size:0.85em;overflow-x:auto;white-space:pre;line-height:1.4;border-left:4px solid #ff79c6}
        .grid-2{display:grid;grid-template-columns:1fr 1fr;gap:20px;text-align:left}
        .card{background:#44475a;padding:15px;border-radius:8px;font-size:0.9em}
        .keyword{color:#ff79c6;font-weight:bold}
        .func{color:#50fa7b}
        .comment{color:#6272a4;font-style:italic}
    </style>
</head>
<body>

    <div class="progress-bar" id="progress"></div>

    <div class="slides-container">

        <!-- Слайд 1 -->
        <div class="slide active">
            <h1>Поиск Жилья</h1>
            <p>Платформа для поиска и точечного бронирования отелей</p>
            <p style="font-size: 0.8em; margin-top: 50px; color: #6272a4;">
                Разработчик: <span class="highlight-text">Олег</span><br>
                Стек: Python / Django / PostgreSQL
            </p>
        </div>


<style>
        * {
            box-sizing: border-box;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }
        html, body {
            margin: 0; padding: 0; width: 100%; height: 100%;
            background-color: #0b0c10;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            color: #ffffff;
            overflow: hidden;
        }
        
        .wrapper {
            width: 100%; height: 100%;
            display: flex; justify-content: center; align-items: center;
        }

        .slide {
            display: none;
            width: 297mm; height: 210mm;
            padding: 22mm 25mm;
            background: #11141a;
            border-radius: 12px;
            box-shadow: 0 30px 60px rgba(0,0,0,0.8);
            border: 1px solid rgba(0, 255, 204, 0.1);
        }
        
        .slide.active {
            display: flex;
            flex-direction: row; /* Текст слева, графика справа */
            align-items: center;
            justify-content: space-between;
        }

        .content { width: 55%; }
        .visual-side { width: 40%; display: flex; justify-content: center; align-items: center; }

        .slide-num { font-size: 14px; color: #00ffcc; font-weight: bold; font-family: monospace; margin-bottom: 15px; text-transform: uppercase; letter-spacing: 3px; }
        h1 { font-size: 42px; font-weight: 800; line-height: 1.2; margin: 0 0 20px 0; color: #ffffff; letter-spacing: -1px; text-transform: uppercase; }
        .highlight { color: #00ffcc; }
        p { font-size: 18px; line-height: 1.5; color: #cbd5e1; margin: 0 0 20px 0; font-weight: 300; }
        ul { margin: 0; padding-left: 20px; color: #94a3b8; }
        li { font-size: 16px; line-height: 1.5; margin-bottom: 12px; }
        li strong { color: #ffffff; }
        
        /* СТИЛЬНЫЕ КНОПКИ */
        .navigation { position: fixed; bottom: 30px; right: 30px; display: flex; gap: 15px; z-index: 100; }
        .nav-btn {
            background-color: rgba(0, 255, 204, 0.1); color: #00ffcc; border: 2px solid #00ffcc;
            padding: 12px 24px; font-size: 16px; font-weight: bold; border-radius: 6px;
            cursor: pointer; transition: all 0.2s ease; text-transform: uppercase; letter-spacing: 1px;
        }
        .nav-btn:hover { background-color: #00ffcc; color: #0b0c10; box-shadow: 0 0 15px rgba(0, 255, 204, 0.4); }
        .nav-btn:disabled { border-color: #475569; color: #475569; background-color: transparent; cursor: not-allowed; box-shadow: none; }

        .progress-timeline { position: fixed; top: 0; left: 0; height: 4px; background-color: #00ffcc; width: 0%; transition: width 0.3s ease; z-index: 1000; }
    </style>
</head>
<body>

    <div class="progress-timeline" id="progress"></div>

    <div class="wrapper">

        <!-- СЛАЙД 2 -->
        <div class="slide active">
            <div class="content">
                <div class="slide-num">// Разработка веб-приложения</div>
                <h1>Удобный поиск отелей: <br><span class="highlight">Новый взгляд на путешествия</span></h1>
                <p>Подробный разбор сайта на Django, созданного для быстрого, безопасного и максимально честного поиска жилья без скрытых условий.</p>
            </div>
            <!-- Векторное изображение 1: Здание отеля с рейтингом звезд -->
            <div class="visual-side">
                <svg width="300" height="350" viewBox="0 0 100 120" fill="none" stroke="#00ffcc" stroke-width="1.5">
                    <rect x="20" y="30" width="60" height="85" rx="2" />
                    <line x1="20" y1="45" x2="80" y2="45" />
                    <line x1="20" y1="65" x2="80" y2="65" />
                    <line x1="20" y1="85" x2="80" y2="85" />
                    <line x1="50" y1="30" x2="50" y2="115" />
                    <rect x="42" y="100" width="16" height="15" fill="#11141a"/>
                    <!-- Звезды отеля сверху -->
                    <path d="M50 5 l2 4 h4 l-3 3 l1 4 l-4-2 l-4 2 l1-4 l-3-3 h4 z" fill="#00ffcc"/>
                    <path d="M35 8 l2 4 h4 l-3 3 l1 4 l-4-2 l-4 2 l1-4 l-3-3 h4 z" fill="#00ffcc"/>
                    <path d="M65 8 l2 4 h4 l-3 3 l1 4 l-4-2 l-4 2 l1-4 l-3-3 h4 z" fill="#00ffcc"/>
                </svg>
            </div>
        </div>

<!-- СЛАЙД 3-->
        <div class="slide">
            <div class="content">
                <div class="slide-num">// С какими проблемами мы боремся</div>
                <h1>Что делает старые сайты <br><span class="highlight">неудобными для людей?</span></h1>
                <p>Большинство крупных агрегаторов сегодня перегружены функциями, которые мешают пользователям:</p>
                <ul>
                    <li><strong>Визуальный хаос и реклама:</strong>  Реклама, баннеры и всплывающие окна отвлекают от выбора жилья.</li>
                    <li><strong>Искусственная паника:</strong> Стрессовые плашки «Успей забронировать - остался последний номер!».</li>
                    <li><strong>Долгое ожидание:</strong> Медленная загрузка тяжелых скриптов со смартфона.</li>
                </ul>
            </div>
            <!-- Векторное изображение 2: Перечеркнутый знак колокольчика / спама -->
            <div class="visual-side">
                <svg width="300" height="350" viewBox="0 0 100 100" fill="none" stroke="#ff5555" stroke-width="1.5">
                    <circle cx="50" cy="50" r="40" stroke-dasharray="4 4" />
                    <path d="M50 20 C40 20 35 30 35 45 L30 60 L70 60 L65 45 C65 30 60 20 50 20 Z" />
                    <path d="M45 60 C45 65 55 65 55 60" />
                    <!-- Линия перечеркивания проблемы -->
                    <line x1="20" y1="20" x2="80" y2="80" stroke-width="3"/>
                </svg>
            </div>
        </div>

 <!-- СЛАЙД 4 -->
        <div class="slide">
            <div class="content">
                <div class="slide-num">// Наш подход</div>
                <h1>Радикальный минимализм <br><span class="highlight">и забота о пользователе</span></h1>
                <p>Мы полностью перестроили логику сайта, убрав маркетинговые уловки и оставив только пользу:</p>
                <ul>
                    <li><strong>Чистый дизайн:</strong> Только реальные фотографии номеров и честные оценки.</li>
                    <li><strong>Абсолютная честность:</strong> Окончательная цена проживания с самого первого клика.</li>
                    <li><strong>Поиск за одну секунду:</strong> Прямая связь гостя и отельера.</li>
                </ul>
            </div>
            <!-- Векторное изображение 3: Кровать (комфортный номер) + Ключ-карта доступа -->
            <div class="visual-side">
                <svg width="300" height="350" viewBox="0 0 100 100" fill="none" stroke="#00ffcc" stroke-width="1.5">
                    <!-- Рисунок кровати отеля -->  
                    <path d="M10 70 V40 M10 50 H90 V70 M90 40 V70" stroke-width="2"/>
                    <path d="M20 50 V43 H40 V50" />
                    <rect x="65" y="20" width="20" height="30" rx="2" stroke-dasharray="2 2" transform="rotate(15 65 20)"/>
                    <circle cx="50" cy="25" r="5" />
                </svg>
              </div>
            </div>
        </div>

<!-- СЛАЙД 5 -->
<div class="slide" id="slide5">
    <svg class="bg-icon icon-top-left" width="180" height="80" viewBox="0 0 100 30"><path d="M10 15 l2 4 h4 l-3 3 l1 4 l-4-2 l-4 2 l1-4 l-3-3 h4 z M30 15 l2 4 h4 l-3 3 l1 4 l-4-2 l-4 2 l1-4 l-3-3 h4 z M50 15 l2 4 h4 l-3 3 l1 4 l-4-2 l-4 2 l1-4 l-3-3 h4 z"/></svg>
    <div class="slide-body" style="display: flex; flex-direction: row; align-items: center; justify-content: space-between;">
        
        <!-- Левая колонка с текстом (занимает 55% ширины) -->
        <div class="content" style="width: 55%; flex-shrink: 0;">
            <div class="slide-num">// Почему это надежно</div>
            <h1>Главные технические <br><span class="highlight">преимущества Django</span></h1>
            <p>Выбор фреймворка Django обеспечивает проекту фундаментальную стабильность и долговечность:</p>
            <ul>
                <li><strong>Защита данных:</strong> Встроенная система безопасности защищает профили и пароли пользователей от взломов.</li>
                <li><strong>Стабильность при нагрузках:</strong> Оптимизированный код позволяет сайту работать без зависаний в пиковый сезон.</li>
                <li><strong>Личный кабинет:</strong> Надежная система профилей для проверки статуса брони и скачивания ваучеров.</li>
            </ul>
        </div>
        
        <!-- Правая колонка с графикой (занимает 40% ширины) -->
        <div class="visual-side" style="width: 40%; flex-shrink: 0; display: flex; justify-content: center; align-items: center;">
            <svg width="300" height="350" viewBox="0 0 100 100" fill="none" stroke="#00ffcc" stroke-width="1.5">
                <path d="M50 15 L80 25 V55 C80 75 50 90 50 90 C50 90 20 75 20 55 V25 Z" stroke-width="2"/>
                <path d="M35 48 L45 58 L65 38" stroke="#50fa7b" stroke-width="2"/>
            </svg>
        </div>

    </div>
</div>

     <!-- СЛАЙД 6 -->
        <div class="slide" id="slide6">
            <div class="slide-body" style="display: flex; flex-direction: row; align-items: center; justify-content: space-between;">
                <div class="content" style="width: 55%; flex-shrink: 0;">
                    <div class="slide-num">// Простота реализации в коде</div>
                    <h1>Автоматический <br><span class="highlight">учет свободных мест</span></h1>
                    <p>Логика списания остатков номеров перенесена напрямую в метод сохранения модели Django, гарантируя стабильность без внешних библиотек:</p>
                    <pre>
<span class="code-keyword">def</span> <span class="code-func">save</span>(self, *args, **kwargs
    <span class="code-keyword">if</span> self.hotel.available_rooms &gt; 0:
        self.hotel.available_rooms -= 1
        self.hotel.save()
    <span class="code-keyword">super</span>().save(*args, **kwargs)</pre>
                </div>
                <div class="visual-side" style="width: 40%; flex-shrink: 0; display: flex; justify-content: center; align-items: center;">
                    <svg width="250" height="250" viewBox="0 0 100 100" fill="none" stroke="#00ffcc" stroke-width="1.5">
                        <rect x="20" y="20" width="60" height="60" rx="5" />
                        <path d="M35 40 H65 M35 50 H55 M35 60 H45" stroke-linecap="round"/>
                        <path d="M65 60 L70 65 L80 55" stroke="#50fa7b" stroke-width="2"/>
                    </svg>
                </div>
            </div>
        </div>

 <!-- Слайд 7 (ТЕПЕРЬ ПОЛНЫЙ АНАЛОГ СЛАЙДА 6) -->
        <div class="slide">
            <div style="width: 100%; text-align: center;">
                <h2>Планы развития (Roadmap)</h2>
                <!-- Убрали inline-block, заменили на block с центрированием самого контейнера через margin -->
                <ul style="list-style: none; padding: 0; text-align: left; display: block; max-width: 600px; margin: 20px auto 0 auto;">
                    <li style="margin-bottom: 15px;">💳 <span class="highlight-text">Этап 1:</span> Интеграция платежного шлюза (ЮKassa / Stripe).</li>
                    <li style="margin-bottom: 15px;">🤖 <span class="highlight-text">Этап 2:</span> Подключение Telegram-бота для мгновенных уведомлений.</li>
                    <li style="margin-bottom: 15px;">🧠 <span class="highlight-text">Этап 3:</span> Внедрение алгоритма умных рекомендаций отелей.</li>
                </ul>
            </div>
        </div>

        <!-- СЛАЙД 8 (ПОЛНЫЙ АНАЛОГ СЛАЙДА 6) -->
        <div class="slide" id="slide7">
            <div class="slide-body" style="display: flex; flex-direction: row; align-items: center; justify-content: space-between;">
                <div class="content" style="width: 55%; flex-shrink: 0;">
                    <div class="slide-num">// Заключение</div>
                    <h1>Спасибо <br><span class="highlight">за внимание!</span></h1>
                    <p>Проект готов к развертыванию</p>
                    <div style="font-size: 18px; color: #cbd5e1; margin-top: 20px; line-height: 1.8;">
                        🌐 <b>Email:</b> your_email@example.com <br>
                        💻 <b>GitHub:</b> ://github.com
                    </div>
                </div>
                <!-- Векторная графика финала (зеленая кнопка Play/Запуск проекта), вставленная точно так же, как в слайде 6 -->
                <div class="visual-side" style="width: 40%; flex-shrink: 0; display: flex; justify-content: center; align-items: center;">
                    <svg width="250" height="250" viewBox="0 0 100 100" fill="none" stroke="#00ffcc" stroke-width="1.5">
                        <circle cx="50" cy="50" r="40"/>
                        <path d="M42 35 L68 50 L42 65 Z" fill="#50fa7b" stroke="#50fa7b"/>
                    </svg>
                </div>
            </div>
        </div>

 <div class="navigation">
        <button class="nav-btn" id="prevBtn">Назад</button>
        <button class="nav-btn" id="nextBtn">Вперед</button>
    </div>

    <script>
        const slides = document.querySelectorAll('.slide');
        const prevBtn = document.getElementById('prevBtn');
        const nextBtn = document.getElementById('nextBtn');
        const progress = document.getElementById('progress');
        let currentIdx = 0;

        function updatePresentation() {
            slides.forEach((slide, idx) => {
                if (idx === currentIdx) {
                    slide.classList.add('active');
                } else {
                    slide.classList.remove('active');
                }
            });

            prevBtn.disabled = (currentIdx === 0);
            nextBtn.disabled = (currentIdx === slides.length - 1);

            // Защита от деления на ноль, если слайд всего один
            const totalSteps = slides.length - 1;
            const percentage = totalSteps > 0 ? (currentIdx / totalSteps) * 100 : 0;
            progress.style.width = percentage + '%';
        }

        function changeSlide(direction) {
            if (direction === 'next' && currentIdx < slides.length - 1) {
                currentIdx++;
            } else if (direction === 'prev' && currentIdx > 0) {
                currentIdx--;
            }
            updatePresentation();
        }

        nextBtn.addEventListener('click', () => changeSlide('next'));
        prevBtn.addEventListener('click', () => changeSlide('prev'));

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === ' ') {
                e.preventDefault();
                changeSlide('next');
            } else if (e.key === 'ArrowLeft') {
                e.preventDefault();
                changeSlide('prev'); /* ИСПРАВЛЕНО: Вместо prevSlide() вызывается правильная функция */
            }
        });

        updatePresentation();
    </script>
</body>
</html>
