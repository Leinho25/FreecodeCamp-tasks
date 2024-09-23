import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates
import calendar 

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date")

# Clean data
df = df[(df["value"]>df["value"].quantile(0.025)) & (df["value"]<df["value"].quantile(0.975))]
df.index=pd.to_datetime(df.index)

def draw_line_plot():
    ax=df.plot(figsize=(20,7), color='firebrick',legend=False)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.xticks(rotation=0)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Page Views', fontsize=12)
    fig=ax.get_figure()
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.reset_index()
    df_bar['date']=pd.to_datetime(df_bar['date'])
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month_name'] = df_bar['date'].dt.month_name()
    df_bar['month_num'] = df_bar['date'].dt.month
    df_bar = df_bar.groupby(['year', 'month_name', 'month_num'])['value'].mean().reset_index()
    # Ordenar por 'year' y 'month_num'
    df_bar.sort_values(['year', 'month_num'], inplace=True)
    #Eliminar la columna 'month_num' si no la necesitas para el gráfico
    df_bar.drop(columns=['month_num'], inplace=True)

    df_bar['month_name'] = pd.Categorical(df_bar['month_name'], 
                                   categories=calendar.month_name[1:], 
                                   ordered=True)
    df_bar=df_bar.pivot(index="year", values="value", columns="month_name")
    df_bar=df_bar[calendar.month_name[1:]]
    # Draw bar plot
    ax=df_bar.plot(kind="bar",figsize=(10,7), xlabel="Years", ylabel="Average page views")
    fig=ax.get_figure()
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(ncols=2, figsize=(30, 10))
    sns.boxplot(x=df_box["year"], y=df_box["value"], ax=axes[0])
    sns.boxplot(x=df_box["month"], y=df_box["value"], ax=axes[1])
    axes[0].set_title("Year-wise Box Plot (Trend)", fontsize=20)
    axes[1].set_title("Month-wise Box Plot (Seasonality)", fontsize=20)
    axes[0].set_xlabel("Year", fontsize=15)
    axes[1].set_xlabel("Month", fontsize=15)
    axes[0].set_ylabel("Page Views", fontsize=15)
    axes[1].set_ylabel("Page Views", fontsize=15)
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
