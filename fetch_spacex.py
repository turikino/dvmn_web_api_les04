import requests
import os
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description='Скачивает фото с последнего запуска SpaceX.')
    parser.add_argument('-p', '--path', help='Путь к папке:')
    parser.add_argument('-f', '--filename', help='Название для файла:')
    return parser


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
        full_name = '{}{}{}.jpeg'.format(path, filename, number + 1)
        with open(full_name, 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    path = args.path
    filename = args.filename
    fetch_spacex_last_lanch(path, filename)