import sys
import os.path
import toga
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import login


class HelloWorld(toga.App):

    def startup(self):
        self.intro_box = login.login(self.login)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.intro_box.getIntroBox()
        self.main_window.show()

    def login(self, widget):
        ID = self.intro_box.ID_input.value
        PW = self.intro_box.PW_input.value

        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, "IDPW.txt")
        f = open(path, 'r', encoding='UTF-8')

        while 1:
            line = f.readline()
            line = line.strip()
            user_info = line.split(':')

            if not line:
                self.intro_box.login_fail()
                break
            else:
                if str(ID) == user_info[0] and str(PW) == user_info[1]:
                    self.intro_box.login_sucs()
                    break
                else:
                    continue

        f.close()


def main():
    return HelloWorld()
