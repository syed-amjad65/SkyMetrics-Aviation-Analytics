"""
SkyMetrics™ Workforce Forecasting Engine
----------------------------------------
This module calculates workforce requirements 
based on fleet size and staffing ratios.
"""

import pandas as pd


def load_data():
    fleet = pd.read_csv("data_models/Fleet_Master.csv")
    crew = pd.read_csv("data_models/Crew_Ratio_Model.csv")
    engineers = pd.read_csv("data_models/Engineer_Ratio_Model.csv")
    return fleet, crew, engineers


def calculate_workforce():
    fleet, crew, engineers = load_data()

    # Merge fleet with crew ratios
    crew_forecast = fleet.merge(crew, on="Aircraft_Type")
    crew_forecast["Total_Pilots"] = (
        crew_forecast["Fleet_Count"] * crew_forecast["Pilots_Per_Aircraft"]
    )
    crew_forecast["Total_Cabin_Crew"] = (
        crew_forecast["Fleet_Count"] * crew_forecast["CabinCrew_Per_Aircraft"]
    )

    # Merge fleet with engineer ratios
    engineer_forecast = fleet.merge(engineers, on="Aircraft_Type")
    engineer_forecast["Total_Engineers"] = (
        engineer_forecast["Fleet_Count"] * engineer_forecast["Engineers_Per_Aircraft"]
    )

    return crew_forecast, engineer_forecast


def summarize_results():
    crew_forecast, engineer_forecast = calculate_workforce()

    total_pilots = crew_forecast["Total_Pilots"].sum()
    total_cabin = crew_forecast["Total_Cabin_Crew"].sum()
    total_engineers = engineer_forecast["Total_Engineers"].sum()

    print("=== SkyMetrics Workforce Forecast Summary ===")
    print(f"Total Pilots Required: {total_pilots}")
    print(f"Total Cabin Crew Required: {total_cabin}")
    print(f"Total Engineers Required: {total_engineers}")


if __name__ == "__main__":
    summarize_results()
