
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


# ==========================================
# 3. EXTRACT STUDENT ABSENCE RECORDS
# ==========================================

student_records = []

for _, row in working_data.iterrows():

    roll_text = str(
        row["ABSENTEES ROLL.NO"]
    ).strip()

    if roll_text not in ["NILL", "HOLIDAY", "nan", ""]:

        rolls = roll_text.split(",")

        for roll in rolls:

            roll = roll.strip()

            if roll:

                student_records.append({
                    "ROLL_NO": roll,
                    "DATE": row["DATE"],
                    "DAY": row["DAY"]
                })


student_data = pd.DataFrame(student_records)


# ==========================================
# 4. STUDENT ABSENCE SUMMARY
# ==========================================

student_summary = (
    student_data
    .groupby("ROLL_NO")
    .agg(
        ABSENCE_DAYS=("DATE", "count"),
        LAST_ABSENCE=("DATE", "max")
    )
    .reset_index()
)


# ==========================================
# 5. CALCULATE ATTENDANCE %
# ==========================================

total_working_days = len(working_data)

student_summary["ATTENDANCE_PERCENT"] = (
    (
        total_working_days
        - student_summary["ABSENCE_DAYS"]
    )
    / total_working_days
) * 100


student_summary["ATTENDANCE_PERCENT"] = (
    student_summary["ATTENDANCE_PERCENT"].round(2)
)


# ==========================================
# 6. CREATE ATTENDANCE RISK
# ==========================================

def get_risk(attendance):

    if attendance < 75:
        return "CRITICAL"

    elif attendance < 80:
        return "HIGH"

    elif attendance < 85:
        return "MONITOR"

    else:
        return "LOW"


student_summary["RISK_LEVEL"] = (
    student_summary["ATTENDANCE_PERCENT"]
    .apply(get_risk)
)


# ==========================================
# 7. STUDENT-WEEKDAY ANALYSIS
# ==========================================

weekday_counts = (
    student_data
    .groupby(["ROLL_NO", "DAY"])
    .size()
    .reset_index(name="ABSENCE_COUNT")
)


# Find the weekday with maximum absences
most_missed_day = (
    weekday_counts
    .sort_values(
        ["ROLL_NO", "ABSENCE_COUNT"],
        ascending=[True, False]
    )
    .drop_duplicates("ROLL_NO")
    [["ROLL_NO", "DAY", "ABSENCE_COUNT"]]
    .rename(
        columns={
            "DAY": "MOST_MISSED_DAY",
            "ABSENCE_COUNT": "MOST_MISSED_DAY_COUNT"
        }
    )
)


# ==========================================
# 8. MERGE WEEKDAY INFORMATION
# ==========================================

student_summary = student_summary.merge(
    most_missed_day,
    on="ROLL_NO",
    how="left"
)


# ==========================================
# 9. SORT BY ABSENCE
# ==========================================

student_summary = student_summary.sort_values(
    "ABSENCE_DAYS",
    ascending=False
).reset_index(drop=True)


# ==========================================
# 10. DISPLAY RESULTS
# ==========================================

print("\n========== STUDENT ANALYSIS ==========")

print(
    student_summary.to_string(index=False)
)


print("\n========== STUDENT COUNT ==========")

print(
    "Students with recorded absences:",
    student_summary["ROLL_NO"].nunique()
)


print("\n========== RISK COUNTS ==========")

print(
    student_summary["RISK_LEVEL"].value_counts()
)


print("\n========== TOP ABSENT STUDENTS ==========")

print(
    student_summary[
        [
            "ROLL_NO",
            "ABSENCE_DAYS",
            "ATTENDANCE_PERCENT",
            "RISK_LEVEL"
        ]
    ].head(10).to_string(index=False)
)


# ==========================================
# 11. SAVE STUDENT SUMMARY
# ==========================================

student_summary.to_csv(
    "student_attendance_analysis.csv",
    index=False
)


weekday_counts.to_csv(
    "student_weekday_analysis.csv",
    index=False
)


print("\n====================================")
print("STUDENT ANALYSIS COMPLETED")
print("====================================")

print("Saved:")
print("student_attendance_analysis.csv")
print("student_weekday_analysis.csv")

