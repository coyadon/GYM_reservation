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

        main_box = toga.ScrollContainer(style=Pack(direction=COLUMN))
        #ScrollContainer 은 add 대신 content 사용

        pag_label = toga.Label(
            "수행하실 운동 유형을 선택해 주세요.",
            style=Pack(text_align=CENTER, padding=(50, 5, 50, 5)),
        )
        button_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER))
        aerobic_button = toga.Button(
            "유산소 운동", on_press=self.aerobic_press, style=Pack(padding=(20))
        )
        weight_button = toga.Button(
            "근력 운동", on_press=self.weight_press, style=Pack(padding=(20))
        )
        traffic_button=toga.Button("헬스장 트래픽 확인",style=Pack(padding=20))
        usa_view = toga.ImageView(
            id="view",
            image="usa.jpg",
            style=Pack(width=150, height=150),
        )
        mus_view = toga.ImageView(
            id="view",
            image="arnold.jpeg",
            style=Pack(width=150, height=150),
        )
        aero_box=toga.Box(style=Pack(direction=ROW,alignment=CENTER))
        weigh_box=toga.Box(style=Pack(direction=ROW,alignment=CENTER))
        aero_box.add(aerobic_button)
        aero_box.add(usa_view)
        weigh_box.add(weight_button)
        weigh_box.add(mus_view)

        button_box.add(pag_label)
        button_box.add(aero_box)
        button_box.add(weigh_box)
        
        
        button_box.add(traffic_button)
        main_box.content = button_box

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def weight_press(self, widget):
        
        pass

    def aerobic_press(self, widget):
        
        pass

  


def main():
    return HelloWorld()
