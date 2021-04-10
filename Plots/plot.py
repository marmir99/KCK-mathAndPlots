import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines

def read_file(name, tab):
    f = open(name)
    i = 0
    for line in f:
        if i > 0:
            tab.append(line.strip().split(','))
        i = i + 1
    f.close()

def create_x(tab, x):
    for m in tab:
        x.append(float(m[1])/1000)

def create_y(tab, y):
    sum = 0
    for n in tab:
        for i in range(2, len(n)):
            sum += float(n[i])
        y.append(sum/32*100)
        sum = 0

def draw_first(fig, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5):
    legend_elements = [mlines.Line2D([0], [0], marker='o', markersize=5, color='blue', label='1-Evol-RS'),
                       mlines.Line2D([0], [0], marker='v', markersize=5, color='green', label='1-Coev-RS'),
                       mlines.Line2D([0], [0], marker='D', markersize=5, color='red', label='2-Coev-RS'),
                       mlines.Line2D([0], [0], marker='s', markersize=5, color='black', label='1-Coev'),
                       mlines.Line2D([0], [0], marker='d', markersize=5, color='magenta', label='2-Coev')]
    ax1 = fig.add_subplot(121)
    ax1.grid(True, linestyle = '--', linewidth = 0.55)
    ax2 = ax1.twiny()
    ax2.set_xlim(0, 5)
    ax2.set_xticks([0, 1, 2, 3, 4, 5])
    ax2.set_xticklabels([0, 40, 80, 120, 160, 200])
    ax2.tick_params(axis='both', direction='in', labelsize =12)
    ax2.set_xlabel("Pokolenie", fontsize = 12, fontname = 'Times New Roman')
    ax3 = ax1.twinx()
    ax3.set_ylim(0, 8)
    ax3.set_yticks([0, 1, 2, 3, 4, 5, 6, 7, 8])
    ax3.set_yticklabels(['', '', '', '', '', '', '', '', ''])
    ax3.tick_params(axis='both', direction='in')
    ax1.plot(x_5, y_5, 'b', markevery=slice(0, 200, 25), marker='o', mec='black', mew='0.5')
    ax1.plot(x_4, y_4, 'g', markevery=slice(0, 200, 25), marker='v', mec='black', mew='0.5')
    ax1.plot(x_2, y_2, 'r', markevery=slice(0, 200, 25), marker='D', mec='black', mew='0.5')
    ax1.plot(x_3, y_3, 'k', markevery=slice(0, 200, 25), marker='s', mec='black', mew='0.5')
    ax1.plot(x_1, y_1, 'm', markevery=slice(0, 200, 25), marker='d', mec='black', mew='0.5')
    legend_elements = [mlines.Line2D([], [], marker='o', markersize=7, mec='black', color='blue', mew='0.5', label='1-Evol-RS'),
                       mlines.Line2D([], [], marker='v', markersize=7, mec='black', color='green', mew='0.5', label='1-Coev-RS'),
                       mlines.Line2D([], [], marker='D', markersize=7, mec='black', color='red', mew='0.5', label='2-Coev-RS'),
                       mlines.Line2D([], [], marker='s', markersize=7, mec='black', color='black', mew='0.5', label='1-Coev'),
                       mlines.Line2D([], [], marker='d', markersize=7, mec='black', color='magenta', mew='0.5', label='2-Coev')]
    legend = plt.legend(handles=legend_elements, loc='lower right', bbox_to_anchor=(0.98, 0.02),
               numpoints=2, prop={'size': 10, 'family':'Times New Roman'})
    frame = legend.get_frame()
    frame.set_linewidth(0.4)
    frame.set_edgecolor('black')
    #frame.set_boxstyle('Square', pad=0.3)

    ax1.set_xlabel("Rozegranych gier x1000", fontsize=12, fontname = 'Times New Roman')
    ax1.set_xlim(0, 500)
    ax1.set_xticks([0, 100, 200, 300, 400, 500])

    ax1.set_ylabel("Odsetek wygranych gier [%]", fontsize=12, fontname = 'Times New Roman')
    ax1.set_ylim(60, 100)
    ax1.set_yticks([60, 65, 70, 75, 80, 85, 90, 95, 100])

    ax1.tick_params(axis='both', which='major', direction='in', labelsize=12)

    for tick in ax1.get_xticklabels():
        tick.set_fontname('Times New Roman')
    for tick in ax1.get_yticklabels():
        tick.set_fontname('Times New Roman')
    for tick in ax2.get_xticklabels():
        tick.set_fontname('Times New Roman')
    for tick in ax3.get_yticklabels():
        tick.set_fontname('Times New Roman')

def change(data):
    tab = []
    for i in data:
        tab.append(float(i)*100)
    return tab

def draw_boxplot(fig, data_1, data_2, data_3, data_4, data_5):
    ax1 = fig.add_subplot(122)
    ax1.grid(True, linestyle='--', linewidth = 0.55)
    df1 = pd.DataFrame({'1-Evol-RS':data_5, '1-Coev_RS':data_4, '2-Coev-RS':data_2, '1-Coev':data_3, '2-Coev':data_1})
    df1.boxplot(ax=ax1, notch = True, showmeans = True, showfliers = True, medianprops = {'color': 'red'},
        meanprops ={"marker":"o", "markerfacecolor": "blue", "markeredgecolor": "black"},
        whiskerprops = {'color': 'blue', 'linestyle': '--'}, capprops = {'color': 'black'},
        flierprops = {'color': 'blue', 'marker': '+'},
        boxprops = {'color': 'blue', 'linestyle': '-'})
    ax1.yaxis.tick_right()
    ax1.set_ylim(60, 100)
    ax1.set_yticks([60, 65, 70, 75, 80, 85, 90, 95, 100])
    ax1.tick_params(axis='both', direction = 'in')
    ax1.tick_params(axis = 'x', rotation = 20)
    
    for tick in ax1.get_xticklabels():
        tick.set_fontname('Times New Roman')
    for tick in ax1.get_yticklabels():
        tick.set_fontname('Times New Roman')

def main():
    tab_1, x_1, y_1, tab_2, x_2, y_2, tab_3, x_3, y_3, tab_4, x_4, y_4, tab_5, x_5, y_5 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
    read_file("2cel.csv", tab_1)
    create_x(tab_1, x_1)
    create_y(tab_1, y_1)
    read_file("2cel-rs.csv", tab_2)
    create_x(tab_2, x_2)
    create_y(tab_2, y_2)
    read_file("cel.csv", tab_3)
    create_x(tab_3, x_3)
    create_y(tab_3, y_3)
    read_file("cel-rs.csv", tab_4)
    create_x(tab_4, x_4)
    create_y(tab_4, y_4)
    read_file("rsel.csv", tab_5)
    create_x(tab_5, x_5)
    create_y(tab_5, y_5)

    fig = plt.figure(figsize = (8,6))
    draw_first(fig, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5)

    data_1, data_2, data_3, data_4, data_5 = tab_1[-1], tab_2[-1], tab_3[-1], tab_4[-1], tab_5[-1]
    data_1, data_2, data_3, data_4, data_5 = data_1[2:], data_2[2:], data_3[2:], data_4[2:], data_5[2:]
    data_1, data_2, data_3, data_4, data_5 = change(data_1), change(data_2), change(data_3), change(data_4), change(
        data_5)

    draw_boxplot(fig, data_1, data_2, data_3, data_4, data_5)
    plt.savefig('plot_141285.pdf')
    plt.show()


if __name__ == '__main__':
    main()