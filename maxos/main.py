import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('2.1.0')

class Calculator(App):

    def build(self):
        return Label(text='I love MaxOS')


if __name__ == '__main__':
    Calculator().run()