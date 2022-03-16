#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import re
import math
from error_bar import *
import logging

try:
    import coloredlogs
    FIELD_STYLES = dict(
        asctime=dict(color='red'),
        levelname=dict(color='white', bold=coloredlogs.CAN_USE_BOLD_FONT),
        filename=dict(color='cyan'),
    )
    LEVEL_STYLES = dict(
        warning=dict(color='yellow'),
        error=dict(color='red'),
        critical=dict(color='red', bold=coloredlogs.CAN_USE_BOLD_FONT)
    )
    coloredlogs.install(fmt='%(asctime)s %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',datefmt='%H:%M:%S', field_styles=FIELD_STYLES, level_styles=LEVEL_STYLES)
except:
    pass
logging.basicConfig(format='%(asctime)s %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',datefmt='%H:%M:%S', level=logging.INFO)

xls = pd.ExcelFile('result.xlsx')
dataframes_tmp = pd.read_excel(xls, index_col=0, sheet_name=None)
dataframes = {}
for sheet_name in xls.sheet_names:
    dataframes[sheet_name]= dataframes_tmp[sheet_name]


xls.close()

MY_KEYS = [
    'nat-Hg',
    'nat-Hc',
    'state-Hg',
    'state-Hc',
    'nat-Hg+Hg-wConsist',
    'nat-Hc+Hc-wConsist',
    'nat-hybrid-wConsist-emdpct-0.05',
    'state-Hg+Hg-wConsist',
    'state-Hc+Hc-wConsist',
    'state-hybrid-wConsist-emdpct-0.05',
    'nat-hybrid-selection-emdpct-0.05',
    'state-hybrid-selection-emdpct-0.05',
]

MY_3LEVEL_KEYS = [
    'wc-Hg',
    'wc-Hc',
    'wcstate-Hg',
    'wcstate-Hc',
    'wcct-Hg',
    'wcct-Hc',
    'wc-Hg+Hg+Hg-wConsist',
    'wc-Hc+Hc+Hc-wConsist',
    'wc-hybrid-wConsist-emdpct-0.05',
    'wcstate-Hg+Hg+Hg-wConsist',
    'wcstate-Hc+Hc+Hc-wConsist',
    'wcstate-hybrid-wConsist-emdpct-0.05',
    'wcct-Hg+Hg+Hg-wConsist',
    'wcct-Hc+Hc+Hc-wConsist',
    'wcct-hybrid-wConsist-emdpct-0.05',
    'wc-hybrid-selection-emdpct-0.05',
    'wcstate-hybrid-selection-emdpct-0.05',
    'wcct-hybrid-selection-emdpct-0.05',
]

v_pattern = '([\d.]+)\s+\(std: ([na\d.]+)\)'

def gen_error_bar(keys, df, title, fname, kind='scatter'):
    logging.info("TITLE: '{}'".format(title))
    logging.info("KEYS: '{}'".format(keys))
    err_bar = MyErrorBar(title)
    filted_df = df.loc[keys, :]
    for index, row in filted_df.iterrows():
        method_name = row.name
        x = []
        y = []
        e = []
        for k, v in row.dropna().items():
            emd, std = re.findall(v_pattern, v)[0]
            emd = float(emd)
            std = float(std) if std != 'nan' else 0
            x.append(k)
            y.append(emd)
            e.append(std/math.sqrt(10))
        if not not x:
            err_bar.add_error_bar(method_name, x, y, e, kind)
    err_bar.save_fig(fname)
    err_bar.clear_fig()

