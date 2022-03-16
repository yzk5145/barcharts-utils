# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from collections import namedtuple
import logging

class PlotStyle:
    def __init__(self, text, color, linestyle, marker, hatch='', markerfacecolor=None):
        self.text = text
        self.color = color
        self.linestyle  = linestyle
        self.marker = marker
        self.hatch = hatch
        self.markerfacecolor = markerfacecolor

plot_info = {}

class MyColor:
    HG = 'dimgray'#'c'#'#0080ff'
    HC = 'gray'#'dodgerblue'#'b'#'#56A902'
    #HC = '#e97f02'
    HYBRID = 'lightgray'#'r'#'#E53A40'

    HCHC ='dodgerblue'
    HGHG = 'c'
    HGHC = 'tomato'
    HCHG = 'mediumpurple'

class MyMarker:
    HG = '^' #triangle
    HC = 'o'
    HYBRID = 's' #square
    HCHC = '*'
    HGHG = 'o'
    HGHC = 's'
    HCHG = '^'
"""#this is to show w. and w.o. consistency per level in one fig
plot_info['nat-Hg'] = PlotStyle(
    text = r'$\mathdefault{nat\_H_g}$',
    color = MyColor.HG,
    linestyle = ':',
    marker = '^')

plot_info['nat-Hc'] = PlotStyle(
    text = r'$\mathdefault{nat\_H_c}$',
    color = MyColor.HC,
    linestyle = '-.',
    marker = '^')

plot_info['state-Hg'] = PlotStyle(
    text = r'$\mathdefault{state\_H_g}$',
    color = MyColor.HG,
    linestyle = ':',
    marker = 'o')

plot_info['state-Hc'] = PlotStyle(
    text = r'$\mathdefault{state\_H_c}$',
    color = MyColor.HC,
    linestyle = '-.',
    marker = 'o')

plot_info['nat-hybrid-selection-emdpct-0.05'] = PlotStyle(
    #text = r'$\mathdefault{nat\_hybrid\_selection\_emdpct\_0.05}$',
    text = r'$\mathdefault{nat\_hybrid}$',
    color = MyColor.HYBRID,
    linestyle = '-',
    marker = '^')

plot_info['state-hybrid-selection-emdpct-0.05'] = PlotStyle(
    #text = r'$\mathdefault{state\_hybrid\_selection\_emdpct\_0.05}$',
    text = r'$\mathdefault{state\_hybrid}$',
    color = MyColor.HYBRID,
    linestyle = '-',
    marker = 'o')

plot_info['nat-Hg+Hg-wConsist'] = PlotStyle(
    text = r'$\mathdefault{nat\_H_g x H_g\_wConsist}$',
    color = 'black',#MyColor.HG,
    linestyle = (0, (3, 10, 1, 10, 1, 10)),#':',
    marker = '^')

plot_info['nat-Hc+Hc-wConsist'] = PlotStyle(
    text = r'$\mathdefault{nat\_H_c x H_c\_wConsist}$',
    color = 'violet',#MyColor.HC,
    linestyle = (0, (3, 5, 1, 5, 1, 5)),#'-.',
    marker = '^')

plot_info['state-Hg+Hg-wConsist'] = PlotStyle(
    text = r'$\mathdefault{state\_H_g x H_g\_wConsist}$',
    color = 'black',#MyColor.HG,
    linestyle = (0, (3, 10, 1, 10, 1, 10)),#':',
    marker = 'o')

plot_info['state-Hc+Hc-wConsist'] = PlotStyle(
    text = r'$\mathdefault{state\_H_c x H_c\_wconsist}$',
    color = 'violet',#MyColor.HC,
    linestyle = (0, (3, 5, 1, 5, 1, 5)), #'-.',
    marker = 'o')

plot_info['nat-hybrid-wConsist-emdpct-0.05'] = PlotStyle(
    #text = r'$\mathdefault{nat\_hybrid\_wConsist\_emdpct\_0.05}$',
    text = r'$\mathdefault{nat\_hybrid\_wConsist}$',
    color = 'orange',#MyColor.HYBRID,
    linestyle = '--',#'-',
    marker = '^')

plot_info['state-hybrid-wConsist-emdpct-0.05'] = PlotStyle(
    #text = r'$\mathdefault{state\_hybrid\_wConsist\_emdpct\_0.05}$',
    text = r'$\mathdefault{state\_hybrid\_wConsist}$',
    color = 'orange',#MyColor.HYBRID,
    linestyle = '--',#'-',
    marker = 'o')


####3level
plot_info['wc-Hg'] = PlotStyle( #excel keyword
    text = r'$\mathdefault{WC\_H_g}$',
    color = MyColor.HG,
    linestyle = ':',
    marker = '^') #level

plot_info['wc-Hc'] = PlotStyle(
    text = r'$\mathdefault{WC\_H_c}$',
    color = MyColor.HC,
    linestyle = '-.',
    marker = '^')

plot_info['wc-hybrid-selection-emdpct-0.05'] = PlotStyle(
    text = r'$\mathdefault{WC\_hybrid}$',
    color = MyColor.HYBRID,
    linestyle = '-',
    marker = '^')


plot_info['wcstate-Hg'] = PlotStyle(
    text = r'$\mathdefault{WCstate\_H_g}$',
    color = MyColor.HG,
    linestyle = ':',
    marker = 'o')

plot_info['wcstate-Hc'] = PlotStyle(
    text = r'$\mathdefault{WCstate\_H_c}$',
    color = MyColor.HC,
    linestyle = '-.',
    marker = 'o')

plot_info['wcstate-hybrid-selection-emdpct-0.05'] = PlotStyle(
    text = r'$\mathdefault{WCstate\_hybrid}$',
    color = MyColor.HYBRID,
    linestyle = '-',
    marker = 'o')

#WCCT Hg Hc Hybrid

plot_info['wcct-Hg'] = PlotStyle(
    text = r'$\mathdefault{WCct\_H_g}$',
    color = MyColor.HG, #color and linestyle represents methods
    linestyle = ':',
    marker = 's')

plot_info['wcct-Hc'] = PlotStyle(
    text = r'$\mathdefault{WCct\_H_c}$',
    color = MyColor.HC,
    linestyle = '-.',
    marker = 's')

plot_info['wcct-hybrid-selection-emdpct-0.05'] = PlotStyle(
    text = r'$\mathdefault{WCct\_hybrid}$',
    color = MyColor.HYBRID,
    linestyle = '-',
    marker = 's')

#w Consist
plot_info['wc-Hg+Hg+Hg-wConsist'] = PlotStyle(
    text = r'$\mathdefault{WC\_H_g x H_g x H_g\_wConsist}$',
    #color = MyColor.HG,
    #linestyle = ':',
    color = 'black',#MyColor.HG,
    linestyle = (0, (3, 10, 1, 10, 1, 10)),#':',
    marker = '^')

plot_info['wc-Hc+Hc+Hc-wConsist'] = PlotStyle(
    text = r'$\mathdefault{WC\_H_c x H_c x H_c\_wConsist}$',
    #color = MyColor.HC,
    #linestyle = '-.',
    color = 'violet',#MyColor.HC,
    linestyle = (0, (3, 5, 1, 5, 1, 5)), #'-.',
    marker = '^')

plot_info['wc-hybrid-wConsist-emdpct-0.05'] = PlotStyle(
    text = r'$\mathdefault{WC\_hybrid\_wConsist}$',
    #color = MyColor.HYBRID,
    #linestyle = '-',
    color = 'orange',
    linestyle = '--',
    marker = '^')

plot_info['wcstate-Hg+Hg+Hg-wConsist'] = PlotStyle(
    text = r'$\mathdefault{WCstate\_H_g x H_g x H_g\_wConsist}$',
    #color = MyColor.HG,
    #linestyle = ':',
    color = 'black',#MyColor.HG,
    linestyle = (0, (3, 10, 1, 10, 1, 10)),#':',
    marker = 'o')

plot_info['wcstate-Hc+Hc+Hc-wConsist'] = PlotStyle(
    text = r'$\mathdefault{WCstate\_H_c x H_c x H_c\_wconsist}$',
    #color = MyColor.HC,
    #linestyle = '-.',
    color = 'violet',#MyColor.HC,
    linestyle = (0, (3, 5, 1, 5, 1, 5)), #'-.',
    marker = 'o')

plot_info['wcstate-hybrid-wConsist-emdpct-0.05'] = PlotStyle(
    text = r'$\mathdefault{WCstate\_hybrid\_wConsist}$',
    #color = MyColor.HYBRID,
    #linestyle = '-',
    color = 'orange',
    linestyle = '--',
    marker = 'o')

#wcct w consist
plot_info['wcct-Hg+Hg+Hg-wConsist'] = PlotStyle(
    text = r'$\mathdefault{WCct\_H_g x H_g x H_g\_wConsist}$',
    #color = MyColor.HG,
    #linestyle = ':',
    color = 'black',#MyColor.HG,
    linestyle = (0, (3, 10, 1, 10, 1, 10)),#':',
    marker = 's') #square

plot_info['wcct-Hc+Hc+Hc-wConsist'] = PlotStyle(
    text = r'$\mathdefault{WCct\_H_c x H_c x H_c\_wconsist}$',
    #color = MyColor.HC,
    #linestyle = '-.',
    color = 'violet',#MyColor.HC,
    linestyle = (0, (3, 5, 1, 5, 1, 5)), #'-.',
    marker = 's')

plot_info['wcct-hybrid-wConsist-emdpct-0.05'] = PlotStyle(
    text = r'$\mathdefault{WCct\_hybrid\_wConsist}$',
    #color = MyColor.HYBRID,
    #linestyle = '-',
    color = 'orange',
    linestyle = '--',
    marker = 's')
"""
#2 level w.o. consistency
plot_info['nat-Hg'] = PlotStyle(
    text = r'$\mathdefault{H_g}$',
    color = MyColor.HYBRID,
    linestyle = ':',
    marker = '^',
    hatch = '//'
)

