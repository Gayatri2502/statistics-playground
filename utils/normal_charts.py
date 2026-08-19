import numpy as np
import plotly.graph_objects as go
from scipy.stats import norm


def bell_curve(mean, std):

    x = np.linspace(
        mean-4*std,
        mean+4*std,
        500
    )

    y = norm.pdf(
        x,
        mean,
        std
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            fill="tozeroy",
            name="Normal Distribution"
        )
    )

    fig.update_layout(
        title="Bell Curve",
        template="plotly_dark",
        height=420
    )

    return fig


def histogram(data):

    fig = go.Figure()

    fig.add_histogram(
        x=data,
        histnorm="probability density"
    )

    fig.update_layout(
        title="Height Distribution",
        template="plotly_dark",
        height=420
    )

    return fig


def probability_gauge(prob):

    fig = go.Figure(
        go.Indicator(

            mode="gauge+number",

            value=prob*100,

            number={"suffix":"%"},

            title={"text":"Probability"},

            gauge={

                "axis":{"range":[0,100]},

                "bar":{"color":"royalblue"}

            }

        )
    )

    fig.update_layout(height=350)

    return fig