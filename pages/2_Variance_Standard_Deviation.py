import streamlit as st
import pandas as pd

from utils.variance import calculate_statistics
from utils.variance_charts import (
    line_chart,
    histogram,
    box_plot
)

from utils.risk import (
    risk_level,
    recommendation
)

st.set_page_config(
    page_title="Variance & Standard Deviation",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Variance & Standard Deviation Dashboard")

st.caption(
    "Understand why two investments with the same average can have completely different levels of risk."
)

st.divider()

df = pd.read_csv("datasets/fund_returns.csv")

left,right = st.columns([1,2])

####################################################

with left:

    st.subheader("Business Case")

    st.info("""

You are a Financial Analyst.

Two mutual funds generated nearly the same average annual return.

Which one should investors choose?

Explore the data and understand how variance and standard deviation measure investment risk.
""")

    edited_df = st.data_editor(
        df,
        use_container_width=True,
        height=420
    )

####################################################

fund = st.radio(
    "Select Fund",
    ["FundA","FundB"],
    horizontal=True
)

stats = calculate_statistics(
    edited_df[fund]
)

####################################################

with right:

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Mean",
        f"{stats['Mean']:.2f}%"
    )

    c2.metric(
        "Variance",
        f"{stats['Variance']:.2f}"
    )

    c3.metric(
        "Std Dev",
        f"{stats['Std Dev']:.2f}"
    )

    c4.metric(
        "Risk",
        risk_level(stats["Std Dev"])
    )

    st.divider()

    ch1,ch2 = st.columns(2)

    with ch1:

        st.plotly_chart(
            line_chart(edited_df),
            use_container_width=True
        )

    with ch2:

        st.plotly_chart(
            histogram(edited_df),
            use_container_width=True
        )

    st.plotly_chart(
        box_plot(edited_df),
        use_container_width=True
    )

####################################################

st.divider()

col1,col2 = st.columns(2)

with col1:

    st.subheader("Business Recommendation")

    st.success(
        recommendation(
            stats["Std Dev"]
        )
    )

with col2:

    st.subheader("Mathematical Interpretation")

    st.markdown(f"""

### Mean

Average Return

**{stats['Mean']:.2f}%**

---

### Variance

Measures how far returns spread around the mean.

**{stats['Variance']:.2f}**

---

### Standard Deviation

Average distance from the mean.

**{stats['Std Dev']:.2f}**

---

### Interpretation

- Low Variance → Stable Returns

- High Variance → Risky Investment

- Mean alone cannot measure investment risk.

""")