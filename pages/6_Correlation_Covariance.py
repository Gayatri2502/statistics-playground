import streamlit as st
import pandas as pd

from utils.correlation import CorrelationEngine

from utils.correlation_business import recommendation

from utils.correlation_charts import *

st.set_page_config(

    page_title="Correlation",

    page_icon="📉",

    layout="wide"

)

st.title("📉 Correlation & Covariance Dashboard")

st.caption(
    "Discover relationships between variables before building Machine Learning models."
)

st.divider()

df = pd.read_csv(
    "datasets/advertising_sales.csv"
)

engine = CorrelationEngine(df)

############################################################

left,right = st.columns([1,2])

############################################################

with left:

    st.subheader("Business Scenario")

    st.info("""

Amazon wants to know whether advertisement spending affects product sales.

If correlation is high,

marketing investment may increase revenue.

""")

    st.subheader("Dataset")

    df = st.data_editor(

        df,

        use_container_width=True,

        height=420

    )

############################################################

cov = engine.covariance()

corr = engine.correlation()

############################################################

with right:

    c1,c2,c3 = st.columns(3)

    c1.metric(

        "Correlation",

        f"{corr:.3f}"

    )

    c2.metric(

        "Covariance",

        f"{cov:.2f}"

    )

    c3.metric(

        "Relationship",

        engine.strength()

    )

    graph1,graph2 = st.columns(2)

    with graph1:

        st.plotly_chart(

            scatter(df),

            use_container_width=True

        )

    with graph2:

        st.plotly_chart(

            line(df),

            use_container_width=True

        )

    st.plotly_chart(

        heatmap(df),

        use_container_width=True

    )

############################################################

st.divider()

col1,col2 = st.columns(2)

with col1:

    st.subheader("Business Insight")

    st.success(

        recommendation(corr)

    )

with col2:

    st.subheader("Mathematical Explanation")

    st.latex(r'''
Correlation=\frac{Cov(X,Y)}
{\sigma_X\sigma_Y}
''')

    st.markdown(f"""

### Covariance

**{cov:.2f}**

---

### Correlation

**{corr:.3f}**

---

### Interpretation

Correlation measures the **direction** and **strength** of the relationship.

Covariance measures how two variables move together.

### Correlation Scale

- +1 → Perfect Positive
- +0.7 → Strong Positive
- 0 → No Linear Relationship
- -0.7 → Strong Negative
- -1 → Perfect Negative

### Applications

- Feature Selection
- Stock Market Analysis
- Recommendation Systems
- Marketing Analytics
- Demand Forecasting
- Healthcare Analytics
- Machine Learning

""")