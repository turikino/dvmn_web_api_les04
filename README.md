# Скрипты для работы с API SpaceX, Hubble и Instagram.

Скрипт `fetch_spacex.py` скачивает все фото с последнего запуска SpaceX.

Скрипт `fetch_hubble.py` скачивает по указанному номеру одно изображение с сайта [hubblesite.org](http://hubblesite.org).

Скрипт `upload_to_instagram.py` позволяет загрузить в аккаунт Instagram все изображения из указанной папки.


### Как установить

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Примеры использования

```python
>>> fetch_spacex.py -f spacex -p .../images/
...
images $ tree
.
├── spacex1.jpeg
├── spacex2.jpeg
├── spacex3.jpeg
├── spacex4.jpeg
├── spacex5.jpeg
└── spacex6.jpeg
```

```python
>>> fetch_hubble.py -i 4000 -p .../images/
...
images $ tree
.
└── Scale and Compass Image for Orion Nebula.png
```

```python
>>> upload_to_instagram.py -u XXXXXX -pass YYYYYY  -p .../images/
...
2019-02-17 15:41:22,849 - INFO - Instabot Started
2019-02-17 15:41:24,531 - INFO - Logged-in successfully as 'XXXXXX'!
2019-02-17 15:41:31,554 - INFO - Photo '.../images/Scale and Compass Image for Orion Nebula.png' is uploaded.
2019-02-17 15:41:32,108 - INFO - Bot stopped. Worked: 3 days, 15:29:38.190158
2019-02-17 15:41:32,109 - INFO - Total requests: 80
```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
