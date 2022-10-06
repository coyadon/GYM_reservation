import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class login:
    def __init__(self, button_func, reserve_func):

        # Title
        header_box = toga.Box()
        header_view = toga.ImageView(id="view", image="header.png", style=Pack(height=60, width=430))
        header_box.add(header_view)
        header_box.style.update(direction=COLUMN, alignment="center")

        image_box = toga.Box()
        logo_view = toga.ImageView(id="view", image="logo.png", style=Pack(height=150, width=150))
        image_box.add(logo_view)
        image_box.style.update(direction=COLUMN, alignment="center", padding_top=30)

        title_label1 = toga.Label('연세대학교 미래캠퍼스',
                                  style=Pack(text_align='center', font_size=27, font_weight='bold', color="#003777"))
        title_label2 = toga.Label('헬스장 예약 시스템',
                                  style=Pack(text_align='center', font_size=27, font_weight='bold', color="#003777"))
        self.nex_page = reserve_func
        title_box = toga.Box()
        title_box.add(header_box)
        title_box.add(image_box)
        title_box.add(title_label1)
        title_box.add(title_label2)
        title_box.style.update(direction=COLUMN, alignment="center", flex=2)

        # Login
        self.fail = toga.Label("", style=Pack(text_align='center', font_size=20, color="RED"))
        fail_box = toga.Box()
        fail_box.add(self.fail)

        self.ID_input = toga.TextInput(style=(Pack(height=25, width=300)))
        ID_box = toga.Box()
        ID_box.add(self.ID_input)
        ID_box.style.update(direction=ROW, height=10, width=300, padding=5, flex=1)

        self.PW_input = toga.PasswordInput(style=(Pack(height=25, width=300)))
        PW_box = toga.Box()
        PW_box.add(self.PW_input)
        PW_box.style.update(direction=ROW, height=10, width=300, padding=5)

        button = toga.Button("LOGIN", on_press=button_func)
        button.style.update()
        button_box = toga.Box()
        button_box.add(button)
        button_box.style.update(direction=COLUMN, height=25, width=300, padding=5)

        login_box = toga.Box()
        login_box.add(fail_box)
        login_box.add(ID_box)
        login_box.add(PW_box)
        login_box.add(button_box)
        login_box.style.update(direction=COLUMN, alignment='center', flex=5)

        # NULL_Box
        NULL_box = toga.Box()
        NULL_box.style.update(flex=2)

        # Main_Box
        self.intro_box = toga.Box(style=Pack(direction=COLUMN, alignment='center', background_color="white"))
        self.intro_box.add(title_box)
        self.intro_box.add(login_box)

    def getIntroBox(self):
        return self.intro_box

    def login_fail(self):
        self.fail.text = "로그인 실패, 정보를 다시 확인하세요."

    def login_sucs(self):
        self.fail.text = "로그인 성공"
        self.nex_page()