plot_info['nat-Hc'] = PlotStyle(
    text = r'$\mathdefault{H_c}$',
    color = MyColor.HYBRID,
    linestyle = ':',
    marker = '^',
    hatch = '.'
)

plot_info['state-Hg'] = PlotStyle(
    text = r'$\mathdefault{H_g}$',
    color = MyColor.HYBRID,
    linestyle = ':',
    marker = '^',
    hatch = '//'
)

plot_info['state-Hc'] = PlotStyle(
    text = r'$\mathdefault{H_c}$',
    color = MyColor.HYBRID,
    linestyle = ':',
    marker = '^',
    hatch = '.'
)


#2 level consistency
plot_info['nat-Hg+Hg-wConsist'] = PlotStyle(
    text = r'$\mathdefault{H_g x H_g\_wConsist}$',
    color = MyColor.HG,
    linestyle = ':',
    marker = MyMarker.HG,
    hatch = '//'
)

plot_info['nat-Hc+Hc-wConsist'] = PlotStyle(
    text = r'$\mathdefault{H_c x H_c\_wConsist}$',
    color = MyColor.HC,
    linestyle = '-.',
    marker = MyMarker.HC,
    hatch = '.'
) #vary with method

plot_info['nat-hybrid-wConsist-emdpct-0.05'] = PlotStyle(
    #text = r'$\mathdefault{nat\_hybrid\_wConsist\_emdpct\_0.05}$',
    text = r'$\mathdefault{Hybrid\_wConsist}$',
    color = MyColor.HYBRID,
    linestyle = '-',
    marker = MyMarker.HYBRID
) #square

