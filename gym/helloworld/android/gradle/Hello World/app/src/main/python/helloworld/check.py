import os.path
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


tmpname = 'res'
stime = '9:00'


def setstime(value):
    global stime
    stime = value


def gettime():
    return stime


def setname(value):
    global tmpname
    tmpname = value
    print(tmpname)


def getname():
    return tmpname


class reservetime:
    def start(self):
        setname('런닝머신')
        self.reserve_box = toga.Box(style=Pack(direction=COLUMN, alignment='center'))
        def selection_handler(self):
            setstime(self.timeline.value)

        self.time_label = toga.Label("예약할 시간을 선택하세요.", style=Pack(text_align='center',
                                                             padding_top=30, padding_bottom=10, font_size=10))
        # 이거 나중에 파일 입출력으로 시간 받아올거임
        time = ["시간을 선택해주세요", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00"]
        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, "예약현황.txt")
        f = open(path, 'r', encoding='UTF-8')
        res = list()
        while True:
            line = f.readline()
            if not line:
                break
            else:
                name = line.split(';')
                if name[0] == getname():  # 나중에 바꿔야함
                    res.append(name[1].strip())
        for x in range(len(res)):
            time.remove(res[x])
        f.close()
        self.timeline = toga.Selection(items=time,
                                  on_select=selection_handler
                                  )

        self.check_box = toga.Box(style=Pack(direction=COLUMN, alignment='center'))
        self.check_box.add(self.time_label)
        self.check_box.add(self.timeline)

        # 예 아니오 버튼 설정
        self.button1 = toga.Button("예", on_press=self.Reservation,
                              style=Pack(height=40, width=100, padding=5, background_color='#ffffff'))
        self.button2 = toga.Button("아니요", on_press=self.Cancel,
                              style=Pack(height=40, width=100, padding=5, background_color='#ffffff'))
        self.button3 = toga.Button("뒤로가기", on_press=self.Back,
                              style=Pack(height=40, width=100, padding=5, background_color='#ffffff'))

        self.button_box = toga.Box(style=Pack(direction=ROW))
        self.button_box.add(self.button1)
        self.button_box.add(self.button2)
        self.button_box2 = toga.Box(style=Pack(direction=COLUMN))
        self.button_box2.add(self.button3)
        self.reserve_box.add(self.check_box)
        self.reserve_box.add(self.button_box)
        self.reserve_box.add(self.button_box2)

        return self.reserve_box

    def Reservation(self, widget):
        if gettime() != '시간을 선택해주세요':
            name = '예약이 완료되었습니다.'
            path = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(path, "예약현황.txt")
            f = open(path, 'a', encoding='UTF-8')
            f.write('\n' + getname() + ';' + gettime())
            f.close()

            return True
        else:
            return False

    def Back(self, widget):
        return True

    def Cancel(self, widget):
        return True



