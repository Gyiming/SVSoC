# -* - coding: UTF-8 -* -
from __future__ import with_statement
from __future__ import print_function
import os
import configparser
import random
import numpy as np 




def main():
    config=configparser.ConfigParser()
    enable_performance = [0 for i in range(11)]
    enable_energy = [0 for i in range(11)]
    start_time = [0 for i in range(10000)]
    sensing_time = [0 for i in range(10000)]
    ISP_time = [0 for i in range(10000)]
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
        latency_sensing = int(config.get("info","latency_sensing"))
        latency_ISP = int(config.get("info","latency_ISP"))
        latency_CPU1 = int(config.get("info","latency_CPU1"))
        latency_CPU2 = int(config.get("info","latency_CPU2"))
        latency_CPU3 = int(config.get("info","latency_CPU3"))
        latency_CPU4 = int(config.get("info","latency_CPU4"))
        latency_CPU5 = int(config.get("info","latency_CPU5"))
        latency_CPU6 = int(config.get("info","latency_CPU6"))
        latency_CPU7 = int(config.get("info","latency_CPU7"))
        latency_CPU8 = int(config.get("info","latency_CPU8"))
        latency_GPU = int(config.get("info","latency_GPU"))
        latency_DSP = int(config.get("info","latency_DSP"))
        latency_accelerator = int(config.get("info","latency_accelerator"))
        latency_predict = int(config.get("info","latency_predict"))
        latency_check = int(config.get("info","latency_check"))
        latency_commit = int(config.get("info","latency_commit"))
        energy_sensing = int(config.get("info","energy_sensing"))
        energy_ISP = int(config.get("info","energy_ISP"))
        energy_CPU1 = int(config.get("info","energy_CPU1"))
        energy_CPU2 = int(config.get("info","energy_CPU2"))
        energy_CPU3 = int(config.get("info","energy_CPU3"))
        energy_CPU4 = int(config.get("info","energy_CPU4"))
        energy_CPU5 = int(config.get("info","energy_CPU5"))
        energy_CPU6 = int(config.get("info","energy_CPU6"))
        energy_CPU7 = int(config.get("info","energy_CPU7"))
        energy_CPU8 = int(config.get("info","energy_CPU8"))
        energy_GPU = int(config.get("info","energy_GPU"))
        energy_DSP = int(config.get("info","energy_DSP"))
        energy_accelerator = int(config.get("info","energy_accelerator"))
        energy_predict = int(config.get("info","energy_predict"))
        energy_check = int(config.get("info","energy_check"))
        energy_commit = int(config.get("info","energy_commit"))
        accuracy = float(config.get("info","accuracy"))

    for i in range(1, frame+1):
        #assuming no check
        if (frames_checked == 0):
            if (i==1):
                predict_frame_location=1;
                start_time[i] = 0
                #sensing_time
                sensing_time[i] = start_time[i] + latency_sensing
                total_energy_CPU1 = total_energy_CPU1 + energy_sensing
                total_energy_CPU5 = total_energy_CPU5 + energy_sensing
                total_energy_GPU = total_energy_GPU + energy_sensing
                total_energy_DSP = total_energy_DSP + energy_sensing
                total_energy_accelerator = total_energy_accelerator + energy_sensing
                total_energy_spec_perf = total_energy_spec_perf + energy_sensing
                total_energy_spec_energy = total_energy_spec_energy + energy_sensing
                #ISP_time
                ISP_time[i] = sensing_time[i] + latency_ISP
                total_energy_CPU1 = total_energy_CPU1 + energy_ISP
                total_energy_CPU5 = total_energy_CPU5 + energy_ISP
                total_energy_GPU = total_energy_GPU + energy_ISP
                total_energy_DSP = total_energy_DSP + energy_ISP
                total_energy_accelerator = total_energy_accelerator + energy_ISP
                total_energy_spec_perf = total_energy_spec_perf + energy_ISP
                total_energy_spec_energy = total_energy_spec_energy + energy_ISP
                #fast_CPU baseline
                CPU1_time[i] = ISP_time[i] + latency_CPU1 + latency_commit
                total_energy_CPU1 = total_energy_CPU1 + energy_CPU1 + energy_commit
                accumulation_CPU1 = accumulation_CPU1 + CPU1_time[i] - start_time[i]
                #slow_CPU baseline
                CPU5_time[i] = ISP_time[i] + latency_CPU5 + latency_commit
                total_energy_CPU5 = total_energy_CPU5 + energy_CPU5 + energy_commit
                accumulation_CPU5 = accumulation_CPU5 + CPU5_time[i] - start_time[i]
                #GPU baseline
                GPU_time[i] = ISP_time[i] + latency_GPU + latency_commit
                total_energy_GPU = total_energy_GPU + energy_GPU + energy_commit
                accumulation_GPU = accumulation_GPU + GPU_time[i] - start_time[i]
                #DSP baseline
                DSP_time[i] = ISP_time[i] + latency_DSP + latency_commit
                total_energy_DSP = total_energy_DSP + energy_DSP + energy_commit
                accumulation_DSP = accumulation_DSP + DSP_time[i] - start_time[i]
                #accelerator baseline
                accelerator_time[i] = ISP_time[i] + latency_accelerator + latency_commit
                total_energy_accelerator = total_energy_accelerator + energy_accelerator + energy_commit
                accumulation_accelerator = accumulation_accelerator + accelerator_time[i] - start_time[i]
                #spec_soc_performance_first
                end_time_perf[i] = ISP_time[i] + latency_accelerator + latency_commit
                total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                accumulation_spec_perf = end_time_perf[i] - start_time[i]
                #spec_soc_energy_first
                end_time_energy[i] = ISP_time[i] + latency_CPU5 + latency_commit
                total_energy_spec_energy = total_energy_spec_energy + energy_CPU5 + energy_commit
                accumulation_spec_energy = end_time_energy[i] - start_time[i]
                #predict_time
                total_energy_spec_perf = total_energy_spec_perf + energy_predict
                total_energy_spec_energy = total_energy_spec_energy + energy_predict
                for j in range(2,frames_predicted+1):
                    predict_time[j] = ISP_time[i] + latency_predict

            elif ((i-predict_frame_location) == (frames_predicted+1)):
                predict_frame_location = i;
                start_time[i] = sensing_time[i-1]
                #sensing_time
                sensing_time[i] = start_time[i] + latency_sensing
                total_energy_CPU1 = total_energy_CPU1 + energy_sensing
                total_energy_CPU5 = total_energy_CPU5 + energy_sensing
                total_energy_GPU = total_energy_GPU + energy_sensing
                total_energy_DSP = total_energy_DSP + energy_sensing
                total_energy_accelerator = total_energy_accelerator + energy_sensing
                total_energy_spec_perf = total_energy_spec_perf + energy_sensing
                total_energy_spec_energy = total_energy_spec_energy + energy_sensing
                #ISP_time
                if (sensing_time[i] > ISP_time[i-1]):
                    ISP_time[i] = sensing_time[i] + latency_ISP
                    total_energy_CPU1 = total_energy_CPU1 + energy_ISP
                    total_energy_CPU5 = total_energy_CPU5 + energy_ISP
                    total_energy_GPU = total_energy_GPU + energy_ISP
                    total_energy_DSP = total_energy_DSP + energy_ISP
                    total_energy_accelerator = total_energy_accelerator + energy_ISP
                    total_energy_spec_perf = total_energy_spec_perf + energy_ISP
                    total_energy_spec_energy = total_energy_spec_energy + energy_ISP
                else:
                    ISP_time[i] = ISP_time[i-1] + latency_ISP
                    total_energy_CPU1 = total_energy_CPU1 + energy_ISP
                    total_energy_CPU5 = total_energy_CPU5 + energy_ISP
                    total_energy_GPU = total_energy_GPU + energy_ISP
                    total_energy_DSP = total_energy_DSP + energy_ISP
                    total_energy_accelerator = total_energy_accelerator + energy_ISP
                    total_energy_spec_perf = total_energy_spec_perf + energy_ISP
                    total_energy_spec_energy = total_energy_spec_energy + energy_ISP
                #fast_CPU baseline
                if (ISP_time[i] > CPU1_time[i-1]):
                    CPU1_time[i] = ISP_time[i] + latency_CPU1 + latency_commit
                    total_energy_CPU1 = total_energy_CPU1 + energy_CPU1 + energy_commit
                    accumulation_CPU1 = accumulation_CPU1 + CPU1_time[i] - start_time[i]
                else:
                    CPU1_time[i] = CPU1_time[i-1] + latency_CPU1 + latency_commit
                    total_energy_CPU1 = total_energy_CPU1 + energy_CPU1 + energy_commit
                    accumulation_CPU1 = accumulation_CPU1 + CPU1_time[i] - start_time[i]
                #slow_CPU baseline
                if (ISP_time[i] > CPU5_time[i-1]):
                    CPU5_time[i] = ISP_time[i] + latency_CPU5 + latency_commit
                    total_energy_CPU5 = total_energy_CPU5 + energy_CPU5 + energy_commit
                    accumulation_CPU5 = accumulation_CPU5 + CPU5_time[i] - start_time[i]
                else:
                    CPU5_time[i] = CPU5_time[i-1] + latency_CPU5 + latency_commit
                    total_energy_CPU5 = total_energy_CPU5 + energy_CPU5 + energy_commit
                    accumulation_CPU5 = accumulation_CPU5 + CPU5_time[i] - start_time[i]
                #GPU baseline
                if (ISP_time[i] > GPU_time[i-1]):
                    GPU_time[i] = ISP_time[i] + latency_GPU + latency_commit
                    total_energy_GPU = total_energy_GPU + energy_GPU + energy_commit
                    accumulation_GPU = accumulation_GPU + GPU_time[i] - start_time[i]
                else:
                    GPU_time[i] = GPU_time[i-1] + latency_GPU + latency_commit
                    total_energy_GPU = total_energy_GPU + energy_GPU + energy_commit
                    accumulation_GPU = accumulation_GPU + GPU_time[i] - start_time[i]
                #DSP baseline
                if (ISP_time[i] > DSP_time[i-1]):
                    DSP_time[i] = ISP_time[i] + latency_DSP + latency_commit
                    total_energy_DSP = total_energy_DSP + energy_DSP + energy_commit
                    accumulation_DSP = accumulation_DSP + DSP_time[i] - start_time[i]
                else:
                    DSP_time[i] = DSP_time[i-1] + latency_DSP + latency_commit
                    total_energy_DSP = total_energy_DSP + energy_DSP + energy_commit
                    accumulation_DSP = accumulation_DSP + DSP_time[i] - start_time[i]
                #accelerator baseline
                if (ISP_time[i] > accelerator_time[i-1]):
                    accelerator_time[i] = ISP_time[i] + latency_accelerator + latency_commit
                    total_energy_accelerator = total_energy_accelerator + energy_accelerator + energy_commit
                    accumulation_accelerator = accumulation_accelerator + accelerator_time[i] - start_time[i]
                else:
                    accelerator_time[i] = accelerator_time[i-1] + latency_accelerator + latency_commit
                    total_energy_accelerator = total_energy_accelerator + energy_accelerator + energy_commit
                    accumulation_accelerator = accumulation_accelerator + accelerator_time[i] - start_time[i]
                #spec_soc_performance_first
                if (ISP_time[i] > end_time_perf[i-1]):
                    end_time_perf[i] = ISP_time[i] + latency_accelerator + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                    accumulation_spec_perf = accumulation_spec_perf + end_time_perf[i] - start_time[i]
                else:
                    end_time_perf[i] = end_time_perf[i-1] + latency_accelerator + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                    accumulation_spec_perf = accumulation_spec_perf + end_time_perf[i] - start_time[i]
                #spec_soc_energy_first
                if (ISP_time[i] > end_time_energy[i-1]):
                    end_time_energy[i] = ISP_time[i] + latency_accelerator + latency_commit
                    total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                    accumulation_spec_energy = accumulation_spec_energy + end_time_energy[i] - start_time[i]
                else:
                    end_time_energy[i] = end_time_energy[i-1] + latency_accelerator + latency_commit
                    total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                    accumulation_spec_energy = accumulation_spec_energy + end_time_energy[i] - start_time[i]
                #predict_time
                total_energy_spec_perf = total_energy_spec_perf + energy_predict
                total_energy_spec_energy = total_energy_spec_energy + energy_predict
                for j in range(i+1,i+frames_predicted+1):
                    predict_time[j] = ISP_time[i] + latency_predict

            else:
                start_time[i] = sensing_time[i-1]
                #sensing time
                sensing_time[i] = start_time[i] + latency_sensing
                total_energy_CPU1 = total_energy_CPU1 + energy_sensing
                total_energy_CPU5 = total_energy_CPU5 + energy_sensing
                total_energy_GPU = total_energy_GPU + energy_sensing
                total_energy_DSP = total_energy_DSP + energy_sensing
                total_energy_accelerator = total_energy_accelerator + energy_sensing
                #total_energy_spec_perf = total_energy_spec_perf + energy_sensing
                #total_energy_spec_energy = total_energy_spec_energy + energy_sensing
                #ISP time
                if (sensing_time[i] > ISP_time[i-1]):
                    ISP_time[i] = sensing_time[i] + latency_ISP
                    total_energy_CPU1 = total_energy_CPU1 + energy_ISP
                    total_energy_CPU5 = total_energy_CPU5 + energy_ISP
                    total_energy_GPU = total_energy_GPU + energy_ISP
                    total_energy_DSP = total_energy_DSP + energy_ISP
                    total_energy_accelerator = total_energy_accelerator + energy_ISP
                    #total_energy_spec_perf = total_energy_spec_perf + energy_ISP
                    #total_energy_spec_energy = total_energy_spec_energy + energy_ISP
                else:
                    ISP_time[i] = ISP_time[i-1] + latency_ISP
                    total_energy_CPU1 = total_energy_CPU1 + energy_ISP
                    total_energy_CPU5 = total_energy_CPU5 + energy_ISP
                    total_energy_GPU = total_energy_GPU + energy_ISP
                    total_energy_DSP = total_energy_DSP + energy_ISP
                    total_energy_accelerator = total_energy_accelerator + energy_ISP
                    #total_energy_spec_perf = total_energy_spec_perf + energy_ISP
                    #total_energy_spec_energy = total_energy_spec_energy + energy_ISP
                #fast_CPU baseline
                if (ISP_time[i] > CPU1_time[i-1]):
                    CPU1_time[i] = ISP_time[i] + latency_CPU1 + latency_commit
                    total_energy_CPU1 = total_energy_CPU1 + energy_CPU1 + energy_commit
                    accumulation_CPU1 = accumulation_CPU1 + CPU1_time[i] - start_time[i]
                else:
                    CPU1_time[i] = CPU1_time[i-1] + latency_CPU1 + latency_commit
                    total_energy_CPU1 = total_energy_CPU1 + energy_CPU1 + energy_commit
                    accumulation_CPU1 = accumulation_CPU1 + CPU1_time[i] - start_time[i]
                #slow_CPU baseline
                if (ISP_time[i] > CPU5_time[i-1]):
                    CPU5_time[i] = ISP_time[i] + latency_CPU5 + latency_commit
                    total_energy_CPU5 = total_energy_CPU5 + energy_CPU5 + energy_commit
                    accumulation_CPU5 = accumulation_CPU5 + CPU5_time[i] - start_time[i]
                else:
                    CPU5_time[i] = CPU5_time[i-1] + latency_CPU5 + latency_commit
                    total_energy_CPU5 = total_energy_CPU5 + energy_CPU5 + energy_commit
                    accumulation_CPU5 = accumulation_CPU5 + CPU5_time[i] - start_time[i]
                #GPU baseline
                if (ISP_time[i] > GPU_time[i-1]):
                    GPU_time[i] = ISP_time[i] + latency_GPU + latency_commit
                    total_energy_GPU = total_energy_GPU + energy_GPU + energy_commit
                    accumulation_GPU = accumulation_GPU + GPU_time[i] - start_time[i]
                else:
                    GPU_time[i] = GPU_time[i-1] + latency_GPU + latency_commit
                    total_energy_GPU = total_energy_GPU + energy_GPU + energy_commit
                    accumulation_GPU = accumulation_GPU + GPU_time[i] - start_time[i]
                #DSP baseline
                if (ISP_time[i] > DSP_time[i-1]):
                    DSP_time[i] = ISP_time[i] + latency_DSP + latency_commit
                    total_energy_DSP = total_energy_DSP + energy_DSP + energy_commit
                    accumulation_DSP = accumulation_DSP + DSP_time[i] - start_time[i]
                else:
                    DSP_time[i] = DSP_time[i-1] + latency_DSP + latency_commit
                    total_energy_DSP = total_energy_DSP + energy_DSP + energy_commit
                    accumulation_DSP = accumulation_DSP + DSP_time[i] - start_time[i]
                #accelerator baseline
                if (ISP_time[i] > accelerator_time[i-1]):
                    accelerator_time[i] = ISP_time[i] + latency_accelerator + latency_commit
                    total_energy_accelerator = total_energy_accelerator + energy_accelerator + energy_commit
                    accumulation_accelerator = accumulation_accelerator + accelerator_time[i] - start_time[i]
                else:
                    accelerator_time[i] = accelerator_time[i-1] + latency_accelerator + latency_commit
                    total_energy_accelerator = total_energy_accelerator + energy_accelerator + energy_commit
                    accumulation_accelerator = accumulation_accelerator + accelerator_time[i] - start_time[i]
                #spec_soc_latencymin, E<=Eb
                #energy_Eb_minL, latency_Eb_minL = runtime2(frames_predicted,latency_CPU1,latency_GPU,latency_DSP,latency_accelerator,energy_CPU1,energy_GPU,energy_DSP,energy_accelerator,E_budget)
                
                if ((i-predict_frame_location)==1):
                    end_time_perf[i] = predict_time[i] + latency_accelerator + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==2):
                    end_time_perf[i] = predict_time[i] + latency_GPU + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_GPU + energy_commit
                elif ((i-predict_frame_location)==3):
                    end_time_perf[i] = predict_time[i] + latency_accelerator*2 + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==4):
                    end_time_perf[i] = predict_time[i] + latency_DSP + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_DSP + energy_commit
                elif ((i-predict_frame_location)==5):
                    end_time_perf[i] = predict_time[i] + latency_accelerator*3 + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==6):
                    end_time_perf[i] = predict_time[i] + latency_GPU*2 + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_GPU + energy_commit
                elif ((i-predict_frame_location)==7):
                    end_time_perf[i] = predict_time[i] + latency_accelerator*4 + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==8):
                    end_time_perf[i] = predict_time[i] + latency_DSP*2 + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_DSP + energy_commit
                elif ((i-predict_frame_location)==9):
                    end_time_perf[i] = predict_time[i] + latency_accelerator*5 + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==10):
                    end_time_perf[i] = predict_time[i] + latency_GPU*3 + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_GPU + energy_commit
                '''
                if ((i-predict_frame_location)==1):
                    end_time_perf[i] = predict_time[i] + latency_accelerator + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==2):
                    end_time_perf[i] = predict_time[i] + latency_GPU + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_GPU + energy_commit
                elif ((i-predict_frame_location)==3):
                    end_time_perf[i] = predict_time[i] + latency_accelerator*2 + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==4):
                    end_time_perf[i] = predict_time[i] + latency_DSP + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_DSP + energy_commit
                elif ((i-predict_frame_location)==5):
                    end_time_perf[i] = predict_time[i] + latency_accelerator*3 + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==6):
                    end_time_perf[i] = predict_time[i] + latency_accelerator*4 + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_GPU + energy_commit
                elif ((i-predict_frame_location)==7):
                    end_time_perf[i] = predict_time[i] + latency_accelerator*5 + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==8):
                    end_time_perf[i] = predict_time[i] + latency_accelerator*6 + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_DSP + energy_commit
                elif ((i-predict_frame_location)==9):
                    end_time_perf[i] = predict_time[i] + latency_accelerator*7 + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==10):
                    end_time_perf[i] = predict_time[i] + latency_accelerator*8 + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_GPU + energy_commit
                '''
                accumulation_spec_perf = accumulation_spec_perf + end_time_perf[i] - start_time[i]                
                
                #spec_soc_energymin, L<=Lb
                #energy_Lb_minE, latency_Lb_minE  = runtime1(frames_predicted,latency_CPU1,latency_GPU,latency_DSP,latency_accelerator,energy_CPU1,energy_GPU,energy_DSP,energy_accelerator,L_budget)
                if ((i-predict_frame_location)==1):
                    end_time_energy[i] = predict_time[i] + latency_accelerator + latency_commit
                    total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==2):
                    end_time_energy[i] = predict_time[i] + latency_accelerator*2 + latency_commit
                    total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==3):
                    end_time_energy[i] = predict_time[i] + latency_DSP + latency_commit
                    total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==4):
                    end_time_energy[i] = predict_time[i] + latency_accelerator*3 + latency_commit
                    total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==5):
                    end_time_energy[i] = predict_time[i] + latency_accelerator*4 + latency_commit
                    total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==6):
                    end_time_energy[i] = predict_time[i] + latency_accelerator*5 + latency_commit
                    total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==7):
                    end_time_energy[i] = predict_time[i] + latency_accelerator*6 + latency_commit
                    total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==8):
                    end_time_energy[i] = predict_time[i] + latency_accelerator*7 + latency_commit
                    total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==9):
                    end_time_energy[i] = predict_time[i] + latency_accelerator*8 + latency_commit
                    total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                elif ((i-predict_frame_location)==10):
                    end_time_energy[i] = predict_time[i] + latency_accelerator*9 + latency_commit
                    total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                accumulation_spec_energy = accumulation_spec_energy + end_time_energy[i] - start_time[i]

        #need check

        else:
            if (i==1):
                predict_frame_location=1;
                start_time[i] = 0
                #sensing_time
                sensing_time[i] = start_time[i] + latency_sensing
                total_energy_CPU1 = total_energy_CPU1 + energy_sensing
                total_energy_CPU5 = total_energy_CPU5 + energy_sensing
                total_energy_GPU = total_energy_GPU + energy_sensing
                total_energy_DSP = total_energy_DSP + energy_sensing
                total_energy_accelerator = total_energy_accelerator + energy_sensing
                total_energy_spec_perf = total_energy_spec_perf + energy_sensing
                total_energy_spec_energy = total_energy_spec_energy + energy_sensing
                #ISP_time
                ISP_time[i] = sensing_time[i] + latency_ISP
                total_energy_CPU1 = total_energy_CPU1 + energy_ISP
                total_energy_CPU5 = total_energy_CPU5 + energy_ISP
                total_energy_GPU = total_energy_GPU + energy_ISP
                total_energy_DSP = total_energy_DSP + energy_ISP
                total_energy_accelerator = total_energy_accelerator + energy_ISP
                total_energy_spec_perf = total_energy_spec_perf + energy_ISP
                total_energy_spec_energy = total_energy_spec_energy + energy_ISP
                #fast_CPU baseline
                CPU1_time[i] = ISP_time[i] + latency_CPU1 + latency_commit
                total_energy_CPU1 = total_energy_CPU1 + energy_CPU1 + energy_commit
                accumulation_CPU1 = accumulation_CPU1 + CPU1_time[i] - start_time[i]
                #slow_CPU baseline
                CPU5_time[i] = ISP_time[i] + latency_CPU5 + latency_commit
                total_energy_CPU5 = total_energy_CPU5 + energy_CPU5 + energy_commit
                accumulation_CPU5 = accumulation_CPU5 + CPU5_time[i] - start_time[i]
                #GPU baseline
                GPU_time[i] = ISP_time[i] + latency_GPU + latency_commit
                total_energy_GPU = total_energy_GPU + energy_GPU + energy_commit
                accumulation_GPU = accumulation_GPU + GPU_time[i] - start_time[i]
                #DSP baseline
                DSP_time[i] = ISP_time[i] + latency_DSP + latency_commit
                total_energy_DSP = total_energy_DSP + energy_DSP + energy_commit
                accumulation_DSP = accumulation_DSP + DSP_time[i] - start_time[i]
                #accelerator baseline
                accelerator_time[i] = ISP_time[i] + latency_accelerator + latency_commit
                total_energy_accelerator = total_energy_accelerator + energy_accelerator + energy_commit
                accumulation_accelerator = accumulation_accelerator + accelerator_time[i] - start_time[i]
                #spec_soc_performance_first
                end_time_perf[i] = ISP_time[i] + latency_accelerator + latency_commit
                total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                accumulation_spec_perf = end_time_perf[i] - start_time[i]
                #spec_soc_energy_first
                end_time_energy[i] = ISP_time[i] + latency_CPU5 + latency_commit
                total_energy_spec_energy = total_energy_spec_energy + energy_CPU5 + energy_commit
                accumulation_spec_energy = end_time_energy[i] - start_time[i]
                #predict_time
                total_energy_spec_perf = total_energy_spec_perf + energy_predict
                total_energy_spec_energy = total_energy_spec_energy + energy_predict
                for j in range(2,frames_predicted+1):
                    predict_time[j] = ISP_time[i] + latency_predict

            elif ((i-predict_frame_location) == (frames_predicted+1)):
                predict_frame_location = i;
                start_time[i] = sensing_time[i-1]
                #sensing_time
                sensing_time[i] = start_time[i] + latency_sensing
                total_energy_CPU1 = total_energy_CPU1 + energy_sensing
                total_energy_CPU5 = total_energy_CPU5 + energy_sensing
                total_energy_GPU = total_energy_GPU + energy_sensing
                total_energy_DSP = total_energy_DSP + energy_sensing
                total_energy_accelerator = total_energy_accelerator + energy_sensing
                total_energy_spec_perf = total_energy_spec_perf + energy_sensing
                total_energy_spec_energy = total_energy_spec_energy + energy_sensing
                #ISP_time
                if (sensing_time[i] > ISP_time[i-1]):
                    ISP_time[i] = sensing_time[i] + latency_ISP
                    total_energy_CPU1 = total_energy_CPU1 + energy_ISP
                    total_energy_CPU5 = total_energy_CPU5 + energy_ISP
                    total_energy_GPU = total_energy_GPU + energy_ISP
                    total_energy_DSP = total_energy_DSP + energy_ISP
                    total_energy_accelerator = total_energy_accelerator + energy_ISP
                    total_energy_spec_perf = total_energy_spec_perf + energy_ISP
                    total_energy_spec_energy = total_energy_spec_energy + energy_ISP
                else:
                    ISP_time[i] = ISP_time[i-1] + latency_ISP
                    total_energy_CPU1 = total_energy_CPU1 + energy_ISP
                    total_energy_CPU5 = total_energy_CPU5 + energy_ISP
                    total_energy_GPU = total_energy_GPU + energy_ISP
                    total_energy_DSP = total_energy_DSP + energy_ISP
                    total_energy_accelerator = total_energy_accelerator + energy_ISP
                    total_energy_spec_perf = total_energy_spec_perf + energy_ISP
                    total_energy_spec_energy = total_energy_spec_energy + energy_ISP
                #fast_CPU baseline
                if (ISP_time[i] > CPU1_time[i-1]):
                    CPU1_time[i] = ISP_time[i] + latency_CPU1 + latency_commit
                    total_energy_CPU1 = total_energy_CPU1 + energy_CPU1 + energy_commit
                    accumulation_CPU1 = accumulation_CPU1 + CPU1_time[i] - start_time[i]
                else:
                    CPU1_time[i] = CPU1_time[i-1] + latency_CPU1 + latency_commit
                    total_energy_CPU1 = total_energy_CPU1 + energy_CPU1 + energy_commit
                    accumulation_CPU1 = accumulation_CPU1 + CPU1_time[i] - start_time[i]
                #slow_CPU baseline
                if (ISP_time[i] > CPU5_time[i-1]):
                    CPU5_time[i] = ISP_time[i] + latency_CPU5 + latency_commit
                    total_energy_CPU5 = total_energy_CPU5 + energy_CPU5 + energy_commit
                    accumulation_CPU5 = accumulation_CPU5 + CPU5_time[i] - start_time[i]
                else:
                    CPU5_time[i] = CPU5_time[i-1] + latency_CPU5 + latency_commit
                    total_energy_CPU5 = total_energy_CPU5 + energy_CPU5 + energy_commit
                    accumulation_CPU5 = accumulation_CPU5 + CPU5_time[i] - start_time[i]
                #GPU baseline
                if (ISP_time[i] > GPU_time[i-1]):
                    GPU_time[i] = ISP_time[i] + latency_GPU + latency_commit
                    total_energy_GPU = total_energy_GPU + energy_GPU + energy_commit
                    accumulation_GPU = accumulation_GPU + GPU_time[i] - start_time[i]
                else:
                    GPU_time[i] = GPU_time[i-1] + latency_GPU + latency_commit
                    total_energy_GPU = total_energy_GPU + energy_GPU + energy_commit
                    accumulation_GPU = accumulation_GPU + GPU_time[i] - start_time[i]
                #DSP baseline
                if (ISP_time[i] > DSP_time[i-1]):
                    DSP_time[i] = ISP_time[i] + latency_DSP + latency_commit
                    total_energy_DSP = total_energy_DSP + energy_DSP + energy_commit
                    accumulation_DSP = accumulation_DSP + DSP_time[i] - start_time[i]
                else:
                    DSP_time[i] = DSP_time[i-1] + latency_DSP + latency_commit
                    total_energy_DSP = total_energy_DSP + energy_DSP + energy_commit
                    accumulation_DSP = accumulation_DSP + DSP_time[i] - start_time[i]
                #accelerator baseline
                if (ISP_time[i] > accelerator_time[i-1]):
                    accelerator_time[i] = ISP_time[i] + latency_accelerator + latency_commit
                    total_energy_accelerator = total_energy_accelerator + energy_accelerator + energy_commit
                    accumulation_accelerator = accumulation_accelerator + accelerator_time[i] - start_time[i]
                else:
                    accelerator_time[i] = accelerator_time[i-1] + latency_accelerator + latency_commit
                    total_energy_accelerator = total_energy_accelerator + energy_accelerator + energy_commit
                    accumulation_accelerator = accumulation_accelerator + accelerator_time[i] - start_time[i]
                #spec_soc_performance_first
                if (ISP_time[i] > end_time_perf[i-1]):
                    end_time_perf[i] = ISP_time[i] + latency_accelerator + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                    accumulation_spec_perf = accumulation_spec_perf + end_time_perf[i] - start_time[i]
                else:
                    end_time_perf[i] = end_time_perf[i-1] + latency_accelerator + latency_commit
                    total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                    accumulation_spec_perf = accumulation_spec_perf + end_time_perf[i] - start_time[i]
                #spec_soc_energy_first
                if (ISP_time[i] > end_time_energy[i-1]):
                    end_time_energy[i] = ISP_time[i] + latency_accelerator + latency_commit
                    total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                    accumulation_spec_energy = accumulation_spec_energy + end_time_energy[i] - start_time[i]
                else:
                    end_time_energy[i] = end_time_energy[i-1] + latency_accelerator + latency_commit
                    total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                    accumulation_spec_energy = accumulation_spec_energy + end_time_energy[i] - start_time[i]
                #predict_time
                total_energy_spec_perf = total_energy_spec_perf + energy_predict
                total_energy_spec_energy = total_energy_spec_energy + energy_predict
                for j in range(i+1,i+frames_predicted+1):
                    predict_time[j] = ISP_time[i] + latency_predict

            else:
                precision=random.random()
                if (precision <=1-accuracy):
                #check wrong
                    predict_frame_location = i;
                    start_time[i] = sensing_time[i-1]
                    #sensing_time
                    sensing_time[i] = start_time[i] + latency_sensing
                    total_energy_CPU1 = total_energy_CPU1 + energy_sensing
                    total_energy_CPU5 = total_energy_CPU5 + energy_sensing
                    total_energy_GPU = total_energy_GPU + energy_sensing
                    total_energy_DSP = total_energy_DSP + energy_sensing
                    total_energy_accelerator = total_energy_accelerator + energy_sensing
                    total_energy_spec_perf = total_energy_spec_perf + energy_sensing
                    total_energy_spec_energy = total_energy_spec_energy + energy_sensing
                    #ISP_time
                    if (sensing_time[i] > ISP_time[i-1]):
                        ISP_time[i] = sensing_time[i] + latency_ISP
                        total_energy_CPU1 = total_energy_CPU1 + energy_ISP
                        total_energy_CPU5 = total_energy_CPU5 + energy_ISP
                        total_energy_GPU = total_energy_GPU + energy_ISP
                        total_energy_DSP = total_energy_DSP + energy_ISP
                        total_energy_accelerator = total_energy_accelerator + energy_ISP
                        total_energy_spec_perf = total_energy_spec_perf + energy_ISP
                        total_energy_spec_energy = total_energy_spec_energy + energy_ISP
                    else:
                        ISP_time[i] = ISP_time[i-1] + latency_ISP
                        total_energy_CPU1 = total_energy_CPU1 + energy_ISP
                        total_energy_CPU5 = total_energy_CPU5 + energy_ISP
                        total_energy_GPU = total_energy_GPU + energy_ISP
                        total_energy_DSP = total_energy_DSP + energy_ISP
                        total_energy_accelerator = total_energy_accelerator + energy_ISP
                        total_energy_spec_perf = total_energy_spec_perf + energy_ISP
                        total_energy_spec_energy = total_energy_spec_energy + energy_ISP
                    #fast_CPU baseline
                    if (ISP_time[i] > CPU1_time[i-1]):
                        CPU1_time[i] = ISP_time[i] + latency_CPU1 + latency_commit
                        total_energy_CPU1 = total_energy_CPU1 + energy_CPU1 + energy_commit
                        accumulation_CPU1 = accumulation_CPU1 + CPU1_time[i] - start_time[i]
                    else:
                        CPU1_time[i] = CPU1_time[i-1] + latency_CPU1 + latency_commit
                        total_energy_CPU1 = total_energy_CPU1 + energy_CPU1 + energy_commit
                        accumulation_CPU1 = accumulation_CPU1 + CPU1_time[i] - start_time[i]
                    #slow_CPU baseline
                    if (ISP_time[i] > CPU5_time[i-1]):
                        CPU5_time[i] = ISP_time[i] + latency_CPU5 + latency_commit
                        total_energy_CPU5 = total_energy_CPU5 + energy_CPU5 + energy_commit
                        accumulation_CPU5 = accumulation_CPU5 + CPU5_time[i] - start_time[i]
                    else:
                        CPU5_time[i] = CPU5_time[i-1] + latency_CPU5 + latency_commit
                        total_energy_CPU5 = total_energy_CPU5 + energy_CPU5 + energy_commit
                        accumulation_CPU5 = accumulation_CPU5 + CPU5_time[i] - start_time[i]
                    #GPU baseline
                    if (ISP_time[i] > GPU_time[i-1]):
                        GPU_time[i] = ISP_time[i] + latency_GPU + latency_commit
                        total_energy_GPU = total_energy_GPU + energy_GPU + energy_commit
                        accumulation_GPU = accumulation_GPU + GPU_time[i] - start_time[i]
                    else:
                        GPU_time[i] = GPU_time[i-1] + latency_GPU + latency_commit
                        total_energy_GPU = total_energy_GPU + energy_GPU + energy_commit
                        accumulation_GPU = accumulation_GPU + GPU_time[i] - start_time[i]
                    #DSP baseline
                    if (ISP_time[i] > DSP_time[i-1]):
                        DSP_time[i] = ISP_time[i] + latency_DSP + latency_commit
                        total_energy_DSP = total_energy_DSP + energy_DSP + energy_commit
                        accumulation_DSP = accumulation_DSP + DSP_time[i] - start_time[i]
                    else:
                        DSP_time[i] = DSP_time[i-1] + latency_DSP + latency_commit
                        total_energy_DSP = total_energy_DSP + energy_DSP + energy_commit
                        accumulation_DSP = accumulation_DSP + DSP_time[i] - start_time[i]
                    #accelerator baseline
                    if (ISP_time[i] > accelerator_time[i-1]):
                        accelerator_time[i] = ISP_time[i] + latency_accelerator + latency_commit
                        total_energy_accelerator = total_energy_accelerator + energy_accelerator + energy_commit
                        accumulation_accelerator = accumulation_accelerator + accelerator_time[i] - start_time[i]
                    else:
                        accelerator_time[i] = accelerator_time[i-1] + latency_accelerator + latency_commit
                        total_energy_accelerator = total_energy_accelerator + energy_accelerator + energy_commit
                        accumulation_accelerator = accumulation_accelerator + accelerator_time[i] - start_time[i]
                    #spec_soc_performance_first
                    if (ISP_time[i] > end_time_perf[i-1]):
                        end_time_perf[i] = ISP_time[i] + latency_accelerator + latency_commit
                        total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                        accumulation_spec_perf = accumulation_spec_perf + end_time_perf[i] - start_time[i]
                    else:
                        end_time_perf[i] = end_time_perf[i-1] + latency_accelerator + latency_commit
                        total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                        accumulation_spec_perf = accumulation_spec_perf + end_time_perf[i] - start_time[i]
                    #spec_soc_energy_first
                    if (ISP_time[i] > end_time_energy[i-1]):
                        end_time_energy[i] = ISP_time[i] + latency_accelerator + latency_commit
                        total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                        accumulation_spec_energy = accumulation_spec_energy + end_time_energy[i] - start_time[i]
                    else:
                        end_time_energy[i] = end_time_energy[i-1] + latency_accelerator + latency_commit
                        total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                        accumulation_spec_energy = accumulation_spec_energy + end_time_energy[i] - start_time[i]
                    #predict_time
                    total_energy_spec_perf = total_energy_spec_perf + energy_predict
                    total_energy_spec_energy = total_energy_spec_energy + energy_predict
                    total_energy_spec_perf = total_energy_spec_perf + energy_sensing + energy_ISP
                    total_energy_spec_energy = total_energy_spec_energy + energy_sensing + energy_ISP
                    for j in range(i+1,i+frames_predicted+1):
                        predict_time[j] = ISP_time[i] + latency_predict


                else:
                    start_time[i] = sensing_time[i-1]
                    #sensing time
                    sensing_time[i] = start_time[i] + latency_sensing
                    total_energy_CPU1 = total_energy_CPU1 + energy_sensing
                    total_energy_CPU5 = total_energy_CPU5 + energy_sensing
                    total_energy_GPU = total_energy_GPU + energy_sensing
                    total_energy_DSP = total_energy_DSP + energy_sensing
                    total_energy_accelerator = total_energy_accelerator + energy_sensing
                    total_energy_spec_perf = total_energy_spec_perf + energy_sensing
                    total_energy_spec_energy = total_energy_spec_energy + energy_sensing
                    #ISP time
                    if (sensing_time[i] > ISP_time[i-1]):
                        ISP_time[i] = sensing_time[i] + latency_ISP
                        total_energy_CPU1 = total_energy_CPU1 + energy_ISP
                        total_energy_CPU5 = total_energy_CPU5 + energy_ISP
                        total_energy_GPU = total_energy_GPU + energy_ISP
                        total_energy_DSP = total_energy_DSP + energy_ISP
                        total_energy_accelerator = total_energy_accelerator + energy_ISP
                        total_energy_spec_perf = total_energy_spec_perf + energy_ISP
                        total_energy_spec_energy = total_energy_spec_energy + energy_ISP
                    else:
                        ISP_time[i] = ISP_time[i-1] + latency_ISP
                        total_energy_CPU1 = total_energy_CPU1 + energy_ISP
                        total_energy_CPU5 = total_energy_CPU5 + energy_ISP
                        total_energy_GPU = total_energy_GPU + energy_ISP
                        total_energy_DSP = total_energy_DSP + energy_ISP
                        total_energy_accelerator = total_energy_accelerator + energy_ISP
                        total_energy_spec_perf = total_energy_spec_perf + energy_ISP
                        total_energy_spec_energy = total_energy_spec_energy + energy_ISP
                    #fast_CPU baseline
                    if (ISP_time[i] > CPU1_time[i-1]):
                        CPU1_time[i] = ISP_time[i] + latency_CPU1 + latency_commit
                        total_energy_CPU1 = total_energy_CPU1 + energy_CPU1 + energy_commit
                        accumulation_CPU1 = accumulation_CPU1 + CPU1_time[i] - start_time[i]
                    else:
                        CPU1_time[i] = CPU1_time[i-1] + latency_CPU1 + latency_commit
                        total_energy_CPU1 = total_energy_CPU1 + energy_CPU1 + energy_commit
                        accumulation_CPU1 = accumulation_CPU1 + CPU1_time[i] - start_time[i]
                    #slow_CPU baseline
                    if (ISP_time[i] > CPU5_time[i-1]):
                        CPU5_time[i] = ISP_time[i] + latency_CPU5 + latency_commit
                        total_energy_CPU5 = total_energy_CPU5 + energy_CPU5 + energy_commit
                        accumulation_CPU5 = accumulation_CPU5 + CPU5_time[i] - start_time[i]
                    else:
                        CPU5_time[i] = CPU5_time[i-1] + latency_CPU5 + latency_commit
                        total_energy_CPU5 = total_energy_CPU5 + energy_CPU5 + energy_commit
                        accumulation_CPU5 = accumulation_CPU5 + CPU5_time[i] - start_time[i]
                    #GPU baseline
                    if (ISP_time[i] > GPU_time[i-1]):
                        GPU_time[i] = ISP_time[i] + latency_GPU + latency_commit
                        total_energy_GPU = total_energy_GPU + energy_GPU + energy_commit
                        accumulation_GPU = accumulation_GPU + GPU_time[i] - start_time[i]
                    else:
                        GPU_time[i] = GPU_time[i-1] + latency_GPU + latency_commit
                        total_energy_GPU = total_energy_GPU + energy_GPU + energy_commit
                        accumulation_GPU = accumulation_GPU + GPU_time[i] - start_time[i]
                    #DSP baseline
                    if (ISP_time[i] > DSP_time[i-1]):
                        DSP_time[i] = ISP_time[i] + latency_DSP + latency_commit
                        total_energy_DSP = total_energy_DSP + energy_DSP + energy_commit
                        accumulation_DSP = accumulation_DSP + DSP_time[i] - start_time[i]
                    else:
                        DSP_time[i] = DSP_time[i-1] + latency_DSP + latency_commit
                        total_energy_DSP = total_energy_DSP + energy_DSP + energy_commit
                        accumulation_DSP = accumulation_DSP + DSP_time[i] - start_time[i]
                    #accelerator baseline
                    if (ISP_time[i] > accelerator_time[i-1]):
                        accelerator_time[i] = ISP_time[i] + latency_accelerator + latency_commit
                        total_energy_accelerator = total_energy_accelerator + energy_accelerator + energy_commit
                        accumulation_accelerator = accumulation_accelerator + accelerator_time[i] - start_time[i]
                    else:
                        accelerator_time[i] = accelerator_time[i-1] + latency_accelerator + latency_commit
                        total_energy_accelerator = total_energy_accelerator + energy_accelerator + energy_commit
                        accumulation_accelerator = accumulation_accelerator + accelerator_time[i] - start_time[i]
                    #spec_soc_latencymin, E<=Eb
                    #energy_Eb_minL, latency_Eb_minL = runtime2(frames_predicted,latency_CPU1,latency_GPU,latency_DSP,latency_accelerator,energy_CPU1,energy_GPU,energy_DSP,energy_accelerator,E_budget)
                    if ((i-predict_frame_location)==1):
                        end_time_perf[i] = predict_time[i] + latency_accelerator + latency_commit
                        total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                    elif ((i-predict_frame_location)==2):
                        end_time_perf[i] = predict_time[i] + latency_GPU + latency_commit
                        total_energy_spec_perf = total_energy_spec_perf + energy_GPU + energy_commit
                    elif ((i-predict_frame_location)==3):
                        end_time_perf[i] = predict_time[i] + latency_accelerator*2 + latency_commit
                        total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                    elif ((i-predict_frame_location)==4):
                        end_time_perf[i] = predict_time[i] + latency_DSP + latency_commit
                        total_energy_spec_perf = total_energy_spec_perf + energy_DSP + energy_commit
                    elif ((i-predict_frame_location)==5):
                        end_time_perf[i] = predict_time[i] + latency_accelerator*3 + latency_commit
                        total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                    elif ((i-predict_frame_location)==6):
                        end_time_perf[i] = predict_time[i] + latency_GPU*2 + latency_commit
                        total_energy_spec_perf = total_energy_spec_perf + energy_GPU + energy_commit
                    elif ((i-predict_frame_location)==7):
                        end_time_perf[i] = predict_time[i] + latency_accelerator*4 + latency_commit
                        total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                    elif ((i-predict_frame_location)==8):
                        end_time_perf[i] = predict_time[i] + latency_DSP*2 + latency_commit
                        total_energy_spec_perf = total_energy_spec_perf + energy_DSP + energy_commit
                    elif ((i-predict_frame_location)==9):
                        end_time_perf[i] = predict_time[i] + latency_accelerator*5 + latency_commit
                        total_energy_spec_perf = total_energy_spec_perf + energy_accelerator + energy_commit
                    elif ((i-predict_frame_location)==10):
                        end_time_perf[i] = predict_time[i] + latency_GPU*3 + latency_commit
                        total_energy_spec_perf = total_energy_spec_perf + energy_GPU + energy_commit
                    accumulation_spec_perf = accumulation_spec_perf + end_time_perf[i] - start_time[i]                
                    
                    #spec_soc_energymin, L<=Lb
                    #energy_Lb_minE, latency_Lb_minE  = runtime1(frames_predicted,latency_CPU1,latency_GPU,latency_DSP,latency_accelerator,energy_CPU1,energy_GPU,energy_DSP,energy_accelerator,L_budget)
                    if ((i-predict_frame_location)==1):
                        end_time_energy[i] = predict_time[i] + latency_accelerator + latency_commit
                        total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                    elif ((i-predict_frame_location)==2):
                        end_time_energy[i] = predict_time[i] + latency_accelerator*2 + latency_commit
                        total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                    elif ((i-predict_frame_location)==3):
                        end_time_energy[i] = predict_time[i] + latency_accelerator*3 + latency_commit
                        total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                    elif ((i-predict_frame_location)==4):
                        end_time_energy[i] = predict_time[i] + latency_accelerator*4 + latency_commit
                        total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                    elif ((i-predict_frame_location)==5):
                        end_time_energy[i] = predict_time[i] + latency_accelerator*5 + latency_commit
                        total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                    elif ((i-predict_frame_location)==6):
                        end_time_energy[i] = predict_time[i] + latency_accelerator*6 + latency_commit
                        total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                    elif ((i-predict_frame_location)==7):
                        end_time_energy[i] = predict_time[i] + latency_accelerator*7 + latency_commit
                        total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                    elif ((i-predict_frame_location)==8):
                        end_time_energy[i] = predict_time[i] + latency_accelerator*8 + latency_commit
                        total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                    elif ((i-predict_frame_location)==9):
                        end_time_energy[i] = predict_time[i] + latency_accelerator*9 + latency_commit
                        total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                    elif ((i-predict_frame_location)==10):
                        end_time_energy[i] = predict_time[i] + latency_accelerator*10 + latency_commit
                        total_energy_spec_energy = total_energy_spec_energy + energy_accelerator + energy_commit
                    accumulation_spec_energy = accumulation_spec_energy + end_time_energy[i] - start_time[i]
                    #check right




    for i in range(1,frame+1):
        if (i==1):
            start_time[i]=0;
            FCFS_sensing_time[i] = start_time[i] + latency_sensing
            FCFS_ISP_time[i] = FCFS_sensing_time[i] + latency_ISP
            FCFS_end_time[i] = FCFS_ISP_time[i] + latency_accelerator + latency_commit
            accumulation_FCFS = accumulation_FCFS+FCFS_end_time[i] - start_time[i]
        else:
            start_time[i]=FCFS_sensing_time[i-1];
            FCFS_sensing_time[i] = start_time[i] + latency_sensing
            if (FCFS_sensing_time[i]>FCFS_ISP_time[i-1]):
                FCFS_ISP_time[i] = FCFS_sensing_time[i] + latency_ISP
            else:
                FCFS_ISP_time[i] = FCFS_ISP_time[i-1] + latency_ISP
            if (flag==flagacc):
                flag = flaggpu
                FCFS_end_time[i] = FCFS_ISP_time[i] + latency_accelerator + latency_commit
            elif (flag==flaggpu):
                flag = flagdsp
                FCFS_end_time[i] = FCFS_ISP_time[i] + latency_GPU + latency_commit
            else:
                flag = flagacc
                FCFS_end_time[i] = FCFS_ISP_time[i] + latency_DSP + latency_commit
            accumulation_FCFS = accumulation_FCFS+FCFS_end_time[i] - start_time[i]

    for i in range(1,frame+1):
        if (count==10):
            base = base+11
            count = 1
        else:
            count = count + 1
        if (i==1):
            start_time[i]=0;
            hold_sensing_time[i] = start_time[i] + latency_sensing
            total_energy_hold = total_energy_hold + energy_sensing
            hold_ISP_time[i] = hold_sensing_time[i] + latency_ISP
            total_energy_hold = total_energy_hold + energy_ISP
            hold_end_time[i] = hold_ISP_time[i] + latency_accelerator
            total_energy_hold = total_energy_hold + energy_accelerator + energy_commit
            accumulation_hold = accumulation_hold+hold_end_time[i] - start_time[i]
        else:
            start_time[i] = hold_sensing_time[i-1]
            hold_sensing_time[i] = start_time[i] + latency_sensing
            total_energy_hold = total_energy_hold + energy_sensing
            if (hold_sensing_time[i] > hold_ISP_time[i-1]):
                hold_ISP_time[i] = hold_sensing_time[i] + latency_ISP
                total_energy_hold = total_energy_hold + energy_ISP
                if (count==1):
                    hold_end_time[i] = hold_sensing_time[base] + frames_predicted * latency_sensing + latency_ISP + latency_accelerator+ latency_commit
                    total_energy_hold = total_energy_hold + energy_accelerator+ energy_commit
                elif (count==2):
                    hold_end_time[i] = hold_sensing_time[base] + frames_predicted * latency_sensing + latency_ISP + latency_GPU+ latency_commit
                    total_energy_hold = total_energy_hold + energy_GPU+ energy_commit
                elif (count==3):
                    hold_end_time[i] = hold_sensing_time[base] + frames_predicted * latency_sensing + latency_ISP + latency_accelerator*2+ latency_commit
                    total_energy_hold = total_energy_hold + energy_accelerator+ energy_commit
                elif (count==4):
                    hold_end_time[i] = hold_sensing_time[base] + frames_predicted * latency_sensing + latency_ISP + latency_DSP+ latency_commit
                    total_energy_hold = total_energy_hold + energy_DSP+ energy_commit
                elif (count==5):
                    hold_end_time[i] = hold_sensing_time[base] + frames_predicted * latency_sensing + latency_ISP + latency_accelerator*3+ latency_commit
                    total_energy_hold = total_energy_hold + energy_accelerator+ energy_commit
                elif (count==6):
                    hold_end_time[i] = hold_sensing_time[base] + frames_predicted * latency_sensing + latency_ISP + latency_GPU*2+ latency_commit
                    total_energy_hold = total_energy_hold + energy_GPU+ energy_commit
                elif (count==7):
                    hold_end_time[i] = hold_sensing_time[base] + frames_predicted * latency_sensing + latency_ISP + latency_accelerator*4+ latency_commit
                    total_energy_hold = total_energy_hold + energy_accelerator+ energy_commit
                elif (count==8):
                    hold_end_time[i] = hold_sensing_time[base] + frames_predicted * latency_sensing + latency_ISP + latency_DSP*2+ latency_commit
                    total_energy_hold = total_energy_hold + energy_DSP+ energy_commit
                elif (count==9):
                    hold_end_time[i] = hold_sensing_time[base] + frames_predicted * latency_sensing + latency_ISP + latency_accelerator*5+ latency_commit
                    total_energy_hold = total_energy_hold + energy_accelerator+ energy_commit
                else:
                    hold_end_time[i] = hold_sensing_time[base] + frames_predicted * latency_sensing + latency_ISP + latency_GPU*3+ latency_commit
                    total_energy_hold = total_energy_hold + energy_GPU+ energy_commit
            else:
                hold_ISP_time[i] = hold_ISP_time[i-1] + latency_ISP
                total_energy_hold = total_energy_hold + energy_ISP
                if (count==1):
                    hold_end_time[i] = hold_ISP_time[base] + latency_ISP*frames_predicted + latency_accelerator+ latency_commit
                    total_energy_hold = total_energy_hold + energy_accelerator+ energy_commit
                elif (count==2):
                    hold_end_time[i] = hold_ISP_time[base] + latency_ISP*frames_predicted + latency_GPU+ latency_commit
                    total_energy_hold = total_energy_hold + energy_GPU+ energy_commit
                elif (count==3):
                    hold_end_time[i] = hold_ISP_time[base] + latency_ISP*frames_predicted + latency_accelerator*2+ latency_commit
                    total_energy_hold = total_energy_hold + energy_accelerator+ energy_commit
                elif (count==4):
                    hold_end_time[i] = hold_ISP_time[base] + latency_ISP*frames_predicted + latency_DSP+ latency_commit
                    total_energy_hold = total_energy_hold + energy_DSP+ energy_commit
                elif (count==5):
                    hold_end_time[i] = hold_ISP_time[base] + latency_ISP*frames_predicted + latency_accelerator*3+ latency_commit
                    total_energy_hold = total_energy_hold + energy_accelerator+ energy_commit
                elif (count==6):
                    hold_end_time[i] = hold_ISP_time[base] + latency_ISP*frames_predicted + latency_GPU*2+ latency_commit
                    total_energy_hold = total_energy_hold + energy_GPU+ energy_commit
                elif (count==7):
                    hold_end_time[i] = hold_ISP_time[base] + latency_ISP*frames_predicted + latency_accelerator*4+ latency_commit
                    total_energy_hold = total_energy_hold + energy_accelerator+ energy_commit
                elif (count==8):
                    hold_end_time[i] = hold_ISP_time[base] + latency_ISP*frames_predicted + latency_DSP*2+ latency_commit
                    total_energy_hold = total_energy_hold + energy_DSP+ energy_commit
                elif (count==9):
                    hold_end_time[i] = hold_ISP_time[base] + latency_ISP*frames_predicted + latency_accelerator*5+ latency_commit
                    total_energy_hold = total_energy_hold + energy_accelerator+ energy_commit
                else:
                    hold_end_time[i] = hold_ISP_time[base] + latency_ISP*frames_predicted + latency_GPU*3+ latency_commit
                    total_energy_hold = total_energy_hold + energy_GPU+ energy_commit              
            accumulation_hold = accumulation_hold + hold_end_time[i] - start_time[i]

    accumulation_hold = 0
    for i in range(1,frame+1):
        if (i==base):
            base = base+11
            hold_end_time[i] = end_time_perf[i]
        else:
            hold_end_time[i] = end_time_perf[i] + 470

        accumulation_hold = accumulation_hold + hold_end_time[i] - start_time[i]
         


        




    
    print('CPU1_baseline', accumulation_CPU1 / frame)
    print('CPU5_baseline', accumulation_CPU5 / frame)
    print('GPU_baseline', accumulation_GPU / frame)
    print('DSP_baseline', accumulation_DSP / frame)
    print('accelerator_baseline', accumulation_accelerator / frame)
    print('perf_limitation', accumulation_spec_perf / frame)
    print('energy_limatition', accumulation_spec_energy / frame)
    print('CPU1_energy', total_energy_CPU1 / frame)
    print('CPU5_energy', total_energy_CPU5 / frame)
    print('GPU_energy', total_energy_GPU / frame)
    print('DSP_energy', total_energy_DSP / frame)
    print('accelerator_energy', total_energy_accelerator / frame)
    print('perfbest_energy', total_energy_spec_perf / frame)
    print('energybest_energy', total_energy_spec_energy / frame)
    print('FCFS',accumulation_FCFS/frame)
    print('hold',accumulation_hold/frame)
    print('hold_energy',total_energy_hold/frame)
    
    




    



if __name__ == '__main__':
    main()
