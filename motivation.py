from __future__ import with_statement
from __future__ import print_function
import os
import configparser
import random
import numpy as np 
import schedule
import bestE


def main():
    config=configparser.ConfigParser()
    enable_performance = [0 for i in range(11)]
    enable_energy = [0 for i in range(11)]
    start_time = [0 for i in range(10000)]
    sensing_time = [0 for i in range(10000)]
    ISP_time = [0 for i in range(10000)]
    predict_time_p = [0 for i in range(10000)]
    predict_time_e = [0 for i in range(10000)]
    predict_time = [0 for i in range(10000)]
    CPU1_time = [0 for i in range(10000)]
    CPU5_time = [0 for i in range(10000)]
    GPU_time = [0 for i in range(10000)]
    DSP_time = [0 for i in range(10000)]
    accelerator_time = [0 for i in range(10000)]
    end_time_perf = [0 for i in range(10000)]
    end_time_energy = [0 for i in range(10000)]
    accumulation_CPU1 = 0
    accumulation_CPU5 = 0
    accumulation_GPU = 0
    accumulation_DSP = 0
    accumulation_accelerator = 0
    accumulation_spec_perf = 0
    accumulation_spec_energy = 0
    total_energy_CPU1 = 0
    total_energy_CPU5 = 0
    total_energy_GPU = 0
    total_energy_DSP = 0
    total_energy_accelerator = 0
    total_energy_spec_perf = 0
    total_energy_spec_energy = 0
    FCFS_sensing_time = [0 for i in range(10000)]
    FCFS_ISP_time = [0 for i in range(10000)]
    FCFS_end_time = [0 for i in range(10000)]
    hold_sensing_time = [0 for i in range(10000)]
    hold_ISP_time = [0 for i in range(10000)]
    hold_end_time = [0 for i in range(10000)]
    FCFS_acc = [0 for i in range(10000)]
    FCFS_gpu = [0 for i in range(10000)]
    FCFS_dsp = [0 for i in range(10000)]
    FCFS_cpu = [0 for i in range(10000)]
    accumulation_FCFS = 0
    accumulation_hold = 0
    total_energy_FCFS = 0
    total_energy_hold = 0
    predict_frame_location = 1
    flagacc = 1
    flaggpu = 2
    flagdsp = 3
    flag = 2
    L_budget = 1000
    E_budget = 1000
    count = 1
    base = 1
    predict_flag = 0
    ACC_signal = 0
    DSP_signal = 0
    GPU_signal = 0
    CPU_signal = 0
    ACC_signale = 0
    DSP_signale = 0
    GPU_signale = 0
    CPU_signale = 0
    with open("soc_configure.cfg","r+") as cfgfile:
        config.readfp(cfgfile)
        frame = int(config.get("info","frame"))
        CPU1_enable = int(config.get("info","CPU1_enable"))
        CPU2_enable = int(config.get("info","CPU2_enable"))
        CPU3_enable = int(config.get("info","CPU3_enable"))
        CPU4_enable = int(config.get("info","CPU4_enable"))
        CPU5_enable = int(config.get("info","CPU5_enable"))
        CPU6_enable = int(config.get("info","CPU6_enable"))
        CPU7_enable = int(config.get("info","CPU7_enable"))
        CPU8_enable = int(config.get("info","CPU8_enable"))
        GPU_enable = int(config.get("info","GPU_enable"))
        DSP_enable = int(config.get("info","DSP_enable"))
        accelerator_enable = int(config.get("info","accelerator_enable"))
        frames_predicted = int(config.get("info","frames_predicted"))
        frames_checked = int(config.get("info","frames_checked"))
        latency_sensing = float(config.get("info","latency_sensing"))
        latency_ISP = float(config.get("info","latency_ISP"))
        latency_CPU1 = float(config.get("info","latency_CPU1"))
        latency_CPU2 = float(config.get("info","latency_CPU2"))
        latency_CPU3 = float(config.get("info","latency_CPU3"))
        latency_CPU4 = float(config.get("info","latency_CPU4"))
        latency_CPU5 = float(config.get("info","latency_CPU5"))
        latency_CPU6 = float(config.get("info","latency_CPU6"))
        latency_CPU7 = float(config.get("info","latency_CPU7"))
        latency_CPU8 = float(config.get("info","latency_CPU8"))
        latency_GPU = float(config.get("info","latency_GPU"))
        latency_DSP = float(config.get("info","latency_DSP"))
        latency_accelerator = float(config.get("info","latency_accelerator"))
        latency_predict = float(config.get("info","latency_predict"))
        latency_check = float(config.get("info","latency_check"))
        latency_commit = float(config.get("info","latency_commit"))
        energy_sensing = float(config.get("info","energy_sensing"))
        energy_ISP = float(config.get("info","energy_ISP"))
        energy_CPU1 = float(config.get("info","energy_CPU1"))
        energy_CPU2 = float(config.get("info","energy_CPU2"))
        energy_CPU3 = float(config.get("info","energy_CPU3"))
        energy_CPU4 = float(config.get("info","energy_CPU4"))
        energy_CPU5 = float(config.get("info","energy_CPU5"))
        energy_CPU6 = float(config.get("info","energy_CPU6"))
        energy_CPU7 = float(config.get("info","energy_CPU7"))
        energy_CPU8 = float(config.get("info","energy_CPU8"))
        energy_GPU = float(config.get("info","energy_GPU"))
        energy_DSP = float(config.get("info","energy_DSP"))
        energy_accelerator = float(config.get("info","energy_accelerator"))
        energy_predict = float(config.get("info","energy_predict"))
        energy_check = float(config.get("info","energy_check"))
        energy_commit = float(config.get("info","energy_commit"))
        accuracy = float(config.get("info","accuracy"))
        energy_budget = float(config.get("info","energy_budget"))
        latency_budget = float(config.get("info","latency_budget"))
        app_degree = int(config.get("info","approximation_degree"))
    key_frame = 0
    for i in range(1,10+1):
    	if (i==1):
            start_time[i] = 0
    		#sensor
            sensing_time[i] = start_time[i] + latency_sensing
            total_energy_GPU = total_energy_GPU + energy_sensing
            total_energy_accelerator = total_energy_accelerator + energy_sensing
            total_energy_spec_perf = total_energy_spec_perf + energy_sensing
    		#ISP
            ISP_time[i] = sensing_time[i] + latency_ISP
            total_energy_GPU = total_energy_GPU + energy_ISP
            total_energy_accelerator = total_energy_accelerator + energy_ISP
            total_energy_spec_perf = total_energy_spec_perf + energy_ISP
    		#GPU
            GPU_time[i] = ISP_time[i] + latency_GPU + latency_commit
            total_energy_GPU = total_energy_GPU + energy_GPU + energy_commit
            accumulation_GPU = accumulation_GPU + GPU_time[i] - start_time[i]
    		#acc
            accelerator_time[i] = ISP_time[i] + latency_accelerator + latency_commit
            total_energy_accelerator = total_energy_accelerator + energy_accelerator + energy_commit
            accumulation_accelerator = accumulation_accelerator + accelerator_time[i] - start_time[i]
    		#pred
            end_time_perf[i] = ISP_time[i] + latency_accelerator + latency_commit
            total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
            accumulation_spec_perf = end_time_perf[i] - start_time[i]
    	else:
            start_time[i] = sensing_time[i-1]
            key_frame = i
    		#sensor
            sensing_time[i] = start_time[i] + latency_sensing
            total_energy_GPU = total_energy_GPU + energy_sensing
            total_energy_accelerator = total_energy_accelerator + energy_sensing
            total_energy_spec_perf = total_energy_spec_perf + energy_sensing
    		#ISP
            if (sensing_time[i] > ISP_time[i-1]):
            	ISP_time[i] = sensing_time[i-1] + latency_ISP
            else:
            	ISP_time[i] = ISP_time[i-1] + latency_ISP
            total_energy_GPU = total_energy_GPU + energy_ISP
            total_energy_accelerator = total_energy_accelerator + energy_ISP
            total_energy_spec_perf = total_energy_spec_perf + energy_ISP
    		#GPU
            if (ISP_time[i] > GPU_time[i-1]):
                GPU_time[i] = ISP_time[i] + latency_GPU
            else:
                GPU_time[i] = GPU_time[i-1] + latency_GPU
            total_energy_GPU = total_energy_GPU + energy_GPU
            accumulation_GPU = accumulation_GPU + GPU_time[i] - start_time[i]
    		#acc
            if (ISP_time[i] > accelerator_time[i-1]):
                accelerator_time[i] = ISP_time[i] + latency_accelerator
            else:
                accelerator_time[i] = accelerator_time[i-1] + latency_accelerator
            total_energy_accelerator = total_energy_accelerator + energy_accelerator + energy_commit
            accumulation_accelerator = accumulation_accelerator + accelerator_time[i] - start_time[i]
    		#pred
            if (ISP_time[i] > end_time_perf[i-1]):
                end_time_perf[i] = ISP_time[i] + latency_accelerator
            else:
                end_time_perf[i] = end_time_perf[i-1] + latency_accelerator
            total_energy_spec_perf = total_energy_spec_perf + energy_accelerator
            accumulation_spec_perf = accumulation_spec_perf + end_time_perf[i] - start_time[i]


    print('base_GPU', accumulation_GPU/10)
    print('base_acc', accumulation_accelerator/10)
    print('prediction', accumulation_spec_perf/10)
    print('base_energy', total_energy_GPU/10)
    print('acc_energy', total_energy_accelerator/10)
    print('pred_energy',total_energy_spec_perf/10)



if __name__ == '__main__':
	main()
