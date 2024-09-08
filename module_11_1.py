from pprint import pprint

from PIL import Image
from PIL import ImageFilter
import requests
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np

#библиотека PIL позволила открывать и обрабатывать изображения, менять формат изображений
img = Image.open("domik.jpg")
img = img.filter(ImageFilter.BoxBlur(8))
img.show()
img.save("domik.png")
img1 = Image.open("fly.jpg")
img2 = Image.open("domik.png")
img = Image.blend(img1,img2, 0.4)
img.show()

#requests
# отправляет запросы на веб-страницы, автоматически декодирует двоичную информацию с сайта обратно в изображение
r = requests.get('https://vk.ru')
pprint(r.text)
url = ('https://get.wallhere.com'
       '/photo/2048x1280-px-animals-baby-cat-cats-cute-fat-fluffy-grass-grey-kitten-kittens-1913313.jpg')
ri = requests.get(url)
i = Image.open(BytesIO(ri.content))
i.show()

#matplotlib
#позволяет строить графики и удобно визуализировать информацию
fig, ax = plt.subplots()
ax.plot([1, 1, 4, 4, 1], [1, 10, 10, 5, 5])
ax.set_xlabel('Hello')
ax.set_ylabel('World')
ax.set_title("My experiment")
plt.show()


