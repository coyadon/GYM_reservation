"""
My first application
"""
from gettext import textdomain
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from pathlib import Path

run_butt_obj = list()
cyc_butt_obj = list()
# 중앙값: padding(0,0,0,285)
class jun_HelloWorld(toga.App):
    def startup(self):

        self.resources_folder = Path(__file__).joinpath("../resources").resolve()
        self.db_filepath = self.resources_folder.joinpath("datasample.txt")

        main_box = toga.Box(style=Pack(direction=COLUMN))
     


        walking_box = toga.Box(style=Pack(direction=ROW))
        cycle_box = toga.Box(style=Pack(direction=ROW))
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
                    on_press=self.show_second_window,
                    style=Pack(padding=(10)),
                )
            )

            walking_box.add(run_butt_obj[x])

        for x in range(len(cyc_lst)):
            cyc_butt_obj.append(
                toga.Button(text=cyc_lst[x], style=Pack(padding=(30, 0, 0, 20)))
            )

            cycle_box.add(cyc_butt_obj[x])

        cycle_run_button = toga.Button("싸이클 런", style=Pack(padding=(30, 10, 0, 100)))

        cycle_box.add(cycle_run_button)
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


def jun_main():
    return jun_HelloWorld()
