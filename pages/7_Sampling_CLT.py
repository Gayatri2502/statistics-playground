import streamlit as st
import pandas as pd

from utils.sampling import SamplingEngine
from utils.sampling_business import recommendation
from utils.sampling_charts import histogram, population_chart

st.set_page_config(
    page_title="Sampling & CLT",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Sampling & Central Limit Theorem")

st.caption(
    "Can a small sample represent millions of customers?"
)

st.divider()

df = pd.read_csv(
    "datasets/customer_satisfaction.csv"
)

engine = SamplingEngine(
    df["SatisfactionScore"]
)

##########################################################

left, right = st.columns([1,2])

##########################################################

with left:

    st.subheader("Business Scenario")

    st.info("""

A company has 10 million customers.

Surveying everyone is impossible.

Can a sample of only a few customers tell the truth about the population?

Experiment with different sample sizes.

""")

    sample_size = st.slider(

        "Sample Size",

        5,

        len(df),

        10

    )

    simulations = st.slider(

        "Number of Samples",

        100,

        3000,

        500,

        step=100

    )

##########################################################

sample = engine.random_sample(sample_size)

sample_mean = engine.sample_mean(sample)

population_mean = engine.population_mean()

sample_means = engine.simulate_clt(
    sample_size,
    simulations
)

error = abs(
    sample_mean-population_mean
)

##########################################################

with right:

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Population Mean",
        f"{population_mean:.2f}"
    )

    c2.metric(
        "Sample Mean",
        f"{sample_mean:.2f}"
    )

    c3.metric(
        "Error",
        f"{error:.2f}"
    )

    c4.metric(
        "Sample Size",
        sample_size
    )

    graph1,graph2 = st.columns(2)

    with graph1:

        st.plotly_chart(

            population_chart(
                df["SatisfactionScore"]
            ),

            use_container_width=True

        )

    with graph2:

        st.plotly_chart(

            histogram(
                sample_means
            ),

            use_container_width=True

        )

##########################################################

st.divider()

left,right = st.columns(2)

with left:

    st.subheader("Business Insight")

    st.success(
        recommendation(error)
    )

with right:

    st.subheader("Central Limit Theorem")

    st.latex(r'''
\bar{X}
=
\frac{\sum X_i}{n}
''')

    st.markdown(f"""

### Population Mean

**{population_mean:.2f}**

---

### Sample Mean

**{sample_mean:.2f}**

---

### Absolute Error

**{error:.2f}**

---

### Why CLT Matters

As the sample size increases:

- Sample means become more stable.
- Their distribution approaches a normal distribution.
- Estimates become more reliable, even if the population is not perfectly normal.

### Real-World Applications

- Election Polling
- Customer Satisfaction Surveys
- Manufacturing Quality Control
- Medical Clinical Trials
- Market Research
- A/B Testing
- Machine Learning Model Evaluation

""")