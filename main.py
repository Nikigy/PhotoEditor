from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from PIL import Image as PILImage
from PIL import ImageOps


class PhotoEditor(App):
    def build(self):
        self.image = Image()
        self.edit_buttons = {
            "Black and White": self.black_and_white,
            "Inverse": self.inverse,
            "Line Drawing": self.line_drawing,
            "Pointilism": self.pointilism,
            "Sepia": self.sepia,
            "Pixliate": self.pixliate,
        }
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.image)
        button_layout = BoxLayout(orientation="horizontal")
        button_layout.add_widget(Button(text="Load Image", on_press=self.load_image))
        for button_text in self.edit_buttons:
            button_layout.add_widget(Button(text=button_text, on_press=self.edit_buttons[button_text]))
        layout.add_widget(button_layout)
        return layout

    def load_image(self, instance):
        content = BoxLayout(orientation="vertical")
        content.add_widget(Label(text="Enter Image Name:"))
        self.image_name_input = TextInput(multiline=False)
        content.add_widget(self.image_name_input)
        content.add_widget(Button(text="Load", on_press=self.load_image_from_input))
        self.popup = Popup(title="Load Image", content=content, size_hint=(0.5, 0.5))
        self.popup.open()

    def load_image_from_input(self, instance):
        image_name = self.image_name_input.text
        try:
            with open(image_name, "rb") as f:
                img = PILImage.open(f)
                self.image.texture = img.convert("RGBA").tobytes()
        except FileNotFoundError:
            self.show_error_popup("File not found.")

    def black_and_white(self, instance):
        self.image.texture = ImageOps.grayscale(PILImage.frombytes("RGBA", self.image.texture.size, self.image.texture)).tobytes()

    def inverse(self, instance):
        self.image.texture = ImageOps.invert(PILImage.frombytes("RGBA", self.image.texture.size, self.image.texture)).tobytes()

    def line_drawing(self, instance):
        self.image.texture = ImageOps.posterize(PILImage.frombytes("RGBA", self.image.texture.size, self.image.texture), 1).tobytes()

    def pointilism(self, instance):
        self.image.texture = ImageOps.posterize(PILImage.frombytes("RGBA", self.image.texture.size, self.image.texture), 4).tobytes()

    def sepia(self, instance):
        self.image.texture = ImageOps.colorize(ImageOps.grayscale(PILImage.frombytes("RGBA", self.image.texture.size, self.image.texture)), "#704214", "#C0C090").tobytes()

    def pixliate(self, instance):
        self.image.texture = PILImage.frombytes("RGBA", self.image.texture.size, self.image.texture).resize((32, 32), PILImage.BOX).resize(self.image.texture.size, PILImage.BOX).tobytes()

    def show_error_popup(self, message):
        content = BoxLayout(orientation="vertical")
        content.add_widget(Label(text=message))
        content.add_widget(Button(text="OK", on_press=self.popup.dismiss))
        self.popup = Popup(title="Error", content=content, size_hint=(0.5, 0.5))
        self.popup.open()


if __name__ == "__main__":
    PhotoEditor().run()
