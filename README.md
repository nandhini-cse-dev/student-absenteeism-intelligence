# AI-Based Student Absenteeism Intelligence & Early Warning System

An AI-powered student absenteeism analysis and forecasting system developed using Python, XGBoost, Pandas, Plotly and Streamlit.

## Features

- Student absenteeism trend analysis
- XGBoost-based absenteeism forecasting
- Student attendance analytics
- Early warning and risk monitoring
- Weekday absence pattern analysis
- Feature importance analysis
- Automatic data-driven insights
- Interactive Streamlit dashboard

## Technologies Used

- Python
- Pandas
- XGBoost
- Scikit-learn
- Plotly
- Streamlit
- Joblib
- OpenPyXL

## Machine Learning Model

The system uses XGBoost Regression to estimate the number of absentees based on historical absenteeism patterns and engineered time-series features.

### Features Used

- Day Number
- Previous Absence
- 3-Day Moving Average
- 7-Day Moving Average
- Previous Week Absence
- Absence Trend

## Project Structure

```text
app.py
clean.py
feature_engineering.py
train_model.py
student_analysis.py
insight_engine.py
requirements.txt
.gitignore