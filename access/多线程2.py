# _*_coding:utf-8_*_


import pexpect
import datetime
from threading import Thread

host = ["192.168.1.1", "192.168.1.123", "192.168.2.1",
        "192.168.1.1", "192.168.1.123", "192.168.2.1",
        "192.168.1.1", "192.168.1.123", "192.168.2.1",
        "192.168.1.1", "192.168.1.123", "192.168.2.1",
        "192.168.1.1"]

report_ok = []
report_error = []




class PING(Thread):
    def __init__(self, ip):
        Thread.__init__(self)
        self.ip = ip

    def run(self):
        Curtime = datetime.datetime.now()
        # Scrtime = Curtime + datetime.timedelta(0,minute,0)
        # print("[%s]主机[%s]" % (Curtime,self.ip))
        ping = pexpect.spawn("ping -c1 %s" % (self.ip))
        check = ping.expect([pexpect.TIMEOUT, "1 packets transmitted, 1 received, 0% packet loss"], 2)
        if check == 0:
            print("[%s] 超时 %s" % (Curtime, self.ip))

        elif check == 1:
            print ("[%s] %s 可达" % (Curtime, self.ip))

        else:
            print("[%s] 主机%s 不可达" % (Curtime, self.ip))


# www.iplaypy.com
# 多线程同时执行
T_thread = []
for i in host:
    t = PING(i)
    T_thread.append(t)
for i in range(len(T_thread)):
    T_thread[i].start()
    #
    # print ("\n=========问题主机情况如下==========\n")
    # output(report_error)
    # print ("\n=========正常主机情况如下==========\n")
    # output(report_ok)