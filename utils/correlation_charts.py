import plotly.express as px


def scatter(df):

    fig = px.scatter(

        df,

        x="Advertisement",

        y="Sales",

        title="Advertisement vs Sales"

    )

    fig.update_layout(

        template="plotly_dark",

        height=450

    )

    return fig


def line(df):

    fig = px.line(

        df,

        x="Month",

        y=["Advertisement","Sales"],

        markers=True,

        title="Monthly Trend"

    )

    fig.update_layout(

        template="plotly_dark",

        height=450

    )

    return fig


def heatmap(df):

    corr = df[
        ["Advertisement","Sales"]
    ].corr()

    fig = px.imshow(

        corr,

        text_auto=True,

        color_continuous_scale="RdBu_r",

        title="Correlation Matrix"

    )

    fig.update_layout(height=400)

    return fig