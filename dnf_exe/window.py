#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :window.py
# @Time      :2021/9/27 15:18
# @Author    :wlgu
import subprocess
import sys
from PyQt5.Qt import *
from dnf_exe.config import *


class Window:
    def __init__(self):
        self._app = QApplication(sys.argv)  # 启动实例对象
        self._window = self._get_window_obj()  # 获取窗口对象
        self._label_path = self._get_label_obj()  # 文件路径
        self._q_file = QFileDialog()  # 文件交互框
        self.btn1 = self._set_btn(btn1['name'], btn1['coordinate'], self._set_path)
        self.btn2 = self._set_btn(btn2['name'], btn2['coordinate'], self._btn_test2)
        self.btn3 = self._set_btn(btn3['name'], btn3['coordinate'], self._get_file)

    def _get_window_obj(self):
        '''
        配置window属性，并返回window对象
        :return:
        '''
        window = QWidget()  # 窗口
        window.resize(window_config['width'], window_config['height'])  # 窗口大小
        window.setWindowTitle('测试')  # 窗口左上角标题
        window.move(window_config['horizontal_shift'], window_config['vertical_shift'])  # 窗口偏移量
        return window

    def _get_label_obj(self):
        label = QLabel(self._window)
        label.setText('请选择文件')
        label.move(10, 10)

        return label

    def _set_path(self):
        '''
        设置启动文件路径
        :return:
        '''
        self._label_path.setText('测试显示btn1')

    # 槽函数2
    def _btn_test2(self):
        self._label_path.setText('点我干啥')

    # 槽函数3
    def _get_file(self):
        # 文件对话框
        a = self._q_file.getOpenFileName()
        if a[0]:
            subprocess.Popen(a[0])  # 启动新的进程
        print(a)

    def _set_btn(self, name, coordinate: tuple, event=None):
        '''实例化按钮'''
        btn = QPushButton(self._window)
        btn.setText(name)
        x, y = coordinate
        btn.move(x, y)
        if callable(event):
            btn.clicked.connect(event)  # 绑定对应点击事件

        return btn

    def main(self):
        self._window.show()
        sys.exit(self._app.exec_())


if __name__ == '__main__':
    # 显示窗体
    window = Window()
    window.main()
