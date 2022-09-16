<h1>Инструкция по установке и настройке django проекта:</h1>

<ul>
<h2>Подготовка сервера:</h2>

[//]: # (Клонирование проекта с github)
<li><code>sudo git clone https://github.com/triviat/stepic_web_project web</code></li>

[//]: # (Переход в директорию проекта)
<li><code>cd web</code></li>

[//]: # (Запуск init скрипта)
<li><code>sudo bash init.sh</code></li>
</ul>

<ul>
<h2>Установка и настройка django:</h2>

[//]: # (Создание django-проекта)
<li><code>django-admin startproject ask</code></li>

[//]: # (Переход к файлу администрирования manage.py)
<li><code>cd ask</code></li>

[//]: # (Создание приложения qa)
<li><code>python manage.py startapp qa</code></li>

[//]: # (Добавление приложения в настройки проекта)
<li>В файл <code>~/web/ask/ask/settings.py</code> в <b>INSTALLED_APPS</b> добавить приложение <b>'qa'</b></li>
</ul>
