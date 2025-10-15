import pandas as pd
from deadlift_data_import import import_data

def top50():
# Load the whole Data Frame
    df = import_data()

    male = df["sex"] == "M"
    female = df["sex"] == "F"
    df = df[male | female]
    
    # First filters down to each lifters best total per weightclass then selects the top 50 totals of all time per weight class
    top50_by_class_sex = (
        df
            .sort_values("deadlift_lbs", ascending=False)
            .groupby(['weightclass_lbs', 'sex', 'name'], as_index=False)
            .first()
            .sort_values(["weightclass_lbs", "deadlift_lbs"], ascending=[True, False])
            .groupby(["weightclass_lbs", "sex"], as_index=False)
            .head(50)
            .reset_index(drop=True)
    )

    return top50_by_class_sex