import streamlit as st
from config import *
from data_store import *
from coach_engine import coach_message, weekly_message
from analytics import get_streak

init_storage()

st.set_page_config(page_title=APP_TITLE)
st.title(APP_TITLE)
st.markdown(f"### 🎯 Goal: {GOAL}")
st.markdown("---")

df = load_workouts()

# ---- METRICS ----
c1, c2, c3 = st.columns(3)
c1.metric("🔥 Streak", f"{get_streak(df)} days")
c2.metric("💪 Total Workouts", len(df))
c3.metric("🎯 Core Sessions", df[df["category"] == "Core"].shape[0])

st.markdown("---")

# ---- LOG WORKOUT ----
st.subheader("🏋️ Log Today’s Workout")

exercise = st.selectbox(
    "Exercise",
    CORE_EXERCISES + FULL_BODY_EXERCISES + ["Other"]
)

category = "Core" if exercise in CORE_EXERCISES else "Full Body"

reps = st.number_input("Reps (optional)", 0, step=1)
duration = st.number_input("Duration (minutes)", 0, step=1)
energy = st.radio("Energy Level", ["High", "Medium", "Low"])
notes = st.text_input("Notes (optional)")

if st.button("💾 Save Workout"):
    log_workout(exercise, category, reps, duration, energy, notes)
    st.success("Workout saved 💖")
    st.rerun()

st.markdown("---")

# ---- COACH ----
st.subheader("🧠 Coach Says")
st.info(coach_message(df))

weekly = weekly_message(df)
if weekly:
    st.success(weekly)

st.markdown("---")

# ---- HISTORY ----
with st.expander("📊 Workout History"):
    st.dataframe(df, use_container_width=True)
