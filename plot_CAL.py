#!/usr/bin/python2.7
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import FuncFormatter
import numpy as np

def figure1():
	data={
	"Spec_Soc_L":[191.69,44.09],
	"Spec_Soc_E":[431.01,19.455],
	"CPU_base":[1290408,410],
	"GPU_base":[342718.5,160],
	"DSP_base":[455241,149],
	"Accelerator_base":[127675.5,101],
	}

	x_axis_ls = [0.5,1.5,2.5,3.5,4.5,5.5]

	energy_norm=[0 for i in range(6)]
	latency_norm=[0 for i in range(6)]
	energy=[44.09,28.191,410,160.0,149.0,101.0]
	latency=[191.69,431.01,1290408.0,342718.5,455241.0,127675.5]

	for i in range(6):
		energy_norm[i] = energy[i]/energy[2]
		latency_norm[i] = latency[i]/latency[2]

	plt.rc('font',size=10)
	ax1 = plt.figure(figsize=(6,4)).add_subplot(111)
	ax1.set_ylabel('Normalized per-frame latency', fontsize=14, fontweight='bold')
	plt.xticks(rotation=60)
	plt.setp(ax1.spines.values(), linewidth=2)

	ax2 = ax1.twinx()
	ax2.set_ylabel('Normalized per-frame energy', fontsize=14, fontweight='bold')

	p1 = ax1.bar(x_axis_ls, latency_norm, 0.5, align='center',color='#71985E', linewidth=2.5);
	p2 = ax2.plot(x_axis_ls, energy_norm, color='#FFBF56', linestyle='none', marker='o',markersize=8);

	plt.subplots_adjust(left=0.2, bottom=0.20, right=0.9, top=0.9,
                wspace=0.2, hspace=0.2)

	plt.xticks(x_axis_ls, ["Spec_Soc_L","Spec_Soc_E","CPU_base","GPU_base","DSP_base","Acc_base"])
	ax2.set_ylim(0.0, 1)
	ax1.set_ylim(0.0, 1)
	ax1.tick_params(axis="y",direction="in")
	ax2.tick_params(axis="y",direction="in")
	ax1.tick_params(axis="x",direction="in")
	plt.grid(color='grey', which='major', axis='y', linestyle='--')
	#ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y))) 
	#ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y))) 
	plt.legend((p1[0], p2[0]), ('latency', 'energy',\
                 ), bbox_to_anchor=(0., 1.01, 1., .101), loc=3,
           ncol=2, mode="expand", borderaxespad=0., frameon=False)
	ax1.set_axisbelow(True)

	plt.savefig("eva_obser1.pdf")

def figure2a():
	x_axis_ls = [0.5,1.5,2.5,3.5,4.5,5.5]
	perframelatency = [431.0,347.78,229.99,191.69,191.69,191.69]
	energy = [28.191,]

	
	latency_norm=[0 for i in range(6)]

	for i in range(6):
		latency_norm[i] = perframelatency[i]/perframelatency[4]
		print(latency_norm[i])
	plt.rc('font',size=13)
	ax1 = plt.figure(figsize=(6,4)).add_subplot(111)
	ax1.set_ylabel('Normalized per-frame latency', fontsize=14, fontweight='bold')
	ax1.set_xlabel('Energy buddget for predicted sequence(mJ)', fontsize=14, fontweight='bold')
	plt.xticks(rotation=60)
	plt.setp(ax1.spines.values(), linewidth=2)

	p1 = ax1.bar(x_axis_ls, latency_norm, 0.5, align='center', color='#71985E', linewidth=2.5)
	plt.subplots_adjust(left=0.1, bottom=0.20, right=0.9, top=0.9,
                wspace=0.2, hspace=0.2)
	plt.xticks(x_axis_ls, ["100","200","300","400","500","600"])
	ax1.set_ylim(0.0,2.5)
	ax1.tick_params(axis="y",direction="in")
	plt.grid(color='grey', which='major', axis='y', linestyle='--')
	ax1.set_axisbelow(True)
	plt.savefig("eva_obser2a.pdf")

def figure2b():
	x_axis_ls = [0.5,1.5,2.5,3.5,4.5,5.5]
	perframelatency = [44.09,38.9,33.55,28.19,23.823,19.455]
	energy = [28.191,]

	
	latency_norm=[0 for i in range(6)]

	for i in range(6):
		latency_norm[i] = perframelatency[i]/perframelatency[5]
		print(latency_norm[i])

	plt.rc('font',size=13)
	ax1 = plt.figure(figsize=(6,4)).add_subplot(111)
	ax1.set_ylabel('Normalized per-frame energy', fontsize=14, fontweight='bold')
	ax1.set_xlabel('latency buddget for predicted sequence(ms)', fontsize=14, fontweight='bold')
	plt.xticks(rotation=60)
	plt.setp(ax1.spines.values(), linewidth=2)

	p1 = ax1.bar(x_axis_ls, latency_norm, 0.5, align='center', color='#FFBF56', linewidth=2.5)
	plt.subplots_adjust(left=0.1, bottom=0.20, right=0.9, top=0.9,
                wspace=0.2, hspace=0.2)
	plt.xticks(x_axis_ls, ["558","600","700","800","900","1000"])
	ax1.set_ylim(0.0,2.5)
	ax1.tick_params(axis="y",direction="in")
	plt.grid(color='grey', which='major', axis='y', linestyle='--')
	ax1.set_axisbelow(True)
	plt.savefig("eva_obser2b.pdf")

