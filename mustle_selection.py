"""
My first application
"""
from gettext import textdomain
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW,LEFT,RIGHT,CENTER
from pathlib import Path

run_butt_obj = list()
cyc_butt_obj = list()
# 중앙값: padding(0,0,0,285)
class HelloWorld(toga.App):
    def startup(self):
        self.resources_folder = Path(__file__).joinpath("../resources").resolve()
        self.db_filepath = self.resources_folder.joinpath("weigh.txt")
        f=open(self.db_filepath,'r',encoding="UTF-8")

        main_box=toga.Box(style=Pack(direction=COLUMN))
        box1=toga.Box(style=Pack(padding=(0,0,0,50),direction=ROW))    #프리웨이트
        box2_1=toga.Box(style=Pack(direction=ROW))                   #렛풀다운
        box2_2=toga.Box(style=Pack(padding_left=250,alignment=RIGHT,direction=ROW))
        box2_3=toga.Box(style=Pack(padding_left=250,alignment=RIGHT,direction=ROW))
        

        
        box3=toga.Box(style=Pack(padding_left=100,direction=ROW))
        box4=toga.Box(style=Pack(padding_left=100,direction=ROW))
        box5_1=toga.Box(style=Pack(padding=(50,0,0,50),direction=ROW))
        box5_2=toga.Box(style=Pack(direction=ROW))

        mechine_name=list()
        while(1):
            line=f.readline()
            line=line.strip()
            if not line:
                break
            else:
                mechine_name.append(line)
        mechine_button_obj=list()
        
        for x in range(0,len(mechine_name)):
            if  mechine_name[x]!='1':
                print(mechine_name[x])
                mechine_button_obj.append(toga.Button(text=mechine_name[x],style=Pack(padding=(10))))
            else:mechine_button_obj.append('1')
        a=0
        
        while(1):
            if mechine_name[a]!='1':
                box1.add(mechine_button_obj[a])
                
                a+=1
            else:
                
                a+=1
                break

        while(1):
            if mechine_name[a]!='1':
                
                box2_1.add(mechine_button_obj[a])
                
                a+=1
            else:
                
                a+=1
                break

        while(1):
            if  mechine_name[a]!='1':
                box2_2.add(mechine_button_obj[a])
                a+=1
            else:
                
                a+=1
                break
        
        
        while(1):
            if mechine_name[a]!='1':
                box2_3.add(mechine_button_obj[a])
                a+=1
            else:
                a+=1
                break
       
      
        while(1):
            if mechine_name[a]!='1':
                box3.add(mechine_button_obj[a])
                a+=1
            else:
                a+=1
                break
        while(1):
            if mechine_name[a]!='1':
                box4.add(mechine_button_obj[a])
                a+=1
            else:
                a+=1
                break
        for x in range(a,len(mechine_button_obj)-5):
            box5_1.add(mechine_button_obj[x])
        a+=4
        for x in range(a,len(mechine_button_obj)):
            box5_2.add(mechine_button_obj[x])

        main_box.add(box1)
        main_box.add(box2_1)
        main_box.add(box2_2)
        main_box.add(box2_3)
        main_box.add(box3)
        main_box.add(box4)
        main_box.add(box5_1)
        main_box.add(box5_2)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        

    def show_second_window(self, widget):
        w = widget
        i = 0
        for x in run_butt_obj:
            if x == w:
                break
            i += 1


def main():
    return HelloWorld()