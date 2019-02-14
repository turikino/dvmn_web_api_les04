import os
from instabot import Bot


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