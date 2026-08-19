import streamlit as st
import pandas as pd

from utils.conditional_probability import ConditionalProbability
from utils.conditional_business import recommendation
from utils.conditional_charts import spam_gauge, spam_pie

st.set_page_config(
    page_title="Conditional Probability",
    page_icon="📧",
    layout="wide"
)

st.title("📧 Conditional Probability Dashboard")

st.caption("Email Spam Detection using Conditional Probability")

st.divider()

df = pd.read_csv(
    "datasets/spam_detection.csv"
)

engine = ConditionalProbability(df)

left,right = st.columns([1,2])

# -------------------------------------------------------

with left:

    st.subheader("Email Features")

    free = st.selectbox(
        "Contains FREE",
        ["Yes","No"]
    )

    link = st.selectbox(
        "Contains LINK",
        ["Yes","No"]
    )

    money = st.selectbox(
        "Contains MONEY",
        ["Yes","No"]
    )

    sender = st.selectbox(
        "Known Sender",
        ["Yes","No"]
    )

# -------------------------------------------------------

prob = engine.spam_probability(
    free,
    link,
    money,
    sender
)

# -------------------------------------------------------

with right:

    k1,k2,k3 = st.columns(3)

    k1.metric(
        "Spam Probability",
        f"{prob*100:.1f}%"
    )

    k2.metric(
        "Spam Emails",
        len(df[df["Spam"]=="Yes"])
    )

    k3.metric(
        "Dataset Size",
        len(df)
    )

    c1,c2 = st.columns(2)

    with c1:
        st.plotly_chart(
            spam_gauge(prob),
            use_container_width=True
        )

    with c2:
        st.plotly_chart(
            spam_pie(df),
            use_container_width=True
        )

st.divider()

a,b = st.columns(2)

with a:

    st.subheader("Business Decision")

    st.success(
        recommendation(prob)
    )

with b:

    st.subheader("Conditional Probability")

    st.latex(
        r"P(A|B)=\frac{P(A\cap B)}{P(B)}"
    )

    st.markdown(f"""

Suppose

**A = Email is Spam**

**B = Contains FREE**

The dashboard updates the spam probability every time new evidence (FREE, LINK, MONEY, Known Sender) is selected.

Current Estimated Probability

# **{prob*100:.2f}%**

""")