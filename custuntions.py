import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from scipy.optimize import curve_fit
import seaborn as sns
import pandas as pd
import numpy as np


phase1start = "2020-03-01"
phase1end = "2020-10-01"
phase2start = "2020-10-01"
phase2end ="2021-03-16"

def phase_mask(dataframe, p1s=phase1start, p1e=phase1end, p2s=phase2start, p2e=phase2end):
    phase1_mask = (dataframe.index >= p1s) & (dataframe.index <= p1e)
    phase2_mask = (dataframe.index >= p2s ) & (dataframe.index <= p2e)
    phase1_df = dataframe.loc[phase1_mask]
    phase2_df = dataframe.loc[phase2_mask]
    return phase1_df, phase2_df


def line_plot(df, title, xlabel="Months", ylabel="Values"):
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.plot(df)
    date_form = DateFormatter("%m")

    ax.xaxis.set_major_formatter(date_form)
    ax.legend(df.columns.tolist(), loc='center left', bbox_to_anchor=(1, .5))

    ax.set(xlabel=xlabel,
           ylabel=ylabel,
           title=title)
    return fig, ax


def scatter_plot(data, x, y):
    c = sns.scatterplot(
    data=data, x=x, y=y,
    sizes=(20, 200), legend="full")
    return c