for name, df in dataframes.items():
    logging.info("SHEET_NAME: '{}'".format(name))
    """
    # without
    gen_error_bar( #gen_error_bar will gen a fig
        [key for key in MY_KEYS if 'Consist' not in key], #keyword list
        df,
        '%s (without consistency)' %(name),
        'output/%s-woc' %(name)
    )
    # with
    gen_error_bar(
        [key for key in MY_KEYS if 'Consist' in key],
        df,
        '%s (with consistency)' %(name),
        'output/%s-wc' %(name)
    )

    gen_error_bar(
        [key for key in MY_KEYS if 'nat' in key], #keyword list
        df,
        '%s (national)' %(name), #title name
        'output/%s-natall' %(name)  #file name
    )

    gen_error_bar(
        [key for key in MY_KEYS if 'state' in key],
        df,
        '%s (state)' %(name),
        'output/%s-stateall' %(name)
    )

    gen_error_bar(
        [key for key in MY_KEYS],
        df,
        '%s (all methods)' %(name),
        'output/%s-all' %(name)
    )
    """
    ####3 level result
    """
    # without
    gen_error_bar( #gen_error_bar will gen a fig
        [key for key in MY_3LEVEL_KEYS if 'Consist' not in key], #keyword list
        df,
        '%s (without consistency)' %(name),
        'output/%s-3lwoc' %(name)
    )

    # with
    gen_error_bar(
        [key for key in MY_3LEVEL_KEYS if 'Consist' in key],
        df,
        '%s (with consistency)' %(name),
        'output/%s-3lwc' %(name)
    )
    """
    """
    gen_error_bar(
        [key for key in MY_3LEVEL_KEYS if 'wc-' in key],
        df,
        '%s (WC)' %(name),
        'output/%s-wcall' %(name)
    )


    gen_error_bar(
        [key for key in MY_3LEVEL_KEYS if 'wcstate' in key],
        df,
        '%s (WCstate)' %(name),
        'output/%s-wcstateall' %(name)
    )

    gen_error_bar(
        [key for key in MY_3LEVEL_KEYS if 'wcct' in key],
        df,
        '%s (WCct)' %(name),
        'output/%s-wcctall' %(name)
    )
    """
    """
    nat_2lv_consistency = ['nat-Hg+Hg-wConsist', 'nat-Hc+Hc-wConsist',
        'nat-hybrid-wConsist-emdpct-0.05']
    ##only consistency per level
    gen_error_bar(
        nat_2lv_consistency,
        df,
        '%s (with consistency)' %(name),
        'output/%s-2lv-consist-nat' %(name)
    )

    state_2lv_consistency = ['state-Hg+Hg-wConsist', 'state-Hc+Hc-wConsist',
    'state-hybrid-wConsist-emdpct-0.05']

    gen_error_bar(
        nat_2lv_consistency,
        df,
        '%s (with consistency)' %(name),
        'output/%s-2lv-consist-state' %(name)
    )
    """
    """
    wc_3lv_consistency = ['wc-Hg+Hg+Hg-wConsist', 'wc-Hc+Hc+Hc-wConsist',
    'wc-hybrid-wConsist-emdpct-0.05']

    gen_error_bar(
        wc_3lv_consistency,
        df,
        '%s (with consistency)' %(name),
        'output/%s-3lv-consist-wc' %(name)
    )


    wcstate_3lv_consistency = ['wcstate-Hg+Hg+Hg-wConsist', 'wcstate-Hc+Hc+Hc-wConsist',
    'wcstate-hybrid-wConsist-emdpct-0.05']

    gen_error_bar(
        wcstate_3lv_consistency,
        df,
        '%s (with consistency)' %(name),
        'output/%s-3lv-consist-wcstate' %(name)
    )

    wcct_3lv_consistency = ['wcct-Hg+Hg+Hg-wConsist', 'wcct-Hc+Hc+Hc-wConsist',
    'wcct-hybrid-wConsist-emdpct-0.05']
    gen_error_bar(
        wcct_3lv_consistency,
        df,
        '%s (with consistency)' %(name),
        'output/%s-3lv-consist-wcct' %(name)
    )
    """

    
    ###2lv consistency, with bar

    #nat_2lv_consistency = ['nat-Hg+Hg-wConsist', 'nat-Hc+Hc-wConsist',
    #    'nat-hybrid-wConsist-emdpct-0.05']
    nat_2lv_consistency = ['nat-Hg+Hg-wConsist', 'nat-Hc+Hc-wConsist']
    ##only consistency per level
    gen_error_bar(
        nat_2lv_consistency,
        df,
        '%s w. consistency national' %(name),
        'output/%s-2lv-consist-nat-bar' %(name),
        kind='bar'
    )

    #state_2lv_consistency = ['state-Hg+Hg-wConsist', 'state-Hc+Hc-wConsist',
    #    'state-hybrid-wConsist-emdpct-0.05']

    state_2lv_consistency = ['state-Hg+Hg-wConsist', 'state-Hc+Hc-wConsist']

    gen_error_bar(
        state_2lv_consistency,
        df,
        '%s w. consistency state' %(name),
        'output/%s-2lv-consist-state-bar' %(name),
        kind='bar'
    )

    
    """
    #wc_3lv_consistency = ['wc-Hg+Hg+Hg-wConsist', 'wc-Hc+Hc+Hc-wConsist',
    #'wc-hybrid-wConsist-emdpct-0.05']

    wc_3lv_consistency = ['wc-Hg+Hg+Hg-wConsist', 'wc-Hc+Hc+Hc-wConsist']

    gen_error_bar(
        wc_3lv_consistency,
        df,
        '%s w. consistency Level 1' %(name),
        'output/%s-3lv-consist-wc-bar' %(name),
        kind='bar'
    )


    #wcstate_3lv_consistency = ['wcstate-Hg+Hg+Hg-wConsist', 'wcstate-Hc+Hc+Hc-wConsist',
    #'wcstate-hybrid-wConsist-emdpct-0.05']

    wcstate_3lv_consistency = ['wcstate-Hg+Hg+Hg-wConsist', 'wcstate-Hc+Hc+Hc-wConsist']

    gen_error_bar(
        wcstate_3lv_consistency,
        df,
        '%s w. consistency Level 2' %(name),
        'output/%s-3lv-consist-wcstate-bar' %(name),
        kind='bar'
    )

    #wcct_3lv_consistency = ['wcct-Hg+Hg+Hg-wConsist', 'wcct-Hc+Hc+Hc-wConsist',
    #'wcct-hybrid-wConsist-emdpct-0.05']

    wcct_3lv_consistency = ['wcct-Hg+Hg+Hg-wConsist', 'wcct-Hc+Hc+Hc-wConsist']
    gen_error_bar(
        wcct_3lv_consistency,
        df,
        '%s w. consistency Level 3' %(name),
        'output/%s-3lv-consist-wcct-bar' %(name),
        kind='bar'
    )
    """

    """
    ##############################################
    #Figure 2. 2-level w. w.o. consistency level #
    ##############################################
    nat_2lv_wo_w_consist = ['nat-Hg', 'nat-Hc', 'nat-Hg+Hg-wConsist', 'nat-Hc+Hc-wConsist']
    gen_error_bar(
        nat_2lv_wo_w_consist, #keyword list
        df,
        '%s (national)' %(name), #title name
        'output/%s-natall' %(name),  #file name
        kind='bar'
    )

    state_2lv_wo_w_consist = ['state-Hg', 'state-Hc', 'state-Hg+Hg-wConsist', 'state-Hc+Hc-wConsist']
    gen_error_bar(
        state_2lv_wo_w_consist, #keyword list
        df,
        '%s (state)' %(name), #title name
        'output/%s-stateall' %(name),  #file name
        kind='bar'
    )
    """

    ##############################################
    #Figure 3. 3-level w. w.o. consistency level #
    ##############################################

    wc_3lv_wo_w_consist = ['wc-Hg', 'wc-Hc', 'wc-Hg+Hg+Hg-wConsist', 'wc-Hc+Hc+Hc-wConsist' ]
    gen_error_bar(
        wc_3lv_wo_w_consist, #keyword list
        df,
        '%s (Level 0)' %(name), #title name
        'output/%s-wcall' %(name),  #file name
        kind='bar'
    )

    wcstate_3lv_wo_w_consist = ['wcstate-Hg', 'wcstate-Hc',
        'wcstate-Hg+Hg+Hg-wConsist', 'wcstate-Hc+Hc+Hc-wConsist']
    gen_error_bar(
        wcstate_3lv_wo_w_consist, #keyword list
        df,
        '%s (Level 1)' %(name), #title name
        'output/%s-wcstateall' %(name),  #file name
        kind='bar'
    )

    wcct_3lv_wo_w_consist = ['wcct-Hg', 'wcct-Hc',
        'wcct-Hg+Hg+Hg-wConsist', 'wcct-Hc+Hc+Hc-wConsist']
    gen_error_bar(
        wcct_3lv_wo_w_consist, #keyword list
        df,
        '%s (Level 2)' %(name), #title name
        'output/%s-wcctall' %(name),  #file name
        kind='bar'
    )


    """
    ###################################
    #Figure 1. 2lv metrics line plot  #
    ###################################
    #nat_8metrics = ['Hc+Hc-avg-nat', 'Hc+Hc-weight-nat', 'Hg+Hg-avg-nat', 'Hg+Hg-weight-nat',
    #    'Hg+Hc-avg-nat', 'Hg+Hc-weight-nat', 'Hc+Hg-avg-nat', 'Hc+Hg-weight-nat']

    #NO Hg+Hg
    nat_8metrics = ['Hc+Hc-avg-nat', 'Hc+Hc-weight-nat',
        'Hg+Hc-avg-nat', 'Hg+Hc-weight-nat', 'Hc+Hg-avg-nat', 'Hc+Hg-weight-nat']
    gen_error_bar(
        nat_8metrics,
        df,
        '%s national' %(name),
        'output/%s-2lv-metric-nat' %(name),
        kind='bar'
    )

    #state_8metrics = ['Hc+Hc-avg-state', 'Hc+Hc-weight-state', 'Hg+Hg-avg-state', 'Hg+Hg-weight-state',
    #    'Hg+Hc-avg-state', 'Hg+Hc-weight-state', 'Hc+Hg-avg-state', 'Hc+Hg-weight-state']

    state_8metrics = ['Hc+Hc-avg-state', 'Hc+Hc-weight-state',
        'Hg+Hc-avg-state', 'Hg+Hc-weight-state', 'Hc+Hg-avg-state', 'Hc+Hg-weight-state']
    gen_error_bar(
        state_8metrics,
        df,
        '%s state' %(name),
        'output/%s-2lv-metric-state' %(name),
        kind='bar'
    )
    """
