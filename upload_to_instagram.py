import os
from instabot import Bot
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description='Загружает все фото из папки в указанный аккаунт Instagram.')
    parser.add_argument('-p', '--path', help='Путь к папке:')
    parser.add_argument('-u', '--username', help='Login Instagram:')
    parser.add_argument('-pass', '--password', help='Password Instagram:')
    return parser


def upload_image_to_instagram(path, username, password):
    """
    Загружает все фото из папки в указанный аккаунт Instagram.
    :param path: srt -- путь к папке с фото
    :param username: str -- login Instagram
    :param password: srt -- password Instagram
    :return:
    """
    bot = Bot()
    bot.login(username=username, password=password)
    for root, dirs, images in os.walk(path):
        for image in images:
            if not image.startswith('.'):
                image_path = os.path.join(root, image)
                image_name = image.split('.')[0]
                bot.upload_photo(image_path, caption=image_name)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    path = args.path
    username = args.username
    password = args.password
    upload_image_to_instagram(path, username, password)