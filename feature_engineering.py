import pandas as pd

# ==========================================
# 1. LOAD CLEANED DATA
# ==========================================

data = pd.read_csv("cleaned_absenteeism_data.csv")

data["DATE"] = pd.to_datetime(data["DATE"])


# ==========================================
# 2. SELECT WORKING DAYS
# ==========================================

working_data = data[
    data["STATUS"] == "WORKING DAY"
].copy()

working_data = working_data.sort_values("DATE").reset_index(drop=True)


# ==========================================
# 3. PREVIOUS ABSENCE
# ==========================================

working_data["PREVIOUS_ABSENCE"] = (
    working_data["NO.OF.ABSENTEES"].shift(1)
)


# ==========================================
# 4. 3-DAY MOVING AVERAGE
# ==========================================

working_data["AVG_3_DAYS"] = (
    working_data["NO.OF.ABSENTEES"]
    .shift(1)
    .rolling(3)
    .mean()
)


# ==========================================
# 5. 7-DAY MOVING AVERAGE
# ==========================================

working_data["AVG_7_DAYS"] = (
    working_data["NO.OF.ABSENTEES"]
    .shift(1)
    .rolling(7)
    .mean()
)


# ==========================================
# 6. DAY NUMBER
# ==========================================

# Monday = 0
# Tuesday = 1
# ...
# Sunday = 6

working_data["DAY_NUMBER"] = (
    working_data["DATE"].dt.dayofweek
)


# ==========================================
# 7. PREVIOUS WEEK ABSENCE
# ==========================================

working_data["PREVIOUS_WEEK_ABSENCE"] = (
    working_data["NO.OF.ABSENTEES"].shift(7)
)


# ==========================================
# 8. ABSENCE TREND
# ==========================================

working_data["ABSENCE_TREND"] = (
    working_data["PREVIOUS_ABSENCE"]
    - working_data["AVG_3_DAYS"]
)


# ==========================================
# 9. DISPLAY FEATURES
# ==========================================

print("\n========== FEATURE ENGINEERING ==========")

print(
    working_data[
        [
            "DATE",
            "DAY",
            "NO.OF.ABSENTEES",
            "PREVIOUS_ABSENCE",
            "AVG_3_DAYS",
            "AVG_7_DAYS",
            "DAY_NUMBER",
            "PREVIOUS_WEEK_ABSENCE",
            "ABSENCE_TREND"
        ]
    ].head(15)
)


# ==========================================
# 10. REMOVE ROWS WITH MISSING FEATURES
# ==========================================

model_data = working_data.dropna().copy()


# ==========================================
# 11. DEFINE MODEL FEATURES
# ==========================================

features = [
    "DAY_NUMBER",
    "PREVIOUS_ABSENCE",
    "AVG_3_DAYS",
    "AVG_7_DAYS",
    "PREVIOUS_WEEK_ABSENCE",
    "ABSENCE_TREND"
]


# ==========================================
# 12. DISPLAY MODEL DATA
# ==========================================

print("\n========== MODEL FEATURES ==========")

print(features)

print("\nTotal working-day records:", len(working_data))

print("Usable model records:", len(model_data))

print("\nModel data preview:")

print(
    model_data[
        ["DATE"] + features + ["NO.OF.ABSENTEES"]
    ].head(10)
)


# ==========================================
# 13. SAVE FEATURE DATA
# ==========================================

model_data.to_csv(
    "model_ready_absenteeism_data.csv",
    index=False
)

print("\n====================================")
print("FEATURE ENGINEERING COMPLETED")
print("Saved as: model_ready_absenteeism_data.csv")
print("====================================")