def figure3():
	x_axis_ls=[0.5,1.5,2.5,3.5]
	perframelatency = [191.68,261.646,241.66,561.47]
	perframeenergy = [44.0908,44.3638,44.2728,44.8188]
	energy_norm=[0 for i in range(4)]
	latency_norm=[0 for i in range(4)]

	for i in range(4):
		energy_norm[i] = perframeenergy[i]/perframeenergy[3]
		latency_norm[i] = perframelatency[i]/perframelatency[3]
		print(energy_norm[i])
		print(latency_norm[i])



	plt.rc('font',size=10)
	ax1 = plt.figure(figsize=(6,4)).add_subplot(111)
	ax1.set_ylabel('Normalized per-frame latency', fontsize=14, fontweight='bold')
	plt.xticks(rotation=60)
	plt.setp(ax1.spines.values(), linewidth=2)

	ax2 = ax1.twinx()
	ax2.set_ylabel('Normalized per-frame energy', fontsize=14, fontweight='bold')

	p1 = ax1.bar(x_axis_ls, latency_norm, 0.5, align='center',color='#71985E', linewidth=2.5);
	p2 = ax2.plot(x_axis_ls, energy_norm, color='#FFBF56', linestyle='none', marker='o',markersize=8);

	plt.subplots_adjust(left=0.1, bottom=0.20, right=0.9, top=0.9,
                wspace=0.2, hspace=0.2)
	ax1.text(1.7,0.62,'FP=Feature Prediction')
	ax1.text(1.7,0.7,'PP=Pixel Prediction')
	ax1.text(0.2,0.62,'DP=Dedicated Preditor')
	ax1.text(0.2,0.7,'EH=Existing Hardware')


	plt.xticks(x_axis_ls, ["FPDP","FPEH","PPDP","PPEH"])
	ax2.set_ylim(0.0, 1.2)
	ax1.set_ylim(0.0, 1.2)
	ax1.tick_params(axis="y",direction="in")
	ax2.tick_params(axis="y",direction="in")
	ax1.tick_params(axis="x",direction="in")
	plt.grid(color='grey', which='major', axis='y', linestyle='--')
	plt.legend((p1[0], p2[0]), ('latency', 'energy',\
                 ), bbox_to_anchor=(0., 1.01, 1., .101), loc=3,
           ncol=2, mode="expand", borderaxespad=0., frameon=False)
	ax1.set_axisbelow(True)

	plt.savefig("eva_obser3.pdf")

def figure5():
	x_axis_ls=[0.5,1.5,2.5]


	perframelatency = [191.68,273.3,661.69]
	perframeenergy = [44.0908,135.67,128.29]
	energy_norm=[0 for i in range(3)]
	latency_norm=[0 for i in range(3)]

	for i in range(3):
		energy_norm[i] = perframeenergy[i]/perframeenergy[1]
		latency_norm[i] = perframelatency[i]/perframelatency[2]



	plt.rc('font',size=10)
	ax1 = plt.figure(figsize=(6,4)).add_subplot(111)
	ax1.set_ylabel('Normalized per-frame latency', fontsize=14, fontweight='bold')
	plt.xticks(rotation=60)
	plt.setp(ax1.spines.values(), linewidth=2)

	ax2 = ax1.twinx()
	ax2.set_ylabel('Normalized per-frame energy', fontsize=14, fontweight='bold')

	p1 = ax1.bar(x_axis_ls, latency_norm, 0.5, align='center',color='#71985E', linewidth=2.5);
	p2 = ax2.plot(x_axis_ls, energy_norm, color='#FFBF56', linestyle='none', marker='o',markersize=8);

	plt.subplots_adjust(left=0.1, bottom=0.20, right=0.9, top=0.9,
                wspace=0.2, hspace=0.2)

	plt.xticks(x_axis_ls, ["Spec_Soc","FCFS","Hold"])
	ax2.set_ylim(0.0, 1.2)
	ax1.set_ylim(0.0, 1.2)
	ax1.tick_params(axis="y",direction="in")
	ax2.tick_params(axis="y",direction="in")
	ax1.tick_params(axis="x",direction="in")
	plt.grid(color='grey', which='major', axis='y', linestyle='--')
	plt.legend((p1[0], p2[0]), ('latency', 'energy',\
                 ), bbox_to_anchor=(0., 1.01, 1., .101), loc=3,
           ncol=2, mode="expand", borderaxespad=0., frameon=False)
	ax1.set_axisbelow(True)

	plt.savefig("eva_obser5.pdf")

