from config import USER_NAME, GOAL
from analytics import get_streak, core_sessions_week, days_since_last, weekly_summary

def coach_message(df):
    if df.empty:
        return f"Hey {USER_NAME} 💛 I’m ready whenever you are. Let’s start building those abs."

    streak = get_streak(df)
    core_week = core_sessions_week(df)
    gap = days_since_last(df)

    if streak >= 7:
        return f"🔥 {streak}-day streak! This is elite consistency, {USER_NAME}. Abs are inevitable."
    if streak >= 3:
        return f"Nice {streak}-day streak 💪 Momentum like this really shows results."
    if core_week >= 4:
        return "Your core focus this week is perfect. Your abs are getting stronger every session."
    if gap and gap >= 3:
        return "It’s okay to slow down 💛 Let’s ease back in — even 5 minutes counts."
    if df.iloc[-1]["energy"] == "Low":
        return "Low-energy days still matter. Listening to your body is strength 🧠"

    return f"Proud of you, {USER_NAME}. Consistency beats intensity every time."

def weekly_message(df):
    summary = weekly_summary(df)
    if not summary:
        return None
    days, core = summary
    return f"📅 This week: {days} workout days, {core} core sessions. That’s real progress 💖"
