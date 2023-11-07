from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk

root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir='/Users/Isaac/PycharmProjects/website/picture', title='Select an Image')

def add_watermark(image, wm_text):
    opened_image = Image.open(image)

    image_width, image_height = opened_image.size
    draw = ImageDraw.Draw(opened_image)

    font_size = int(image_width / 8)

    font = ImageFont.truetype('arial.ttf', font_size)

    x, y = int(image_width/2), int(image_height/2)

    draw.text((x,y), wm_text, font=font, fill='#FFF', stroke_width=5, stroke_fill='#222', anchor='ms')

    opened_image.show()

add_watermark(filename, 'Aloha Hut')