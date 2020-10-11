import kivy
kivy.require("1.11.1")
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty


class ErrorMessage(Popup):
    error_label = ObjectProperty()

    def show_error(self, value):
        error_message = ErrorMessage()
        error_message.error_label.text = f"{value}"
        error_message.open()
