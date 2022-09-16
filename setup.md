<h1>Инструкция по установке и настройке django проекта:</h1>

<ul>
<h2>Подготовка сервера:</h2>

<p>Клонирование проекта с github</p>
<li><code>sudo git clone https://github.com/triviat/stepic_web_project web</code></li>

<p>Переход в директорию проекта</p>
<li><code>cd web</code></li>

<p>Установка python3.X-venv (где X - версия python) и nginx</p>
<li><code>sudo apt install python3.X-venv nginx</code></li>

<p>Создание и активация виртуального окружение web</p>
<li><code>python3 -m venv web</code></li>
<li><code>. ./web/bin/activate</code></li>

<p>Установка django и gunicorn</p>
<li><code>pip install django gunicorn</code></li>

<p>Запуск init скрипта</p>
<li><code>sudo bash init.sh</code></li>
</ul>

<ul>
<h2>Настройка django:</h2>

<p>Создание django-проекта</p>
<li><code>django-admin startproject ask</code></li>

<p>Переход к файлу администрирования manage.py</p>
<li><code>cd ask</code></li>

<p>Создание приложения qa</p>
<li><code>python manage.py startapp qa</code></li>

<p>Добавление приложения в настройки проекта</p>
<li>В файл <code>~/web/ask/ask/settings.py</code> в <b>INSTALLED_APPS</b> добавить приложение <b>'qa'</b></li>
</ul>

<ul>
<h2>Установка и настройка gunicorn:</h2>

<p>Установка gunicorn</p>
<li><code>pip install gunicorn</code></li>
</ul>
