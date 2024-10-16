import pandas as pd
from dash import Dash, html, dcc
from plotly.express import line

DATA_PATH = "./formatted_output.csv"

data = pd.read_csv(DATA_PATH)
data['date'] = pd.to_datetime(data['date'])  # Ensure 'date' is a datetime object
data = data.sort_values(by="date")

app = Dash(__name__)

line_chart = line(
    data,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Sales"},  # Axis labels
)

price_increase_date = pd.to_datetime('2021-01-15')  # Ensure it's a datetime object


price_increase_date_timestamp = price_increase_date.timestamp()  # Convert to a timestamp


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



