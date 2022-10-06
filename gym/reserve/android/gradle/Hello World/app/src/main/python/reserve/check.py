# 예약 시스템 만들기
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class cdhelloworld(toga.App):
    def __init__(
            self,
            formal_name=None,
            app_id=None,
            app_name=None,
            id=None,
            icon=None,
            author=None,
            version=None,
            home_page=None,
            description=None,
            startup=None,
            windows=None,
            on_exit=None,
            factory=None,
    ):

        super().__init__(formal_name, app_id, app_name, id, icon, author, version, home_page, description, startup,
                         windows, on_exit, factory)
        self.second_window = toga.Window(title='Second window')

    def startup(self):
        # 여기에 정환이가 만든 코드 넣을 예정
        main_box = toga.Box()
        main_box.add(toga.Button('Open Window', on_press=self.show_second_window))

        self.main_window = toga.Window(title=self.formal_name, closeable=True)
        self.main_window.content = main_box
        self.main_window.show()

    # 마지막 예약 확인
    def Reservation(self, widget):
        name = '예약이 완료되었습니다.'
        # 여기에 주은이가 split 만들어오면 넣어서 값 비교
        self.second_window.info_dialog('예약 확인', name)  # dialog title, message, name
        self.second_window.close()

    def Cancel(self, widget):
        name = '예약이 취소되었습니다.'
        self.main_window.info_dialog('예약 취소', name)

    def Back(self, widget):
        self.second_window.close()

    # 새창 만들기
    def show_second_window(self, widget):
        self.second_window = toga.Window(title='예약하기')
        self.windows.add(self.second_window)

        reserve_box = toga.Box(style=Pack(direction=COLUMN, alignment='center'))

        def selection_handler(widget, row):
            toga.Label(timeline.value)

        time_label = toga.Label("예약할 시간을 선택하세요.", style=Pack(text_align='center',
                                                             padding_top=30, padding_bottom=10, font_size=10))
        timeline = toga.Selection(items=['9:00', '10:00', '11:00', '12:00'],
                                  on_select=selection_handler
                                  )

        check_box = toga.Box(style=Pack(direction=ROW, alignment='center'))
        check_box.add(timeline)
        check_box.add(time_label)


        name_label = toga.Label(timeline.value+"땡땡땡 기구 ~ 시 맞습니까?", style=Pack(text_align='center',
                                                               padding_top=30, padding_bottom=10, font_size=10))
        reserve_box.add(name_label)

        # 예 아니오 버튼 설정
        button1 = toga.Button("예", on_press=self.Reservation,
                              style=Pack(height=40, width=100, padding=5, background_color='#ffffff'))
        button2 = toga.Button("아니요", on_press=self.Cancel,
                              style=Pack(height=40, width=100, padding=5, background_color='#ffffff'))
        button3 = toga.Button("뒤로가기", on_press=self.Back,
                              style=Pack(height=40, width=100, padding=5, background_color='#ffffff'))

        button_box = toga.Box(style=Pack(direction=ROW))
        button_box.add(button1)
        button_box.add(button2)
        button_box2 = toga.Box(style=Pack(direction=COLUMN))
        button_box2.add(button3)

        reserve_box.add(check_box)
        reserve_box.add(button_box)
        reserve_box.add(button_box2)


        self.second_window.content = reserve_box
        self.second_window.show()


def main():
    return cdhelloworld()