plot_info['state-Hg+Hg-wConsist'] = PlotStyle(
    text = r'$\mathdefault{H_g x H_g\_wConsist}$',
    color = MyColor.HG,
    linestyle = ':',
    marker = MyMarker.HG,
    hatch = '//'
)

plot_info['state-Hc+Hc-wConsist'] = PlotStyle(
    text = r'$\mathdefault{H_c x H_c\_wconsist}$',
    color = MyColor.HC,
    linestyle = '-.',
    marker = MyMarker.HC,
    hatch = '.'
)

plot_info['state-hybrid-wConsist-emdpct-0.05'] = PlotStyle(
    #text = r'$\mathdefault{state\_hybrid\_wConsist\_emdpct\_0.05}$',
    text = r'$\mathdefault{Hybrid\_wConsist}$',
    color = MyColor.HYBRID,
    linestyle = '-',
    marker = MyMarker.HYBRID
)

#3 level w.o. consistency: all use hybrid color, Hg use hatch = '//', Hc use hatch = '.'
plot_info['wc-Hg'] = PlotStyle( #excel keyword
    text = r'$\mathdefault{H_g}$',
    color = MyColor.HYBRID,
    marker = MyMarker.HG,
    linestyle = ':',
    hatch = '//'
) #level

plot_info['wc-Hc'] = PlotStyle(
    text = r'$\mathdefault{H_c}$',
    color = MyColor.HYBRID,
    marker = MyMarker.HC,
    linestyle = ':',
    hatch = '.'
)

