import pandas as pd
from dash import Dash, html, dcc
from plotly.express import line

data_file = "./formatted_output.csv"

data = pd.read_csv(data_file)
data['date'] = pd.to_datetime(data['date'])
data = data.sort_values(by="date")

app = Dash(__name__)

line_chart = line(
    data,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Sales"},
)
price_increase_date = pd.to_datetime('2021-01-15')
price_increase_date_timestamp = price_increase_date.timestamp()

if price_increase_date in data['date'].values:
    line_chart.add_vline(
        x=price_increase_date_timestamp,
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase",
        annotation_position="top right"
    )
else:
    print(f"Price increase date {price_increase_date} not found in the data.")

header = html.H1(
    "Pink Morsel Sales Visualizer",
    id="header"
)

app.layout = html.Div(
    [
        header,
        dcc.Graph(
            id="visualization",
            figure=line_chart
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)


