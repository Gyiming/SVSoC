#!/usr/bin/python2.7
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import FuncFormatter
import numpy as np


# manually added the result and plot the three category.
def plotCategoryBMF():
    data = {"ImgGoogle" : {'Currrent workload': 0, 'Previous lag': 25, 'Others': 3, 'Mistaken idle': 19, "percetage": 0.2305},
            "Twitter" : {'Currrent workload': 18, 'Previous lag': 0, 'Others': 11, 'Mistaken idle': 51, "percetage": 0.3803},
            "ESPN" : {'Currrent workload': 32, 'Previous lag': 0, 'Others': 8, 'Mistaken idle': 57, "percetage": 0.5631},
            "YouTube" : {'Currrent workload': 34, 'Previous lag': 2, 'Others': 27, 'Mistaken idle': 56, "percetage": 0.6882},
            "163" : {'Currrent workload': 17, 'Previous lag': 0, 'Others': 11, 'Mistaken idle': 3, "percetage": 0.7993},
            }
        
    for key in data:
        print([ data[key][k] for k in data[key]])
        data[key]["total"] = sum([ data[key][k] for k in data[key]])

    plt.rc('font', size=12, weight='bold')
    ax = plt.figure(figsize=(6, 4)).add_subplot(111)
    ax.set_ylabel('Aggregated FMR', fontsize=14, fontweight='bold')

    # p1 = ax.bar([0.1, 1.1, 2.1, 3.1, 4.1], [ data[key]['Previous lag']/data[key]["total"] for key in data], 0.2, 0, align='center',color='b');
    # p2 = ax.bar([0.3, 1.3, 2.3, 3.3, 4.3], [ data[key]['Currrent workload']/data[key]["total"] for key in data], 0.2, 0, align='center', color='#FFBF56');
    # p3 = ax.bar([0.7, 1.7, 2.7, 3.7, 4.7], [ data[key]['Mistaken idle']/data[key]["total"] for key in data], 0.2, 0, align='center', color='r');
    # p4 = ax.bar([0.5, 1.5, 2.5, 3.5, 4.5], [ data[key]['Others']/data[key]["total"] for key in data], 0.2, 0, align='center', color='g');


    bottom_data = [0, 0, 0, 0, 0]
    p1 = ax.bar([0.5, 1.5, 2.5, 3.5, 4.5], [ data[key]['Previous lag']/data[key]["total"]*data[key]["percetage"] for key in data], 0.5, 
                bottom=bottom_data, align='center',color='b', linewidth=3);

    bottom_data = np.add(bottom_data, [ data[key]['Previous lag']/data[key]["total"]*data[key]["percetage"] for key in data ])
    
    p2 = ax.bar([0.5, 1.5, 2.5, 3.5, 4.5], [ data[key]['Currrent workload']/data[key]["total"]*data[key]["percetage"] for key in data], 0.5, 
                bottom=bottom_data, align='center', color='#FFBF56', linewidth=3);

    bottom_data = np.add(bottom_data, [ data[key]['Currrent workload']/data[key]["total"]*data[key]["percetage"] for key in data ])
    p3 = ax.bar([0.5, 1.5, 2.5, 3.5, 4.5], [ data[key]['Mistaken idle']/data[key]["total"]*data[key]["percetage"] for key in data], 0.5, 
                bottom=bottom_data, align='center', color='r', linewidth=3);

    bottom_data = np.add(bottom_data, [ data[key]['Mistaken idle']/data[key]["total"]*data[key]["percetage"] for key in data ])
    p4 = ax.bar([0.5, 1.5, 2.5, 3.5, 4.5], [ data[key]['Others']/data[key]["total"]*data[key]["percetage"] for key in data], 0.5, 
                bottom=bottom_data, align='center', color='g', linewidth=3);

    plt.subplots_adjust(left=0.2, bottom=0.20, right=0.9, top=0.8,
                wspace=0.2, hspace=0.2)
    plt.xticks([0.5, 1.5, 2.5, 3.5, 4.5], [key for key in data])
    ax.set_ylim(0.0, 0.80)
    ax.tick_params(axis="y",direction="in")
    ax.tick_params(axis="x",direction="in")
    plt.xticks(rotation=45)
    plt.setp(ax.spines.values(), linewidth=2)
    plt.grid(color='grey', which='major', axis='y', linestyle='--')
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y))) 
    ax.set_axisbelow(True)

    plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Previous lag', 'Currrent workload',\
                 'Mistaken idle', 'Others'), bbox_to_anchor=(0., 1.01, 1., .101), loc=3,
           ncol=2, mode="expand", borderaxespad=0., frameon=False)
    
    plt.savefig("result_figures/fm-category.pdf");



