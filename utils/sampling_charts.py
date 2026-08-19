import plotly.express as px


def histogram(sample_means):

    fig = px.histogram(

        x=sample_means,

        nbins=30,

        title="Distribution of Sample Means"

    )

    fig.update_layout(

        template="plotly_dark",

        height=420

    )

    return fig


def population_chart(population):

    fig = px.histogram(

        x=population,

        nbins=15,

        title="Population Distribution"

    )

    fig.update_layout(

        template="plotly_dark",

        height=420

    )

    return fig