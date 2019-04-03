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
        conf.set("info","latency_accelerator","12.5")
        conf.set("info","energy_accelerator","2.5")
        conf.set("info","latency_gpu","447")
        conf.set("info","energy_gpu","34.73")
        conf.set("info","latency_dsp","521")
        conf.set("info","energy_dsp","25.2")
        conf.set("info","latency_npu1","26")
        conf.set("info","energy_npu1","2.7")
        conf.set("info","latency_npu2","24")
        conf.set("info","energy_npu2","2.7")
        conf.set("info","latency_predict","12.5")
        conf.set("info","energy_predict","0.5")
        conf.set("info","latency_check","2.5")

    if multi == 200704:
    	conf.set("info","CPU1_enable","30")
    	conf.set("info","latency_accelerator","92")
    	conf.set("info","energy_accelerator","12")
    	conf.set("info","latency_gpu","548")
    	conf.set("info","energy_gpu","80")
    	conf.set("info","latency_dsp","657.6")
    	conf.set("info","energy_dsp","67.2")
    	conf.set("info","latency_npu1","185")
    	conf.set("info","energy_npu1","12")
    	conf.set("info","latency_npu2","183")
    	conf.set("info","energy_npu2","12")
    	conf.set("info","latency_predict","62.5")
    	conf.set("info","energy_predict","3")
    	conf.set("info","latency_check","15")

    if multi == 369664:
        conf.set("info","latency_sensing","34")
        conf.set("info","latency_isp","34")
        conf.set("info","energy_sensing","6.5")
        conf.set("info","energy_isp","6.5")
        conf.set("info","CPU1_enable","70")
        conf.set("info","latency_accelerator","172")
        conf.set("info","energy_accelerator","20.6")
        conf.set("info","latency_gpu","651")
        conf.set("info","energy_gpu","77.25")
        conf.set("info","latency_dsp","742.8")
        conf.set("info","energy_dsp","57.225")
        conf.set("info","latency_npu1","346")
        conf.set("info","energy_npu1","20.6")
        conf.set("info","latency_npu2","344")
        conf.set("info","energy_npu2","20.6")
        conf.set("info","latency_predict","115")
        conf.set("info","energy_predict","5")
        conf.set("info","latency_check","27")

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