# manually added the result and plot the three category.
def PlotTypeCategory():

    data = {
        "163" : [49, 11, 10, 0, 70, 0.15714285714285714] ,
        "msn" : [41, 11, 10, 1, 63, 0.19047619047619047] ,
        "slashdot" : [57, 17, 16, 1, 91, 0.1978021978021978] ,
        "youtube" : [93, 23, 20, 5, 141, 0.19858156028368795] ,
        "google" : [79, 23, 21, 3, 126, 0.20634920634920634] ,
        "amazon" : [74, 21, 19, 4, 118, 0.211864406779661] ,
        "ebay" : [50, 14, 11, 4, 79, 0.22784810126582278] ,
        "sina" : [37, 10, 10, 4, 61, 0.22950819672131145] ,
        "espn" : [110, 29, 26, 12, 177, 0.23163841807909602] ,
        "bbc" : [60, 20, 18, 4, 102, 204, 0.23529411764705882] ,
        "cnn" : [79, 34, 32, 7, 152, 0.26973684210526316] ,
        "twitter" : [42, 14, 12, 7, 75, 0.28],

    }


    x_axis_ls = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5]
        
    for key in data:
        data[key].append(sum(data[key]))

    Type_I = []
    Type_II = []
    Type_III = []
    Type_IV = []
    for key in data:
        Type_I.append(data[key][1] / data[key][4])
        Type_II.append(data[key][2] / data[key][4])
        Type_III.append(data[key][3] / data[key][4])
        Type_IV.append(data[key][0] / data[key][4])


    print(sum(Type_I)/len(Type_I)+sum(Type_III)/len(Type_III))
    print(sum(Type_II)/len(Type_II))

    # sorted_data = sorted(data.items(), key=lambda kv: (kv[1][5],kv[0]))
    # for key,value in sorted_data:
    #     print("\"",key, "\" : ",value, ",")

    plt.rc('font', size=10) # , weight='bold'
    ax = plt.figure(figsize=(6, 3)).add_subplot(111)
    ax.set_ylabel('Type Percentage', fontsize=10)
    plt.grid(color='grey', which='major', axis='y', linestyle='--')

    bottom_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    p1 = ax.bar(x_axis_ls, Type_I, 0.5, 
                bottom=bottom_data, align='center',color='#71985E',\
                edgecolor=['k']*len(x_axis_ls), linewidth=1.5, hatch="--");

    bottom_data = np.add(bottom_data, Type_I)
    
    p2 = ax.bar(x_axis_ls, Type_III, 0.5, 
                bottom=bottom_data, align='center', color='#8154D1',\
                edgecolor=['k']*len(x_axis_ls), linewidth=1.5, hatch="||");

    bottom_data = np.add(bottom_data, Type_III)
    p3 = ax.bar(x_axis_ls, Type_II, 0.5, 
                bottom=bottom_data, align='center', color='#FFBF56',\
                edgecolor=['k']*len(x_axis_ls), linewidth=1.5, hatch="oo");

    bottom_data = np.add(bottom_data, Type_II)
    p4 = ax.bar(x_axis_ls, Type_IV, 0.5, 
                bottom=bottom_data, align='center', color='#5b87f2',\
                edgecolor=['k']*len(x_axis_ls), linewidth=1.5, hatch="//");

    plt.subplots_adjust(left=0.12, bottom=0.20, right=0.95, top=0.9,
                wspace=0.2, hspace=0.2)
    plt.xticks(x_axis_ls, [key for key in data])
    ax.set_ylim(0.0, 1.0)
    ax.tick_params(axis="y",direction="in")
    ax.tick_params(axis="x",direction="in")
    plt.xticks(rotation=60)
    plt.setp(ax.spines.values(), linewidth=1.5)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y))) 
    ax.set_axisbelow(True)

    plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Type I', 'Type II',\
                 'Type III', 'Type IV'), bbox_to_anchor=(0., 1.01, 1., .101), loc=3,
           ncol=4, mode="expand", borderaxespad=0., frameon=False)
    
    plt.savefig("type-category.pdf");



