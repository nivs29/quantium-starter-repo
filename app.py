import pandas as pd
from dash import Dash, html, dcc, Input, Output
from plotly.express import line

DATA_PATH = "./formatted_output.csv"

data = pd.read_csv(DATA_PATH)
data['date'] = pd.to_datetime(data['date'])
data = data.sort_values(by="date")

data['date_timestamp'] = data['date'].apply(lambda x: x.timestamp())

app = Dash(__name__)

header = html.H1("Pink Morsel Sales Visualizer", id="header")

region_filter = dcc.RadioItems(
    id='region-filter',
    options=[
        {'label': 'All', 'value': 'all'},
        {'label': 'North', 'value': 'north'},
        {'label': 'East', 'value': 'east'},
        {'label': 'South', 'value': 'south'},
        {'label': 'West', 'value': 'west'}
    ],
    value='all',
    className='dash-radioitems'
)

app.layout = html.Div(
    [
        header,
        region_filter,
        dcc.Graph(id="visualization")
    ]
)

@app.callback(
    Output('visualization', 'figure'),
    [Input('region-filter', 'value')]
)
def update_chart(selected_region):

    filtered_data = data
    if selected_region != 'all':
        filtered_data = data[data['region'] == selected_region]

    line_chart = line(
        filtered_data,
        x="date_timestamp",
        y="sales",
        title="Pink Morsel Sales Over Time",
        labels={"date_timestamp": "Date", "sales": "Sales"}
    )

    price_increase_date = pd.to_datetime('2021-01-15').timestamp()

    line_chart.add_vline(
        x=price_increase_date,
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase",
        annotation_position="top right"
    )

    return line_chart

if __name__ == '__main__':
    app.run_server(debug=True)







