from kivy.app import App
from kivy.uix.screenmanager import Screen
from PIL import Image, ImageOps, ImageDraw
import os, random

for filename in os.listdir():
    if filename.endswith("_temp.jpg"):
        os.remove(filename)

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
        filename = self.ids.filename.text
        temp_filename = os.path.splitext(filename)[0] + '_temp' + os.path.splitext(filename)[1]
        edited_filename = os.path.splitext(filename)[0] + '_edited' + os.path.splitext(filename)[1]
        
        if os.path.exists(edited_filename):
            i = 1
            while os.path.exists(os.path.splitext(edited_filename)[0] + f'({i})' + os.path.splitext(edited_filename)[1]):
                i += 1
            edited_filename = os.path.splitext(edited_filename)[0] + f'({i})' + os.path.splitext(edited_filename)[1]
        
        image = Image.open(temp_filename)
        image.save(edited_filename)

    def blackAndWhite(self, filename):
        temp_filename = os.path.splitext(filename)[0] + '_temp' + os.path.splitext(filename)[1]
        image = Image.open(temp_filename)
        image = ImageOps.grayscale(image)

        print("Done Black and White Effect")
        image.save(temp_filename)
        self.ids.image.reload()

    def invert(self, filename):
        temp_filename = os.path.splitext(filename)[0] + '_temp' + os.path.splitext(filename)[1]
        image = Image.open(temp_filename)
        image = ImageOps.invert(image)

        print("Done Invert Effect")
        image.save(temp_filename)
        self.ids.image.reload()

    def lineDraw(self, filename):
        temp_filename = os.path.splitext(filename)[0] + '_temp' + os.path.splitext(filename)[1]
        image = Image.open(temp_filename)
        image = ImageOps.grayscale(image)
        image = ImageOps.posterize(image, 1)

        print("Done Line Draw Effect")
        image.save(temp_filename)
        self.ids.image.reload()

    def pointilism(self, filename):
        temp_filename = os.path.splitext(filename)[0] + '_temp' + os.path.splitext(filename)[1]
        image = Image.open(temp_filename)

        pixels = image.load()
        canvas = Image.new("RGB",(image.size[0],image.size[1]), "white")
        for y in range(0, image.size[1], 1):
            for x in range(0, image.size[0], random.randint(1,3)):
                size = random.randint(2,10)
                color = pixels[x,y]
                draw = ImageDraw.Draw(canvas)
                draw.ellipse((x-size/2,y-size/2,x+size/2,y+size/2), fill=color)

        print("Done Pointilism Effect")
        canvas.save(temp_filename)
        self.ids.image.reload()

    def sepia(self, filename):
        temp_filename = os.path.splitext(filename)[0] + '_temp' + os.path.splitext(filename)[1]
        image = Image.open(temp_filename)
        image = ImageOps.grayscale(image)
        image = ImageOps.colorize(image, (205, 168, 130), (255, 255, 255))

        print("Done Sepia Effect")
        image.save(temp_filename)
        self.ids.image.reload()

    def pixelate(self,button_state , filename, x1, y1, x2, y2):
        if button_state == 'down':
            temp_filename = os.path.splitext(filename)[0] + '_temp' + os.path.splitext(filename)[1]
            image = Image.open(temp_filename)

            pixels = image.load()
            for y in range(y1, y2, 1):
                for x in range(x1, x2, 1):
                    size = random.randint(2,10)
                    color = pixels[x,y]
                    draw = ImageDraw.Draw(image)
                    draw.ellipse((x-size/2,y-size/2,x+size/2,y+size/2), fill=color)

            print("Done Pixelate Effect")
            image.save(temp_filename)
            self.ids.image.reload()

PhotoEditorApp().run()                