# manually added the result and plot the three category.
def PlotQoSViolation():
    data = { #   energy saving,  oracle QoS,  actual QoS  
        "163" : [0.21, 0.1570, 0.1570],
        "msn" : [0.13, 0.1746, 0.1904],
        "slashdot" : [0.26, 0.1318, 0.1978],
        "youtube" : [0.30, 0.1560, 0.1989],
        "google" : [0.25, 0.1428, 0.2063],
        "amazon" : [0.36, 0.1271, 0.2118],
        "ebay" : [0.16, 0.1800, 0.2278],
        "sina" : [0.12, 0.1600, 0.2295],
        "espn" : [0.18, 0.1751, 0.2316],
        "bbc" : [0.25, 0.1764, 0.2353],
        "cnn" : [0.22, 0.1644, 0.2697],
        "twitter" : [0.18, 0.1866, 0.28],

    }

    x_axis_ls = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5]

    energy_saving = []
    qos_improvement = []
    for key in data:
        energy_saving.append(data[key][0])
        qos_improvement.append(1.0 - data[key][1]/data[key][2])
        print(data[key][0], 1.0 - data[key][1]/data[key][2])

    print(sum(energy_saving)/len(energy_saving))
    print(sum(qos_improvement)/len(qos_improvement))

    plt.rc('font', size=10)
    ax1 = plt.figure(figsize=(6, 4)).add_subplot(111)
    ax1.set_ylabel('Energy Saving', fontsize=14, fontweight='bold')
    plt.xticks(rotation=60)
    plt.setp(ax1.spines.values(), linewidth=2)

    ax2 = ax1.twinx()
    ax2.set_ylabel('QoS Improvement', fontsize=14, fontweight='bold')

    p1 = ax1.bar(x_axis_ls, energy_saving, 0.5, align='center',color='#71985E', linewidth=2.5);
    
    p2 = ax2.plot(x_axis_ls, qos_improvement, color='tomato', linestyle='dashed', linewidth=2, marker='o',markersize=8);

    plt.subplots_adjust(left=0.1, bottom=0.20, right=0.9, top=0.9,
                wspace=0.2, hspace=0.2)
    plt.xticks(x_axis_ls, [key for key in data])
    ax2.set_ylim(0.0, 0.5)
    ax1.set_ylim(0.0, 0.5)
    ax1.tick_params(axis="y",direction="in")
    ax2.tick_params(axis="y",direction="in")
    ax1.tick_params(axis="x",direction="in")
    plt.grid(color='grey', which='major', axis='y', linestyle='--')
    ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y))) 
    ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y))) 
    plt.legend((p1[0], p2[0]), ('energy', 'QoS',\
                 ), bbox_to_anchor=(0., 1.01, 1., .101), loc=3,
           ncol=2, mode="expand", borderaxespad=0., frameon=False)
    ax1.set_axisbelow(True)
    
    plt.savefig("oracle_qos.pdf");



# manually added the result and plot the three category.
def PlotPredictionAccuracy():
    data = { #   accuracy
        "163" : 0.8915,
        "msn" : 0.9267,
        "slashdot" : 0.9705,
        "youtube" : 0.9415,
        "google" : 0.8221,
        "amazon" : 0.8433,
        "ebay" : 0.9460,
        "sina" : 0.9502,
        "espn" : 0.9077,
        "bbc" : 0.9417,
        "cnn" : 0.9158,
        "twitter" : 0.9280,
        "average": 0.9328,

    }

    x_axis_ls = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 13.5]

    y_val = []
    for key in data:
        y_val.append(data[key]*100)

    std_v = []
    for k in data:
        std_v.append(data[k])
    # print("stdev", np.std(std_v))
    plt.rc('font', size=10)
    ax1 = plt.figure(figsize=(6, 2.5)).add_subplot(111)
    ax1.set_ylabel('Prediction Accuracy (%)', fontsize=10)
    plt.xticks(rotation=60)
    plt.setp(ax1.spines.values(), linewidth=1.5)
    plt.grid(color='grey', which='major', axis='y', linestyle='--')

    p1 = ax1.bar(x_axis_ls, y_val, 0.65, align='center', color='#71985E',\
                    edgecolor=['k']*len(y_val),linewidth=1.5);

    plt.rcParams["patch.force_edgecolor"] = True
    plt.subplots_adjust(left=0.15, bottom=0.25, right=0.95, top=0.9,
                wspace=0.2, hspace=0.2)
    plt.xticks(x_axis_ls, [key for key in data])
    ax1.set_ylim(70.0, 100)
    ax1.tick_params(axis="y",direction="in")
    ax1.tick_params(axis="x",direction="in")
    
    # ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y))) 
    ax1.set_axisbelow(True)
    
    plt.savefig("prediction-accuracy.pdf");



