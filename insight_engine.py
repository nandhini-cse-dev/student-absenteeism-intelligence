
import pandas as pd


# ==========================================
# 1. LOAD DATA
# ==========================================

data = pd.read_csv("cleaned_absenteeism_data.csv")

data["DATE"] = pd.to_datetime(data["DATE"])


working_data = data[
    data["STATUS"] == "WORKING DAY"
].copy()

working_data = working_data.sort_values("DATE")


# ==========================================
# 2. LOAD STUDENT ANALYSIS
# ==========================================

student_data = pd.read_csv(
    "student_attendance_analysis.csv"
)


# ==========================================
# 3. BASIC STATISTICS
# ==========================================

average_absence = (
    working_data["NO.OF.ABSENTEES"].mean()
)

highest_absence = (
    working_data["NO.OF.ABSENTEES"].max()
)

highest_day = working_data.loc[
    working_data["NO.OF.ABSENTEES"].idxmax()
]


# ==========================================
# 4. RECENT TREND
# ==========================================

recent_data = working_data.tail(5)

previous_data = working_data.iloc[-10:-5]


recent_average = (
    recent_data["NO.OF.ABSENTEES"].mean()
)

previous_average = (
    previous_data["NO.OF.ABSENTEES"].mean()
)


if recent_average > previous_average:
    trend_message = "Absenteeism has increased recently."

elif recent_average < previous_average:
    trend_message = "Absenteeism has decreased recently."

else:
    trend_message = "Absenteeism is relatively stable."


# ==========================================
# 5. WEEKDAY ANALYSIS
# ==========================================

weekday_average = (
    working_data
    .groupby("DAY")["NO.OF.ABSENTEES"]
    .mean()
    .sort_values(ascending=False)
)


highest_absence_day = (
    weekday_average.index[0]
)

highest_day_average = (
    weekday_average.iloc[0]
)


# ==========================================
# 6. STUDENT RISK ANALYSIS
# ==========================================

monitor_students = student_data[
    student_data["RISK_LEVEL"] == "MONITOR"
]

high_students = student_data[
    student_data["RISK_LEVEL"] == "HIGH"
]

critical_students = student_data[
    student_data["RISK_LEVEL"] == "CRITICAL"
]


# ==========================================
# 7. TOP ABSENT STUDENTS
# ==========================================

top_students = (
    student_data
    .sort_values(
        "ABSENCE_DAYS",
        ascending=False
    )
    .head(3)
)


# ==========================================
# 8. DISPLAY INSIGHTS
# ==========================================

print("\n")
print("========================================")
print("       AUTOMATIC INSIGHT ENGINE")
print("========================================")


print("\n📊 OVERALL")

print(
    f"Average daily absenteeism: "
    f"{average_absence:.2f}"
)

print(
    f"Highest absence recorded: "
    f"{highest_absence} students"
)

print(
    f"Highest absence occurred on: "
    f"{highest_day['DATE'].date()}"
)


print("\n📈 TREND")

print(trend_message)

print(
    f"Recent 5-day average: "
    f"{recent_average:.2f}"
)

print(
    f"Previous 5-day average: "
    f"{previous_average:.2f}"
)


print("\n📅 WEEKDAY PATTERN")

print(
    f"Highest average absenteeism day: "
    f"{highest_absence_day}"
)

print(
    f"Average absentees on {highest_absence_day}: "
    f"{highest_day_average:.2f}"
)


print("\n⚠️ ATTENDANCE MONITORING")

print(
    f"Students in monitoring range: "
    f"{len(monitor_students)}"
)

print(
    f"Students in high-risk range: "
    f"{len(high_students)}"
)

print(
    f"Students in critical range: "
    f"{len(critical_students)}"
)


print("\n👥 FREQUENT ABSENCE STUDENTS")

for _, row in top_students.iterrows():

    print(
        f"Roll No. {row['ROLL_NO']} → "
        f"{row['ABSENCE_DAYS']} absence days, "
        f"attendance {row['ATTENDANCE_PERCENT']:.2f}%"
    )


print("\n========================================")
print("INSIGHT GENERATION COMPLETED")
print("========================================")

