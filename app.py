"""
My first application
"""
from ctypes import alignment
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER


# 중앙값: padding(0,0,0,285)
class HelloWorld(toga.App):
    def startup(self):

        main_box = toga.Box(style=Pack(direction=COLUMN))

        pag_label = toga.Label(
            "수행하실 운동 유형을 선택해 주세요.",
            style=Pack(text_align=CENTER, padding=(50, 5, 50, 5)),
        )
        button_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER))
        aerobic_button = toga.Button(
            "유산소 운동", on_press=self.aerobic_press, style=Pack(padding=(5))
        )
        weight_button = toga.Button(
            "근력 운동", on_press=self.weight_press, style=Pack(padding=(5))
        )

        bong_view = toga.ImageView(
            id="view",
            image="usa.jpg",
            style=Pack(width=250, height=250),
        )
        mus_view = toga.ImageView(
            id="view",
            image="mustle.jpg",
            style=Pack(width=250, height=250),
        )

        button_box.add(aerobic_button)
        button_box.add(bong_view)

        button_box.add(weight_button)
        button_box.add(mus_view)
        button_box.style
        main_box.add(pag_label)
        main_box.add(button_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def weight_press(self, widget):

        pass

    def aerobic_press(self, widget):
        pass

  


def main():
    return HelloWorld()
