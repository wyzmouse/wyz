# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 10:34:10 2018
@author: Administrator
创造者多帐户管理，解决创造者账户限制
"""
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pandas as pd
import webbrowser

# 窗口
window = tk.Tk()
window.title('欢迎进入学习系统')
window.geometry('800x600')

# 标签 用户名密码
tk.Label(window, text='用户名:').place(x=100, y=150)
tk.Label(window, text='密码:').place(x=100, y=190)
# 用户名输入框
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
# 密码输入框
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)


#取会员信息
#user_url = 'https://creator.zohopublic.com.cn/zt19jhht/app2/csv/hygl1/v08XMxv7PEW0rMrMVnEJhSVsKH22WPAdQwUz3xOsP4UUCr1wV3VRtN6W4t8Nn1JUjDheWHAEM2WUp6RF6srvEBAWDuwuEtM6KGOX/'
user_url1 = 'https://app.zohocreator.com.cn/zt19jhht/19htgl/csv/jbtzb/1QN3PZ3te3PAQxxFhuqu5hs4GBNBzx0EfhrJnaOOgCMYvvKuMQHKDngRZxQYw3enEbPSuFeuBUV62YKaef0dqf9b5PAJhw7Cm56d/'
user_url = 'https://app.zohocreator.com.cn/zt19jhht/app2/csv/hygl1/v08XMxv7PEW0rMrMVnEJhSVsKH22WPAdQwUz3xOsP4UUCr1wV3VRtN6W4t8Nn1JUjDheWHAEM2WUp6RF6srvEBAWDuwuEtM6KGOX'
user = pd.read_csv(user_url).set_index('帐号')
usrs_info = user.index

#会员注册链接
reg_url = 'https://creator.zohopublic.com.cn/zt19jhht/app2/page-perma/zche/wkMbKmsGu8MTMu30Cv3HGhvJthF1qEOhX0QZWKThhrpUQOF3UYOABKpzD71xjttuFkKAdxfjb3SkCkMjBEkuhJ4QyAr3zWTZahDC'

# 登录函数
def usr_log_in():
    # 输入框获取用户名密码
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    # 判断用户名和密码是否匹配
    
    
    if usr_name in usrs_info:
        print('有此用户！')
        mm = user.loc[usr_name,'手机']
        print(mm)
        if usr_pwd == str(mm):
            tk.messagebox.showinfo(title='welcome',message='欢迎您：' + usr_name)
            webbrowser.open('https://creator.zohopublic.com.cn/zt19jhht/app2/form-perma/hygl/UewRKR1xZ6R8nmVg4DMHUtCUOzGKdsmZ2vSZQCd7eS3wBnra50sUHrmHCHrznmq6Q7gXznm3gDZ5sX17S1pTX6VZgtJpCuRRRhVt')
            #window.destroy()
 

        else:
            tk.messagebox.showerror(message='密码错误,请重新输入密码！')
    # 用户名密码不能为空
    elif usr_name == '' or usr_pwd == '':
        tk.messagebox.showerror(message='用户名或密码为空')
    # 不在数据库中弹出是否注册的框
    else:
        is_signup = tk.messagebox.askyesno('警告', '您还没有注册，是否现在注册？')
        if is_signup:
            webbrowser.open('https://creator.zohopublic.com.cn/zt19jhht/app2/form-perma/hygl/UewRKR1xZ6R8nmVg4DMHUtCUOzGKdsmZ2vSZQCd7eS3wBnra50sUHrmHCHrznmq6Q7gXznm3gDZ5sX17S1pTX6VZgtJpCuRRRhVt?zh='+usr_name)


# 退出的函数
def usr_sign_quit():
    window.destroy()



#注册程序
def sign_up():
    w_sign = tk.Tk()
    w_sign.title('注册管理')
    w_sign.geometry('500x400')
    tk.Label(w_sign, text='单位:').place(x=100, y=100)
    tk.Label(w_sign, text='帐号:').place(x=100, y=150)
    tk.Label(w_sign, text='密码:').place(x=100, y=190)
    tk.Label(w_sign, text='姓名:').place(x=100, y=230)
    tk.Label(w_sign, text='手机:').place(x=100, y=270)    
    tk.Label(w_sign, text='邮箱:').place(x=100, y=310)
    
    # 用户名输入框
    usr_acount = tk.StringVar()
    en_usr_acount = tk.Entry(w_sign, textvariable=usr_acount)
    en_usr_acount.place(x=160, y=150)
    # 密码输入框
    usr_pwd = tk.StringVar()
    en_usr_pwd = tk.Entry(w_sign, textvariable=usr_pwd, show='*')
    en_usr_pwd.place(x=160, y=190)
    #姓名输入
    usr_name = tk.StringVar()
    en_usr_name = tk.Entry(w_sign, textvariable=usr_name)
    en_usr_name.place(x=160, y=230)    
    #手机输入
    usr_phone = tk.StringVar()
    en_usr_phone = tk.Entry(w_sign, textvariable=usr_phone)
    en_usr_phone.place(x=160, y=270)    
    #邮箱输入
    usr_mail = tk.StringVar()
    en_usr_mail = tk.Entry(w_sign, textvariable=usr_mail)
    en_usr_mail.place(x=160, y=310)   
    #取输入值
    figure = tk.StringVar()   
    en_usr_dw = ttk.Combobox(w_sign, textvariable=figure, state='readonly')
    en_usr_dw['values'] =('一处','二处','三处','五处','六处','七处')
    en_usr_dw.current(0)
    en_usr_dw.place(x=160,y=100)

    def sure_sign_up():
        qzh = en_usr_acount.get()
        qmm = en_usr_pwd.get()
        qxm = en_usr_name.get()
        qsj = en_usr_phone.get()
        qyx = en_usr_mail.get()
        cs = '?czh='+qzh+'&cmm='+qmm+'&cxm='+qxm+'&csj='+qsj+'&cyx='+qyx
        webbrowser.open(reg_url+cs)    

    def cancle_sign_up():
        w_sign.destroy()
    #确认注册按钮
    bt_sign_up = tk.Button(w_sign, text='确定', command=sure_sign_up)     
    bt_sign_up.place(x=120,y=350)
    bt_sign_up = tk.Button(w_sign, text='取消', command=cancle_sign_up)     
    bt_sign_up.place(x=180,y=350)
  
    w_sign.mainloop()
    
# 登录 注册按钮
bt_login = tk.Button(window, text='登录', command=usr_log_in)
bt_login.place(x=140, y=230)
bt_logup = tk.Button(window, text='注册', command=sign_up)
bt_logup.place(x=210, y=230)
bt_logquit = tk.Button(window, text='退出', command=usr_sign_quit)
bt_logquit.place(x=280, y=230)
# 主循环
window.mainloop()