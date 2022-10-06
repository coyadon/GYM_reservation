# 예약 시스템 만들기
import os.path
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import check

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

    def startup(self):
        self.sbox = check.reservetime().start()
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        self.walking_box = toga.Box(style=Pack(direction=ROW))
        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, "data_sample.txt")
        f = open(path, 'r', encoding='UTF-8')
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
            obj.append(toga.Button(text=my_lst[x], on_press=self.seting))
            self.walking_box.add(obj[x])
        self.main_box.add(self.walking_box)
        f.close()
        self.finish_box = toga.Box(style=Pack(direction=ROW))
        self.finish_box.add(toga.Button(text='종료', on_press=self.finish))
        self.main_box.add(self.finish_box)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    def seting(self, widget):
        self.main_box.remove(self.walking_box)
        self.main_box.remove(self.finish_box)
        self.main_box.add(self.sbox)

    def finish(self, widget):
        self.main_window.close()


def main():
    return cdhelloworld()
