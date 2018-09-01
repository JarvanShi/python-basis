import time

# 主窗口函数
def output_window(sentence):
    system_sentence = '学生信息管理系统 v1.0'
    print(' ' * left_margin + '=' * box_width)
    print(' ' * ((screen_width - len(system_sentence)) // 2) + system_sentence)
    if sentence == 'top_menu':
        top_menu()
    elif sentence == 'sub_menu':
        sub_menu()
    elif sentence == 'inquiry':
        inquiry_information()
    elif sentence == 'ergodic':
        ergodic_information()
    elif sentence == 'verify':
        verify_passed()
    elif sentence == 'wrong_choice':
        wrong_choice()
    elif sentence == 'wrong_password':
        wrong_password()
    elif sentence == 'invalid_username':
        invalid_username()
    print(' ' * left_margin + '=' * box_width)

# 主菜单函数
def top_menu():
    print(' ' * left_margin + '1.添加信息')
    print(' ' * left_margin + '2.删除信息')
    print(' ' * left_margin + '3.修改信息')
    print(' ' * left_margin + '4.查询信息')
    print(' ' * left_margin + '5.查询所有信息')
    print(' ' * left_margin + '6.退出系统')

# 修改子菜单函数
def sub_menu():
    print(' ' * left_margin + '1.修改姓名')
    print(' ' * left_margin + '2.修改学号')
    print(' ' * left_margin + '3.修改出生日期')
    print(' ' * left_margin + '4.修改兴趣爱好')
    print(' ' * left_margin + '5.修改完成')

# 日期设置
def date_set():
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    day_endings = ['st','nd','rd'] + ['th'] * 17 + ['st','nd','rd'] + ['th'] * 7 + ['st']
    year = input('请输入出生年份：')
    month = input('请输入出生月份：')
    day = input('请输入出生日：')
    month_name = months[int(month) - 1]
    day_name = day + day_endings[int(day) - 1]
    birthday = month_name + ' ' + day_name + ', ' + year
    return birthday

# 增加信息函数
def input_information():
    new_name = input('请输入姓名：')
    if new_name in [name for [name,student_number,birthday,hobby] in student_information]:
        print(' ' * left_margin + '该学生信息已存在！')
        return student_information
    else:
        student_number = input('请输入学号：')
        new_birthday = date_set()
        hobby = input('请输入兴趣爱好：')
        new_student_information =[new_name,student_number,new_birthday,hobby]
        print(' ' * left_margin + '添加完成')
        student_information.append(new_student_information)
        return student_information

# 删除信息函数
def delete_information():
    delete_name = input('请输入删除的姓名：')
    delay_time()
    if delete_name in student_name_list:
        student_information.pop(student_name_list.index(delete_name))
        print(' ' * left_margin + '删除成功！')
        return student_information

    else:
        print(' ' * left_margin + '该学生不存在！')
        return student_information

# 修改信息函数
def modify_information():
    modify_name = input('请输入姓名：')
    if modify_name in student_name_list:
        output_window('sub_menu')
        while True:
            operation = int(input('请选择操作（序号）：'))
            # 修改姓名
            if operation == 1:
                new_name = input('请输入新姓名：')
                student_information[student_name_list.index(modify_name)][0] = new_name

            # 修改学号
            elif operation == 2:
                new_stu_number = input('请输入新学号：')
                student_information[student_name_list.index(modify_name)][1] = new_stu_number

            # 修改出生日期
            elif operation == 3:
                new_birthday = date_set()
                student_information[student_name_list.index(modify_name)][2] = new_birthday

            # 修改兴趣爱好
            elif operation == 4:
                new_hobby = input('请输入新的兴趣爱好：')
                student_information[student_name_list.index(modify_name)][3] = new_hobby

            # 修改完成
            elif operation == 5:
                break

            #  选择的操作无效
            else:
                output_window('wrong_choice')
        return student_information

    else:
        print(' ' * left_margin + '该学生不存在')
        return student_information

# 查询信息函数
def inquiry_information():
    inquiry_name = input('请输入要查询的姓名：')
    delay_time()
    if inquiry_name in student_name_list:
        temp = student_information[student_name_list.index(inquiry_name)]
        print(' ' * left_margin + '姓名   ' + '学号     ' + '出生日期            ' + '兴趣爱好')
        print(' ' * left_margin + '%s   %s    %s      %s' % (temp[0],temp[1],temp[2],temp[3]))
    else:
        print(' ' * left_margin + '该学生不存在')

# 遍历所有信息
def ergodic_information():
    delay_time()
    print(' ' * left_margin + '姓名   ' + '学号     ' + '出生日期            ' + '兴趣爱好')
    for temp in student_information:
        print(' ' * left_margin + '%s   %s    %s      %s' % (temp[0], temp[1], temp[2], temp[3]))

# 操作错误提示
def wrong_choice():
    print(' ' * left_margin + '您选择的操作无效，请重新选择！')

# 验证通过
def verify_passed():
    print(' ' * left_margin + '授权通过，欢迎使用！')
    delay_time()

# 密码错误
def wrong_password():
    print(' ' * left_margin + '您输入的密码错误，请重新输入！按任意键继续...')

# 用户名不存在
def invalid_username():
    print(' ' * left_margin + '您输入的用户名不存在，请重新输入！按任意键继续...')

# 延时函数
def delay_time():
    for i in range(3):
        print('\r{}请稍后，正在处理中...{}'.format(' '*left_margin,3-i),end='')
        time.sleep(1)
    print('\n')

# 初始化输出窗口设置
screen_width = 80
box_width = 60
left_margin = 20

# 初始化管理员信息
user_database = (('Jarvan','123456'),('David','234567'),('Smith','345678'))
user_name_list = [user_name for (user_name,password) in user_database]

# 初始化系统信息
student_information = [['张三','10010','Mar 8th, 1998','fish'],
                       ['李四','10086','Jun 9th, 1998','game'],
                       ['王五','10000','Oct 1st, 1998','sing']]

while True:
    # 验证管理员信息
    user_name = input('请输入管理员账号：')
    password = input('请输入密码：')

    # 验证通过
    if (user_name,password) in user_database:
        output_window('verify')
        while True:
            # 提示管理员选择操作
            student_name_list = [name for [name, student_number, birthday, hobby] in student_information]
            output_window('top_menu')
            operation = int(input('请选择操作（序号）：'))
            # 执行操作
            # 1.增加信息
            if operation == 1:
                student_information = input_information()

            # 2.删除信息
            elif operation == 2:
                student_information = delete_information()

            # 3.修改信息
            elif operation == 3:
                student_information = modify_information()

            # 4.查询信息
            elif operation == 4:
                output_window('inquiry')

            # 查询所有信息
            elif operation == 5:
                output_window('ergodic')

            # 退出系统
            elif operation == 6:
                break

            # 选择操作无效
            else:
                output_window('wrong_choice')
        break

    # 密码错误
    elif user_name in user_name_list:
        output_window('wrong_password')

    # 用户名不存在
    else:
        output_window('invalid_username')