def figure1a():
	x_axis_ls = [0.5,1.5,2.5,3.5,4.5,5.5]
	improvement1 = [0.7344,0.6472,0.9008]
	improvement2 = [0.9998,0.9995]
	improvement3 = [0.9999]
	x1 = [0.5,1.5,2.5]
	x2=[3.5,4.5]
	x3 = [5.5]
	fuck_1=[0.8,0.7,0.6]
	fuck_2=[0.5,0.4]
	plt.rc('font',size=13)
	ax1 = plt.figure(figsize=(6,4.5)).add_subplot(111)
	ax1.set_ylabel('Per-frame latency improvement', fontsize=14, fontweight='bold')
	plt.xticks(rotation=60)
	plt.setp(ax1.spines.values(), linewidth=2)
	p1 = ax1.bar(x1,improvement1, 0.5, align='center',color='#71985E', linewidth=2.5)
	p2 = ax1.bar(x2, improvement2,0.5,align='center',color='#71985E',linewidth=2.5)
	p3 = ax1.bar(x3, improvement3, 0.5, align='center',color='#71985E',linewidth=2.5,)
	plt.subplots_adjust(left=0.2, bottom=0.20, right=0.9, top=0.9,
                wspace=0.2, hspace=0.2)
	ax1.annotate('Sequential Execution', xy=(1.5, 0.8), xytext=(0.5,1),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
	ax1.annotate('Sequential Execution with heterogeneity', xy=(4, 1.0), xytext=(0.2,1.2),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

	ax1.annotate('Speculative execution', xy=(5.5, 1.0), xytext=(3,1.4),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

	plt.xticks(x_axis_ls, ["GPU_base","DSP_base","ACC_base","FCFS","HOLD","SVSoC"])
	plt.grid(color='grey', which='major', axis='y', linestyle='--')
	ax1.set_ylim(0.0, 1.5)
	ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))  
	ax1.set_axisbelow(True)
	plt.savefig("eva_obser1a.pdf")

def figure1b():
	x_axis_ls = [0.5,1.5,2.5,3.5,4.5,5.5]
	improvement1 = [0.6098,0.6366,0.7537]
	improvement2 = [0.6691,0.6861]
	improvement3 = [0.9525]
	x1 = [0.5,1.5,2.5]
	x2=[3.5,4.5]
	x3 = [5.5]
	fuck_1=[0.8,0.7,0.6]
	fuck_2=[0.5,0.4]
	plt.rc('font',size=13)
	ax1 = plt.figure(figsize=(6,4.5)).add_subplot(111)
	ax1.set_ylabel('Per-frame latency improvement', fontsize=14, fontweight='bold')
	plt.xticks(fontsize=12,rotation=60)
	plt.setp(ax1.spines.values(), linewidth=2)
	p1 = ax1.bar(x1,improvement1, 0.5, align='center',color='#FFBF56', linewidth=2.5)
	p2 = ax1.bar(x2, improvement2,0.5,align='center',color='#FFBF56',linewidth=2.5)
	p3 = ax1.bar(x3, improvement3, 0.5, align='center',color='#FFBF56',linewidth=2.5,)
	plt.subplots_adjust(left=0.2, bottom=0.20, right=0.9, top=0.9,
                wspace=0.2, hspace=0.2)
	ax1.annotate('Sequential Execution', xy=(1.5, 0.8), xytext=(0.2,1),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
	ax1.annotate('Sequential Execution with heterogeneity', xy=(4, 0.7), xytext=(0.2,1.2),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

	ax1.annotate('Speculative execution', xy=(5.5, 1.0), xytext=(3,1.4),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

	plt.xticks(x_axis_ls, ["GPU_base","DSP_base","ACC_base","FCFS","HOLD","SVSoC"])
	plt.grid(color='grey', which='major', axis='y', linestyle='--')
	ax1.set_ylim(0.0, 1.5)
	ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))  
	ax1.set_axisbelow(True)
	plt.savefig("eva_obser1b.pdf")

def figure6a():
	x_axis_ls=[i*1 for i in range(10)]
	b = np.load("ssim.npy")
	accuracy = b.tolist()
	accuracy_ext=[0 for i in range(5000)]
	for i in range(5000):
		if (i>829):
			accuracy_ext[i] = accuracy[i%829-1]
		else:
			accuracy_ext[i] = accuracy[i]
	plt.rc('font',size=13)
	ax1=plt.figure(figsize=(8,4.4)).add_subplot(111)
	ax1.set_ylabel('SSIM value', fontsize=14, fontweight='bold')
	plt.setp(ax1.spines.values(), linewidth=2)
	p1 = ax1.plot(x_axis_ls,accuracy_ext[10:20], color='blue', linestyle='-', linewidth=2)
	plt.xlabel("First 300 frames in the test dataset",fontsize=14,fontweight='bold')
	plt.grid(color='grey', which='major', axis='y', linestyle='--')
	ax1.set_ylim(0.0, 1.0)
	plt.savefig("eva_obser6.pdf")


def main():
	#figure1()
	#figure2a()
	#figure2b()
	#figure3()
	#figure5()
	#figure1a()
	#figure1b()
	figure6a()





if __name__=='__main__':

	main()

