import plotly.graph_objects as go
import plotly.express as px


def probability_gauge(prob):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=prob*100,

            number={
                "suffix":"%"
            },

            title={
                "text":"Purchase Probability"
            },

            gauge={
                "axis":{
                    "range":[0,100]
                },

                "bar":{
                    "color":"royalblue"
                },

                "steps":[
                    {"range":[0,30],"color":"#ffcccc"},
                    {"range":[30,60],"color":"#ffe699"},
                    {"range":[60,100],"color":"#ccffcc"},
                ]
            }
        )
    )

    fig.update_layout(height=350)

    return fig


def purchase_pie(df):

    fig = px.pie(
        df,
        names="Purchased",
        hole=.5,
        title="Purchased vs Not Purchased"
    )

    return fig


def feature_bar(df):

    yes = []

    cols = [
        "VisitedWebsite",
        "ClickedAd",
        "ReturningCustomer",
        "Weekend",
        "CouponSent"
    ]

    for c in cols:

        yes.append(
            len(df[df[c]=="Yes"])
        )

    fig = px.bar(
        x=cols,
        y=yes,
        title="Customer Behaviour"
    )

    return fig