# manually added the result and plot the three category.
def PlotCompareOndemand():
    x_names = [
        "163", "msn", "slashdot", "youtube", \
        "google", "amazon", "ebay", "sina", "espn", \
        "bbc", "cnn", "twitter", "average"]
    
    x_axis_ls = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 13.5]
    ebs_axis_ls = [0.3, 1.3, 2.3, 3.3, 4.3, 5.3, 6.3, 7.3, 8.3, 9.3, 10.3, 11.3, 13.3]
    pes_axis_ls = [0.7, 1.7, 2.7, 3.7, 4.7, 5.7, 6.7, 7.7, 8.7, 9.7, 10.7, 11.7, 13.7]
           

    # 0    1      2        3        4       5       6    7     8     9    10     11       13      
    #163, msn, slashdot, youtube, google, amazon, ebay, sina, espn, bbc, cnn, twitter, average
    y_ebs_energy_ratio = [1.444, 1.345,  0,  0,  0, 1.371, 1.356, 1.603, 1.309, 1.345, 1.273,  0, 1.38]
    y_pes_energy_ratio = [1.032, 0.955,  0,  0,  0, 0.900, 1.146, 1.165, 0.798, 0.892, 0.873,  0, 0.97]
    y_ebs_qos_ratio = [0.665, 0.359,  0,  0,  0, 0.370, 0.498, 0.663, 0.353, 0.252, 0.243,  0, 0.42]
    y_pes_qos_ratio = [0.881, 0.836,  0,  0,  0, 0.892, 0.907, 0.923, 0.893, 0.822, 0.817,  0, 0.87]

    plt.rc('font', size=10)
    ax1 = plt.figure(figsize=(6, 3)).add_subplot(111)
    ax1.set_ylabel('Norm. Energy', fontsize=12, fontweight='bold')
    plt.xticks(rotation=60)
    plt.setp(ax1.spines.values(), linewidth=2)

    ax2 = ax1.twinx()
    ax2.set_ylabel('QoS Improvement', fontsize=12, fontweight='bold')

    p1 = ax1.bar(ebs_axis_ls, y_ebs_energy_ratio, 0.4, align='center',color='#71985E',\
        edgecolor=['k']*len(ebs_axis_ls), linewidth=2, hatch="/");
    p2 = ax1.bar(pes_axis_ls, y_pes_energy_ratio, 0.4, align='center',color='#FFBF56',\
     edgecolor=['k']*len(pes_axis_ls), linewidth=2, hatch="\\");
    
    p3 = ax2.plot(ebs_axis_ls, y_ebs_qos_ratio, color='tomato', linestyle='--',\
            linewidth=2, markeredgecolor='k', marker='d', markersize=8);
    p4 = ax2.plot(pes_axis_ls, y_pes_qos_ratio, color='#8154D1', linestyle=':',\
            linewidth=2, markeredgecolor='k', marker='o', markersize=8);

    plt.subplots_adjust(left=0.2, bottom=0.20, right=0.8, top=0.8,
                wspace=0.2, hspace=0.2)
    plt.xticks(x_axis_ls, x_names)
    ax1.set_ylim(0.0, 2.0)
    ax2.set_ylim(0.0, 1.0)
    ax1.tick_params(axis="y",direction="in")
    ax2.tick_params(axis="y",direction="in")
    ax1.tick_params(axis="x",direction="in")
    plt.grid(color='grey', which='major', axis='y', linestyle='--')
    ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y))) 
    ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y))) 
    plt.legend((p1[0], p2[0], p3[0], p4[0]), ('EBS energy', 'PES energy', \
        'EBS QoS','PES QoS'), bbox_to_anchor=(0., 1.01, 1., .101), loc=3,
           ncol=2, mode="expand", borderaxespad=0., frameon=False)
    ax1.set_axisbelow(True)
    
    plt.savefig("compare-ondemand.pdf");





