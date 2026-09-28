import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="EduAI | Student Absenteeism Intelligence",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PREMIUM EDUAI THEME
# ============================================================

st.markdown("""
<style>

/* ============================================================
   GLOBAL
   ============================================================ */

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(99,102,241,0.10),
            transparent 28%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(14,165,233,0.08),
            transparent 25%
        ),
        linear-gradient(
            135deg,
            #f8fafc 0%,
            #eef2ff 50%,
            #f8fafc 100%
        );
}

.block-container {
    padding-top: 1.8rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}


/* ============================================================
   HEADER
   ============================================================ */

.hero-card {
    background:
        linear-gradient(
            135deg,
            #111827 0%,
            #312e81 48%,
            #4f46e5 100%
        );

    border-radius: 24px;
    padding: 30px 34px;
    margin-bottom: 25px;

    box-shadow:
        0 18px 45px rgba(49,46,129,0.25);

    position: relative;
    overflow: hidden;
}

.hero-card::after {
    content: "";
    position: absolute;
    width: 220px;
    height: 220px;
    right: -60px;
    top: -90px;
    border-radius: 50%;
    background: rgba(255,255,255,0.08);
}

.hero-card::before {
    content: "";
    position: absolute;
    width: 140px;
    height: 140px;
    right: 120px;
    bottom: -80px;
    border-radius: 50%;
    background: rgba(56,189,248,0.12);
}

.hero-title {
    color: white;
    font-size: 2.35rem;
    font-weight: 850;
    letter-spacing: -1px;
    position: relative;
    z-index: 2;
}

.hero-subtitle {
    color: #c7d2fe;
    font-size: 0.98rem;
    margin-top: 7px;
    position: relative;
    z-index: 2;
}

.hero-badge {
    display: inline-block;
    margin-top: 18px;
    padding: 7px 14px;
    border-radius: 999px;
    background: rgba(255,255,255,0.12);
    color: #e0e7ff;
    font-size: 0.78rem;
    font-weight: 650;
}


/* ============================================================
   SECTION TITLES
   ============================================================ */

.section-title {
    color: #1e1b4b;
    font-size: 1.45rem;
    font-weight: 800;
    margin-top: 18px;
    margin-bottom: 14px;
}

.section-caption {
    color: #64748b;
    font-size: 0.9rem;
    margin-bottom: 16px;
}


/* ============================================================
   KPI CARDS
   ============================================================ */

.kpi-card {
    background: rgba(255,255,255,0.88);
    backdrop-filter: blur(12px);

    border: 1px solid rgba(226,232,240,0.9);

    border-radius: 19px;

    padding: 20px;

    min-height: 142px;

    box-shadow:
        0 10px 28px rgba(15,23,42,0.07);

    transition: all 0.25s ease;
}

.kpi-card:hover {
    transform: translateY(-4px);
    box-shadow:
        0 15px 35px rgba(79,70,229,0.13);
}

.kpi-icon {
    font-size: 1.45rem;
}

.kpi-label {
    color: #64748b;
    font-size: 0.82rem;
    font-weight: 650;
    margin-top: 6px;
}

.kpi-value {
    color: #1e1b4b;
    font-size: 2rem;
    font-weight: 850;
    margin-top: 5px;
}

.kpi-desc {
    color: #94a3b8;
    font-size: 0.73rem;
    margin-top: 4px;
}


/* ============================================================
   INFO / INSIGHT CARDS
   ============================================================ */

.insight-card {
    background: rgba(255,255,255,0.90);
    backdrop-filter: blur(10px);

    border-radius: 18px;

    padding: 22px;

    border: 1px solid #e2e8f0;

    box-shadow:
        0 9px 25px rgba(15,23,42,0.06);
}

.insight-title {
    color: #312e81;
    font-size: 1rem;
    font-weight: 750;
    margin-bottom: 10px;
}

.insight-text {
    color: #475569;
    font-size: 0.88rem;
    line-height: 1.6;
}


/* ============================================================
   AI BADGE
   ============================================================ */

.ai-badge {
    display: inline-block;

    background:
        linear-gradient(
            90deg,
            #4f46e5,
            #7c3aed
        );

    color: white;

    padding: 6px 13px;

    border-radius: 999px;

    font-size: 0.75rem;

    font-weight: 700;

    box-shadow:
        0 5px 15px rgba(79,70,229,0.25);
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            #0f172a 0%,
            #1e1b4b 55%,
            #312e81 100%
        );

}

section[data-testid="stSidebar"] * {
    color: #f8fafc !important;
}

.sidebar-brand {
    text-align: center;

    padding: 15px 5px 20px;

    border-bottom:
        1px solid rgba(255,255,255,0.10);

    margin-bottom: 18px;
}

.sidebar-logo {
    font-size: 2.2rem;
}

.sidebar-title {
    font-size: 1.25rem;
    font-weight: 800;
}

.sidebar-subtitle {
    font-size: 0.72rem;
    color: #c7d2fe !important;
    margin-top: 4px;
}


/* ============================================================
   RADIO BUTTONS
   ============================================================ */

section[data-testid="stSidebar"]
div[role="radiogroup"] label {

    border-radius: 11px;

    padding: 8px 10px;

    margin: 3px 0;

    transition: 0.2s ease;
}

section[data-testid="stSidebar"]
div[role="radiogroup"] label:hover {

    background:
        rgba(255,255,255,0.10);
}


/* ============================================================
   BUTTONS
   ============================================================ */

.stButton > button {

    border: none;

    border-radius: 12px;

    background:
        linear-gradient(
            90deg,
            #4f46e5,
            #7c3aed
        );

    color: white;

    font-weight: 750;

    min-height: 44px;

    box-shadow:
        0 7px 18px rgba(79,70,229,0.24);

    transition: 0.2s ease;
}

.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 10px 25px rgba(79,70,229,0.32);
}


/* ============================================================
   DOWNLOAD
   ============================================================ */

.stDownloadButton > button {

    border-radius: 11px;

    font-weight: 700;
}


/* ============================================================
   ALERTS
   ============================================================ */

div[data-testid="stAlert"] {

    border-radius: 14px;

    border: none;

    box-shadow:
        0 5px 16px rgba(15,23,42,0.05);
}


/* ============================================================
   SELECT BOX
   ============================================================ */

div[data-baseweb="select"] > div {

    border-radius: 11px;

    border: 1px solid #cbd5e1;

    background: rgba(255,255,255,0.8);
}


/* ============================================================
   DATAFRAME
   ============================================================ */

div[data-testid="stDataFrame"] {

    border-radius: 14px;

    overflow: hidden;

    border:
        1px solid #e2e8f0;

    box-shadow:
        0 5px 18px rgba(15,23,42,0.05);
}


/* ============================================================
   DIVIDER
   ============================================================ */

hr {
    border-color: #e2e8f0;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {

    text-align: center;

    margin-top: 35px;

    padding: 22px;

    border-radius: 18px;

    background:
        rgba(255,255,255,0.65);

    color: #64748b;

    font-size: 0.78rem;
}

.footer strong {
    color: #312e81;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 900px) {

    .hero-title {
        font-size: 1.8rem;
    }

    .kpi-card {
        margin-bottom: 10px;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    return joblib.load(
        "xgboost_absenteeism_model.pkl"
    )


# ============================================================
# LOAD MAIN DATA
# ============================================================

@st.cache_data
def load_data():

    data = pd.read_csv(
        "cleaned_absenteeism_data.csv"
    )

    data["DATE"] = pd.to_datetime(
        data["DATE"]
    )

    return data


# ============================================================
# LOAD STUDENT DATA
# ============================================================

@st.cache_data
def load_student_data():

    student_summary = pd.read_csv(
        "student_attendance_analysis.csv"
    )

    student_weekday = pd.read_csv(
        "student_weekday_analysis.csv"
    )

    return student_summary, student_weekday


model_package = load_model()

model = model_package["model"]

features = model_package["features"]

data = load_data()

student_summary, student_weekday = load_student_data()


# ============================================================
# WORKING DAY DATA
# ============================================================

working_data = data[
    data["STATUS"] == "WORKING DAY"
].copy()

working_data = (
    working_data
    .sort_values("DATE")
    .reset_index(drop=True)
)


# ============================================================
# MOVING AVERAGES
# ============================================================

working_data["AVG_3_DAYS"] = (
    working_data["NO.OF.ABSENTEES"]
    .shift(1)
    .rolling(3)
    .mean()
)

working_data["AVG_7_DAYS"] = (
    working_data["NO.OF.ABSENTEES"]
    .shift(1)
    .rolling(7)
    .mean()
)


# ============================================================
# COMMON STATISTICS
# ============================================================

working_days = len(
    working_data
)

student_count = (
    student_summary["ROLL_NO"]
    .nunique()
)

average_absence = (
    working_data[
        "NO.OF.ABSENTEES"
    ].mean()
)

highest_absence = (
    working_data[
        "NO.OF.ABSENTEES"
    ].max()
)

highest_date = working_data.loc[
    working_data[
        "NO.OF.ABSENTEES"
    ].idxmax(),
    "DATE"
]

monitor_count = len(
    student_summary[
        student_summary["RISK_LEVEL"]
        == "MONITOR"
    ]
)

high_count = len(
    student_summary[
        student_summary["RISK_LEVEL"]
        == "HIGH"
    ]
)

critical_count = len(
    student_summary[
        student_summary["RISK_LEVEL"]
        == "CRITICAL"
    ]
)


# ============================================================
# HERO HEADER
# ============================================================

st.markdown("""
<div class="hero-card">

<div class="hero-title">
🎓 AI-Based Student Absenteeism Intelligence
</div>

<div class="hero-subtitle">
Smart attendance analytics • XGBoost forecasting •
Student monitoring • Early-warning intelligence
</div>

<div class="hero-badge">
🤖 AI POWERED  &nbsp; • &nbsp;
📊 DATA DRIVEN  &nbsp; • &nbsp;
🎯 EARLY WARNING
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("""
<div class="sidebar-brand">

<div class="sidebar-logo">🎓</div>

<div class="sidebar-title">
EduAI Analytics
</div>

<div class="sidebar-subtitle">
Student Absenteeism Intelligence
</div>

</div>
""", unsafe_allow_html=True)


st.sidebar.markdown(
    "### 🧭 Navigation"
)

page = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Dashboard",
        "📈 Trend Analysis",
        "🔮 XGBoost Forecast",
        "👥 Student Analytics",
        "⚠️ Early Warning",
        "📅 Weekday Patterns",
        "🔍 Model Analysis",
        "💡 Automatic Insights"
    ],
    label_visibility="collapsed"
)


