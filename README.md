# TZ_appCode - техническое задание в файле TZ.md

<h2>Задача №2</h2>

Реализовать API, которое на HTTP-запрос `GET /weather?city=<city_name>`,
где `<city_name>` - это название города на английском языке, 
возвращает текущую температуру в этом городе в градусах Цельсия, атомсферное давление (мм рт.ст.) и скорость ветра (м/c).
При первом запросе, сервис должен получать данные о погоде от https://openweathermap.org,
при последующих запросах для этого города в течение получаса запросы на сервис openweathermap.com происходить не должны.

<b>Дополнително сделано:</b>
<ul>
  <li>Регистр букв в название города не важен</li>
  <li>Можно легко изменить время обновления данных изменив <code>interval=30</code> в функции <code>weather.main.update_check_time</code></li>
  <li>Также дополнительно в ответе приходит: ID , название города , последнее время обновления данных</li>
</ul>

<b>Установка:</b>
<pre>
# Скачивание пакета с  github
$ git clone https://github.com/impuls64s/TZ_appCode.git
$ cd TZ_appCode/task2

# Установка виртуального окружения и установка зависимостей
$ python -m venv env
$ env\Scripts\activate.bat - для Windows;
$ source env/bin/activate - для Linux и MacOS.
$ python -m pip install -r requirements. txt

# Запуск приложения 
$ python manage.py runserver

# http://127.0.0.1:8000/weather/ - список всех данных
# http://127.0.0.1:8000/weather/weather?city=<city_name> - инфо вашего города

# Остановка приложения и деактивация виртуального приложения
$ Ctrl + c
$ deactivate
</pre>