# manually added the result and plot the three category.
def PlotCompareInteractiveEnergy():
    x_names = [
        "163", "msn", "slashdot", "youtube", \
        "google", "amazon", "ebay", "sina", "espn", \
        "bbc", "cnn", "twitter"]
    
    interative_axis_ls = [0.1, 1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1, 8.1, 9.1, 10.1, 11.1, 12.6]
    ebs_axis_ls = [0.3, 1.3, 2.3, 3.3, 4.3, 5.3, 6.3, 7.3, 8.3, 9.3, 10.3, 11.3, 12.8]
    pes_axis_ls = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 13.0]
    oracle_axis_ls = [0.7, 1.7, 2.7, 3.7, 4.7, 5.7, 6.7, 7.7, 8.7, 9.7, 10.7, 11.7, 13.2]
           
    Energy_data = {
        # Interactive Energy_EBS  Energy_PES  Energy_Oracle   QoS_real    QoS_EBS QoS_PES
        "163":[1,0.836713005823,0.653322324161,0.604484271],
        "amazon":[1,0.90908670,0.707251624,0.589289378],
        "bbc":[1,0.9597444,0.805747781,0.583834848],
        "ebay":[1,0.87099202,0.736169851,0.603919895],
        "espn":[1,0.97471718,0.695431582,0.581856032],
        "sina":[1,0.84939929,0.804507253,0.581856032],
        "cnn":[1,0.9632766606,0.769067756,0.60677652],
        "msn":[1,0.87271354,0.617838075,0.581856032],
        "twitter":[1,0.73065644185,0.70851412,0.617155468],
        "youtube":[1,0.96202055,0.734491221,0.581856032],
        "google":[1, 0.87314340,0.735811039,0.581856032],
        "slashdot":[1,0.98490521,0.682303091,0.601672644],
    }
    Interactive = []
    EBS_energy = []
    PES_energy = []
    Oracle_energy = []
    for key in x_names:
        Interactive.append(Energy_data[key][0]*100)
        EBS_energy.append(Energy_data[key][1]*100)
        PES_energy.append(Energy_data[key][2]*100)
        Oracle_energy.append(Energy_data[key][3]*100)

    x_names.append("average")
    Interactive.append(100)
    EBS_energy.append(sum(EBS_energy)/len(EBS_energy))
    PES_energy.append(sum(PES_energy)/len(PES_energy))
    Oracle_energy.append(sum(Oracle_energy)/len(Oracle_energy))

    print((1-PES_energy[-1], EBS_energy[-1]-PES_energy[-1]),\
        PES_energy[-1]-Oracle_energy[-1])


    plt.rc('font', size=10)
    ax1 = plt.figure(figsize=(6, 2.5)).add_subplot(111)
    ax1.set_ylabel('Norm. Energy (%)', fontsize=10)
    plt.xticks(rotation=60)
    plt.grid(color='grey', which='major', axis='y', linestyle='--')
    plt.setp(ax1.spines.values(), linewidth=1.5)

    p0 = ax1.bar(interative_axis_ls, Interactive, 0.2, align='center',color='tomato',\
        edgecolor=['k']*len(ebs_axis_ls), linewidth=1.5, hatch="\\\\");
    p1 = ax1.bar(ebs_axis_ls, EBS_energy, 0.2, align='center',color='#FFBF56',\
        edgecolor=['k']*len(ebs_axis_ls), linewidth=1.5);
    p2 = ax1.bar(pes_axis_ls, PES_energy, 0.2, align='center',color='#71985E',\
     edgecolor=['k']*len(pes_axis_ls), linewidth=1.5, hatch="//");
    p3 = ax1.bar(oracle_axis_ls, Oracle_energy, 0.2, align='center',color='#5b87f2',\
     edgecolor=['k']*len(pes_axis_ls), linewidth=1.5);

    plt.subplots_adjust(left=0.09, bottom=0.24, right=0.98, top=0.9,
                wspace=0.0, hspace=0.2)
    plt.xticks(ebs_axis_ls, x_names)
    ax1.set_ylim(40.0, 100.0)
    ax1.set_xlim(-0.2, 13.6)
    ax1.tick_params(axis="y",direction="in")
    ax1.tick_params(axis="x",direction="in")
    
    # ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
    plt.legend((p0[0], p1[0], p2[0], p3[0]), ('Interactive','EBS', 'PES', \
        'Oracle'), bbox_to_anchor=(0., 1.01, 1., .101), loc=3,
           ncol=4, mode="expand", borderaxespad=0., frameon=False)
    ax1.set_axisbelow(True)
    
    plt.savefig("compare-interactive-energy.pdf");


