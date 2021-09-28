#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test.py
# @Time      :2021/9/27 15:05
# @Author    :wlgu


import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)  # 实例对象

# 窗体大小
window = QWidget()
window.resize(800, 800)
window.setWindowTitle('测试')
window.move(400, 200)

label = QLabel(window)
label.setText('测试显示')
label.move(250, 100)


# 槽函数1
def btn_Old():
    label.setText('测试显示')


# 槽函数2
def btn_New():
    label.setText('点我干啥')


# 按钮1
btn1 = QPushButton(window)
btn1.setText('恢复显示')
btn1.move(200, 200)
btn1.clicked.connect(btn_Old)  # 信号与槽

# 按钮2
btn1 = QPushButton(window)
btn1.setText('修改显示')
btn1.move(300, 200)
btn1.clicked.connect(btn_New)  # 信号与槽

# 显示窗体
window.show()
sys.exit(app.exec_())
