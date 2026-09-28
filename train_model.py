import pandas as pd
import joblib

from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ==========================================
# 1. LOAD MODEL-READY DATA
# ==========================================

data = pd.read_csv("model_ready_absenteeism_data.csv")

data["DATE"] = pd.to_datetime(data["DATE"])


# ==========================================
# 2. DEFINE FEATURES
# ==========================================

features = [
    "DAY_NUMBER",
    "PREVIOUS_ABSENCE",
    "AVG_3_DAYS",
    "AVG_7_DAYS",
    "PREVIOUS_WEEK_ABSENCE",
    "ABSENCE_TREND"
]

target = "NO.OF.ABSENTEES"


# ==========================================
# 3. TIME-BASED TRAIN / TEST SPLIT
# ==========================================

split_index = int(len(data) * 0.80)

train_data = data.iloc[:split_index].copy()
test_data = data.iloc[split_index:].copy()


X_train = train_data[features]
y_train = train_data[target]

X_test = test_data[features]
y_test = test_data[target]


print("========== DATA SPLIT ==========")

print("Total records:", len(data))
print("Training records:", len(train_data))
print("Testing records:", len(test_data))

print(
    "\nTraining period:",
    train_data["DATE"].min().date(),
    "to",
    train_data["DATE"].max().date()
)

print(
    "Testing period:",
    test_data["DATE"].min().date(),
    "to",
    test_data["DATE"].max().date()
)


# ==========================================
# 4. CREATE XGBOOST MODEL
# ==========================================

model = XGBRegressor(
    n_estimators=100,
    max_depth=2,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    objective="reg:squarederror"
)


# ==========================================
# 5. TRAIN MODEL
# ==========================================

print("\n========== TRAINING XGBOOST ==========")

model.fit(X_train, y_train)

print("XGBoost training completed!")


# ==========================================
# 6. MAKE TEST PREDICTIONS
# ==========================================

predictions = model.predict(X_test)


# ==========================================
# 7. EVALUATION
# ==========================================

mae = mean_absolute_error(y_test, predictions)

rmse = mean_squared_error(
    y_test,
    predictions
) ** 0.5

r2 = r2_score(y_test, predictions)


print("\n========== MODEL EVALUATION ==========")

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.2f}")


# ==========================================
# 8. ACTUAL VS PREDICTED
# ==========================================

results = pd.DataFrame({
    "DATE": test_data["DATE"],
    "ACTUAL_ABSENTEES": y_test.values,
    "PREDICTED_ABSENTEES": predictions
})

print("\n========== ACTUAL VS PREDICTED ==========")

print(results.to_string(index=False))


# ==========================================
# 9. FEATURE IMPORTANCE
# ==========================================

importance = pd.DataFrame({
    "FEATURE": features,
    "IMPORTANCE": model.feature_importances_
})

importance = importance.sort_values(
    "IMPORTANCE",
    ascending=False
)

print("\n========== FEATURE IMPORTANCE ==========")

print(importance.to_string(index=False))


# ==========================================
# 10. SAVE MODEL
# ==========================================

model_package = {
    "model": model,
    "features": features,
    "training_date": str(pd.Timestamp.today().date()),
    "mae": mae,
    "rmse": rmse,
    "r2": r2
}

joblib.dump(
    model_package,
    "xgboost_absenteeism_model.pkl"
)


# ==========================================
# 11. SAVE RESULTS
# ==========================================

results.to_csv(
    "model_predictions.csv",
    index=False
)

importance.to_csv(
    "feature_importance.csv",
    index=False
)


print("\n====================================")
print("MODEL TRAINING COMPLETED")
print("Model saved as:")
print("xgboost_absenteeism_model.pkl")
print("")
print("Additional files:")
print("model_predictions.csv")
print("feature_importance.csv")
print("====================================")