# manually added the result and plot the three category.
def PlotCompareInteractiveQoS():
    x_names = [
        "163", "msn", "slashdot", "youtube", \
        "google", "amazon", "ebay", "sina", "espn", \
        "bbc", "cnn", "twitter"]
    
    real_axis_ls = [0.3, 1.3, 2.3, 3.3, 4.3, 5.3, 6.3, 7.3, 8.3, 9.3, 10.3, 11.3, 12.6]
    ebs_axis_ls = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.8]
    pes_axis_ls = [0.7, 1.7, 2.7, 3.7, 4.7, 5.7, 6.7, 7.7, 8.7, 9.7, 10.7, 11.7, 13.0]

    QoS_data = {
        # Energy_EBS  Energy_PES  Energy_Oracle   QoS_real    QoS_EBS QoS_PES
        "163":[0.066666667,0.088888889,0.022222222],
        "amazon":[0.435282359,0.377811094,0.092453773],
        "bbc":[0.192063492,0.176984127,0.096825397],
        "ebay":[0.292638258,0.236556349,0.050479487],
        "espn":[0.409615385,0.428846154,0.107692308],
        "sina":[0.147950089,0.128342246,0.054367201],
        "cnn":[0.266917293,0.319548872,0.071428571],
        "msn":[0.170460157,0.160359147,0.038024691],
        "twitter":[0.1,0.1,0.1],
        "youtube":[0.366346154,0.309615385,0.123557692],
        "google":[0,0.166666667,0.055555556],
        "slashdot":[0.532922603,0.432422025,0.08586831],
    }

    real_qos = []
    EBS_qos = []
    PES_qos = []
    for key in x_names:
        real_qos.append(QoS_data[key][0]*100)
        EBS_qos.append(QoS_data[key][1]*100)
        PES_qos.append(QoS_data[key][2]*100)

    x_names.append("average")
    real_qos.append(sum(real_qos)/len(real_qos))
    EBS_qos.append(sum(EBS_qos)/len(EBS_qos))
    PES_qos.append(sum(PES_qos)/len(PES_qos))

    print(PES_qos[-1], EBS_qos[-1],real_qos[-1])
    print("stdev", np.std(PES_qos))

    plt.rc('font', size=10)
    ax1 = plt.figure(figsize=(6, 2.5)).add_subplot(111)
    ax1.set_ylabel('QoS Violation (%)', fontsize=10)
    plt.xticks(rotation=60)
    plt.setp(ax1.spines.values(), linewidth=1.5)
    plt.grid(color='grey', which='major', axis='y', linestyle='--')

    p1 = ax1.bar(real_axis_ls, real_qos, 0.2, align='center',color='tomato',\
        edgecolor=['k']*len(ebs_axis_ls), linewidth=1.5, hatch="\\\\");
    p2 = ax1.bar(ebs_axis_ls, EBS_qos, 0.2, align='center',color='#FFBF56',\
     edgecolor=['k']*len(pes_axis_ls), linewidth=1.5);
    p3 = ax1.bar(pes_axis_ls, PES_qos, 0.2, align='center',color='#71985E',\
     edgecolor=['k']*len(pes_axis_ls), linewidth=1.5, hatch="//");

    plt.subplots_adjust(left=0.08, bottom=0.24, right=0.98, top=0.9,
                wspace=0.0, hspace=0.2)
    plt.xticks(real_axis_ls, x_names)
    ax1.set_ylim(0.0, 60)
    ax1.yaxis.set_ticks([0, 10, 20, 30, 40, 50, 60])
    ax1.set_xlim(0.0, 13.4)
    ax1.tick_params(axis="y",direction="in")
    ax1.tick_params(axis="x",direction="in")
    
    # ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
    plt.legend((p1[0], p2[0], p3[0]), ('Interactive', 'EBS', \
        'PES'), bbox_to_anchor=(0., 1.01, 1., .101), loc=3, \
        ncol=3, mode="expand", borderaxespad=0., frameon=False)
    ax1.set_axisbelow(True)
    
    plt.savefig("compare-interactive-qos.pdf");



