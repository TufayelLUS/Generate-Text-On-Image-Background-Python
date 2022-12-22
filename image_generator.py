from pilmoji import Pilmoji
from PIL import Image, ImageFont


# pip3 install Pillow
# pip3 install pilmoji


def generateImageFromText(text):
    width = 512 # set width
    height = 512 # set height
    message = text
    font = ImageFont.truetype("arial.ttf", size=40)

    img = Image.new('RGB', (width, height), color='black')

    imgDraw = Pilmoji(img)

    imgDraw.text((10, 10), message, font=font, fill=(255, 255, 255), stroke_width=1, stroke_fill="white")

    img.save('result.png')


if __name__ == "__main__":
    generateImageFromText("Hello boss!\nthis works🏠")
