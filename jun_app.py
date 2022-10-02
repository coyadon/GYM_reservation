"""
My first application
"""
from turtle import st
from click import style
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from PIL import Image

# 중앙값: padding(0,0,0,285)
class jun_HelloWorld(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))
        walking_box=toga.Box(style=Pack(direction=ROW))
        cycle_box=toga.Box(style=Pack(direction=ROW))
        f=open("C:\\Users\\zad34\Desktop\\h_sys\\helloworld\\src\\helloworld\datasample.txt",'r',encoding='UTF-8')
        run_lst=list()
        cyc_lst=list()
        h_map_lst=[[],[]]
        while 1:
            line=f.readline()
            if not line:
                break;
            else:
                if "run" in line:
                    run_lst.append(line)
                elif "cyc" in line:
                    cyc_lst.append(line)
        for x in range(len(run_lst)):
            obj=toga.Button(text=run_lst[x],style=Pack(padding=(10)))
            walking_box.add(obj)    
        
        for x in range(len(cyc_lst[1])):
            obj=toga.Button(text=cyc_lst[x],style=Pack(padding=(30,20,0,20)))
            cycle_box.add(obj)
        cycle_run_button=toga.Button("싸이클 런",style=Pack(padding=(30,20,0,100)))
        cycle_box.add(cycle_run_button)
      
        main_box.add(walking_box)
        main_box.add(cycle_box)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def jun_main():
    return jun_HelloWorld()
