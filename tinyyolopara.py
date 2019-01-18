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
        conf.set("info","CPU1_enable","50")
        conf.set("info","latency_accelerator","2.25")
        conf.set("info","energy_accelerator","0.34")
        conf.set("info","latency_gpu","413")
        conf.set("info","energy_gpu","17.6")
        conf.set("info","latency_dsp","498")
        conf.set("info","energy_dsp","14.8")
        conf.set("info","latency_npu1","4.5")
        conf.set("info","energy_npu1","0.38")
        conf.set("info","latency_npu2","4.49")
        conf.set("info","energy_npu2","0.38")
        conf.set("info","latency_predict","12.5")
        conf.set("info","energy_predict","0.5")
        conf.set("info","latency_check","2.5")

    if multi == 200704:
        conf.set("info","CPU1_enable","30")
        conf.set("info","latency_accelerator","18")
        conf.set("info","energy_accelerator","2")
        conf.set("info","latency_gpu","450")
        conf.set("info","energy_gpu","29.1")
        conf.set("info","latency_dsp","542")
        conf.set("info","energy_dsp","24.4")
        conf.set("info","latency_npu1","37")
        conf.set("info","energy_npu1","2")
        conf.set("info","latency_npu2","35")
        conf.set("info","energy_npu2","2")
        conf.set("info","latency_predict","62.5")
        conf.set("info","energy_predict","3")
        conf.set("info","latency_check","15")

    if multi == 369664:
        conf.set("info","CPU1_enable","70")
        conf.set("info","latency_accelerator","35")
        conf.set("info","energy_accelerator","3.84")
        conf.set("info","latency_gpu","468")
        conf.set("info","energy_gpu","55.5")
        conf.set("info","latency_dsp","563")
        conf.set("info","energy_dsp","46.6")
        conf.set("info","latency_npu1","70")
        conf.set("info","energy_npu1","3.84")
        conf.set("info","latency_npu2","60")
        conf.set("info","energy_npu2","3.84")
        conf.set("info","latency_predict","115")
        conf.set("info","energy_predict","5")
        conf.set("info","latency_check","27")

    if multi == 1036800:
        conf.set("info","CPU1_enable","90")
        conf.set("info","latency_accelerator","100")
        conf.set("info","energy_accelerator","11.3")
        conf.set("info","latency_gpu","596")
        conf.set("info","energy_gpu","200.256")
        conf.set("info","latency_dsp","718.1")
        conf.set("info","energy_dsp","168.4")
        conf.set("info","latency_npu1","200")
        conf.set("info","energy_npu1","11.3")
        conf.set("info","latency_npu2","199")
        conf.set("info","energy_npu2","11.3")
        conf.set("info","latency_predict","322.5")
        conf.set("info","energy_predict","14")
        conf.set("info","latency_check","75.6")

    with open("soc_configure.cfg","w+") as f:
        conf.write(f)
if __name__ == '__main__':
	main()
