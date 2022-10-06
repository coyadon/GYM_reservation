import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER

class select_exercise:
    def select_getBox(self, change_view, finish):
        self.changeview = change_view
        self.finish = finish
        # ScrollContainer 은 add 대신 content 사용
        main_box = toga.ScrollContainer(style=Pack(direction=COLUMN))
        pag_label = toga.Label(
            "수행하실 운동 유형을 선택해 주세요.",
            style=Pack(text_align=CENTER, padding=(50, 5, 50, 5)),
        )
        button_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER))
        aerobic_button = toga.Button(
            "유산소 운동", on_press=self.changeview, style=Pack(padding=(20))
        )
        weight_button = toga.Button(
            "근력 운동", on_press=self.changeview, style=Pack(padding=(20))
        )
        traffic_button = toga.Button("헬스장 트래픽 확인", on_press=self.changeview, style=Pack(padding=20))
        finish_button = toga.Button("종료", on_press=self.finish, style=Pack(padding=20))
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
        aero_box = toga.Box(style=Pack(direction=ROW, alignment=CENTER))
        weigh_box = toga.Box(style=Pack(direction=ROW, alignment=CENTER))
        aero_box.add(aerobic_button)
        aero_box.add(usa_view)
        weigh_box.add(weight_button)
        weigh_box.add(mus_view)

        button_box.add(pag_label)
        button_box.add(aero_box)
        button_box.add(weigh_box)

        button_box.add(traffic_button)
        button_box.add(finish_button)
        main_box.content = button_box
        return main_box
