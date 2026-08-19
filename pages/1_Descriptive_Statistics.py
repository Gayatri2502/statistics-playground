import streamlit as st
import pandas as pd

from utils.statistics import descriptive_statistics
from utils.charts import histogram, boxplot, violin
from utils.business_insights import generate_insight

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------

st.set_page_config(
    page_title="Statistics Playground",
    page_icon="📊",
    layout="wide"
)

# ----------------------------------------------------------
# HEADER
# ----------------------------------------------------------

st.title("📊 Descriptive Statistics Dashboard")
st.caption("Understand your data before making predictions")

st.divider()

# ----------------------------------------------------------
# LOAD DATA
# ----------------------------------------------------------

df = pd.read_csv("datasets/amazon_delivery.csv")

uploaded = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded:
    df = pd.read_csv(uploaded)

# ----------------------------------------------------------
# DASHBOARD LAYOUT
# ----------------------------------------------------------

left, right = st.columns([1,2], gap="large")

# ==========================================================
# LEFT PANEL
# ==========================================================

with left:

    st.subheader("📦 Business Problem")

    st.info("""
Amazon wants to understand its delivery performance.

One delayed shipment can distort the average.

Should the company report the **Mean** or the **Median**?

Modify the data below and observe how the statistics change.
""")

    st.subheader("📁 Delivery Dataset")

    edited_df = st.data_editor(
        df,
        use_container_width=True,
        num_rows="dynamic",
        height=420
    )

# ==========================================================
# CALCULATE STATS
# ==========================================================

stats = descriptive_statistics(
    edited_df["DeliveryDays"]
)

# ==========================================================
# RIGHT PANEL
# ==========================================================

with right:

    # ------------------------------------------------------
    # KPI CARDS
    # ------------------------------------------------------

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("📈 Mean",f"{stats['Mean']:.2f}")

    c2.metric("📍 Median",f"{stats['Median']:.2f}")

    c3.metric("📊 Mode",stats["Mode"])

    c4.metric("📏 Std Dev",f"{stats['Standard Deviation']:.2f}")

    c5,c6,c7,c8 = st.columns(4)

    c5.metric("Variance",f"{stats['Variance']:.2f}")

    c6.metric("Range",stats["Range"])

    c7.metric("Minimum",stats["Minimum"])

    c8.metric("Maximum",stats["Maximum"])

    st.divider()

    # ------------------------------------------------------
    # CHARTS
    # ------------------------------------------------------

    chart1, chart2 = st.columns(2)

    with chart1:
        st.plotly_chart(
            histogram(edited_df),
            use_container_width=True
        )

    with chart2:
        st.plotly_chart(
            boxplot(edited_df),
            use_container_width=True
        )

    st.plotly_chart(
        violin(edited_df),
        use_container_width=True
    )

# ==========================================================
# BOTTOM SECTION
# ==========================================================

st.divider()

left,right = st.columns([1,1])

# ----------------------------------------------------------
# BUSINESS INSIGHT
# ----------------------------------------------------------

with left:

    st.subheader("💼 Business Insight")

    st.success(
        generate_insight(stats)
    )

# ----------------------------------------------------------
# MATHEMATICAL SUMMARY
# ----------------------------------------------------------

with right:

    st.subheader("🧮 Statistical Summary")

    st.markdown(f"""
### Mean

\[
\\frac{{\sum X}}{{N}}
=
{edited_df['DeliveryDays'].sum()}
/
{len(edited_df)}
=
{stats['Mean']:.2f}
\]

---

### Median

Middle value after sorting

**{stats['Median']}**

---

### Mode

Most frequently occurring value

**{stats['Mode']}**

---

### Standard Deviation

Measures how spread out the delivery times are.

**{stats['Standard Deviation']:.2f}**

---

### Business Interpretation

- Mean changes when an outlier is introduced.
- Median remains stable.
- Standard deviation increases when variability increases.
- Large variance indicates inconsistent delivery performance.
""")