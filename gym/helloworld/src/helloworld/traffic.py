"""
My first application
"""
from ctypes import alignment
from gettext import textdomain
import os.path
from tkinter import CENTER, font
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from pathlib import Path

run_butt_obj = list()
cyc_butt_obj = list()


# 중앙값: padding(0,0,0,285)
class traffic_view:
    def get_traffic(self, pre_view):
        self.pre_view = pre_view
        ret_box=toga.Box(style=Pack(direction=COLUMN, alignment=CENTER))
        sec_main = toga.Box(style=Pack(direction=ROW, alignment=CENTER))
        main_box = toga.ScrollContainer(style=Pack(alignment=CENTER))
        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, "예약현황.txt")
        f = open(path, 'r', encoding="UTF-8")

        time = ["09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00",
                "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:30", "20:00",
                "20:30", "21:00", "21:30"]

        f = open(path, 'r', encoding="UTF-8")
        sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        count = 0
        while (1):
            line = f.readline()
            line = line.strip()
            if not line:
                break
            else:
                line = line.split(';')

            for x in range(len(time)):

                if line[2] == time[x]:
                    sum[x] += 1

        time_lis = list()
        traffic_list = list()
        time_box = toga.Box(style=Pack(height=100, width=100, direction=COLUMN))
        col_box = toga.Box(style=Pack(height=100, width=100, direction=COLUMN))
        for x in range(len(time)):
            time_lis.append(
                toga.Label(text=time[x], style=Pack(font_size=20, alignment=CENTER, height=25, font_weight='bold')))
            time_box.add(time_lis[x])

        for x in range(len(sum)):
            col = ''
            if sum[x] >= 0 and sum[x] < 10:
                col = 'green'
            elif sum[x] >= 10 and sum[x] < 25:
                col = 'yellow'
            else:
                col = 'red'
            traffic_list.append(toga.Box(style=Pack(height=25, width=200, background_color=col)))
            col_box.add(traffic_list[x])
        sec_main.add(time_box)
        sec_main.add(col_box)
        ret_box.add(sec_main)
        button3 = toga.Button("뒤로가기", on_press=self.pre_view,
                              style=Pack(height=40, width=100, padding=5, background_color='#ffffff'))
        ret_box.add(button3)
        main_box.content = ret_box
        f.close()
        return main_box

    def show_second_window(self, widget):
        w = widget
        i = 0
        for x in run_butt_obj:
            if x == w:
                break
            i += 1
