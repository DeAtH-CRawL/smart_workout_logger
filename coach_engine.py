from config import USER_NAME
from analytics import get_streak, core_sessions_week, days_since_last, weekly_summary

def coach_message(df):
    if df.empty:
        return f"Hey {USER_NAME} 💛 I’m ready whenever you are. Let’s start building those abs."

    df.columns = df.columns.str.strip().str.lower()

    streak = get_streak(df)
    core_week = core_sessions_week(df)
    gap = days_since_last(df)

    if streak >= 7:
        return f"🔥 {streak}-day streak! Elite consistency, {USER_NAME}."
    if streak >= 3:
        return f"💪 {streak}-day streak! Momentum is building."
    if core_week >= 4:
        return "🧠 Core work this week is on point."
    if gap and gap >= 3:
        return "💛 Missed a few days — ease back in, even 5 minutes counts."
    if "energy" in df.columns and df.iloc[-1]["energy"] == "Low":
        return "😴 Low energy today — recovery is also progress."

    return f"🌱 Proud of you, {USER_NAME}. Consistency wins."

def weekly_message(df):
    summary = weekly_summary(df)
    if not summary:
        return None
    days, core = summary
    return f"📅 This week: {days} workout days, {core} core sessions."
