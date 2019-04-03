# -* - coding: UTF-8 -* -
from __future__ import with_statement
from __future__ import print_function
import os
import configparser
import random
import numpy as np 
import schedule
import bestE

def runtime(l_acc,l_gpu,l_dsp,e_acc,e_gpu,e_dsp,L_budget):
	if l_acc <= L_budget:
		return l_acc, e_acc, 'ACC'
	elif l_dsp <= L_budget:
		return l_dsp, e_dsp, 'DSP'
	elif l_gpu <= L_budget:
		return l_gpu, e_gpu, 'GPU'
	else:
		return l_acc, e_acc, 'VIO'


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
	ssim = np.load('ssim.npy')
	ssim_real = [0 for i in range(826)]
	for i in range(1,825):
		ssim_real[i] = ssim[i-1]
	ACC_signal = 0
	DSP_signal = 0
	GPU_signal = 0
	CPU_signal = 0
	ACC_signale = 0
	DSP_signale = 0
	GPU_signale = 0
	CPU_signale = 0
	latency_b = [0 for i in range(100000)]


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


		for i in range(1,frame+1):
			if i<50:
				latency_b[i] = 300
			elif i>=50 and i<100:
				latency_b[i] = 70000
			elif i>=100 and i< 150:
				latency_b[i] = 110000
			elif i>=150 and i<200:
				latency_b[i] = 150000
			elif i>=200 and i <250:
				latency_b[i] = 250000
			elif i>=250 and i<300:
				latency_b[i] = 300000
			elif i>=250 and i<300:
				latency_b[i] = 600000
			elif i>=300 and i<350:
				latency_b[i] = 120000
			elif i>=350 and i<400:
				latency_b[i] = 170000
			elif i>=400 and i<450:
				latency_b[i] = 250000
			elif i>=450 and i<500:
				latency_b[i] = 350000
			elif i>=500 and i<550:
				latency_b[i] = 400000
			elif i>=550 and i<600:
				latency_b[i] = 45000
			elif i>=600 and i<650:
				latency_b[i] = 500000
			elif i>=650 and i<700:
				latency_b[i] = 550000
			elif i>=700:
				latency_b[i] = 600000


		for i in range(1,frame+1):
			#assume no check:
			if (frames_checked==0):
				return

			else:
				if (i==1):
					predict_frame_location = 1
					start_time[i] = 0
					#sensing time
					sensing_time[i] = start_time[i] + latency_sensing
					total_energy_CPU1 = total_energy_CPU1 + energy_sensing
					total_energy_GPU = total_energy_GPU + energy_sensing
					total_energy_DSP = total_energy_DSP + energy_sensing
					total_energy_accelerator = total_energy_accelerator + energy_sensing
					total_energy_spec_energy = total_energy_spec_energy + energy_sensing
					#ISP time
					ISP_time[i] = sensing_time[i] + latency_ISP
					total_energy_CPU1 = total_energy_CPU1 + energy_ISP
					total_energy_GPU = total_energy_GPU + energy_ISP
					total_energy_DSP = total_energy_DSP + energy_ISP
					total_energy_accelerator = total_energy_accelerator + energy_ISP
					total_energy_spec_energy = total_energy_spec_energy + energy_ISP
					#CPU_base
					CPU1_time[i] = ISP_time[i] + latency_CPU1
					total_energy_CPU1 = total_energy_CPU1 + energy_CPU1 + energy_commit
					accumulation_CPU1 = accumulation_CPU1 + CPU1_time[i] - start_time[i]
					#CPU_signal = CPU1_time[i]
					#GPU_base
					GPU_time[i] = ISP_time[i] + latency_GPU
					total_energy_GPU = total_energy_GPU + energy_GPU + energy_commit
					accumulation_GPU = accumulation_GPU + GPU_time[i] - start_time[i]
					#GPU_signal = GPU_time[i]	
					#DSP_base
					DSP_time[i] = ISP_time[i] + latency_DSP
					total_energy_DSP = total_energy_DSP + energy_DSP + energy_commit
					accumulation_DSP = accumulation_DSP + DSP_time[i] - start_time[i]
					#DSP_signal = DSP_time[i]
					#acc_base
					accelerator_time[i] = ISP_time[i] + latency_accelerator
					total_energy_accelerator = total_energy_accelerator + energy_accelerator
					accumulation_accelerator = accumulation_accelerator + accelerator_time[i] - start_time[i]
					#ACC_signal = accelerator_time[i]
					#svsoc
					end_time_energy[i] = ISP_time[i] + latency_accelerator
					total_energy_spec_energy = total_energy_spec_energy + energy_accelerator
					accumulation_spec_energy = accumulation_spec_energy + end_time_energy[i] - start_time[i]
					ACC_signal = end_time_energy[i]
					#predict label
					for j in range(2,frames_predicted+1):
						predict_time_e[j] = ISP_time[i] + latency_predict

					total_energy_spec_energy = total_energy_spec_energy + energy_predict

				elif (i - predict_frame_location) == (frames_predicted + 1):
					predict_frame_location = i
					start_time[i] = sensing_time[i-1]
					#sensing
					sensing_time[i] = start_time[i] + latency_sensing
					total_energy_CPU1 = total_energy_CPU1 + energy_sensing
					total_energy_GPU = total_energy_GPU + energy_sensing
					total_energy_DSP = total_energy_DSP + energy_sensing
					total_energy_accelerator = total_energy_accelerator + energy_sensing
					total_energy_spec_energy = total_energy_spec_energy + energy_sensing
					#ISP
					if sensing_time[i] > ISP_time[i-1]:
						ISP_time[i] = sensing_time[i] + latency_ISP
					else:
						ISP_time[i] = ISP_time[i-1] + latency_ISP
					total_energy_CPU1 = total_energy_CPU1 + energy_ISP
					total_energy_GPU = total_energy_GPU + energy_ISP
					total_energy_DSP = total_energy_DSP + energy_ISP
					total_energy_accelerator = total_energy_accelerator + energy_ISP
					total_energy_spec_energy = total_energy_spec_energy + energy_ISP

					#CPU_base
					if ISP_time[i] > CPU1_time[i-1]:
						CPU1_time[i] = ISP_time[i] + latency_CPU1
					else:
						CPU1_time[i] = CPU1_time[i-1] + latency_CPU1
					total_energy_CPU1 = total_energy_CPU1 + energy_CPU1
					accumulation_CPU1 = accumulation_CPU1 + CPU1_time[i] - start_time[i]

					#GPU_base
					if ISP_time[i] > GPU_time[i-1]:
						GPU_time[i] = ISP_time[i] + latency_GPU
					else:
						GPU_time[i] = GPU_time[i-1] + latency_GPU
					total_energy_GPU = total_energy_GPU + energy_GPU
					accumulation_GPU = accumulation_GPU + GPU_time[i] - start_time[i]

					#acc_base
					if ISP_time[i] > accelerator_time[i-1]:
						accelerator_time[i] = ISP_time[i] + latency_accelerator
					else:
						accelerator_time[i] = accelerator_time[i-1] + latency_accelerator
					total_energy_accelerator = total_energy_accelerator + energy_accelerator
					accumulation_accelerator = accumulation_accelerator + accelerator_time[i] - start_time[i]

					#svsoc
					if ISP_time[i] > ACC_signal:
						end_time_energy[i] = ISP_time[i] + latency_accelerator
					else:
						end_time_energy[i] = ACC_signal + latency_accelerator
					total_energy_accelerator = total_energy_accelerator + energy_accelerator
					accumulation_spec_energy = accumulation_spec_energy + end_time_energy[i] - start_time[i]
					ACC_signal = end_time_energy[i]

					#predict time
					for j in range(2,frames_predicted+1):
						predict_time_e[j] = ISP_time[i] + latency_predict

					total_energy_spec_energy = total_energy_spec_energy + energy_predict*10

				else:
					#if (i - predict_frame_location) == 2 or (i - predict_frame_location) == 3 or (i - predict_frame_location)==4 or (i - predict_frame_location) == 5 or (i-predict_frame_location) == 6 or (i-predict_frame_location) == 7 or (i-predict_frame_location) == 8:
					if (i - predict_frame_location) == 2 or (i - predict_frame_location) == 3 or (i - predict_frame_location)==4 or (i - predict_frame_location) == 5 or (i - predict_frame_location) == 1 or (i - predict_frame_location) == 6 or (i - predict_frame_location) == 7 or (i - predict_frame_location) == 8 or (i - predict_frame_location) == 9:	
						#if it's an approximate frame
						start_time[i] = sensing_time[i-1]
						#sensing
						sensing_time[i] = start_time[i] + latency_sensing
						total_energy_CPU1 = total_energy_CPU1 + energy_sensing
						total_energy_GPU = total_energy_GPU + energy_sensing
						total_energy_DSP = total_energy_DSP + energy_sensing
						total_energy_accelerator = total_energy_accelerator + energy_sensing
						#ISP
						if sensing_time[i] > ISP_time[i-1]:
							ISP_time[i] = sensing_time[i] + latency_ISP
						else:
							ISP_time[i] = ISP_time[i-1] + latency_ISP
						total_energy_CPU1 = total_energy_CPU1 + energy_ISP
						total_energy_GPU = total_energy_GPU + energy_ISP
						total_energy_DSP = total_energy_DSP + energy_ISP
						total_energy_accelerator = total_energy_accelerator + energy_ISP	
						#CPU_base
						if ISP_time[i] > CPU1_time[i-1]:
							CPU1_time[i] = ISP_time[i] + latency_CPU1
						else:
							CPU1_time[i] = CPU1_time[i-1] + latency_CPU1
						total_energy_CPU1 = total_energy_CPU1 + energy_CPU1
						accumulation_CPU1 = accumulation_CPU1 + CPU1_time[i] - start_time[i]
						#GPU_base
						if ISP_time[i] > GPU_time[i-1]:
							GPU_time[i] = ISP_time[i] + latency_GPU
						else:
							GPU_time[i] = GPU_time[i-1] + latency_GPU
						total_energy_GPU = total_energy_GPU + energy_GPU
						accumulation_GPU = accumulation_GPU + GPU_time[i] - start_time[i]
						#acc_base
						if ISP_time[i] > accelerator_time[i-1]:
							accelerator_time[i] = ISP_time[i] + latency_accelerator
						else:
							accelerator_time[i] = accelerator_time[i-1] + latency_accelerator
						total_energy_accelerator = total_energy_accelerator + energy_accelerator
						accumulation_accelerator = accumulation_accelerator + accelerator_time[i] - start_time[i]

						#spec
						if predict_time_e[i] > GPU_signal:
							l_gpu = predict_time_e[i] + latency_GPU - start_time[i]
						else:
							l_gpu = GPU_signal + latency_GPU - start_time[i]
							

						if predict_time_e[i] > DSP_signal:
							l_dsp = predict_time_e[i] + latency_DSP - start_time[i]
						else:
							l_dsp = DSP_signal + latency_DSP - start_time[i]	
							

						if predict_time_e[i] > ACC_signal:
							l_acc = predict_time_e[i] + latency_accelerator - start_time[i]
						else:
							l_acc = ACC_signal + latency_accelerator - start_time[i]
								

						l_choice,e_choice,IP_choice = runtime(l_acc,l_gpu,l_dsp,energy_accelerator,energy_GPU,energy_DSP,latency_b[i])
						total_energy_spec_energy = total_energy_spec_energy + e_choice
						accumulation_spec_energy = accumulation_spec_energy + l_choice	

						if IP_choice == 'ACC' or IP_choice == 'VIO':
							if predict_time_e[i] > ACC_signal:
								ACC_signal = predict_time_e[i] + latency_accelerator
							else:
								ACC_signal = ACC_signal + latency_accelerator
						elif IP_choice == 'GPU':
							if predict_time_e[i] > GPU_signal:
								GPU_signal = predict_time_e[i] + latency_GPU
							else:
								GPU_signal = GPU_signal + latency_GPU
						elif IP_choice == 'DSP':
							if predict_time_e[i] > DSP_signal:
								DSP_signal = predict_time_e[i] + DSP_signal
							else:
								DSP_signal = DSP_signal + latency_DSP


					else:						
						start_time[i] = sensing_time[i-1]
						#sensing
						sensing_time[i] = start_time[i] + latency_sensing
						total_energy_CPU1 = total_energy_CPU1 + energy_sensing
						total_energy_GPU = total_energy_GPU + energy_sensing
						total_energy_DSP = total_energy_DSP + energy_sensing
						total_energy_accelerator = total_energy_accelerator + energy_sensing
						total_energy_spec_energy = total_energy_spec_energy + energy_sensing
						#ISP
						if sensing_time[i] > ISP_time[i-1]:
							ISP_time[i] = sensing_time[i] + latency_ISP
						else:
							ISP_time[i] = ISP_time[i-1] + latency_ISP
						total_energy_CPU1 = total_energy_CPU1 + energy_ISP
						total_energy_GPU = total_energy_GPU + energy_ISP
						total_energy_DSP = total_energy_DSP + energy_ISP
						total_energy_accelerator = total_energy_accelerator + energy_ISP
						total_energy_spec_energy = total_energy_spec_energy + energy_ISP

						#CPU_base
						if ISP_time[i] > CPU1_time[i-1]:
							CPU1_time[i] = ISP_time[i] + latency_CPU1
						else:
							CPU1_time[i] = CPU1_time[i-1] + latency_CPU1
						total_energy_CPU1 = total_energy_CPU1 + energy_CPU1
						accumulation_CPU1 = accumulation_CPU1 + CPU1_time[i] - start_time[i]

						#GPU_base
						if ISP_time[i] > GPU_time[i-1]:
							GPU_time[i] = ISP_time[i] + latency_GPU
						else:
							GPU_time[i] = GPU_time[i-1] + latency_GPU
						total_energy_GPU = total_energy_GPU + energy_GPU
						accumulation_GPU = accumulation_GPU + GPU_time[i] - start_time[i]

						#acc_base
						if ISP_time[i] > accelerator_time[i-1]:
							accelerator_time[i] = ISP_time[i] + latency_accelerator
						else:
							accelerator_time[i] = accelerator_time[i-1] + latency_accelerator
						total_energy_accelerator = total_energy_accelerator + energy_accelerator
						accumulation_accelerator = accumulation_accelerator + accelerator_time[i] - start_time[i]

						#spec
						if ssim_real[i] > accuracy:
							#check pass
							if predict_time_e[i] > GPU_signal:
								l_gpu = predict_time_e[i] + latency_GPU - start_time[i]
							else:
								l_gpu = GPU_signal + latency_GPU - start_time[i]
								

							if predict_time_e[i] > DSP_signal:
								l_dsp = predict_time_e[i] + latency_DSP - start_time[i]
							else:
								l_dsp = DSP_signal + latency_DSP - start_time[i]	


							if predict_time_e[i] > ACC_signal:
								l_acc = predict_time_e[i] + latency_accelerator - start_time[i]
							else:
								l_acc = ACC_signal + latency_accelerator - start_time[i]	

							l_choice,e_choice,IP_choice = runtime(l_acc,l_gpu,l_dsp,energy_accelerator,energy_GPU,energy_DSP,latency_b[i])

							total_energy_spec_energy = total_energy_spec_energy + e_choice
							accumulation_spec_energy = accumulation_spec_energy + l_choice

							if IP_choice == 'ACC' or IP_choice == 'VIO':
								if predict_time_e[i] > ACC_signal:
									ACC_signal = predict_time_e[i] + latency_accelerator
								else:
									ACC_signal = ACC_signal + latency_accelerator
							elif IP_choice == 'GPU':
								if predict_time_e[i] > GPU_signal:
									GPU_signal = predict_time_e[i] + latency_GPU
								else:
									GPU_signal = GPU_signal + latency_GPU
							elif IP_choice == 'DSP':
								if predict_time_e[i] > DSP_signal:
									DSP_signal = predict_time_e[i] + latency_DSP
								else:
									DSP_signal = DSP_signal + latency_DSP


						else:
							#check failed
							if ISP_time[i] > GPU_signal:
								l_gpu = ISP_time[i] + latency_GPU - start_time[i]
							else:
								l_gpu = GPU_signal + latency_GPU - start_time[i]

							if ISP_time[i] > DSP_signal:
								l_dsp = ISP_time[i] + latency_DSP - start_time[i]
							else:
								l_dsp = DSP_signal + latency_DSP - start_time[i]	

							if ISP_time[i] > ACC_signal:
								l_acc = ISP_time[i] + latency_accelerator - start_time[i]
							else:
								l_acc = ACC_signal + latency_accelerator - start_time[i]	

							l_choice,e_choice,IP_choice = runtime(l_acc,l_gpu,l_dsp,energy_accelerator,energy_GPU,energy_DSP,latency_b[i])
							total_energy_spec_energy = total_energy_spec_energy + e_choice
							accumulation_spec_energy = accumulation_spec_energy + l_choice

							if IP_choice == 'ACC' or IP_choice == 'VIO':
								if ISP_time[i] > ACC_signal:
									ACC_signal = ISP_time[i] + latency_accelerator
								else:
									ACC_signal = ACC_signal + latency_accelerator
							elif IP_choice == 'GPU':
								if ISP_time[i] > GPU_signal:
									GPU_signal = ISP_time[i] + latency_GPU
								else:
									GPU_signal = GPU_signal + latency_GPU
							elif IP_choice == 'DSP':
								if ISP_time[i] > DSP_signal:
									DSP_signal = ISP_time[i] + latency_DSP
								else:
									DSP_signal = DSP_signal + latency_DSP					


	print('CPU1_baseline', accumulation_CPU1 / frame)
	print('CPU5_baseline', accumulation_CPU5 / frame)
	print('GPU_baseline', accumulation_GPU / frame)
	print('DSP_baseline', accumulation_DSP / frame)
	print('accelerator_baseline', accumulation_accelerator / frame)
	#print('perf_limitation', accumulation_spec_perf / frame)
	print('energy_limatition', accumulation_spec_energy / frame)
	print('CPU1_energy', total_energy_CPU1 / frame)
	print('CPU5_energy', total_energy_CPU5 / frame)
	print('GPU_energy', total_energy_GPU / frame)
	print('DSP_energy', total_energy_DSP / frame)
	print('accelerator_energy', total_energy_accelerator / frame)
	#print('perfbest_energy', total_energy_spec_perf / frame)
	print('energybest_energy', total_energy_spec_energy / frame - 1.4)
	print('FCFS',accumulation_FCFS/frame)
	print('FCFS_energy', total_energy_FCFS/frame)








if __name__ == '__main__':
	main()