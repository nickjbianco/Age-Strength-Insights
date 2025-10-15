import pandas as pd
from sqlalchemy import create_engine

def import_data():
    # Create engine
    engine = create_engine("postgresql+psycopg2://postgres:Show1256x!@localhost:5433/powerlifting")

    # Read the whole table into a DataFrame
    df = pd.read_sql("SELECT name, age, sex, date, bodyweight_lbs, weightclass_lbs, squat_lbs FROM raw_squat", engine, parse_dates=["date"])

    # Set the date as the index
    df.set_index('date', inplace=True)

    return df