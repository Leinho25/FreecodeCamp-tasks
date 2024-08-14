# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:39:27 2024

@author: jose.lavadores
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("medical_examination.csv")

df["BMI"]=df["weight"]/(df["height"]/100)**2
df['overweight'] = df["BMI"].apply(lambda x: 1 if ((x>25)) else 0)
df=df.drop(columns=["BMI"])

df["cholesterol"]=df["cholesterol"].apply(lambda x: 0 if((x==1)) else 1)
df["gluc"]=df["gluc"].apply(lambda x: 0 if((x==1)) else 1)

def draw_cat_plot():
    df_cat =pd.melt(df,id_vars=["id","cardio"], value_vars=["cholesterol", "gluc", "smoke","alco","active","overweight"]).sort_values(by=["variable"])

    fig =sns.catplot(df_cat,x="variable",col="cardio", kind="count", height=5, aspect=1, hue="value")
    fig.set_axis_labels("variable", "total")

    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    df_heat = df[(df["ap_lo"]<=df["ap_hi"]) & (df["height"]>=df["height"].quantile(0.025)) & (df["height"]<df["height"].quantile(0.975)) & (df["weight"]>=df["weight"].quantile(0.025)) & (df["weight"]<df["weight"].quantile(0.975))]

    corr = round(df_heat.corr(),1)

    mask = np.triu(np.ones_like(corr))

    fig, ax = plt.subplots(figsize=(9,7))
    sns.heatmap(corr, annot=True, mask=mask, fmt=".1f",linewidth=.5, vmin=-0.08, vmax=0.24, center=0, ax=ax)
    fig.savefig('heatmap.png')
    return fig