plot_info['wcstate-Hg'] = PlotStyle(
    text = r'$\mathdefault{H_g}$',
    color = MyColor.HYBRID,
    marker = MyMarker.HG,
    linestyle = ':',
    hatch = '//'
)

plot_info['wcstate-Hc'] = PlotStyle(
    text = r'$\mathdefault{H_c}$',
    color = MyColor.HYBRID,
    marker = MyMarker.HC,
    linestyle = ':',
    hatch = '.'
)


plot_info['wcct-Hg'] = PlotStyle(
    text = r'$\mathdefault{H_g}$',
    color = MyColor.HYBRID,
    marker = MyMarker.HG,
    linestyle = ':',
    hatch = '//'
)

plot_info['wcct-Hc'] = PlotStyle(
    text = r'$\mathdefault{H_c}$',
    color = MyColor.HYBRID,
    marker = MyMarker.HC,
    linestyle = ':',
    hatch = '.'
)
#3 level consistency
plot_info['wc-Hg+Hg+Hg-wConsist'] = PlotStyle(
    text = r'$\mathdefault{H_g x H_g x H_g}$',
    color = MyColor.HG,
    linestyle = ':',
    marker = MyMarker.HG,
    hatch = '//'
)

plot_info['wc-Hc+Hc+Hc-wConsist'] = PlotStyle(
    text = r'$\mathdefault{H_c x H_c x H_c}$',
    color = MyColor.HC,
    linestyle = '-.',
    marker = MyMarker.HC,
    hatch = '.'
)

plot_info['wc-hybrid-wConsist-emdpct-0.05'] = PlotStyle(
    text = r'$\mathdefault{Hybrid}$',
    color = MyColor.HYBRID,
    linestyle = '-',
    marker = MyMarker.HYBRID
)

plot_info['wcstate-Hg+Hg+Hg-wConsist'] = PlotStyle(
    text = r'$\mathdefault{H_g x H_g x H_g}$',
    color = MyColor.HG,
    linestyle = ':',
    marker = MyMarker.HG,
    hatch = '//'
)

plot_info['wcstate-Hc+Hc+Hc-wConsist'] = PlotStyle(
    text = r'$\mathdefault{H_c x H_c x H_c}$',
    color = MyColor.HC,
    linestyle = '-.',
    marker = MyMarker.HC,
    hatch = '.'
)

plot_info['wcstate-hybrid-wConsist-emdpct-0.05'] = PlotStyle(
    text = r'$\mathdefault{Hybrid}$',
    color = MyColor.HYBRID,
    linestyle = '-',
    marker = MyMarker.HYBRID
)

#wcct w consist
plot_info['wcct-Hg+Hg+Hg-wConsist'] = PlotStyle(
    text = r'$\mathdefault{H_g x H_g x H_g}$',
    color = MyColor.HG,
    linestyle = ':',
    marker = MyMarker.HG,
    hatch = '//'
) #square

plot_info['wcct-Hc+Hc+Hc-wConsist'] = PlotStyle(
    text = r'$\mathdefault{H_c x H_c x H_c}$',
    color = MyColor.HC,
    linestyle = '-.',
    marker = MyMarker.HC,
    hatch = '.'
)

plot_info['wcct-hybrid-wConsist-emdpct-0.05'] = PlotStyle(
    text = r'$\mathdefault{Hybrid}$',
    color = MyColor.HYBRID,
    linestyle = '-',
    marker = MyMarker.HYBRID
)




#2lv metric - weight is filled, avg is not

