import sys
import time
from datetime import datetime as date

isLogin=False
account=[{"account": "admin", "password": "admin"}]
curren_acc=""

class User:

    def login(self):
        global isLogin
        global curren_acc
        acc = input("请输入登录账号：")
        pwd = input("请输入登录密码：")
        for item in account:
            if acc==item["account"] and pwd==item["password"]:
                print("登录成功！")
                isLogin=True
                curren_acc=acc
                break
        else:
            print("请核对登录信息......")
            self.login()

    def regisit(self):
        acc=input("请输入注册账号：")
        for i in account:
            if acc==i["account"]:
                print("该账号已存在......")
            else:
                pwd=input("请输入该账号的密码：")
                account.append({"account":acc,"password":pwd})
                print("注册账号成功")
                break


class Comment:

    def __init__(self):
        self.lst=[
            ["lucy", "帖子1", 10, 30, date.now()],
            ["lilei", "帖子2", 60, 100, date.now()],
            ["just do", "帖子3", 74, 200, date.now()],
        ]
        self.reply=[]

    #显示菜单
    def disp_menu(self):
        global isLogin
        while True:
            print("序号\t发帖人\t主题\t回复数量\t点击量\t最后回复时间")
            for i in range(len(self.lst)):
                print(i+1, self.lst[i][0], self.lst[i][1], self.lst[i][2], self.lst[i][3], self.lst[i][4], end="\t\t\t")
                print()
            print("="*50, "当前帖子", "="*50)
            func=input("请选择：1.回复主题 2.查看回复主题 3.注册账号 4.退出")
            if func=="1":
                if isLogin:
                    try:
                        num=eval(input("请输入需回复的主题序号："))
                        self.recall(num)
                    except Exception:
                        print("输入有误......")
                else:
                    print("请先登录......")
                    u=User()
                    u.login()
            elif func=="2":
                self.disp_comm()
            elif func=="3":
                u=User()
                u.regisit()
            elif func=="4":
                time.sleep(2)
                sys.exit()
            else:
                print("数据有误......")

    #查看回复
    def disp_comm(self):
        global curren_acc
        print("发帖人\t主题\t回复数量\t点击量\t最后回复时间")
        for item in self.reply:
            for i in range(len(self.lst)):
                if item["subject"]==self.lst[i][1]:
                    print(self.lst[i][0], item["subject"], len(item["context"]), curren_acc, self.lst[i][-1], end="\t\t\t\t")
                    print()
        print("-"*100)

    #回复帖子
    def recall(self, index):
        context=input("请输入回复主题：")
        if context!="":
            for item in self.reply:
                if self.lst[index-1][1]==item["subject"]: #判断主题
                    item["context"].append(context)
                    break
            else: #循环正常结束时执行的代码
                self.reply.append({"subject": self.lst[index-1][1], "context": [context]})
            self.lst[index-1][2]+=1
            self.lst[index-1][3]+=1
            self.lst[index-1][-1]=date.now()
            print("主题回复完毕!")
        else:
            self.recall(index)

if __name__ == '__main__':
    comm=Comment()
    comm.disp_menu()