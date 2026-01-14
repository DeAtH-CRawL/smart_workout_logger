from datetime import date, timedelta

def get_streak(df):
    if df.empty:
        return 0
    dates = list(df["date"])
    streak = 0
    d = date.today()
    while d.isoformat() in dates:
        streak += 1
        d -= timedelta(days=1)
    return streak

def core_sessions_week(df):
    if df.empty:
        return 0
    last_7 = df.tail(30)
    return last_7[last_7["category"] == "Core"].shape[0]

def days_since_last(df):
    if df.empty:
        return None
    last = date.fromisoformat(df.iloc[-1]["date"])
    return (date.today() - last).days

def weekly_summary(df):
    if df.empty:
        return None
    last_7 = df.tail(30)
    days = last_7["date"].nunique()
    core = last_7[last_7["category"] == "Core"].shape[0]
    return days, core
