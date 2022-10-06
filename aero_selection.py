"""
My first application
"""
from gettext import textdomain
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW,LEFT
from pathlib import Path

run_butt_obj = list()
cyc_butt_obj = list()
# 중앙값: padding(0,0,0,285)
class HelloWorld(toga.App):
    def startup(self):

        self.resources_folder = Path(__file__).joinpath("../resources").resolve()
        self.db_filepath = self.resources_folder.joinpath("datasample.txt")

        main_box = toga.Box(style=Pack(direction=COLUMN))
        run_box1=toga.Box(style=Pack(direction=ROW,height=100,width=100))
        run_box2=toga.Box(style=Pack(direction=ROW,height=100,width=100))
        run_box3=toga.Box(style=Pack(direction=ROW,height=100,width=100))
        cycle_box1=toga.Box(style=Pack(direction=ROW,height=100,width=100))
        cycle_box2=toga.Box(style=Pack(direction=ROW,height=100,width=100))
        cycle_box3=toga.Box(style=Pack(direction=ROW,height=100,width=100))
        self.running_lab=toga.Label('런닝머신',style=Pack(alignment='left'))
        self.cycle_lab=toga.Label('싸이클',style=Pack(alignment='left'))


        walking_box = toga.Box(style=Pack(direction=COLUMN))
        cycle_box = toga.Box(style=Pack(direction=COLUMN,padding=(150,0,0,0)))
        f = open(
            self.db_filepath,
            "r",
            encoding="UTF-8",
        )

        run_lst = list()
        cyc_lst = list()
        while 1:
            line = f.readline()
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
                    on_press=self.show_second_window,           #함수작동 부분 개조 부탁
                    style=Pack(padding=(10)),
                )
            )
            if 0<=x<4:
                run_box1.add(run_butt_obj[x])
            elif 4<=x <8:
                run_box2.add(run_butt_obj[x])
            else:
                run_box3.add(run_butt_obj[x])

        for x in range(len(cyc_lst)):
            cyc_butt_obj.append(
                toga.Button(text=cyc_lst[x], style=Pack(padding=(10)))
            )

            if 0<=x<4:
                cycle_box1.add(cyc_butt_obj[x])
            elif 4<=x <8:
                cycle_box2.add(cyc_butt_obj[x])
            else:
                cycle_box3.add(cyc_butt_obj[x])

        
        cycle_run_button = toga.Button("싸이클 런", style=Pack(padding=(10)))
        cycle_box3.add(cycle_run_button)

        
        walking_box.add(self.running_lab)
        walking_box.add(run_box1)
        walking_box.add(run_box2)
        walking_box.add(run_box3)
        cycle_box.add(self.cycle_lab)
        cycle_box.add(cycle_box1)
        cycle_box.add(cycle_box2)
        cycle_box.add(cycle_box3)
        
        main_box.add(walking_box)
        main_box.add(cycle_box)
        
        

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        #f.close()
        #print(run_butt_obj[0])

    def show_second_window(self, widget):
        w = widget
        i = 0
        for x in run_butt_obj:
            if x == w:
                break
            i += 1


def main():
    return HelloWorld()
