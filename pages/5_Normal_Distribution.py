import streamlit as st
import pandas as pd

from utils.normal_distribution import NormalDistribution

from utils.normal_charts import (
    bell_curve,
    histogram,
    probability_gauge
)

from utils.normal_business import insight


st.set_page_config(
    page_title="Normal Distribution",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Normal Distribution Dashboard")

st.caption(
    "Understanding the Bell Curve using Human Heights"
)

st.divider()

df = pd.read_csv(
    "datasets/heights.csv"
)

distribution = NormalDistribution(
    df["Height"]
)

#########################################################

left,right = st.columns([1,2])

#########################################################

with left:

    st.subheader(
        "Business Scenario"
    )

    st.info("""

An apparel company wants to manufacture T-Shirts.

Question:

What percentage of customers have heights between two values?

The answer comes from the Normal Distribution.

""")

    lower = st.slider(

        "Minimum Height",

        140,

        200,

        160

    )

    upper = st.slider(

        "Maximum Height",

        140,

        200,

        175

    )

#########################################################

prob = distribution.probability_between(
    lower,
    upper
)

#########################################################

with right:

    c1,c2,c3 = st.columns(3)

    c1.metric(
        "Mean",
        f"{distribution.mean:.2f} cm"
    )

    c2.metric(
        "Std Dev",
        f"{distribution.std:.2f}"
    )

    c3.metric(
        "Probability",
        f"{prob*100:.2f}%"
    )

    ch1,ch2 = st.columns(2)

    with ch1:

        st.plotly_chart(

            bell_curve(
                distribution.mean,
                distribution.std
            ),

            use_container_width=True

        )

    with ch2:

        st.plotly_chart(

            histogram(
                df["Height"]
            ),

            use_container_width=True

        )

    st.plotly_chart(

        probability_gauge(
            prob
        ),

        use_container_width=True

    )

#########################################################

st.divider()

a,b = st.columns(2)

with a:

    st.subheader(
        "Business Interpretation"
    )

    st.success(
        insight(prob)
    )

with b:

    st.subheader(
        "Mathematical Proof"
    )

    st.latex(r'''
f(x)=\frac{1}{\sigma\sqrt{2\pi}}
e^{-\frac{(x-\mu)^2}{2\sigma^2}}
''')

    st.markdown(f"""

### Dataset Statistics

Mean (μ)

**{distribution.mean:.2f}**

---

Standard Deviation (σ)

**{distribution.std:.2f}**

---

Selected Range

**{lower} cm**

to

**{upper} cm**

---

Probability

### **{prob*100:.2f}%**

This means approximately **{prob*100:.1f}%** of people are expected to have heights within this interval if the data follows a normal distribution.

### Real World Applications

- Human Heights
- IQ Scores
- Manufacturing Quality Control
- Measurement Errors
- Stock Returns (Approximation)
- Machine Learning Assumptions
- Six Sigma Process Improvement

""")