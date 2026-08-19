import plotly.express as px


def line_chart(df):

    fig = px.line(
        df,
        x="Month",
        y=["FundA","FundB"],
        markers=True,
        title="Monthly Returns Comparison"
    )

    return fig


def histogram(df):

    fig = px.histogram(
        df,
        x=["FundA","FundB"],
        barmode="overlay",
        title="Distribution of Returns"
    )

    return fig


def box_plot(df):

    fig = px.box(
        df,
        y=["FundA","FundB"],
        points="all",
        title="Spread of Returns"
    )

    return fig