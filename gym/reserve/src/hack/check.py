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


class reservetime(toga.App):
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



    def Reservation(self, widget):
        if gettime() != '시간을 선택해주세요':
            name = '예약이 완료되었습니다.'
            self.second_window.info_dialog('예약 확인', getname() + gettime() + name)  # dialog title, message, name
            f = open("C:\\Users\\문승재\예약현황.txt", 'a', encoding='UTF-8')
            f.write('\n' + getname() + ';' + gettime())
            f.close()
            self.second_window.close()

        else:
            self.second_window.info_dialog('예약 확인', "다시 ㄱㄱ")
        self.second_window.close()

    def Cancel(self, widget):
        name = '예약이 취소되었습니다.'
        self.main_window.info_dialog('예약 취소', name)

    def Back(self, widget):
        self.second_window.close()