#nat level
plot_info['Hc+Hc-weight-nat'] = PlotStyle(
    text = r'$\mathdefault{H_c x H_c\_weight}$',
    color = MyColor.HCHC,
    linestyle = ':',
    marker = MyMarker.HCHC,
    hatch = '//'
)
plot_info['Hc+Hc-avg-nat'] = PlotStyle(
    text = r'$\mathdefault{H_c x H_c\_avg}$',
    color = MyColor.HCHC,
    linestyle = ':',
    marker = MyMarker.HCHC,
    hatch = '//',
    markerfacecolor = 'white'
)

plot_info['Hg+Hg-weight-nat'] = PlotStyle(
    text = r'$\mathdefault{H_g x H_g\_weight}$',
    color = MyColor.HGHG,
    linestyle = ':',
    marker = MyMarker.HGHG,

)
plot_info['Hg+Hg-avg-nat'] = PlotStyle(
    text = r'$\mathdefault{H_g x H_g\_avg}$',
    color = MyColor.HGHG,
    linestyle = ':',
    marker = MyMarker.HGHG,
    markerfacecolor = 'white'
)


plot_info['Hg+Hc-weight-nat'] = PlotStyle(
    text = r'$\mathdefault{H_g x H_c\_weight}$',
    color = MyColor.HGHC,
    linestyle = ':',
    marker = MyMarker.HGHC,
    hatch = '.'
)
plot_info['Hg+Hc-avg-nat'] = PlotStyle(
    text = r'$\mathdefault{H_g x H_c\_avg}$',
    color = MyColor.HGHC,
    linestyle = ':',
    marker = MyMarker.HGHC,
    hatch = '.',
    markerfacecolor = 'white'
)

plot_info['Hc+Hg-weight-nat'] = PlotStyle(
    text = r'$\mathdefault{H_c x H_g\_weight}$',
    color = MyColor.HCHG,
    linestyle = ':',
    marker = MyMarker.HCHG,
    hatch = '*'
)
plot_info['Hc+Hg-avg-nat'] = PlotStyle(
    text = r'$\mathdefault{H_c x H_g\_avg}$',
    color = MyColor.HCHG,
    linestyle = ':',
    marker = MyMarker.HCHG,
    hatch = '*',
    markerfacecolor = 'white'
)


#state level
plot_info['Hc+Hc-weight-state'] = PlotStyle(
    text = r'$\mathdefault{H_c x H_c\_weight}$',
    color = MyColor.HCHC,
    linestyle = ':',
    marker = MyMarker.HCHC,
    hatch = '//'
)
plot_info['Hc+Hc-avg-state'] = PlotStyle(
    text = r'$\mathdefault{H_c x H_c\_avg}$',
    color = MyColor.HCHC,
    linestyle = ':',
    marker = MyMarker.HCHC,
    hatch = '//',
    markerfacecolor = 'white'
)

plot_info['Hg+Hg-weight-state'] = PlotStyle(
    text = r'$\mathdefault{H_g x H_g\_weight}$',
    color = MyColor.HGHG,
    linestyle = ':',
    marker = MyMarker.HGHG,

)
plot_info['Hg+Hg-avg-state'] = PlotStyle(
    text = r'$\mathdefault{H_g x H_g\_avg}$',
    color = MyColor.HGHG,
    linestyle = ':',
    marker = MyMarker.HGHG,
    markerfacecolor = 'white'
)


plot_info['Hg+Hc-weight-state'] = PlotStyle(
    text = r'$\mathdefault{H_g x H_c\_weight}$',
    color = MyColor.HGHC,
    linestyle = ':',
    marker = MyMarker.HGHC,
    hatch = '.'
)
plot_info['Hg+Hc-avg-state'] = PlotStyle(
    text = r'$\mathdefault{H_g x H_c\_avg}$',
    color = MyColor.HGHC,
    linestyle = ':',
    marker = MyMarker.HGHC,
    hatch = '.',
    markerfacecolor = 'white'
)

