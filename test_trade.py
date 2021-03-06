#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = ''

from py_ctp.trade import CtpTrade
from py_ctp.quote import CtpQuote
from py_ctp.enums import *
import time


class TestTrade(object):
    def __init__(self):
        self.t = CtpTrade()
        self.t.OnConnected = lambda x: self.t.ReqUserLogin('008107', '1', '9999')
        self.t.OnUserLogin = lambda o, x: print(x)
        self.t.OnDisConnected = lambda o, x: print(x)
        self.t.OnRtnNotice = lambda obj, time, msg: print(f'OnNotice: {time}:{msg}')
        self.t.OnErrRtnQuote = lambda obj, quote, info: None
        self.t.OnErrRtnQuoteInsert = lambda obj, o: None
        self.t.OnOrder = lambda obj, o: None
        self.t.OnErrOrder = lambda obj, f, info: None
        self.t.OnTrade = lambda obj, o: None
        self.t.OnInstrumentStatus = lambda obj, inst, stat: None

    def run(self):
        self.t.ReqConnect('tcp://180.168.146.187:10000')
        # self.t.ReqConnect('tcp://192.168.52.4:41205')

    def release(self):
        self.t.ReqUserLogout()


class TestQuote(object):
    """TestQuote"""

    def __init__(self):
        """"""
        self.q = CtpQuote()
        self.q.OnConnected = lambda x: self.q.ReqUserLogin('008107', '1', '9999')
        self.q.OnUserLogin = lambda o, i: self.q.ReqSubscribeMarketData('rb1910')

    def run(self):
        self.q.ReqConnect('tcp://180.168.146.187:10010')

    def release(self):
        self.q.ReqUserLogout()


if __name__ == "__main__":
    tt = TestTrade()
    tt.run()
    time.sleep(5)
    tt.t.ReqOrderInsert('j1905', DirectType.Buy, OffsetType.Open, 2060, 3)

    time.sleep(3)
    qq = TestQuote()
    qq.run()

    # time.sleep(6)
    # for inst in tt.t.instruments.values():
    #     print(inst)
    input()
    tt.release()
    qq.release()
    input()
