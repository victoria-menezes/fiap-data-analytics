import pandas as pd
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from cycler import cycler
import numpy as np
import seaborn as sb
from datetime import date
import matplotlib.ticker as ticker
import matplotlib

def rotate_label(rot : float = 45, ha : str ='right'):
    plt.xticks(rotation=rot, ha=ha)

def add_grid(ax):
    ax.set_axisbelow(True)
    plt.grid(zorder=-1, linestyle='--')

def set_y_lim(df : pd.DataFrame, column : str, percentage : float = 0.2):
    max = df.max()[column]
    plt.ylim(0, max*(1 + percentage))

def set_labels(x : str = '', y : str = ''):
    plt.xlabel(x)
    plt.ylabel(y)

def ticks_on_years(ax, axis='x'):
    if axis == 'x':
        ax.xaxis.set_major_locator(matplotlib.dates.YearLocator())
    else:
        ax.yaxis.set_major_locator(matplotlib.dates.YearLocator())
    return ax

def ticks_per_interval(ax, base, offset, axis='x',):
    if axis == 'x':
        ax.xaxis.set_major_locator(ticker.MultipleLocator(base, offset=offset))
    else:
        ax.yaxis.set_major_locator(ticker.MultipleLocator(base, offset=offset))

def set_axes_cycler(cycler):
    plt.rc('axes',prop_cycle = cycler)

def get_top(df, column_sort, column_top, top = 5):
    return df.sort_values(column_sort, ascending=False).head(top).reset_index()[column_top]

def move_legend(loc : str ='center left', bbox : tuple = (1.0,0.5)):
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

def set_figsize(size):
    plt.figure(figsize=size)