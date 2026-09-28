
import pandas as pd

# ==========================================
# 1. LOAD DATA
# ==========================================

data = pd.read_excel("STUDENT ABSENTEES DETAIL.xlsx")

print("========== ORIGINAL DATA ==========")
print(data.head())


# ==========================================
# 2. CLEAN ABSENTEE COUNT
# ==========================================

data["NO.OF.ABSENTEES"] = data["NO.OF.ABSENTEES"].replace("-", 0)
data["NO.OF.ABSENTEES"] = data["NO.OF.ABSENTEES"].astype(int)


# ==========================================
# 3. CONVERT DATE
# ==========================================

data["DATE"] = pd.to_datetime(data["DATE"])


# ==========================================
# 4. CREATE STATUS
# ==========================================

data["STATUS"] = "WORKING DAY"

data.loc[
    data["ABSENTEES ROLL.NO"].isin(["HOLIDAY", "NILL"]),
    "STATUS"
] = "NON-WORKING / NO RECORD"


# ==========================================
# 5. SORT BY DATE
# ==========================================

data = data.sort_values("DATE").reset_index(drop=True)


# ==========================================
# 6. DISPLAY CLEANED DATA
# ==========================================

print("\n========== CLEANED DATA ==========")
print(data.head(10))

print("\n========== DATA TYPES ==========")
print(data.dtypes)

print("\n========== DATE RANGE ==========")
print(data["DATE"].min(), "to", data["DATE"].max())

print("\n========== ABSENTEE SUMMARY ==========")
print(data["NO.OF.ABSENTEES"].describe())

print("\n========== STATUS COUNTS ==========")
print(data["STATUS"].value_counts())


# ==========================================
# 7. WORKING-DAY DATA
# ==========================================

working_data = data[
    data["STATUS"] == "WORKING DAY"
].copy()

print("\n========== WORKING DAYS ==========")
print("Total working days:", len(working_data))

print("\n========== HIGHEST ABSENCE ==========")
print(
    working_data["NO.OF.ABSENTEES"].max()
)


# ==========================================
# 8. SAVE CLEANED DATA
# ==========================================

data.to_csv("cleaned_absenteeism_data.csv", index=False)

print("\n====================================")
print("CLEANING COMPLETED SUCCESSFULLY")
print("Saved as: cleaned_absenteeism_data.csv")
print("====================================")