def PlotParento():
    
    plt.rc('font', size=11)

    
    ax1 = plt.figure(figsize=(4,3)).add_subplot(111)
    ax1.set_ylabel('Norm. Energy (%)', fontsize=11)
    ax1.set_xlabel('QoS Violation (%)', fontsize=11)
    plt.setp(ax1.spines.values(), linewidth=1.5)
    x_axis_ls = []
    y_val = []
    for v in range(1, 100):
        x_axis_ls.append(v)
        y_val.append(2700/v)


    pareto = ax1.plot(x_axis_ls, y_val, color='k', linestyle='--',\
            linewidth=1.5);

    ebs = ax1.plot([25], [90], color='#FFBF56', linestyle='none',\
            linewidth=1.5,markeredgecolor='k', marker='o', markersize=10);

    pes = ax1.plot([7.6], [72.1], color='#71985E', linestyle='none',\
            linewidth=1.5,markeredgecolor='k', marker='*', markersize=12);

    interactive = ax1.plot([25], [100], color='tomato', linestyle='none',\
            linewidth=1.5,markeredgecolor='k', marker='d', markersize=10);

    ondemand = ax1.plot([36], [79], color='#8154D1', linestyle='none',\
            linewidth=1.5,markeredgecolor='k', marker='H', markersize=10);

    oracle = ax1.plot([0], [59], color='#5b87f2', linestyle='none',\
            linewidth=1.5,markeredgecolor='k', marker='s', markersize=10,clip_on=False);

    plt.minorticks_on()

    plt.grid(color='grey', which='major', axis='y', linestyle='--')
    plt.grid(color='grey', which='major', axis='x', linestyle='--')
    plt.subplots_adjust(left=0.2, bottom=0.15, right=0.9, top=0.9,
                wspace=0.2, hspace=0.2)
    ax1.set_ylim(40, 120)
    ax1.set_xlim(-5, 80)
    ax1.yaxis.set_ticks([40, 60, 80, 100, 120])
    ax1.xaxis.set_ticks([0, 20, 40, 60, 80])
    ax1.arrow(25, 65, -13, -13, head_width=2.5, head_length=3, fc='limegreen',\
             ec='limegreen', lw=2.5)
    ax1.text(20, 50, 'better', fontsize=11,color='limegreen')
    ax1.tick_params(axis="y",direction="in")
    ax1.tick_params(axis="x",direction="in")
    ax1.tick_params(axis='x',which='minor',direction="in")
    ax1.tick_params(axis='y',which='minor',direction="in")
    ax1.set_axisbelow(True)
    plt.legend((interactive[0], ondemand[0], ebs[0], pes[0], oracle[0]), \
        ('Interactive', 'Ondemand', 'EBS', 'PES', 'Oracle'), prop={'size': 9})
    
    plt.savefig("pareto.pdf");



