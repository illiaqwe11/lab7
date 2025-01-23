import pandas as pd
from time_series_visualizer import *

df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

df_cleaned = clean_data(df)

line_fig = draw_line_plot(df_cleaned)
line_fig.savefig('line_plot.png')  

bar_fig = draw_bar_plot(df_cleaned)
bar_fig.savefig('bar_plot.png')  

box_fig = draw_box_plot(df_cleaned)
box_fig.savefig('box_plot.png')  
