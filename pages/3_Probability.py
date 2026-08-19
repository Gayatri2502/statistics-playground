import streamlit as st
import pandas as pd

from utils.probability import ProbabilityEngine
from utils.probability_business import recommendation
from utils.probability_charts import *

st.set_page_config(
    page_title="Probability",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Customer Purchase Probability Dashboard")

st.caption(
    "Predict customer behaviour using Probability."
)

st.divider()

df = pd.read_csv(
    "datasets/customer_probability.csv"
)

engine = ProbabilityEngine(df)

########################################################

left,right = st.columns(
    [1,2]
)

########################################################

with left:

    st.subheader(
        "Business Scenario"
    )

    st.info("""

Marketing budget is limited.

Not every customer should receive coupons.

Use Probability to predict which customers are more likely to purchase.

""")

    st.subheader(
        "Customer Simulator"
    )

    visited = st.selectbox(
        "Visited Website",
        ["Yes","No"]
    )

    clicked = st.selectbox(
        "Clicked Advertisement",
        ["Yes","No"]
    )

    returning = st.selectbox(
        "Returning Customer",
        ["Yes","No"]
    )

    weekend = st.selectbox(
        "Weekend",
        ["Yes","No"]
    )

    coupon = st.selectbox(
        "Coupon Sent",
        ["Yes","No"]
    )

########################################################

prob = engine.purchase_probability(
    visited,
    clicked,
    returning,
    weekend,
    coupon
)

########################################################

with right:

    c1,c2,c3 = st.columns(3)

    c1.metric(
        "Purchase Probability",
        f"{prob*100:.1f}%"
    )

    c2.metric(
        "Purchase",
        len(df[df["Purchased"]=="Yes"])
    )

    c3.metric(
        "Customers",
        len(df)
    )

    col1,col2 = st.columns(2)

    with col1:

        st.plotly_chart(
            probability_gauge(prob),
            use_container_width=True
        )

    with col2:

        st.plotly_chart(
            purchase_pie(df),
            use_container_width=True
        )

    st.plotly_chart(
        feature_bar(df),
        use_container_width=True
    )

########################################################

st.divider()

left,right = st.columns(2)

with left:

    st.subheader(
        "Business Recommendation"
    )

    st.success(
        recommendation(prob)
    )

with right:

    st.subheader(
        "Mathematical Proof"
    )

    st.latex(r"P(A)=\frac{Successful\ Outcomes}{Total\ Outcomes}")

    st.markdown(f"""

Successful Outcomes = **{len(df[df['Purchased']=='Yes'])}**

Total Customers = **{len(df)}**

Purchase Probability

### **{prob*100:.2f}%**

""")