from datetime import date, timedelta

def get_streak(df):
    if df.empty:
        return 0
    dates = set(df["date"])
    streak = 0
    d = date.today()
    while d.isoformat() in dates:
        streak += 1
        d -= timedelta(days=1)
    return streak

def core_sessions_week(df):
    if df.empty:
        return 0
    recent = df.tail(30)
    return recent[recent["category"] == "Core"].shape[0]

def days_since_last(df):
    if df.empty:
        return None
    last = date.fromisoformat(df.iloc[-1]["date"])
    return (date.today() - last).days

def weekly_summary(df):
    if df.empty:
        return None
    recent = df.tail(30)
    days = recent["date"].nunique()
    core = recent[recent["category"] == "Core"].shape[0]
    return days, core
