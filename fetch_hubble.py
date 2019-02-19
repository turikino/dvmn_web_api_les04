import requests
import os
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description='Скачивает одно изображение с указанным номером.')
    parser.add_argument('-p', '--path', help='Путь к папке:')
    parser.add_argument('-i', '--image_id', help='Номер изображения:')
    return parser


def fetch_hubble_image(path, image_id):
    """
    Скачивает одно изображение с указанным номером.
    :param path: str -- локальный путь к папке, куда положить файл
    :param image_id: int -- номер изображения из коллекции http://hubblesite.org
    :return:
    """
    url = "http://hubblesite.org/api/v3/image/{}".format(image_id)
    response = requests.get(url)
    image_link = response.json()['image_files'][-1]['file_url']
    filename = response.json()['name'].replace('/', '-')
    image_extention = os.path.splitext(image_link)[-1]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    response = requests.get(image_link)
    full_name = path + filename + '.' + image_extention
    with open(full_name, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    path = args.path
    image_id = args.image_id
    fetch_hubble_image(path, image_id)