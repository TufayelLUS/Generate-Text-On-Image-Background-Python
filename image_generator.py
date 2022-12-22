from pilmoji import Pilmoji
from PIL import Image, ImageFont


# pip3 install Pillow
# pip3 install pilmoji


def generateImageFromText(text):
    width = 512 # set width
    height = 512 # set height
    message = text
    # font family and font size can be set below
    font = ImageFont.truetype("arial.ttf", size=40)
    # change color to anything else for changing the background color of the image
    img = Image.new('RGB', (width, height), color='black')

    imgDraw = Pilmoji(img)
    # imgDraw.text((x_coordinate, y_cooridinate), text_to_type, font=font_to_use, fill=(colors_in_rgb_numbers))
    imgDraw.text((10, 10), message, font=font, fill=(255, 255, 255), stroke_width=1, stroke_fill="white")
    # below line generates non bold text while above line generates a bold text
    imgDraw.text((10, 10), message, font=font, fill=(255, 255, 255))

    img.save('result.png')


if __name__ == "__main__":
    generateImageFromText("Hello boss!\nthis works🏠")
