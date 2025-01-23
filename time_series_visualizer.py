import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def clean_data(df):
    """Очищення даних: фільтрація за межами верхніх та нижніх 2,5%."""
    lower_percentile = df['page_views'].quantile(0.025)
    upper_percentile = df['page_views'].quantile(0.975)
    
    df_cleaned = df[(df['page_views'] >= lower_percentile) & (df['page_views'] <= upper_percentile)]
    
    return df_cleaned

def draw_line_plot(df):
    """Побудова лінійної діаграми."""
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['page_views'], color='blue')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt

def draw_bar_plot(df):
    """Побудова стовпчикової діаграми для середніх переглядів по місяцях і роках."""
    df['year'] = df.index.year
    df['month'] = df.index.month
    
    monthly_avg = df.groupby(['year', 'month'])['page_views'].mean().unstack()
    
    plt.figure(figsize=(10, 6))
    monthly_avg.plot(kind='bar', stacked=False, figsize=(10, 6))
    plt.title('Average Page Views per Month (Yearly)')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title="Months", labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.tight_layout()
    return plt

def draw_box_plot(df):
    """Побудова коробкових діаграм для річних та місячних переглядів."""
    df['year'] = df.index.year
    df['month'] = df.index.month
    
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='page_views', data=df)
    plt.title('Year-wise Box Plot (Trend)')
    
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='page_views', data=df)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xticks(ticks=range(12), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.tight_layout()
    return plt
