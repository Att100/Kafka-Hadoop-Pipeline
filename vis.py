import dash
from dash import dcc, html
from dash.dependencies import Output, Input
from jmxquery import JMXConnection, JMXQuery
import plotly.graph_objs as go
import numpy as np
from threading import Lock
import random
import time
from datetime import datetime

lock = Lock()

app = dash.Dash(__name__)


# global data
brokers = [f'Broker {i+1}' for i in range(3)]
data = {
    'data_bytes_in': {k: {'x': [], 'y': []} for k in brokers},
    'data_bytes_out': {k: {'x': [], 'y': []} for k in brokers},
    'cpu': {k: {'x': [], 'y': []} for k in brokers}
}

kafka_broker_ports = {
    'Broker 1': 19092,
    'Broker 2': 19093,
    'Broker 3': 19094
}
kafka_jmx_connections = {k:JMXConnection("service:jmx:rmi:///jndi/rmi://localhost:{}/jmxrmi".format(p)) for k, p in kafka_broker_ports.items()}
max_points = 60


app.layout = html.Div([
    html.H1('Brokers Metrics', style={'textAlign': 'center'}),
    # Bytes in per sec
    html.Div([
        dcc.Graph(id='live-graph-1', style={'display': 'inline-block', 'width': '33%'}),
        dcc.Graph(id='live-graph-2', style={'display': 'inline-block', 'width': '33%'}),
        dcc.Graph(id='live-graph-3', style={'display': 'inline-block', 'width': '33%'}),
        
    ]),
    # Bytes out per sec
    html.Div([
        dcc.Graph(id='live-graph-4', style={'display': 'inline-block', 'width': '33%'}),
        dcc.Graph(id='live-graph-5', style={'display': 'inline-block', 'width': '33%'}),
        dcc.Graph(id='live-graph-6', style={'display': 'inline-block', 'width': '33%'}),
    ]),
    # CPU utilization rate
    # html.Div([
    #     dcc.Graph(id='live-graph-7', style={'display': 'inline-block', 'width': '33%'}),
    #     dcc.Graph(id='live-graph-8', style={'display': 'inline-block', 'width': '33%'}),
    #     dcc.Graph(id='live-graph-9', style={'display': 'inline-block', 'width': '33%'}),
        
    # ]),
    dcc.Interval(
        id='graph-update',
        interval=1000,  # ms
        n_intervals=0
    ),
])


def update_graph(
    n, broker_id, color="0, 0, 255", dt_key='data_bytes_in',
    query_text="kafka.server:type=BrokerTopicMetrics,name=BytesInPerSec",
    query_attr_key="OneMinuteRate",
    subtitle="Bytes In per Second (One Minute)",
    ylabel="Bytes/s"):
    
    x_new = datetime.now()
    metrics = kafka_jmx_connections[broker_id].query([JMXQuery(query_text, attributeKey=query_attr_key)])
    # for metric in metrics:
    #     print(f"{metric.to_query_string()}={metric.value}")
    try:
        y_new = float(metrics[0].value)
    except:
        print(metrics)
        raise Exception()

    with lock:
        data[dt_key][broker_id]['x'].append(x_new)
        data[dt_key][broker_id]['y'].append(y_new)
        
        data[dt_key][broker_id]['x'] = data[dt_key][broker_id]['x'][-max_points:]
        data[dt_key][broker_id]['y'] = data[dt_key][broker_id]['y'][-max_points:]
        
        trace = go.Scatter(
            x=data[dt_key][broker_id]['x'],
            y=data[dt_key][broker_id]['y'],
            name=f'{broker_id} Data',
            mode='lines+markers',
            line=dict(color='rgba({}, 0.5)'.format(color)),
            fill='tozeroy',
            fillcolor='rgba({}, 0.2)'.format(color)
        )

        layout = go.Layout(
            title=f'{broker_id}: {subtitle}',
            xaxis=dict(title='Time'),
            yaxis=dict(title=ylabel),
            margin={'l': 50, 'r': 30, 't': 50, 'b': 50}, 
            height=300
        )

        return {'data': [trace], 'layout': layout}

