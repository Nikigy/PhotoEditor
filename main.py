# FILEPATH: /home/nikolai/Documents/VSCode/PhotoEditor/main.py
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from PIL import Image, ImageOps, ImageFilter
from io import BytesIO

class PhotoManager(ScreenManager):
    pass

class PhotoEditorScreen(Screen):

    def save_image(self):
        image = self.ids.image
        image.texture.save("output.png")

    def black_and_white(self):
        image = self.ids.image
        data = image.texture.pixels
        img = Image.frombytes(mode='RGBA', size=image.texture.size, data=data)
        img = ImageOps.grayscale(img)
        img_data = img.tobytes()
        texture = Texture.create(size=img.size, colorfmt='rgba')
        texture.blit_buffer(img_data, colorfmt='rgba', bufferfmt='ubyte')
        image.texture = texture

    def invert(self):
        image = self.ids.image
        data = image.texture.pixels
        img = Image.frombytes(mode='RGBA', size=image.texture.size, data=data)
        img = ImageOps.invert(img)
        img_data = img.tobytes()
        texture = Texture.create(size=img.size, colorfmt='rgba')
        texture.blit_buffer(img_data, colorfmt='rgba', bufferfmt='ubyte')
        image.texture = texture

    def line_drawing(self):
        image = self.ids.image
        data = image.texture.pixels
        img = Image.frombytes(mode='RGBA', size=image.texture.size, data=data)
        img = img.convert('L')
        img = img.filter(ImageFilter.CONTOUR)
        img_data = img.tobytes()
        texture = Texture.create(size=img.size, colorfmt='rgba')
        texture.blit_buffer(img_data, colorfmt='rgba', bufferfmt='ubyte')
        image.texture = texture

    def pointilism(self):
        image = self.ids.image
        data = image.texture.pixels
        img = Image.frombytes(mode='RGBA', size=image.texture.size, data=data)
        img = img.filter(ImageFilter.MedianFilter(size=5))
        img = img.quantize(colors=10)
        img_data = img.tobytes()
        texture = Texture.create(size=img.size, colorfmt='rgba')
        texture.blit_buffer(img_data, colorfmt='rgba', bufferfmt='ubyte')
        image.texture = texture

    def sepia(self):
        image = self.ids.image
        data = image.texture.pixels
        img = Image.frombytes(mode='RGBA', size=image.texture.size, data=data)
        sepia = (112, 66, 20)
        depth = 30
        r, g, b = img.split()
        gray = ImageOps.grayscale(img)
        r = r.filter(ImageFilter.GaussianBlur(depth))
        b = b.filter(ImageFilter.GaussianBlur(depth))
        g = g.filter(ImageFilter.GaussianBlur(depth))
        r, g, b = map(lambda x: ImageOps.colorize(x, (0, 0, 0), sepia), (r, g, b))
        img = Image.merge('RGB', (r, g, b))
        img_data = img.tobytes()
        texture = Texture.create(size=img.size, colorfmt='rgba')
        texture.blit_buffer(img_data, colorfmt='rgba', bufferfmt='ubyte')
        image.texture = texture

    def pixilate(self):
        image = self.ids.image
        data = image.texture.pixels
        img = Image.frombytes(mode='RGBA', size=image.texture.size, data=data)
        img = img.resize((img.size[0] // 10, img.size[1] // 10), resample=Image.BOX)
        img = img.resize((img.size[0] * 10, img.size[1] * 10), resample=Image.NEAREST)
        img_data = img.tobytes()
        texture = Texture.create(size=img.size, colorfmt='rgba')
        texture.blit_buffer(img_data, colorfmt='rgba', bufferfmt='ubyte')
        image.texture = texture

class PhotoEditorApp(App):
    def build(self):
        return Builder.load_file("photolayout.kv")

if __name__ == "__main__":
    PhotoEditorApp().run()
