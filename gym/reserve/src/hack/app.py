import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class MultiWindow(toga.App):

    def startup(self):

        main_box = toga.Box()
        main_box.add(toga.Button('Open Window', on_press=self.show_second_window))

        self.main_window = toga.Window(title=self.formal_name, closeable=True)
        self.main_window.content = main_box
        self.main_window.show()

    def show_second_window(self, widget):
        outer_box = toga.Box()
        self.second_window = toga.Window(title='Second window')
        self.windows.add(self.second_window)
        self.second_window.content = outer_box
        self.second_window.show()
        self.main_window.close()


def main():
    return MultiWindow()