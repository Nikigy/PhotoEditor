from kivy.app import App
from kivy.uix.screenmanager import Screen
from PIL import Image, ImageOps, ImageDraw
import os

class PhotoEditorApp(App):
    pass

class PhotoEditorScreen(Screen):

    def load_image(self):        
        filename = self.ids.filename.text
        image = Image.open(filename)
        temp_filename = os.path.splitext(filename)[0] + '_temp' + os.path.splitext(filename)[1]
        image.save(temp_filename)

        self.ids.image.source = temp_filename
        self.ids.image.reload()

    def save_image(self):
        pass

    def blackAndWhite(self, filename):
        temp_filename = os.path.splitext(filename)[0] + '_temp' + os.path.splitext(filename)[1]
        image = Image.open(temp_filename)
        image = ImageOps.grayscale(image)

        image.save(temp_filename)
        self.ids.image.reload()

    def invert(self, filename):
        temp_filename = os.path.splitext(filename)[0] + '_temp' + os.path.splitext(filename)[1]
        image = Image.open(temp_filename)
        image = ImageOps.invert(image)

        image.save(temp_filename)
        self.ids.image.reload()

    def lineDraw(self, filename):
        temp_filename = os.path.splitext(filename)[0] + '_temp' + os.path.splitext(filename)[1]
        image = Image.open(temp_filename)
        image = ImageOps.grayscale(image)
        image = ImageOps.posterize(image, 1)

        image.save(temp_filename)
        self.ids.image.reload()

    def pointilism(self, filename):
        temp_filename = os.path.splitext(filename)[0] + '_temp' + os.path.splitext(filename)[1]
        image = Image.open(temp_filename)

        for x in range(image.width):
            for y in range(image.height):
                color = image.getpixel((x, y))
                ImageDraw.ellipse((x-2, y-2, x+2, y+2), fill=color)

        image.save(temp_filename)
        self.ids.image.reload()

PhotoEditorApp().run()                