
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Lab 10 | Framing the Data Story",
    layout="wide"
)

# Updated fictional data
# Data storytelling changed from 2.4 to 3.8
skills = [
    "Data storytelling",
    "Python",
    "Chart selection",
    "Color and labels",
    "Data cleaning"
]

ratings = [3.8, 3.0, 3.2, 3.7, 4.1]

df = pd.DataFrame({
    "Skill": skills,
    "Average rating": ratings
})

# Identify the lowest-rated skill automatically
lowest_index = df["Average rating"].idxmin()
lowest_skill = df.loc[lowest_index, "Skill"]
lowest_rating = df.loc[lowest_index, "Average rating"]

# Page heading
st.title("Planning a Workshop Around Students' Needs")

st.write(
    "**Audience:** Workshop instructors planning data visualization training."
)

st.write(
    "**Purpose:** Identify which skills need more attention "
    "when planning the next workshop."
)

st.info(
    f"**Key takeaway:** {lowest_skill} received the lowest average "
    f"self-rating ({lowest_rating:.1f}/5). "
    "Instructors should prioritise this skill in the next workshop."
)

# Display the chart
fig, ax = plt.subplots(figsize=(10, 5))

# Highlight only the lowest-rated skill
bar_colors = [
    "#E07A3F" if i == lowest_index else "#4C78A8"
    for i in range(len(skills))
]

bars = ax.barh(
    df["Skill"],
    df["Average rating"],
    color=bar_colors
)

# Axis formatting
ax.set_xlim(0, 5)
ax.set_xticks(range(0, 6))

ax.set_xlabel(
    "Average self-rating (1 = Beginner, 5 = Confident)"
)

ax.set_title(
    f"{lowest_skill} has the lowest average self-rating",
    fontsize=14,
    fontweight="bold"
)

ax.invert_yaxis()

# Grid and chart appearance
ax.grid(
    axis="x",
    color="#DDDDDD",
    linewidth=0.7
)

ax.set_axisbelow(True)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add numerical labels
for bar, value in zip(bars, ratings):
    ax.text(
        value + 0.05,
        bar.get_y() + bar.get_height() / 2,
        f"{value:.1f}",
        va="center",
        fontsize=10
    )

fig.tight_layout()

st.pyplot(fig, clear_figure=True)

# Additional explanation
st.subheader("What does this tell us?")

st.write(
    f"{lowest_skill} received a score of {lowest_rating:.1f} out of 5, "
    "making it the area with the greatest need for improvement. "
    "Workshop instructors can use this information to allocate "
    "more time to Python exercises and practical demonstrations."
)

# Data table
with st.expander("View the example data"):
    st.dataframe(df, use_container_width=True)

# Source note
st.caption(
    "Source: Fictional example averages created for TFB3133/TEB3133 Lab 10. "
    "These are not findings from a real student survey."
)
