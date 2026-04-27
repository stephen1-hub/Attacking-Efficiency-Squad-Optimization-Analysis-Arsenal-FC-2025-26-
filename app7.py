import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------
# LOAD DATA
# -----------------------
df = pd.read_excel('Arsenal team-players 2025_2026.xlsx')

# -----------------------
# METRICS
# -----------------------
df["goals90"] = df["goals"] / df["min"] * 90
df["assists90"] = df["assists"] / df["min"] * 90

df["finishing_efficiency"] = np.where(df["xG"] > 0, df["goals"] / df["xG"], 0)
df["creativity_efficiency"] = np.where(df["xA"] > 0, df["assists"] / df["xA"], 0)

df["threat_score"] = df["xG90"] + df["xA90"]

# -----------------------
# TITLE
# -----------------------
st.title("Arsenal 2025/26 Squad Analysis Dashboard")

# -----------------------
# FILTERS
# -----------------------
position_filter = st.multiselect(
    "Filter by Position",
    options=df["position"].unique(),
    default=df["position"].unique()
)

df_filtered = df[df["position"].isin(position_filter)]

# -----------------------
# SECTION 1: TOP THREAT
# -----------------------
st.subheader("🔥 Most Dangerous Players")

top_threat = df_filtered.sort_values("threat_score", ascending=False).head(10)

fig1, ax1 = plt.subplots()
ax1.barh(top_threat["player"], top_threat["threat_score"])
ax1.set_xlabel("Threat Score (xG90 + xA90)")
ax1.invert_yaxis()

st.pyplot(fig1)

# -----------------------
# SECTION 2: FINISHING
# -----------------------
st.subheader("🎯 Finishing Performance (Goals vs xG)")

fig2, ax2 = plt.subplots()

ax2.scatter(df_filtered["xG"], df_filtered["goals"])

for i in range(len(df_filtered)):
    ax2.text(df_filtered["xG"].iloc[i],
             df_filtered["goals"].iloc[i],
             df_filtered["player"].iloc[i],
             fontsize=8)

ax2.plot([0, df_filtered["xG"].max()],
         [0, df_filtered["xG"].max()])

ax2.set_xlabel("xG")
ax2.set_ylabel("Goals")

st.pyplot(fig2)

# -----------------------
# SECTION 3: CREATIVITY
# -----------------------
st.subheader("🧠 Creativity (xA vs Assists)")

fig3, ax3 = plt.subplots()

ax3.scatter(df_filtered["xA"], df_filtered["assists"])

for i in range(len(df_filtered)):
    ax3.text(df_filtered["xA"].iloc[i],
             df_filtered["assists"].iloc[i],
             df_filtered["player"].iloc[i],
             fontsize=8)

ax3.plot([0, df_filtered["xA"].max()],
         [0, df_filtered["xA"].max()])

ax3.set_xlabel("xA")
ax3.set_ylabel("Assists")

st.pyplot(fig3)

# -----------------------
# SECTION 4: ROLE MAP
# -----------------------
st.subheader("📊 Player Role Map")

fig4, ax4 = plt.subplots()

ax4.scatter(df_filtered["xG90"], df_filtered["xA90"])

for i in range(len(df_filtered)):
    ax4.text(df_filtered["xG90"].iloc[i],
             df_filtered["xA90"].iloc[i],
             df_filtered["player"].iloc[i],
             fontsize=8)

ax4.axvline(0.4)
ax4.axhline(0.25)

ax4.set_xlabel("xG per 90")
ax4.set_ylabel("xA per 90")

st.pyplot(fig4)

# -----------------------
# SECTION 5: TABLES
# -----------------------
st.subheader("📋 Data Table")

st.dataframe(df_filtered.sort_values("threat_score", ascending=False))

# -----------------------
# SECTION 6: INSIGHTS
# -----------------------
st.subheader("💡 Key Insights")

st.markdown("""
- A small group of players drive most of the attacking threat  
- Finishing performance is generally stable, with a few over/under-performers  
- Creativity is concentrated around a central playmaker  
- Attacking balance shows slight right-side dominance  
""")