plot_info['Hc+Hg-weight-state'] = PlotStyle(
    text = r'$\mathdefault{H_c x H_g\_weight}$',
    color = MyColor.HCHG,
    linestyle = ':',
    marker = MyMarker.HCHG,
    hatch = '*'
)
plot_info['Hc+Hg-avg-state'] = PlotStyle(
    text = r'$\mathdefault{H_c x H_g\_avg}$',
    color = MyColor.HCHG,
    linestyle = ':',
    marker = MyMarker.HCHG,
    hatch = '*',
    markerfacecolor = 'white'
)
class MyErrorBar():
    def __init__(self, title):
        #self.fig = plt.figure()
        #self.fig.suptitle(title, fontsize=14, fontweight='bold')
        self.fig, self.ax = plt.subplots()
        #self.fig.subplots_adjust(top=0.15)
        self.ax.set_title(title, fontsize=14, fontweight='bold')
        self.bars = []
        self.kind = 'scatter'

    def add_error_bar(self, k, x, y, e, kind='scatter'):
        self.kind = kind
        plot_style = plot_info[k]
        if kind == 'scatter':
            self.ax.errorbar(
                x,
                y,
                e,
                label=plot_style.text,
                color=plot_style.color,
                linestyle=plot_style.linestyle,
                marker=plot_style.marker,
                mfc=plot_style.markerfacecolor,
                #mec='black',
                ms=10
            )
        elif kind == 'bar':
            if plot_style.markerfacecolor:
                edgecolor = plot_style.color
                color = plot_style.markerfacecolor
            else:
                color = plot_style.color
                edgecolor = None

            self.bar(
                x,
                y,
                e,
                label=plot_style.text,
                color=color,
                edgecolor=edgecolor,
                linestyle=plot_style.linestyle,
                hatch=plot_style.hatch
            )
        else:
            logging.error('unknown type: "{}"'.format(g_type))

    def bar(self, x, y, e, label, color, edgecolor, linestyle, hatch):
        self.bars.append((x, y, e, label, color, edgecolor, linestyle, hatch))

    def autolabel(self, rects):
        for rect in rects:
            h = rect.get_height()
            self.ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

    def draw_hist(self):
        num = len(self.bars)
        width_full = 0.8
        width = width_full/num
        rects = []
        for i in range(num):
            x, y, e, label, color, edgecolor, linestyle, hatch = self.bars[i]
            rects.append(
                self.ax.bar(
                    [idx+width*i for idx in range(len(x))],
                    y,
                    width,
                    yerr=e,
                    color=color,
                    edgecolor=edgecolor,
                    #linestyle=linestyle,
                    linewidth=1.2,
                    hatch=hatch,
                    error_kw=dict(elinewidth=2,ecolor='black')
                )
            )
        if len(self.bars)%2:
            logging.info('num%2')
            width_dist = width_full/2-width/2
        else:
            logging.info('else')
            width_dist = width_full/2-width/2#width_d = width

        self.ax.set_xticks([width_dist + i for i in range(len(self.bars[0][0]))])
        self.ax.set_xticklabels(self.bars[0][0])
        self.ax.legend(rects, [bar[3] for bar in self.bars])

    def save_fig(self, fname):
        if self.kind  == 'bar':
            self.draw_hist()
            #logging.info('self.ax.get_xticklabels(): {}'.format(self.ax.get_xticklabels()))
            self.ax.set_xticklabels(self.ax.get_xticklabels(), fontsize=15)
            self.ax.set_yticklabels(self.ax.get_yticklabels(), fontsize=15)
            self.ax.yaxis.grid()
            self.ax.set_yscale("log")
        else:
            #self.ax.set_yscale("log")
            plt.grid(True)
        self.ax.set_xlabel('budget', fontsize=15)
        self.ax.set_ylabel("average emd", fontsize=15)
        handles, labels = self.ax.get_legend_handles_labels()
        if not not labels and not not handles:
            labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0]))
            # lgd = self.ax.legend(handles, labels, loc=2, bbox_to_anchor=(1, 1))#, ncol=2)
            lgd = self.ax.legend(handles, labels, fontsize=50, loc="upper right")#, ncol=2)
        params = {'legend.fontsize': 14, 'legend.handlelength': 1}
        plt.rcParams.update(params)
        plt.tight_layout()
        #self.fig.savefig(fname, bbox_extra_artists=(lgd, self.ax,), bbox_inches='tight')
        if not not labels and not not handles:
            self.fig.savefig(fname, bbox_extra_artists=(lgd, self.ax,), bbox_inches='tight')
        else:
            self.fig.savefig(fname)

    def clear_fig(self):
        plt.close(self.fig)
        plt.clf()
