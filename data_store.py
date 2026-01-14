import pandas as pd
from datetime import date
import os

FILE_NAME = "workouts.csv"

COLUMNS = ["date", "exercise", "category", "reps", "duration", "energy", "notes"]

def init_storage():
    if not os.path.exists(FILE_NAME):
        pd.DataFrame(columns=COLUMNS).to_csv(FILE_NAME, index=False)

def log_workout(exercise, category, reps, duration, energy, notes):
    init_storage()
    df = pd.read_csv(FILE_NAME)
    df.loc[len(df)] = [
        date.today().isoformat(),
        exercise,
        category,
        reps,
        duration,
        energy,
        notes
    ]
    df.to_csv(FILE_NAME, index=False)

def load_workouts():
    init_storage()
    df = pd.read_csv(FILE_NAME)
    df.columns = df.columns.str.strip().str.lower()
    return df
