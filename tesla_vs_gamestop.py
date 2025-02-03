#%%

# Comparativo entre açoes da Tesla e Gamestop

import pandas as pd #manipular dados
import requests #fazer requisições HTTP
from bs4 import BeautifulSoup #parsear HTML
import yfinance as yf #baixar dados do Yahoo Finance

# %%
# criando ticker para a Tesla e Gamestop

tesla = yf.Ticker('TSLA')
game = yf.Ticker('GME')

#%%
## função para criar graficos

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

# %%
## Baixando dados históricos
tesla_data = tesla.history(period='max')
game_data = game.history(period='max')


# %%
tesla_data.reset_index(inplace=True)
game_data.reset_index(inplace=True)

# %%

html_data_tesla = requests.get('https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue').text
html_data_game = requests.get('https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue').text

#%%
soup_tesla = BeautifulSoup(html_data_tesla, 'html.parser')
# %%
