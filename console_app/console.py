# This is a sample Python script.
import sys
import os.path

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def start_app():
    print('id,password 형식을 지켜 id와 비밀번호를 입력해주세요')
    user_info = input()
    info = user_info.split(',')
    boolean = login(info[0], info[1])
    if boolean:
        start_reservation(info[0])
    else:
        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, "user_info.txt")
        print('정보에 없는 유저입니다. 이 정보로 회원가입 하시겠습니까? [Y/N]')
        yesno = input()
        if yesno == 'Y':
            print('정보저장완료')
            f = open(path, 'a', encoding='UTF-8')
            print('위 정보로 다시 로그인 하세요')
            f.write('\n' + info[0] + ';' + info[1])

        else:
            print('정보를 다시 확인하여 입력해주세요')
            print('=================================')
        start_app()


def login(u_id, u_password):
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path, "user_info.txt")
    f = open(path, 'r', encoding='UTF-8')
    while 1:
        line = f.readline()
        line = line.strip()
        if not line:
            break
        else:
            name = line.split(';')
            if name[0] == u_id and name[1] == u_password:
                return True
    return False


def file_res_read():
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path, "예약현황.txt")
    res = open(path, 'r', encoding='UTF-8')
    return res


def file_machine_read():
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path, "data_sample.txt")
    f = open(path, 'r', encoding='UTF-8')
    return f


def start_reservation(user_id):
    print('예약하기')
    print('예약할 기구의 이름을 입력해주세요')
    f = file_machine_read()
    my_lst = list()
    while 1:
        line = f.readline()
        line = line.strip()
        if not line:
            break
        else:
            name = line.split(' ')
            my_lst.append(name[0])
    print(my_lst)
    print()
    f.close()
    machine_value = input()
    machine_value = machine_value.strip()
    reservation(machine_value, user_id)


def reservation(value, user_id):
    print('시간 예약하기')
    print('======================')
    print('시간을 선택해주세요.')
    time = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00']
    f = file_res_read()
    while 1:
        line = f.readline()
        line = line.strip()
        if not line:
            break
        else:
            name = line.split(';')
            if user_id == name[0]:
                print('예약한 정보가 있습니다.')
                print(user_id + ' : ' + name[1] + ' ' + name[2])
            if value == name[1]:
                time.remove(name[2])

    f.close()
    print(time)
    print('되돌아가기 : exit')
    time_input = input()

    if time_input == 'exit':
        start_reservation(user_id)
    else:
        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, "예약현황.txt")
        f = open(path, 'a', encoding='UTF-8')
        f.write('\n' + value + ';' + time_input)


start_app()
