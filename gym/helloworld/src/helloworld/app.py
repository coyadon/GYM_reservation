import os.path
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW,LEFT,RIGHT,CENTER
from gettext import textdomain
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import check
import login
import select_aer_muc_tra
import traffic


class main_win(toga.App):
    def setName(self, name: str):
        self.machine_name = name

    def setId(self, name: str):
        self.user_id = name

    def getId(self):
        return self.user_id

    def getName(self):
        return self.machine_name

    def startup(self):
        self.machine_name = '1'
        self.user_id = ''
        self.check_value = 1
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        self.main_window = toga.MainWindow(title=self.name + '예약하기')
        self.main_in_box = toga.Box(style=Pack(direction=COLUMN))
        self.main_window.content = self.main_box
        self.pre_box = None

        # 처음 보여주는 화면
        self.login_view_1st = login.login(self.login, self.select_amt_view)
        self.main_box.add(self.login_view_1st.getIntroBox())
        self.main_window.show()

        # 사용할 모든 화면들
        self.traffic_view = traffic.traffic_view().get_traffic(self.goback)
        self.select_amt = select_aer_muc_tra.select_exercise().select_getBox(self.change_view, self.finish)
        self.check_view_4th = check.reservetime(self.goback, self.Reservation, self.getId())
        self.reserve_view_3rd = self.machine_getBox()
        self.muscle_view = self.muscle_getBox()
        self.now_box = self.login_view_1st.getIntroBox()

    def login(self, widget):
        ID = self.login_view_1st.ID_input.value
        PW = self.login_view_1st.PW_input.value

        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, "IDPW.txt")
        f = open(path, 'r', encoding='UTF-8')

        while 1:
            line = f.readline()
            line = line.strip()
            user_info = line.split(':')

            if not line:
                self.login_view_1st.login_fail()
                break
            else:
                if str(ID) == user_info[0] and str(PW) == user_info[1]:
                    self.login_view_1st.login_sucs()
                    self.setId(user_info[0])
                    break
                else:
                    continue

        f.close()

    def to_traffic(self, widget):
        self.main_box.remove(self.now_box)
        self.main_box.add(self.traffic_view)
        self.pre_box = self.now_box
        self.now_box = self.traffic_view

    def goback(self, widget):
        self.main_box.remove(self.now_box)
        self.main_box.add(self.pre_box)
        self.now_box = self.pre_box

    def goback_button(self, widget):
        self.main_box.remove(self.now_box)
        self.main_box.add(self.select_amt)
        self.pre_box = self.now_box
        self.now_box = self.select_amt

    def reserve(self):
        self.main_box.remove(self.now_box)
        self.main_box.add(self.reserve_view_3rd)
        self.pre_box = self.now_box
        self.now_box = self.reserve_view_3rd

    def name_check(self, name):
        self.setName(name)
        self.main_box.remove(self.now_box)
        self.main_box.add(self.reserve_view_3rd)
        self.pre_box = self.now_box
        self.now_box = self.reserve_view_3rd

    def select_amt_view(self):
        self.main_box.remove(self.now_box)
        self.main_box.add(self.select_amt)
        self.pre_box = self.now_box
        self.now_box = self.select_amt

    def to_check(self, widget: toga.Button):
        bt = widget.text.strip()
        self.main_box.remove(self.now_box)
        self.setName(bt)
        self.ch_view = self.check_view_4th.check_getBox(self.getName(), self.getId())
        self.main_box.add(self.ch_view)
        self.pre_box = self.now_box
        self.now_box = self.ch_view

    def finish(self, widget):
        self.main_window.close()

    def change_view(self, widget: toga.Button):
        view_text = widget.text.strip()
        self.main_box.remove(self.now_box)
        if view_text == '근력 운동':
            self.main_box.add(self.muscle_view)
            self.pre_box = self.now_box
            self.now_box = self.muscle_view
        elif view_text == '유산소 운동':
            self.aero_view = self.reserve_view_3rd
            self.main_box.add(self.aero_view)
            self.pre_box = self.now_box
            self.now_box = self.aero_view
        elif view_text == '헬스장 트래픽 확인':
            self.main_box.add(self.traffic_view)
            self.pre_box = self.now_box
            self.now_box = self.traffic_view

    # 주요 함수
    def machine_getBox(self):

        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, "data_sample.txt")

        main_box = toga.Box(style=Pack(direction=COLUMN))
        run_box1 = toga.Box(style=Pack(direction=ROW, height=100, width=100))
        run_box2 = toga.Box(style=Pack(direction=ROW, height=100, width=100))
        run_box3 = toga.Box(style=Pack(direction=ROW, height=100, width=100))
        cycle_box1 = toga.Box(style=Pack(direction=ROW, height=100, width=100))
        cycle_box2 = toga.Box(style=Pack(direction=ROW, height=100, width=100))
        cycle_box3 = toga.Box(style=Pack(direction=ROW, height=100, width=100))
        self.running_lab = toga.Label('런닝머신', style=Pack(alignment='left'))
        self.cycle_lab = toga.Label('싸이클', style=Pack(alignment='left'))

        walking_box = toga.Box(style=Pack(direction=COLUMN))
        cycle_box = toga.Box(style=Pack(direction=COLUMN, padding=(0, 0, 0, 0)))
        run_butt_obj = list()
        cyc_butt_obj = list()
        f = open(
            path,
            "r",
            encoding="UTF-8",
        )

        run_lst = list()
        cyc_lst = list()
        while 1:
            line = f.readline().strip()
            if not line:
                break
            else:
                if "run" in line:
                    run_lst.append(line)
                elif "cyc" in line:
                    cyc_lst.append(line)
        for x in range(len(run_lst)):
            run_butt_obj.append(
                toga.Button(
                    text=run_lst[x],
                    on_press=self.to_check,
                    style=Pack(padding=(10)),
                )
            )
            if 0 <= x < 4:
                run_box1.add(run_butt_obj[x])
            elif 4 <= x < 8:
                run_box2.add(run_butt_obj[x])
            else:
                run_box3.add(run_butt_obj[x])

        for x in range(len(cyc_lst)):
            cyc_butt_obj.append(
                toga.Button(text=cyc_lst[x], on_press=self.to_check, style=Pack(padding=(10)))
            )

            if 0 <= x < 4:
                cycle_box1.add(cyc_butt_obj[x])
            elif 4 <= x < 8:
                cycle_box2.add(cyc_butt_obj[x])
            else:
                cycle_box3.add(cyc_butt_obj[x])

        cycle_run_button = toga.Button("싸이클 런", on_press=self.to_check, style=Pack(padding=(10)))
        cycle_box3.add(cycle_run_button)

        walking_box.add(self.running_lab)
        walking_box.add(run_box1)
        walking_box.add(run_box2)
        walking_box.add(run_box3)
        cycle_box.add(self.cycle_lab)
        cycle_box.add(cycle_box1)
        cycle_box.add(cycle_box2)
        cycle_box.add(cycle_box3)

        finish_button=toga.Button(text='뒤로가기', on_press=self.goback_button)

        main_box.add(walking_box)
        main_box.add(cycle_box)
        main_box.add(finish_button)

        return main_box

    def muscle_getBox(self):
        path = os.path.dirname(os.path.abspath(__file__))
        mus_main_box = toga.ScrollContainer(style=Pack(direction=ROW))
        path = os.path.join(path, "weigh.txt")
        f = open(path, 'r', encoding="UTF-8")
        main_box = toga.Box(style=Pack(direction=COLUMN))
        box1 = toga.Box(style=Pack(padding=(0, 0, 0, 50), direction=ROW))  # 프리웨이트
        box2_1 = toga.Box(style=Pack(direction=ROW))  # 렛풀다운
        box2_2 = toga.Box(style=Pack(padding_left=250, alignment=RIGHT, direction=ROW))
        box2_3 = toga.Box(style=Pack(padding_left=250, alignment=RIGHT, direction=ROW))

        box3 = toga.Box(style=Pack(padding_left=100, direction=ROW))
        box4 = toga.Box(style=Pack(padding_left=100, direction=ROW))
        box5_1 = toga.Box(style=Pack(padding=(50, 0, 0, 50), direction=ROW))
        box5_2 = toga.Box(style=Pack(direction=ROW))

        mechine_name = list()
        while (1):
            line = f.readline()
            line = line.strip()
            if not line:
                break
            else:
                mechine_name.append(line)
        mechine_button_obj = list()

        for x in range(0, len(mechine_name)):
            if mechine_name[x] != '1':
                print(mechine_name[x])
                mechine_button_obj.append(toga.Button(text=mechine_name[x], on_press=self.to_check, style=Pack(padding=(10))))
            else:
                mechine_button_obj.append('1')
        a = 0

        while (1):
            if mechine_name[a] != '1':
                box1.add(mechine_button_obj[a])

                a += 1
            else:

                a += 1
                break

        while (1):
            if mechine_name[a] != '1':

                box2_1.add(mechine_button_obj[a])

                a += 1
            else:

                a += 1
                break

        while (1):
            if mechine_name[a] != '1':
                box2_2.add(mechine_button_obj[a])
                a += 1
            else:

                a += 1
                break

        while (1):
            if mechine_name[a] != '1':
                box2_3.add(mechine_button_obj[a])
                a += 1
            else:
                a += 1
                break

        while (1):
            if mechine_name[a] != '1':
                box3.add(mechine_button_obj[a])
                a += 1
            else:
                a += 1
                break
        while (1):
            if mechine_name[a] != '1':
                box4.add(mechine_button_obj[a])
                a += 1
            else:
                a += 1
                break
        for x in range(a, len(mechine_button_obj) - 5):
            box5_1.add(mechine_button_obj[x])
        a += 4
        for x in range(a, len(mechine_button_obj)):
            box5_2.add(mechine_button_obj[x])

        main_box.add(box1)
        main_box.add(box2_1)
        main_box.add(box2_2)
        main_box.add(box2_3)
        main_box.add(box3)
        main_box.add(box4)
        main_box.add(box5_1)
        main_box.add(box5_2)
        finish_button = toga.Button(text='뒤로가기', on_press=self.goback_button)
        main_box.add(finish_button)
        mus_main_box.content = main_box
        return mus_main_box

    def Reservation(self, widget):
        if self.check_view_4th.gettime() != '시간을 선택해주세요':
            name = '예약이 완료되었습니다.'
            path = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(path, "예약현황.txt")
            f = open(path, 'a', encoding='UTF-8')
            f.write('\n' + self.user_id + ';' + self.machine_name + ';' + self.check_view_4th.gettime())
            f.close()
            self.main_box.remove(self.now_box)
            self.main_box.add(self.pre_box)
            sus_label = toga.Label('예약이 완료되었습니다.\n'+'기구이름 : '+self.machine_name+'시간 : '+self.check_view_4th.gettime(),
                                      style=Pack(text_align='center', font_size=27, font_weight='bold',
                                                 color="#003777"))
            self.now_box = self.pre_box
            self.reserve_view_3rd.add(sus_label)
        else:
            cancel_box = toga.Box(style=Pack(direction=ROW))
            title_label1 = toga.Label('시간을 올바르게 선택해주세요.',
                                      style=Pack(text_align='center', font_size=27, font_weight='bold',
                                                 color="#003777"))
            if self.check_value == 1:
                cancel_box.add(title_label1)
                self.check_value = 2
            else:
                pass
            self.ch_view.add(cancel_box)

def main():
    return main_win()