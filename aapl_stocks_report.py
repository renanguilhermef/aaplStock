import plotly.graph_objects as go
import sys
from db import database 
from stockApi import stockData 

s = stockData.stock()
db = database.oracle() 
db.createTableAaplStocks()
db.insertDataAaplStocks(s.get_historical_data("AAPL")['data'])

df = db.sqlQueryDataFrame()
chart_scatter = [
    go.Scatter(x=df['STOCK_DATE'], y=df['BEST_STOCK_DAY'], name='Best stock day'),
    go.Scatter(x=df['STOCK_DATE'], y=df['WORST_STOCK_DAY'], name='Worst stock day')
]
fig = go.Figure(data=chart_scatter, layout=dict())

html = f'''
    <html>
        <head>
            <title>AAPL Stocks</title>
        </head>
        <body>
            <h1>AAPL stocks best/worst day</h1>
            {fig.to_html()}
            <h2>AAPL stocks history</h2>
            {df.to_html()}
        </body>
    </html>
    '''
with open('aapl_stocks_report.html', 'w') as f:
    f.write(html)

print ("Report generated: " + sys.path[0] + "/" + f.name)