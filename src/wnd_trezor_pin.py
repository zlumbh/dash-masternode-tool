#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Bertrand256
# Created on: 2017-03

from src import wnd_trezor_pin_base
from src.wnd_utils import WndUtils


class Ui_DialogTrezorPin(wnd_trezor_pin_base.Ui_DialogTrezorPin, WndUtils):
    def __init__(self, message):
        super().__init__()
        self.pin = ''
        self.message = message

    def new_key(self, new_key):
        self.pin += new_key
        self.edtPin.setText('*' * len(self.pin))

    def setupUi(self, window):
        self.window = window
        wnd_trezor_pin_base.Ui_DialogTrezorPin.setupUi(self, window)
        self.btnDelete.clicked.connect(self.btnDeleteClick)
        self.btnPin1.clicked.connect(lambda: self.new_key('1'))
        self.btnPin2.clicked.connect(lambda: self.new_key('2'))
        self.btnPin3.clicked.connect(lambda: self.new_key('3'))
        self.btnPin4.clicked.connect(lambda: self.new_key('4'))
        self.btnPin5.clicked.connect(lambda: self.new_key('5'))
        self.btnPin6.clicked.connect(lambda: self.new_key('6'))
        self.btnPin7.clicked.connect(lambda: self.new_key('7'))
        self.btnPin8.clicked.connect(lambda: self.new_key('8'))
        self.btnPin9.clicked.connect(lambda: self.new_key('9'))
        self.btnEnterPin.clicked.connect(self.btnEnterClick)
        self.lblMessage.setText(self.message)
        self.window.setWindowTitle('Hardware wallet PIN')

    def btnDeleteClick(self):
        self.pin = self.pin[:-1]
        self.edtPin.setText('*' * len(self.pin))

    def btnEnterClick(self):
        if self.pin:
            self.window.accept()
        else:
            self.errorMsg('Empty PIN!')
