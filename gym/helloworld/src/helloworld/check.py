import os.path
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

tmpname = 'res'
stime = '9:00'




class reservetime:
    def __init__(self, pre_view, res_fun, u_id):
        self.pre_view = pre_view
        self.resfunc = res_fun
        self.UID = u_id
    def setuid(self, value):
        self.UID = value

    def getuid(self):
        return self.UID

    def setstime(self, value):
        global stime
        stime = value

    def gettime(self):
        global stime
        return stime

    def getName(self):
        return self.name

    def selection_handler(self, widget):
        self.setstime(self.time_select.value)

    def setName(self, name: str):
        self.name = name

    def check_getBox(self, name: str, id:str):
        self.name = name
        #name = 머신이름
        print(self.setuid(id))
        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, "예약현황.txt")
        time = ['시간을 선택해주세요', "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00",
                "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:30", "20:00",
                "20:30", "21:00", "21:30"]
        f = open(path, 'r', encoding='UTF-8')
        res = list()
        while True:
            line = f.readline()
            if not line:
                break
            else:
                userinfo = line.split(';')
                if userinfo[1] == self.name:
                    res.append(userinfo[2].strip())
                    print(self.getuid())
                if userinfo[0] == self.getuid():
                    if userinfo[1] != self.name:
                        res.append(userinfo[2].strip())

        for x in range(len(res)):
            time.remove(res[x])
        f.close()

        self.time_select = toga.Selection(items=time,
                                          on_select=self.selection_handler)
        time_label = toga.Label("예약할 시간을 선택하세요.", style=Pack(text_align='center',
                                                             padding_top=30, padding_bottom=10, font_size=10))

        check_box = toga.Box(style=Pack(direction=COLUMN, alignment='center'))
        check_box.add(time_label)
        check_box.add(self.time_select)

        # 예 아니오 버튼 설정
        button1 = toga.Button("예", on_press=self.resfunc,
                              style=Pack(height=40, width=100, padding=5, background_color='#ffffff'))
        button2 = toga.Button("아니요", on_press=self.pre_view,
                              style=Pack(height=40, width=100, padding=5, background_color='#ffffff'))
        button3 = toga.Button("뒤로가기", on_press=self.pre_view,
                              style=Pack(height=40, width=100, padding=5, background_color='#ffffff'))

        button_box = toga.Box(style=Pack(direction=ROW))
        button_box.add(button1)
        button_box.add(button2)
        button_box2 = toga.Box(style=Pack(direction=COLUMN))
        button_box2.add(button3)
        reserve_box = toga.Box(style=Pack(direction=COLUMN, alignment='center'))
        reserve_box.add(check_box)
        reserve_box.add(button_box)
        reserve_box.add(button_box2)
        return reserve_box


