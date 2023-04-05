
import os
filename = 'student.txt'  # 全局变量

def main():
    while True:
        menu()
        choice=int(input('请选择'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定要退出系统吗?y/n')
                if answer=='y' or answer=='y':
                    print('谢谢您的使用!!!')
                    break  # 退出系统
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()

def menu():
    print('==============================学生信息管理系统==================================')
    print('--------------------------------------功能菜单----------------------------------')
    print("""
    1.录入学生信息
    2.查找学生信息
    3.删除学生信息
    4.修改学生信息
    5.排序
    6.统计学生总人数
    7.显示所有学生信息
    0.退出
    """)
    print('---------------------------------------------------------------------------------')

def insert():
    stu_list=[]

    while True:
        id=input('请输入ID(如1001)：')
        if not id:
            break
        name=input('请输入姓名：')
        if not name: # 利用到了对象的布尔值
            break
        try:
            english=int(input('请输入英语成绩：'))
            python=int(input('请输入python成绩：'))
            java=int(input('请输入Java成绩：'))
        except:
            print('输入无敌，不是整数类型，请重新输入')
            continue

        stu={'id':id, 'name': name, 'english': english, 'python': python, 'java': java}

        stu_list.append(stu)

        answer=input('是否继续添加?y/n\n')
        if answer=='y':
            continue
        else:
            break

    save(stu_list)
    print('学生信息录入完毕！')

def save(lst):
    try:
        stu_txt=open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst: # item的数据类型是字典
        stu_txt.write(str(item)+'\n')

    stu_txt.close() # 关闭文件


def search():
    stu_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按ID查找请输入1，按姓名查找请输入2：')
            if mode=='1':
                id=input('请输入学生ID')
            elif mode=='2':
                name=input('请输入学生姓名')
            else:
                print('您的输入有误，请重新输入')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                stu=rfile.readlines()
                for item in stu:
                    d=dict(eval(item))
                    if id!='':
                        if d['id']==id:
                            stu_query.append(d)
                    elif name!='':
                        if d['name']==name:
                            stu_query.append(d)

            show_student(stu_query)

            stu_query.clear()
            answer=input('是否要继续查询？y/n\n')
            if answer=='y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息')
            return

def show_student(lst):
    if len(lst)==0:
        print('没有查询到学生信息，无数据显示！！！')
        return

    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}' # 字符的格式化输出
    print(format_title.format('ID','姓名','英语成绩','Python成绩','Java成绩','总成绩'))

    format_data='{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english'))+int(item.get('python'))+int(item.get('java'))
                                 ))

def delete():
    while True:
        stu_id=input('请输入要删除的学生的ID：')
        if stu_id!='':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    stu_old=file.readlines()
            else:
                stu_old=[]

            flag=False # 删除标记
            if stu_old:
                with open(filename, 'w', encoding='utf-8') as wfile: #通过重新写入实现删除
                    d={}
                    for item in stu_old:
                        d=dict(eval(item))
                        if d['id']!=stu_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag=True
                    if flag:
                        print(f'id为{stu_id}的学生信息已被删除')
                    else:
                        print(f'没有找到ID为{stu_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()
            answer=input('是否继续删除？y/n\n')
            if answer == 'y':
                continue
            else:
                break

def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            stu_old=rfile.readlines()
    else:
        return

    stu_id=input('请输入要修改的学员的ID：')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in stu_old:
            d=dict(eval(item))
            if d['id']==stu_id:
                print('找到学生信息，可以修改他的相关信息了!')
                while True:
                    try:
                        d['name'] = input('请输入姓名:')
                        d['english'] = input('请输入英语成绩:')
                        d['python'] = input('请输入Python成绩:')
                        d['java'] = input('请输入Java成绩:')
                    except:
                        print('您的输入有误，请重新输入!!!')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('修改成功')
            else:
                wfile.write(str(d)+'\n')

        answer=input('是否继续修改其他学生信息？y/n\n')
        if answer=='y':
            modify()

def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
        student_new = []
        for item in student_list:
            d=dict(eval(item))
            student_new.append(d)
    else:
        return

    asc_or_desc=input('请选择(0.升序 1.降序):')
    if asc_or_desc=='0':
        asc_or_desc_bool = False
    elif asc_or_desc=='1':
        asc_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入')
        sort()

    mode=input('请选择排序方式(1.按英语成绩排序 2.按Python成绩排序 3.按Java成绩排序 0.按总成绩排序):')
    if mode=='1':
        student_new.sort(key=lambda x :int(x['english']),reverse=asc_or_desc_bool)
    elif mode=='2':
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode=='3':
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    elif mode=='0':
        student_new.sort(key=lambda x: int(x['english'])+int(x['python'])+ int(x['java']), reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入！！！')
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students=rfile.readlines() #读一个列表
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存信息...')

def show():
    stu_list=[]
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()  # 读一个列表
            for item in students:
                stu_list.append(eval(item))

            if stu_list:
                show_student(stu_list)
    else:
        print('暂未保存信息...')


if __name__ == '__main__':
    main()