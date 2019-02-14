import requests
import os


def fetch_spacex_last_lanch(path, filename):
    """
    Скачивает фото с последнего запуска SpaceX.
    :param path: str -- локальный путь к папке, куда положить файлы
    :param filename: str -- имя для скачанных файлов
    :return:
    """
    url = "https://api.spacexdata.com/v3/launches/latest"
    response = requests.get(url)
    spacex_links = response.json()['links']['flickr_images']
    os.makedirs(os.path.dirname(path), exist_ok=True)
    for number, url in enumerate(spacex_links):
        response = requests.get(url)
        full_name = path + filename + str(number + 1) + '.jpeg'
        with open(full_name, 'wb') as file:
            file.write(response.content)