st.sidebar.divider()

st.sidebar.markdown(
    "### 📊 Dataset Overview"
)

st.sidebar.write(
    f"📅 Working Days  **{working_days}**"
)

st.sidebar.write(
    f"👥 Students  **{student_count}**"
)

st.sidebar.write(
    f"📊 Avg Absentees  **{average_absence:.2f}**"
)

st.sidebar.write(
    f"⚠️ Monitoring  **{monitor_count}**"
)

st.sidebar.divider()

st.sidebar.caption(
    "Built with Python • Pandas • XGBoost • Plotly • Streamlit"
)


# ============================================================
# 1. DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.markdown(
        '<div class="section-title">'
        '🏠 Executive Dashboard'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-caption">'
        'A quick overview of attendance behaviour, '
        'absenteeism trends and student monitoring.'
        '</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # KPI CARDS
    # --------------------------------------------------------

    c1, c2, c3, c4, c5 = st.columns(5)


    with c1:

        st.markdown(
            f"""
            <div class="kpi-card">

            <div class="kpi-icon">📅</div>

            <div class="kpi-label">
            WORKING DAYS
            </div>

            <div class="kpi-value">
            {working_days}
            </div>

            <div class="kpi-desc">
            Recorded working days
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c2:

        st.markdown(
            f"""
            <div class="kpi-card">

            <div class="kpi-icon">👥</div>

            <div class="kpi-label">
            STUDENTS
            </div>

            <div class="kpi-value">
            {student_count}
            </div>

            <div class="kpi-desc">
            Students with recorded absences
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c3:

        st.markdown(
            f"""
            <div class="kpi-card">

            <div class="kpi-icon">📊</div>

            <div class="kpi-label">
            AVG ABSENTEES
            </div>

            <div class="kpi-value">
            {average_absence:.2f}
            </div>

            <div class="kpi-desc">
            Per working day
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c4:

        st.markdown(
            f"""
            <div class="kpi-card">

            <div class="kpi-icon">🚨</div>

            <div class="kpi-label">
            PEAK ABSENCE
            </div>

            <div class="kpi-value">
            {highest_absence}
            </div>

            <div class="kpi-desc">
            {highest_date.strftime('%d %b %Y')}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c5:

        st.markdown(
            f"""
            <div class="kpi-card">

            <div class="kpi-icon">⚠️</div>

            <div class="kpi-label">
            MONITORING
            </div>

            <div class="kpi-value">
            {monitor_count}
            </div>

            <div class="kpi-desc">
            Project-defined range
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.write("")


    # --------------------------------------------------------
    # TREND + SNAPSHOT
    # --------------------------------------------------------

    col1, col2 = st.columns(
        [2.2, 1]
    )


    with col1:

        st.markdown(
            '<div class="section-title">'
            '📈 Absenteeism Trend'
            '</div>',
            unsafe_allow_html=True
        )

        fig = go.Figure()


        fig.add_trace(
            go.Scatter(
                x=working_data["DATE"],
                y=working_data[
                    "NO.OF.ABSENTEES"
                ],
                mode="lines+markers",
                name="Daily Absentees"
            )
        )


        fig.add_trace(
            go.Scatter(
                x=working_data["DATE"],
                y=working_data[
                    "AVG_3_DAYS"
                ],
                mode="lines",
                name="3-Day Average"
            )
        )


        fig.update_layout(
            height=440,
            hovermode="x unified",
            xaxis_title="Date",
            yaxis_title="Absentees",
            template="plotly_white",
            margin=dict(
                l=10,
                r=10,
                t=35,
                b=10
            ),
            legend=dict(
                orientation="h",
                y=1.08
            )
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


    with col2:

        st.markdown(
            """
            <div class="section-title">
            🤖 AI Snapshot
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="insight-card">

            <div class="insight-title">
            📌 Attendance Intelligence
            </div>

            <div class="insight-text">

            <b>Peak Absenteeism</b><br>
            {highest_absence} students

            <br><br>

            <b>Peak Date</b><br>
            {highest_date.strftime('%d %B %Y')}

            <br><br>

            <b>Students in Monitoring</b><br>
            {monitor_count}

            <br><br>

            <b>Prediction Engine</b><br>
            XGBoost Regressor

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


        st.write("")


        st.markdown(
            """
            <div class="insight-card">

            <div class="insight-title">
            💡 What this dashboard does
            </div>

            <div class="insight-text">

            • Tracks daily absenteeism<br>
            • Identifies attendance patterns<br>
            • Forecasts future absenteeism<br>
            • Highlights students for monitoring<br>
            • Explains model features

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # --------------------------------------------------------
    # STATUS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">'
        '📊 Dataset Status'
        '</div>',
        unsafe_allow_html=True
    )


    status_data = (
        data["STATUS"]
        .value_counts()
        .reset_index()
    )

    status_data.columns = [
        "STATUS",
        "COUNT"
    ]


    fig_status = px.pie(
        status_data,
        names="STATUS",
        values="COUNT",
        hole=0.48,
        title="Recorded Day Status"
    )


    fig_status.update_layout(
        template="plotly_white",
        height=390
    )


    st.plotly_chart(
        fig_status,
        use_container_width=True
    )


    st.info(
        "ℹ️ Students analyzed are students appearing in "
        "the available absence records. A complete class "
        "roster would be required to include students with "
        "zero recorded absences."
    )


# ============================================================
# 2. TREND ANALYSIS
# ============================================================

elif page == "📈 Trend Analysis":

    st.header(
        "📈 Absenteeism Trend Analysis"
    )

    st.markdown(
        '<span class="ai-badge">📊 PATTERN ANALYTICS</span>',
        unsafe_allow_html=True
    )

    st.write("")


    st.info(
        "Moving averages smooth daily fluctuations and help "
        "highlight the broader absenteeism pattern."
    )


    trend_data = working_data.copy()


    trend_data["AVG_3"] = (
        trend_data[
            "NO.OF.ABSENTEES"
        ]
        .rolling(3)
        .mean()
    )


    trend_data["AVG_7"] = (
        trend_data[
            "NO.OF.ABSENTEES"
        ]
        .rolling(7)
        .mean()
    )


    fig = go.Figure()


    fig.add_trace(
        go.Scatter(
            x=trend_data["DATE"],
            y=trend_data[
                "NO.OF.ABSENTEES"
            ],
            mode="lines+markers",
            name="Daily Absence"
        )
    )


    fig.add_trace(
        go.Scatter(
            x=trend_data["DATE"],
            y=trend_data["AVG_3"],
            mode="lines",
            name="3-Day Average"
        )
    )


    fig.add_trace(
        go.Scatter(
            x=trend_data["DATE"],
            y=trend_data["AVG_7"],
            mode="lines",
            name="7-Day Average"
        )
    )


    fig.update_layout(
        height=510,
        template="plotly_white",
        hovermode="x unified",
        xaxis_title="Date",
        yaxis_title="Number of Absentees"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.markdown(
        '<div class="section-title">'
        '📅 Weekday Behaviour'
        '</div>',
        unsafe_allow_html=True
    )


    weekday_avg = (
        working_data
        .groupby("DAY")[
            "NO.OF.ABSENTEES"
        ]
        .agg(
            Average="mean",
            Maximum="max",
            Working_Days="count"
        )
        .reset_index()
    )


    weekday_avg["Average"] = (
        weekday_avg["Average"]
        .round(2)
    )


    fig2 = px.bar(
        weekday_avg,
        x="DAY",
        y="Average",
        text="Average",
        title="Average Absentees by Weekday"
    )


    fig2.update_traces(
        textposition="outside"
    )


    fig2.update_layout(
        height=430,
        template="plotly_white",
        yaxis_title="Average Absentees"
    )


    st.plotly_chart(
        fig2,
        use_container_width=True
    )


    st.dataframe(
        weekday_avg,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# 3. XGBOOST FORECAST
# ============================================================

elif page == "🔮 XGBoost Forecast":

    st.header(
        "🔮 XGBoost Absenteeism Forecast"
    )

    st.markdown(
        '<span class="ai-badge">🤖 AI FORECAST ENGINE</span>',
        unsafe_allow_html=True
    )

    st.write("")


    st.markdown(
        """
        <div class="insight-card">

        <div class="insight-title">
        🎯 Forecast Objective
        </div>

        <div class="insight-text">
        Generate a model-based estimate of the expected number
        of absentees using historical absenteeism patterns.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")


    latest_date = (
        working_data["DATE"].max()
    )


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "📅 Latest Recorded Date",
            latest_date.strftime(
                "%d %b %Y"
            )
        )


    with col2:

        st.metric(
            "📊 Historical Average",
            f"{average_absence:.2f}"
        )


    st.divider()


    selected_date = st.date_input(
        "📅 Select future date",

        value=(
            latest_date
            + pd.Timedelta(days=1)
        ).date(),

        min_value=(
            latest_date
            + pd.Timedelta(days=1)
        ).date()
    )


    selected_date = pd.Timestamp(
        selected_date
    )


    if selected_date.dayofweek == 6:

        st.warning(
            "🏖️ Sunday is treated as a college holiday. "
            "No absenteeism prediction is generated."
        )

        st.metric(
            "College Status",
            "🏖️ HOLIDAY"
        )


    else:

        st.success(
            f"📚 {selected_date.strftime('%A')} — "
            "treated as a possible working day."
        )


        if st.button(
            "🔮 Generate XGBoost Forecast",
            use_container_width=True
        ):

            history = (
                working_data[
                    "NO.OF.ABSENTEES"
                ]
                .tolist()
            )


            future_dates = pd.date_range(
                start=latest_date
                + pd.Timedelta(days=1),

                end=selected_date,

                freq="D"
            )


            prediction = None


            for future_date in future_dates:

                if future_date.dayofweek == 6:
                    continue


                previous_absence = (
                    history[-1]
                )


                avg_3 = (
                    sum(history[-3:])
                    / min(
                        3,
                        len(history)
                    )
                )


                avg_7 = (
                    sum(history[-7:])
                    / min(
                        7,
                        len(history)
                    )
                )


                previous_week = (
                    history[-7]
                    if len(history) >= 7
                    else history[0]
                )


                trend = (
                    previous_absence
                    - avg_3
                )


                day_number = (
                    future_date.dayofweek
                )


                input_data = pd.DataFrame(
                    [[
                        day_number,
                        previous_absence,
                        avg_3,
                        avg_7,
                        previous_week,
                        trend
                    ]],
                    columns=features
                )


                prediction = model.predict(
                    input_data
                )[0]


                prediction = max(
                    0,
                    prediction
                )


                history.append(
                    prediction
                )


            if prediction is not None:

                st.success(
                    "✅ Forecast generated successfully!"
                )


                c1, c2, c3 = st.columns(3)


                with c1:

                    st.metric(
                        "🎯 Expected Absentees",
                        f"{prediction:.0f}"
                    )


                with c2:

                    st.metric(
                        "📊 Historical Average",
                        f"{average_absence:.2f}"
                    )


                with c3:

                    difference = (
                        prediction
                        - average_absence
                    )


                    st.metric(
                        "Difference",
                        f"{difference:+.2f}"
                    )


                if prediction >= 7:

                    st.error(
                        "🚨 Higher absenteeism level projected."
                    )

                elif prediction >= 4:

                    st.warning(
                        "⚠️ Moderate absenteeism level projected."
                    )

                else:

                    st.success(
                        "✅ Lower absenteeism level projected."
                    )


                st.markdown(
                    '<div class="section-title">'
                    '📋 Forecast Summary'
                    '</div>',
                    unsafe_allow_html=True
                )


                forecast_summary = pd.DataFrame({

                    "Metric": [
                        "Selected Date",
                        "College Status",
                        "Expected Absentees",
                        "Historical Average",
                        "Difference"
                    ],

                    "Value": [

                        selected_date.strftime(
                            "%d %B %Y"
                        ),

                        "Possible Working Day",

                        f"{prediction:.2f}",

                        f"{average_absence:.2f}",

                        f"{difference:+.2f}"
                    ]
                })


                st.dataframe(
                    forecast_summary,
                    use_container_width=True,
                    hide_index=True
                )


                st.caption(
                    "This is a model-based projection from historical "
                    "patterns. It is an estimate and not a guaranteed "
                    "future outcome."
                )


# ============================================================
# 4. STUDENT ANALYTICS
# ============================================================

elif page == "👥 Student Analytics":

    st.header(
        "👥 Student Analytics"
    )

    st.markdown(
        '<span class="ai-badge">👤 INDIVIDUAL PROFILE</span>',
        unsafe_allow_html=True
    )

    st.write("")


    st.markdown(
        "Explore recorded attendance behaviour for an individual student."
    )


    roll_numbers = (
        student_summary["ROLL_NO"]
        .astype(str)
        .tolist()
    )


    selected_roll = st.selectbox(
        "🔎 Select Student",
        roll_numbers
    )


    selected_data = student_summary[
        student_summary[
            "ROLL_NO"
        ].astype(str)
        == selected_roll
    ]


    if not selected_data.empty:

        student = (
            selected_data.iloc[0]
        )


        student_weekday_data = (
            student_weekday[
                student_weekday[
                    "ROLL_NO"
                ].astype(str)
                == selected_roll
            ]
            .copy()
        )


        st.markdown(
            f"""
            <div class="insight-card">

            <div class="insight-title">
            👤 Student Profile — Roll No. {selected_roll}
            </div>

            <div class="insight-text">
            Historical absence behaviour and calculated
            attendance indicators.
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


        st.write("")


        c1, c2, c3, c4 = st.columns(4)


        with c1:

            st.metric(
                "📊 Attendance",
                f"{student['ATTENDANCE_PERCENT']:.2f}%"
            )


        with c2:

            st.metric(
                "📅 Absence Days",
                int(
                    student[
                        "ABSENCE_DAYS"
                    ]
                )
            )


        with c3:

            st.metric(
                "📆 Most Missed Day",
                student[
                    "MOST_MISSED_DAY"
                ]
            )


        with c4:

            st.metric(
                "⚠️ Risk Level",
                student[
                    "RISK_LEVEL"
                ]
            )


        attendance = (
            student[
                "ATTENDANCE_PERCENT"
            ]
        )


        if attendance < 75:

            st.error(
                "🚨 Calculated attendance is below 75%. "
                "Higher-level attendance monitoring may be required."
            )

        elif attendance < 80:

            st.warning(
                "🟠 Calculated attendance is below 80%. "
                "Closer attendance monitoring may be useful."
            )

        elif attendance < 85:

            st.warning(
                "🟡 Calculated attendance is in the "
                "project-defined monitoring range."
            )

        else:

            st.success(
                "🟢 Calculated attendance is currently 85% or above."
            )


        st.divider()


        st.markdown(
            '<div class="section-title">'
            '📅 Student Absence Pattern'
            '</div>',
            unsafe_allow_html=True
        )


        if not student_weekday_data.empty:

            weekday_chart = (
                student_weekday_data
                .groupby("DAY")[
                    "ABSENCE_COUNT"
                ]
                .sum()
                .reset_index()
            )


            fig = px.bar(
                weekday_chart,
                x="DAY",
                y="ABSENCE_COUNT",
                text="ABSENCE_COUNT",
                title=(
                    f"Recorded Absence Frequency — "
                    f"Roll No. {selected_roll}"
                )
            )


            fig.update_traces(
                textposition="outside"
            )


            fig.update_layout(
                template="plotly_white",
                height=430
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


        st.markdown(
            '<div class="section-title">'
            '📋 Recorded Absence Dates'
            '</div>',
            unsafe_allow_html=True
        )


        records = []


        for _, row in working_data.iterrows():

            roll_list = str(
                row[
                    "ABSENTEES ROLL.NO"
                ]
            ).split(",")


            roll_list = [
                roll.strip()
                for roll in roll_list
            ]


            if selected_roll in roll_list:

                records.append({

                    "DATE":
                        row["DATE"],

                    "DAY":
                        row["DAY"],

                    "TOTAL ABSENTEES":
                        row[
                            "NO.OF.ABSENTEES"
                        ]
                })


        if records:

            records_df = (
                pd.DataFrame(records)
            )


            records_df["DATE"] = (
                pd.to_datetime(
                    records_df["DATE"]
                )
            )


            st.dataframe(
                records_df,
                use_container_width=True,
                hide_index=True
            )


        st.markdown(
            '<div class="section-title">'
            '💡 Student Pattern Insight'
            '</div>',
            unsafe_allow_html=True
        )


        absence_days = int(
            student[
                "ABSENCE_DAYS"
            ]
        )


        missed_day = (
            student[
                "MOST_MISSED_DAY"
            ]
        )


        st.info(
            f"Roll No. **{selected_roll}** has "
            f"**{absence_days} recorded absence days**. "
            f"The weekday with the highest recorded absence "
            f"frequency is **{missed_day}**."
        )


        st.caption(
            "Most Missed Weekday represents the weekday with "
            "the highest recorded absence frequency. It does "
            "not imply a guaranteed future absence."
        )


# ============================================================
# 5. EARLY WARNING
# ============================================================

elif page == "⚠️ Early Warning":

    st.header(
        "⚠️ Attendance Early Warning System"
    )

    st.markdown(
        '<span class="ai-badge">🚨 RISK MONITORING</span>',
        unsafe_allow_html=True
    )

    st.write("")


    st.info(
        "Risk levels are project-defined monitoring thresholds "
        "based on calculated attendance percentage."
    )


    c1, c2, c3 = st.columns(3)


    with c1:

        st.metric(
            "🟡 Monitor",
            monitor_count
        )


    with c2:

        st.metric(
            "🟠 High",
            high_count
        )


    with c3:

        st.metric(
            "🔴 Critical",
            critical_count
        )


    st.divider()


    warning_students = student_summary[
        student_summary[
            "ATTENDANCE_PERCENT"
        ] < 85
    ].copy()


    warning_students = (
        warning_students
        .sort_values(
            "ATTENDANCE_PERCENT"
        )
    )


    if not warning_students.empty:

        st.markdown(
            '<div class="section-title">'
            '🚨 Students Requiring Monitoring'
            '</div>',
            unsafe_allow_html=True
        )


        st.dataframe(
            warning_students[
                [
                    "ROLL_NO",
                    "ABSENCE_DAYS",
                    "ATTENDANCE_PERCENT",
                    "RISK_LEVEL",
                    "LAST_ABSENCE",
                    "MOST_MISSED_DAY"
                ]
            ],
            use_container_width=True,
            hide_index=True
        )


        st.markdown(
            '<div class="section-title">'
            '📊 Risk Distribution'
            '</div>',
            unsafe_allow_html=True
        )


        risk_counts = (
            student_summary[
                "RISK_LEVEL"
            ]
            .value_counts()
            .reset_index()
        )


        risk_counts.columns = [
            "RISK_LEVEL",
            "STUDENT_COUNT"
        ]


        fig = px.pie(
            risk_counts,
            names="RISK_LEVEL",
            values="STUDENT_COUNT",
            hole=0.50,
            title="Student Risk Distribution"
        )


        fig.update_layout(
            template="plotly_white",
            height=450
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


    else:

        st.success(
            "No students currently fall below "
            "the project monitoring threshold."
        )


    st.caption(
        "These thresholds are project-defined and should not "
        "be interpreted as official institutional attendance rules."
    )


# ============================================================
# 6. WEEKDAY PATTERNS
# ============================================================

elif page == "📅 Weekday Patterns":

    st.header(
        "📅 Weekday Absence Patterns"
    )

    st.markdown(
        '<span class="ai-badge">🧩 PATTERN DISCOVERY</span>',
        unsafe_allow_html=True
    )

    st.write("")


    st.info(
        "Explore how recorded absenteeism varies across "
        "weekdays and individual students."
    )


    pivot_data = student_weekday.pivot_table(
        index="ROLL_NO",
        columns="DAY",
        values="ABSENCE_COUNT",
        aggfunc="sum",
        fill_value=0
    )


    fig = px.imshow(
        pivot_data,
        title="Student × Weekday Absence Heatmap",
        labels={
            "x": "Weekday",
            "y": "Roll Number",
            "color": "Recorded Absences"
        },
        aspect="auto"
    )


    fig.update_layout(
        height=650,
        template="plotly_white"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.markdown(
        '<div class="section-title">'
        '📊 Weekday Summary'
        '</div>',
        unsafe_allow_html=True
    )


    weekday_summary = (
        working_data
        .groupby("DAY")[
            "NO.OF.ABSENTEES"
        ]
        .agg(
            Average="mean",
            Maximum="max",
            Working_Days="count"
        )
        .reset_index()
    )


    weekday_summary["Average"] = (
        weekday_summary[
            "Average"
        ]
        .round(2)
    )


    st.dataframe(
        weekday_summary,
        use_container_width=True,
        hide_index=True
    )


    csv_data = (
        weekday_summary
        .to_csv(index=False)
    )


    st.download_button(
        "📥 Download Weekday Summary",
        data=csv_data,
        file_name="weekday_absenteeism_summary.csv",
        mime="text/csv"
    )


# ============================================================
# 7. MODEL ANALYSIS
# ============================================================

elif page == "🔍 Model Analysis":

    st.header(
        "🔍 XGBoost Model Analysis"
    )

    st.markdown(
        '<span class="ai-badge">🧠 MODEL INTELLIGENCE</span>',
        unsafe_allow_html=True
    )

    st.write("")


    predictions = pd.read_csv(
        "model_predictions.csv"
    )


    importance = pd.read_csv(
        "feature_importance.csv"
    )


    predictions["DATE"] = (
        pd.to_datetime(
            predictions["DATE"]
        )
    )


    c1, c2, c3 = st.columns(3)


    with c1:

        st.metric(
            "MAE",
            f"{model_package['mae']:.2f}"
        )


    with c2:

        st.metric(
            "RMSE",
            f"{model_package['rmse']:.2f}"
        )


    with c3:

        st.metric(
            "R²",
            f"{model_package['r2']:.2f}"
        )


    st.info(
        "The model uses a time-based train/test split. "
        "Because the available dataset and test set are small, "
        "these metrics should be treated as an initial evaluation."
    )


    st.divider()


    st.markdown(
        '<div class="section-title">'
        '🎯 Actual vs Predicted'
        '</div>',
        unsafe_allow_html=True
    )


    fig = go.Figure()


    fig.add_trace(
        go.Scatter(
            x=predictions["DATE"],
            y=predictions[
                "ACTUAL_ABSENTEES"
            ],
            mode="lines+markers",
            name="Actual"
        )
    )


    fig.add_trace(
        go.Scatter(
            x=predictions["DATE"],
            y=predictions[
                "PREDICTED_ABSENTEES"
            ],
            mode="lines+markers",
            name="Predicted"
        )
    )


    fig.update_layout(
        height=460,
        template="plotly_white",
        hovermode="x unified",
        xaxis_title="Date",
        yaxis_title="Absentees"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.markdown(
        '<div class="section-title">'
        '📋 Prediction Details'
        '</div>',
        unsafe_allow_html=True
    )


    display_predictions = (
        predictions.copy()
    )


    display_predictions[
        "PREDICTED_ABSENTEES"
    ] = (
        display_predictions[
            "PREDICTED_ABSENTEES"
        ].round(2)
    )


    st.dataframe(
        display_predictions,
        use_container_width=True,
        hide_index=True
    )


    st.markdown(
        '<div class="section-title">'
        '🧠 Feature Importance'
        '</div>',
        unsafe_allow_html=True
    )


    importance = (
        importance
        .sort_values(
            "IMPORTANCE",
            ascending=True
        )
    )


    fig2 = px.bar(
        importance,
        x="IMPORTANCE",
        y="FEATURE",
        orientation="h",
        text="IMPORTANCE",
        title="XGBoost Feature Importance"
    )


    fig2.update_traces(
        texttemplate="%{text:.3f}",
        textposition="outside"
    )


    fig2.update_layout(
        height=450,
        template="plotly_white"
    )


    st.plotly_chart(
        fig2,
        use_container_width=True
    )


    st.caption(
        "Feature importance indicates the contribution of "
        "input features to the trained model. It does not "
        "establish causation."
    )


    st.download_button(
        "📥 Download Model Predictions",
        data=predictions.to_csv(
            index=False
        ),
        file_name="xgboost_model_predictions.csv",
        mime="text/csv"
    )


# ============================================================
# 8. AUTOMATIC INSIGHTS
# ============================================================

elif page == "💡 Automatic Insights":

    st.header(
        "💡 Automatic Data Insights"
    )

    st.markdown(
        '<span class="ai-badge">✨ AI-STYLE INSIGHT ENGINE</span>',
        unsafe_allow_html=True
    )

    st.write("")


    st.markdown(
        """
        <div class="insight-card">

        <div class="insight-title">
        🧠 What the system analyses
        </div>

        <div class="insight-text">

        The insight engine automatically examines recent
        absenteeism, weekday patterns, peak absence days,
        frequent recorded absences and attendance monitoring.

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")


    recent = working_data.tail(5)

    previous = working_data.iloc[-10:-5]


    recent_avg = (
        recent[
            "NO.OF.ABSENTEES"
        ].mean()
    )


    previous_avg = (
        previous[
            "NO.OF.ABSENTEES"
        ].mean()
    )


    if recent_avg > previous_avg:

        st.warning(
            f"📈 Recent absenteeism is higher than the "
            f"previous comparison period "
            f"({recent_avg:.2f} vs {previous_avg:.2f})."
        )


    elif recent_avg < previous_avg:

        st.success(
            f"📉 Recent absenteeism is lower than the "
            f"previous comparison period "
            f"({recent_avg:.2f} vs {previous_avg:.2f})."
        )


    else:

        st.info(
            "➡️ Recent absenteeism is relatively stable "
            "compared with the previous period."
        )


    weekday_avg = (
        working_data
        .groupby("DAY")[
            "NO.OF.ABSENTEES"
        ]
        .mean()
        .sort_values(
            ascending=False
        )
    )


    top_day = (
        weekday_avg.index[0]
    )


    top_day_avg = (
        weekday_avg.iloc[0]
    )


    st.info(
        f"📅 **{top_day}** has the highest average "
        f"recorded absenteeism at approximately "
        f"**{top_day_avg:.2f} students**."
    )


    st.warning(
        f"🚨 The highest recorded daily absenteeism was "
        f"**{highest_absence} students** on "
        f"**{highest_date.strftime('%d %B %Y')}**."
    )


    st.markdown(
        '<div class="section-title">'
        '👥 Frequent Recorded Absence'
        '</div>',
        unsafe_allow_html=True
    )


    top_students = (
        student_summary
        .sort_values(
            "ABSENCE_DAYS",
            ascending=False
        )
        .head(5)
    )


    for _, row in top_students.iterrows():

        st.write(
            f"• **Roll No. {row['ROLL_NO']}** — "
            f"{int(row['ABSENCE_DAYS'])} recorded absence days — "
            f"{row['ATTENDANCE_PERCENT']:.2f}% calculated attendance"
        )


    st.markdown(
        '<div class="section-title">'
        '⚠️ Attendance Monitoring'
        '</div>',
        unsafe_allow_html=True
    )


    if monitor_count > 0:

        st.warning(
            f"**{monitor_count} students** are currently "
            f"in the project-defined monitoring range."
        )


    else:

        st.success(
            "No students are currently in the monitoring range."
        )


    st.divider()


    st.markdown(
        """
        <div class="insight-card">

        <div class="insight-title">
        ℹ️ Interpretation Note
        </div>

        <div class="insight-text">

        These insights describe patterns in the available
        historical data. They do not establish causal reasons
        for absence. The current dataset does not contain
        absence-reason information.

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

<strong>🎓 EduAI — Student Absenteeism Intelligence</strong>

<br><br>

AI-Based Attendance Analytics • XGBoost Forecasting •
Student Monitoring • Early Warning

<br><br>

Python • Pandas • XGBoost • Plotly • Streamlit

</div>
""", unsafe_allow_html=True)