# manually added the result and plot the three category.
def PlotEnergySensitive():
    x_names = [
        "163", "msn", "slashdot", "youtube", \
        "google", "amazon", "ebay", "sina", "espn", \
        "bbc", "cnn", "twitter", "average"]
    x_axis_ls = [0.3, 0.5, 0.7, 0.9, 1.0]
    energy_ratio = { 
        "163" : [0.720062814,0.700422298,0.707239091,0.761859017,1],
        "amazon" : [0.725933509,0.725933509,0.710327122,0.744628403,1],
        "bbc" : [0.724643565,0.720336974,0.709649777,0.748408393,1],
        "ebay" : [0.716297509,0.716297509,0.716297509,0.670567046,1],
        "espn" : [0.678445058,0.678445058,0.678445058,0.750388277,1],
        "sina" : [0.817630628,0.681198409,0.712280879,0.714891055,1],
        "cnn" : [0.602848857,0.602848857,0.602848857,0.621226955,1],
        "msn" : [0.693543408,0.693543408,0.693543408,0.77162733,1]
    }
    plt.rc('font', size=11)

    
    ax1 = plt.figure(figsize=(3.5,2.5)).add_subplot(111)
    ax1.set_ylabel('Norm. Energy', fontsize=11)
    ax1.set_xlabel('Confidence Threshold', fontsize=11)
    plt.setp(ax1.spines.values(), linewidth=1.5)
    
    for key in energy_ratio:
        p1 = ax1.plot(x_axis_ls, energy_ratio[key], linewidth=1);

    plt.minorticks_on()
    # Hide the right and top spines
    # ax1.spines['right'].set_visible(False)
    # ax1.spines['top'].set_visible(False)
    plt.subplots_adjust(left=0.2, bottom=0.15, right=0.9, top=0.9,\
                wspace=0.2, hspace=0.2)
    ax1.set_ylim(0.5, 1.0)
    ax1.set_xlim(0.2, 1.0)
    ax1.tick_params(axis="y",direction="in")
    ax1.tick_params(axis="x",direction="in")
    ax1.tick_params(axis='x',which='minor',direction="in")
    ax1.tick_params(axis='y',which='minor',direction="in")
    ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y))) 
    ax1.xaxis.set_major_formatter(FuncFormatter(lambda x, _: '{:.0%}'.format(x))) 
    ax1.set_axisbelow(True)
    
    plt.savefig("sensitive-energy.pdf");



# manually added the result and plot the three category.
def PlotQoSSensitive():
    x_names = [
        "163", "msn", "slashdot", "youtube", \
        "google", "amazon", "ebay", "sina", "espn", \
        "bbc", "cnn", "twitter", "average"]
    x_axis_ls = [0.3, 0.5, 0.7, 0.9, 1.0]

    QoS_ratio = {
        "163" : [0.246,0.263,0.263,0.368,1],
        "amazon" : [0.222,0.222,0.222,0.278,1],
        "bbc" : [0.229,0.235,0.235,0.307,1],
        "ebay" : [0.129,0.129,0.129,0.227,1],
        "espn" : [0.142,0.143,0.143,0.357,1],
        "sina" : [0.166,0.1666,0.1666,0.25,1],
        "cnn" : [0.2,0.2,0.2,0.266666667,1],
        "msn" : [0.222222222,0.222222222,0.222222222,0.333333333,1],
    }

    plt.rc('font', size=11)

    
    ax1 = plt.figure(figsize=(3.5,2.5)).add_subplot(111)
    ax1.set_ylabel('Reduction of QoS Violation', fontsize=11)
    ax1.set_xlabel('Confidence Threshold', fontsize=11)
    plt.setp(ax1.spines.values(), linewidth=1.5)
    
    for key in QoS_ratio:
        p1 = ax1.plot(x_axis_ls, [ 1-v for v in QoS_ratio[key]], linewidth=1);

    plt.minorticks_on()
    # Hide the right and top spines
    # ax1.spines['right'].set_visible(False)
    # ax1.spines['top'].set_visible(False)
    plt.subplots_adjust(left=0.2, bottom=0.15, right=0.9, top=0.9,
                wspace=0.2, hspace=0.2)
    ax1.set_ylim(0.0, 1.0)
    ax1.set_xlim(0.2, 1.0)
    ax1.tick_params(axis="y",direction="in")
    ax1.tick_params(axis="x",direction="in")
    ax1.tick_params(axis='x',which='minor',direction="in")
    ax1.tick_params(axis='y',which='minor',direction="in")
    ax1.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y))) 
    ax1.xaxis.set_major_formatter(FuncFormatter(lambda x, _: '{:.0%}'.format(x))) 
    ax1.set_axisbelow(True)
    
    plt.savefig("sensitive-qos.pdf");
    # manually added the result and plot the three category.



#PlotTypeCategory()
PlotQoSViolation()
#PlotPredictionAccuracy()
#PlotCompareOndemand()
#PlotEnergySensitive()
#PlotQoSSensitive()
#PlotCompareInteractiveEnergy()
#PlotCompareInteractiveQoS()
#PlotParento()
