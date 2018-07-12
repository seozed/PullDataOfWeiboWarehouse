# -*- coding:utf-8 -*-
"""
DATE: 2018-07-12
"""
import requests
import settings
import json
import os


def fetch_data(url):
    response = requests.get(url)
    return response.text


def process_data(data):
    """
    转换来自API接口的内容为易捷指定的格式
    :param data:
    :type data:
    :return:
    :rtype: str
    """
    item = json.loads(data)
    text = item['content']
    images = "|".join(split_basename(url) for url in item['img_url'])
    content = "{images}&{text}".format(images=images, text=text)

    for img_url in item['img_url']:
        download_image(img_url)

    return content


def download_image(url):
    response = requests.get(url)
    filename = os.path.join(os.getcwd(), settings.OUTPUT_DIR, "images", split_basename(url))
    with open(filename, 'wb') as img_file:
        img_file.write(response.content)



def split_basename(url):
    filename = url.split('/')[-1]
    return filename


def save_to_file(content, path=None):
    if not path:
        path = settings.OUTPUT_FILE

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content + "\n")


def run():
    content_list = []
    for i in range(1, settings.PULL_COUNT+1):
        print("Start asyncing no.{count} article.".format(count=i))
        data = fetch_data(settings.API_URL)
        content_list.append(process_data(data))

    content = "\n".join(content_list)
    save_to_file(content)

    print("{count} article have been synced.".format(count=settings.PULL_COUNT))


if __name__ == '__main__':
    run()