# Bytes in per sec
@app.callback(Output('live-graph-1', 'figure'), [Input('graph-update', 'n_intervals')])
def update_graph_1(n):
    return update_graph(
        n, 'Broker 1', "0, 0, 255", 'data_bytes_in',
        query_text="kafka.server:type=BrokerTopicMetrics,name=BytesInPerSec",
        query_attr_key="OneMinuteRate",
        subtitle="Bytes In per Second (One Minute)",
        ylabel="Bytes/s")

@app.callback(Output('live-graph-2', 'figure'), [Input('graph-update', 'n_intervals')])
def update_graph_2(n):
    return update_graph(
        n, 'Broker 2', "0, 0, 255", 'data_bytes_in',
        query_text="kafka.server:type=BrokerTopicMetrics,name=BytesInPerSec",
        query_attr_key="OneMinuteRate",
        subtitle="Bytes In per Second (One Minute)",
        ylabel="Bytes/s")

@app.callback(Output('live-graph-3', 'figure'), [Input('graph-update', 'n_intervals')])
def update_graph_3(n):
    return update_graph(
        n, 'Broker 3', "0, 0, 255", 'data_bytes_in',
        query_text="kafka.server:type=BrokerTopicMetrics,name=BytesInPerSec",
        query_attr_key="OneMinuteRate",
        subtitle="Bytes In per Second (One Minute)",
        ylabel="Bytes/s")
    
# Bytes out per sec
@app.callback(Output('live-graph-4', 'figure'), [Input('graph-update', 'n_intervals')])
def update_graph_4(n):
    return update_graph(
        n, 'Broker 1', "0, 255, 0", 'data_bytes_out',
        query_text="kafka.server:type=BrokerTopicMetrics,name=BytesOutPerSec",
        query_attr_key="OneMinuteRate",
        subtitle="Bytes Out per Second (One Minute)",
        ylabel="Bytes/s")

@app.callback(Output('live-graph-5', 'figure'), [Input('graph-update', 'n_intervals')])
def update_graph_5(n):
    return update_graph(
        n, 'Broker 2', "0, 255, 0", 'data_bytes_out',
        query_text="kafka.server:type=BrokerTopicMetrics,name=BytesOutPerSec",
        query_attr_key="OneMinuteRate",
        subtitle="Bytes Out per Second (One Minute)",
        ylabel="Bytes/s")

@app.callback(Output('live-graph-6', 'figure'), [Input('graph-update', 'n_intervals')])
def update_graph_6(n):
    return update_graph(
        n, 'Broker 3', "0, 255, 0", 'data_bytes_out',
        query_text="kafka.server:type=BrokerTopicMetrics,name=BytesOutPerSec",
        query_attr_key="OneMinuteRate",
        subtitle="Bytes Out per Second (One Minute)",
        ylabel="Bytes/s")

# CPU utilization rate
# @app.callback(Output('live-graph-7', 'figure'), [Input('graph-update', 'n_intervals')])
# def update_graph_7(n):
#     return update_graph(
#         n, 'Broker 1', "255, 0, 0", 'cpu',
#         query_text="java.lang:type=OperatingSystem",
#         query_attr_key="SystemCpuLoad",
#         subtitle="CPU Utilization",
#         ylabel="Percentage")

# @app.callback(Output('live-graph-8', 'figure'), [Input('graph-update', 'n_intervals')])
# def update_graph_8(n):
#     return update_graph(
#         n, 'Broker 2', "255, 0, 0", 'cpu',
#         query_text="java.lang:type=OperatingSystem",
#         query_attr_key="SystemCpuLoad",
#         subtitle="CPU Utilization",
#         ylabel="Percentage")

# @app.callback(Output('live-graph-9', 'figure'), [Input('graph-update', 'n_intervals')])
# def update_graph_9(n):
#     return update_graph(
#         n, 'Broker 3', "255, 0, 0", 'cpu',
#         query_text="java.lang:type=OperatingSystem",
#         query_attr_key="SystemCpuLoad",
#         subtitle="CPU Utilization",
#         ylabel="Percentage")



if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")


