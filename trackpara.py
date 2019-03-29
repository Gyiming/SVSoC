from __future__ import with_statement
from __future__ import print_function
import os
import configparser
import random
import numpy as np 
import schedule
import bestE
import sys


def main():

    conf = configparser.ConfigParser()
    conf.read("soc_configure.cfg")
    sections = conf.sections()  
    resolution1 = int(sys.argv[1])
    resolution2 = int(sys.argv[2])
    #print(resolution1)
    #print(resolution2)
    multi = resolution2*resolution1
    print(multi)
    if multi == 32768:
        conf.set("info","latency_sensing","25")
        conf.set("info","latency_isp","25")
        conf.set("info","energy_sensing","5")
        conf.set("info","energy_isp","5")
        conf.set("info","CPU1_enable","50")
        conf.set("info","latency_accelerator","14.1")
        conf.set("info","energy_accelerator","18.45")
        conf.set("info","latency_gpu","421")
        conf.set("info","energy_gpu","217.4")
        conf.set("info","latency_dsp","490")
        conf.set("info","energy_dsp","157.7")
        conf.set("info","latency_npu1","26")
        conf.set("info","energy_npu1","2.7")
        conf.set("info","latency_npu2","24")
        conf.set("info","energy_npu2","2.7")
        conf.set("info","latency_predict","12.5")
        conf.set("info","energy_predict","0.5")
        conf.set("info","latency_check","2.5")
        conf.set("info","energy_budget","250")

    if multi == 369664:
        conf.set("info","latency_sensing","34")
        conf.set("info","latency_isp","34")
        conf.set("info","energy_sensing","6.5")
        conf.set("info","energy_isp","6.5")
        conf.set("info","CPU1_enable","50")
        conf.set("info","latency_accelerator","23.1")
        conf.set("info","energy_accelerator","20.45")
        conf.set("info","latency_gpu","421")
        conf.set("info","energy_gpu","217.4")
        conf.set("info","latency_dsp","490")
        conf.set("info","energy_dsp","157.7")
        conf.set("info","latency_npu1","26")
        conf.set("info","energy_npu1","2.7")
        conf.set("info","latency_npu2","24")
        conf.set("info","energy_npu2","2.7")
        conf.set("info","latency_predict","12.5")
        conf.set("info","energy_predict","5")
        conf.set("info","latency_check","2.5")
        conf.set("info","energy_budget","250")

    if multi == 1036800:
        conf.set("info","CPU1_enable","90")
        conf.set("info","latency_accelerator","892.4")
        conf.set("info","energy_accelerator","58.49")
        conf.set("info","latency_gpu","976")
        conf.set("info","energy_gpu","391")
        conf.set("info","latency_dsp","1171.2")
        conf.set("info","energy_dsp","332.3")
        conf.set("info","latency_npu1","1785")
        conf.set("info","energy_npu1","58.48")
        conf.set("info","latency_npu2","1785")
        conf.set("info","energy_npu2","58.49")
        conf.set("info","latency_predict","322.5")
        conf.set("info","energy_predict","14")
        conf.set("info","latency_check","75.6")

    with open("soc_configure.cfg","w+") as f:
        conf.write(f)
if __name__ == '__main__':
	main()
