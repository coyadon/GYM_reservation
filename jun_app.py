"""
My first application
"""
from turtle import color, st
from click import style
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from PIL import Image
import sys
# 중앙값: padding(0,0,0,285)
class jun_HelloWorld(toga.App):
    def startup(self):
        mod=sys.modules[__name__]
        main_box = toga.Box(style=Pack(direction=COLUMN))
        walking_box=toga.Box(style=Pack(direction=ROW))
        cycle_box=toga.Box(style=Pack(direction=ROW))
        f=open("C:\\Users\\zad34\Desktop\\h_sys\\helloworld\\src\\helloworld\datasample.txt",'r',encoding='UTF-8')
        run_lst=list()
        run_butt_obj=list()
        cyc_lst=list()
        cyc_butt_obj=list()
        while 1:
            line=f.readline()
            if not line:
                break;
            else:
                if "run" in line:
                    run_lst.append(line)
                    run_butt_obj.append(0)
                elif "cyc" in line:
                    cyc_lst.append(line)
                    cyc_butt_obj.append(0)
        for x in range(len(run_butt_obj)):
            run_butt_obj[x]=toga.Button(text=run_lst[x],style=Pack(padding=(10)))
            
            walking_box.add(run_butt_obj[x])    
        
        for x in range(len(cyc_butt_obj)):
            cyc_butt_obj[x]=toga.Button(text=cyc_lst[x],style=Pack(padding=(30,20,0,20)))
            cycle_box.add(cyc_butt_obj[x])
        cycle_run_button=toga.Button("싸이클 런",style=Pack(padding=(30,20,0,100)))
        cycle_box.add(cycle_run_button)
        print(type(cycle_box))
        main_box.add(walking_box)
        main_box.add(cycle_box)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        print(id(run_butt_obj[0]),id(run_butt_obj[1]))

def jun_main():
    return jun_HelloWorld()

