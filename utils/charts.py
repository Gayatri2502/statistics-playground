import plotly.express as px
import plotly.graph_objects as go


def histogram(df):

    fig = px.histogram(
        df,
        x="DeliveryDays",
        nbins=20,
        title="Delivery Time Distribution"
    )

    fig.update_layout(height=450)

    return fig


def boxplot(df):

    fig = px.box(
        df,
        y="DeliveryDays",
        points="all",
        title="Box Plot"
    )

    fig.update_layout(height=450)

    return fig


def violin(df):

    fig = px.violin(
        df,
        y="DeliveryDays",
        box=True,
        points="all"
    )

    fig.update_layout(height=450)

    return fig