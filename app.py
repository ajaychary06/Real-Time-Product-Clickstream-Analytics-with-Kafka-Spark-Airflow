from flask import Flask, render_template
import pandas as pd
import glob
import plotly.graph_objs as go
import plotly.io as pio
import os
import time

app = Flask(__name__)

last_loaded_time = 0
cached_df = pd.DataFrame()

def load_parquet_data():
    global last_loaded_time, cached_df
    current_time = time.time()
    
    # Reload data only every 10 seconds
    if current_time - last_loaded_time < 10 and not cached_df.empty:
        return cached_df

    files = glob.glob("/home/ajaychary06/product_pipeline_output_parquet/batch_*/part-*.parquet")
    if not files:
        return pd.DataFrame()

    cached_df = pd.concat([pd.read_parquet(f) for f in files])
    last_loaded_time = current_time
    return cached_df

@app.route("/")
def dashboard():
    df = load_parquet_data()
    if df.empty:
        return "No data available."

    bar_data = df.groupby("product")["count"].sum().reset_index()
    bar_chart = go.Figure([go.Bar(x=bar_data["product"], y=bar_data["count"])])
    bar_div = pio.to_html(bar_chart, full_html=False)

    line_data = df.groupby("start_time")["count"].sum().reset_index()
    line_chart = go.Figure([go.Scatter(x=line_data["start_time"], y=line_data["count"], mode="lines+markers")])
    line_div = pio.to_html(line_chart, full_html=False)

    return render_template("index.html", bar_plot=bar_div, line_plot=line_div)

if __name__ == "__main__":
    app.run(debug=True)

