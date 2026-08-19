import streamlit as st

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Statistics Playground",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------
# Custom CSS
# -------------------------------------------------------

st.markdown("""
<style>

.main-title{
    font-size:48px;
    font-weight:700;
    color:#4F8BF9;
}

.subtitle{
    font-size:20px;
    color:#BBBBBB;
}

.card{
    background-color:#111827;
    padding:20px;
    border-radius:15px;
    border:1px solid #2E2E2E;
    margin-bottom:15px;
}

.card h3{
    color:#4F8BF9;
}

.card p{
    color:#DDDDDD;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# Header
# -------------------------------------------------------

st.markdown(
"""
<div class="main-title">
📊 Statistics Playground
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="subtitle">
Learn Statistics by Solving Real Business Problems
through Interactive Dashboards.
</div>
""",
unsafe_allow_html=True
)

st.divider()

# -------------------------------------------------------
# Overview
# -------------------------------------------------------

st.header("🎯 Project Overview")

st.write("""
Statistics Playground is an interactive learning platform designed to bridge the gap between
mathematical concepts and real-world business analytics.

Instead of memorizing formulas, each module presents a realistic business scenario,
allowing you to explore datasets, visualize insights, interact with graphs,
and understand why each statistical technique is used.

Every dashboard is built using **Python**, **Streamlit**, **Pandas**, **NumPy**, **SciPy**, and **Plotly**.
""")

st.divider()

# -------------------------------------------------------
# Modules
# -------------------------------------------------------

st.header("📚 Learning Modules")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
<div class="card">

<h3>📊 Module 1 — Descriptive Statistics</h3>

<p>
Understand your dataset before making decisions.

Topics Covered

• Mean

• Median

• Mode

• Range

• Variance

• Standard Deviation

Business Case

Amazon Delivery Analysis
</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="card">

<h3>📈 Module 3 — Probability</h3>

<p>

Predict customer purchases using probability.

Topics

• Sample Space

• Events

• Addition Rule

• Multiplication Rule

Business Case

Marketing Campaign Prediction

</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="card">

<h3>📉 Module 5 — Normal Distribution</h3>

<p>

Learn why the Bell Curve appears everywhere.

Topics

• Mean

• Standard Deviation

• PDF

• CDF

Business Case

Human Height Distribution

</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="card">

<h3>🎯 Module 7 — Sampling & CLT</h3>

<p>

Discover how a small sample can represent millions.

Topics

• Random Sampling

• Population

• Sample

• Central Limit Theorem

Business Case

Customer Satisfaction Survey

</p>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="card">

<h3>📏 Module 2 — Variance & Standard Deviation</h3>

<p>

Measure uncertainty and data spread.

Topics

• Variance

• Standard Deviation

• Dispersion

Business Case

Stock Price Volatility

</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="card">

<h3>📧 Module 4 — Conditional Probability</h3>

<p>

Update probabilities using new evidence.

Topics

• Conditional Probability

• Bayes' Theorem

Business Case

Spam Email Detection

</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="card">

<h3>📊 Module 6 — Correlation & Covariance</h3>

<p>

Find relationships between variables.

Topics

• Correlation

• Covariance

• Positive/Negative Relationship

Business Case

Advertisement vs Sales

</p>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="card">

<h3>🧠 Module 8 — Scenario-Based Analytics</h3>

<p>

Test your statistical thinking using realistic business problems.

Topics

• Business Decision Making

• Statistical Reasoning

• Interactive Quiz

</p>

</div>
""", unsafe_allow_html=True)

st.divider()

# -------------------------------------------------------
# Technologies
# -------------------------------------------------------

st.header("🛠 Technology Stack")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Language", "Python")
c2.metric("Framework", "Streamlit")
c3.metric("Visualization", "Plotly")
c4.metric("Libraries", "NumPy • Pandas • SciPy")

st.divider()

# -------------------------------------------------------
# Learning Outcome
# -------------------------------------------------------

st.header("🎓 What You Will Learn")

st.success("""
✔ Understand raw data before prediction

✔ Measure spread using Variance & Standard Deviation

✔ Predict events using Probability

✔ Update beliefs using Conditional Probability & Bayes' Theorem

✔ Understand the Bell Curve and Normal Distribution

✔ Discover relationships using Correlation & Covariance

✔ Learn why Sampling works using the Central Limit Theorem

✔ Apply statistical thinking to real-world business problems
""")

st.divider()

# -------------------------------------------------------
# Footer
# -------------------------------------------------------

st.info("""
👈 **Select any module from the left sidebar to begin exploring Statistics through interactive dashboards.**

Each module is independent, hands-on, and based on a real-world business scenario to help you build intuition and practical skills.
""")