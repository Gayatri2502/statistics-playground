import plotly.graph_objects as go
import plotly.express as px


def spam_gauge(prob):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=prob*100,
            number={"suffix":"%"},
            title={"text":"Spam Probability"},
            gauge={
                "axis":{"range":[0,100]},
                "bar":{"color":"crimson"},
                "steps":[
                    {"range":[0,40],"color":"lightgreen"},
                    {"range":[40,70],"color":"gold"},
                    {"range":[70,100],"color":"salmon"}
                ]
            }
        )
    )

    fig.update_layout(height=330)

    return fig


def spam_pie(df):

    return px.pie(
        df,
        names="Spam",
        hole=.55,
        title="Spam vs Genuine Emails"
    )