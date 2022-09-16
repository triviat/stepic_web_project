<h1>Инструкция по установке и настройке django проекта:</h1>

<ul>
<h2>Подготовка сервера:</h2>

<li>
<p>Клонирование проекта с github</p>
<code>sudo git clone https://github.com/triviat/stepic_web_project web</code>
</li>

<li>
<p>Переход в директорию проекта</p>
<code>cd web</code>
</li>

<li>
<p>Установка python3.X-venv (где X - версия python) и nginx</p>
<code>sudo apt install python3.X-venv nginx</code>
</li>

<li>
<p>Создание и активация виртуального окружение web</p>
<p><code>python3 -m venv web</code></p>
<code>. ./web/bin/activate</code>
</li>

<li>
<p>Установка django и gunicorn</p>
<code>pip install django gunicorn</code>
</li>

<li>
<p>Запуск init скрипта</p>
<code>sudo bash init.sh</code>
</li>
</ul>

<ul>
<h2>Настройка django:</h2>

<li>
<p>Создание django-проекта</p>
<code>django-admin startproject ask</code>
</li>

<li>
<p>Переход к файлу администрирования manage.py</p>
<code>cd ask</code>
</li>

<li>
<p>Создание приложения qa</p>
<code>python manage.py startapp qa</code>
</li>


<li>
<p>Добавление приложения в настройки проекта</p>
В файл <code>~/web/ask/ask/settings.py</code> в <b>INSTALLED_APPS</b> добавить приложение <b>'qa'</b>
</li>
</ul>
