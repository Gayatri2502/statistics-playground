import streamlit as st

from utils.scenarios import SCENARIOS
from utils.score_engine import calculate_score

st.set_page_config(
    page_title="Statistics Decision Lab",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Statistics Decision Lab")

st.caption(
    "Solve real-world business problems using statistical thinking."
)

st.divider()

st.markdown("""
## Final Challenge

You are now a Data Analyst.

For each business scenario:

- Identify the correct concept
- Make the correct business decision
- Apply statistical reasoning

Let's test your understanding.
""")

user_answers = []

for i, scenario in enumerate(SCENARIOS):

    with st.container(border=True):

        st.subheader(
            f"Scenario {i+1}: {scenario['title']}"
        )

        st.write(
            scenario["question"]
        )

        answer = st.radio(

            "Choose your answer",

            scenario["options"],

            key=f"q{i}"

        )

        user_answers.append(answer)

if st.button(
    "🚀 Submit Assessment",
    use_container_width=True
):

    score = calculate_score(
        user_answers,
        SCENARIOS
    )

    percentage = (
        score / len(SCENARIOS)
    ) * 100

    st.divider()

    st.header("📊 Assessment Result")

    c1,c2,c3 = st.columns(3)

    c1.metric(
        "Score",
        f"{score}/{len(SCENARIOS)}"
    )

    c2.metric(
        "Percentage",
        f"{percentage:.1f}%"
    )

    if percentage >= 80:
        level = "Advanced"

    elif percentage >= 60:
        level = "Intermediate"

    else:
        level = "Beginner"

    c3.metric(
        "Level",
        level
    )

    st.divider()

    st.subheader(
        "Detailed Feedback"
    )

    for i, scenario in enumerate(
        SCENARIOS
    ):

        if (
            user_answers[i]
            ==
            scenario["answer"]
        ):

            st.success(
                f"✅ {scenario['title']} | Correct"
            )

        else:

            st.error(
                f"❌ {scenario['title']} | Correct Answer: {scenario['answer']}"
            )

    if percentage >= 80:

        st.balloons()

        st.success("""

Excellent.

You can confidently explain:

✔ Descriptive Statistics

✔ Variance & Standard Deviation

✔ Probability

✔ Conditional Probability

✔ Normal Distribution

✔ Correlation

✔ Sampling & CLT

This demonstrates strong foundational statistical reasoning.
""")