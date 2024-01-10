#-*- coding:utf-8 -*-
from tool import Frame
#格式(5*2)
#hh mm
#ss ff
a=Frame(5,2,"0.yuv")

#hh(10小时)
for h0 in range(0,1):
    a.SetChar(0,0,h0)
    for h1 in range(0,10):
        a.SetChar(1,0,h1)
        #mm(每小时60分钟)
        for m0 in range(0,6):
            a.SetChar(3,0,m0)
            for m1 in range(0,10):
                a.SetChar(4,0,m1)
                #ss(每分钟60秒)
                for s0 in range(0,6):
                    a.SetChar(0,1,s0)
                    for s1 in range(0,10):
                        a.SetChar(1,1,s1)
                        #ff(每秒30帧)
                        for f0 in range(0,3):
                            a.SetChar(3,1,f0)
                            for f1 in range(0,10):
                                a.SetChar(4,1,f1)
                                #每帧写入文件
                                #print(f"{h0}{h1}:{m0}{m1}:{s0}{s1}:{f0}{f1}")
                                a.Write()

#结束
a.Flush()
a.Close()
print(f"ffmpeg -r 30 {a.ffmpeg} -vcodec libx264 -threads 1 -preset slow -qp 0 -g 300 0.flv")