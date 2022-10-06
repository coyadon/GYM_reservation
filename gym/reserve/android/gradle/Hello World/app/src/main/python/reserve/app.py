# 예약 시스템 만들기
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

global tmpname
global stime


def setname(value):
    tmpname = value
    print(tmpname)


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

        main_box = toga.Box(style=Pack(direction=COLUMN))
        walking_box = toga.Box(style=Pack(direction=ROW))
        f = open("C:\\Users\\문승재\datasample.txt", 'r', encoding='UTF-8')
        my_lst = list()
        obj = list()
        while 1:
            line = f.readline()
            if not line:
                break
            else:
                name = line.split(' ')
                my_lst.append(name[0])
        for x in range(len(my_lst)):
            obj.append(toga.Button(text=my_lst[x], on_press=self.show_second_window and setname(my_lst[x])))
            walking_box.add(obj[x])
        main_box.add(walking_box)
        f.close()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    # 마지막 예약 확인

    # 새창 만들기
    def show_second_window(self, widget):
        self.second_window = toga.Window(title='예약하기')
        self.windows.add(self.second_window)

        reserve_box = toga.Box(style=Pack(direction=COLUMN, alignment='center'))

        def selection_handler(self):
            print(timeline.value + "이거 선택함요")
            stime = timeline.value

        time_label = toga.Label("예약할 시간을 선택하세요.", style=Pack(text_align='center',
                                                             padding_top=30, padding_bottom=10, font_size=10))
        # 이거 나중에 파일 입출력으로 시간 받아올거임
        time = ['시간을 선택해주세요', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00']

        timeline = toga.Selection(items=time,
                                  on_select=selection_handler
                                  )

        check_box = toga.Box(style=Pack(direction=COLUMN, alignment='center'))
        check_box.add(time_label)
        check_box.add(timeline)

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

    def Reservation(self, widget):
        name = '예약이 완료되었습니다.'
        if(stime!='시간을 선택해주세요'):
            self.second_window.info_dialog('예약 확인', name)  # dialog title, message, name
        else:
            self.second_window.info_dialog('예약 확인', "다시 고르세요")
        self.second_window.close()

    def Cancel(self, widget):
        name = '예약이 취소되었습니다.'
        self.main_window.info_dialog('예약 취소', name)

    def Back(self, widget):
        self.second_window.close()


def main():
    return cdhelloworld()
