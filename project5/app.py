import streamlit as st
import joblib
import numpy as np
import pandas as pd

# ---------------- Page Config ---------------- #
st.set_page_config(page_title="Placement Predictor", page_icon="🎓", layout="centered")

# ---------------- Custom UI ---------------- #
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #eef2ff, #f5f3ff);
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Load Model ---------------- #
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# ---------------- Load Dataset ---------------- #
df = pd.read_csv("Dataset/placedata v2.0 synthetic.csv")

# 🔥 FIX
df['PlacementStatus'] = df['PlacementStatus'].map({'Placed':1, 'NotPlaced':0})

# ---------------- Session ---------------- #
if "prob" not in st.session_state:
    st.session_state.prob = None
    st.session_state.level = None
    st.session_state.suggestions = None
    st.session_state.inputs = None

# ---------------- Skill Gap ---------------- #
def skill_gap(input_data):
    suggestions = []
    
    if input_data['CGPA'] < 7:
        suggestions.append("📚 Improve CGPA")
    if input_data['Internships'] == 0:
        suggestions.append("💼 Do internship")
    if input_data['Projects'] < 2:
        suggestions.append("🛠️ Build 2-3 strong projects")
    if input_data['AptitudeTestScore'] < 70:
        suggestions.append("🧠 Practice aptitude daily")
    if input_data['SoftSkillsRating'] < 3:
        suggestions.append("🗣️ Improve communication skills")
    if input_data['PlacementTraining'] == 0:
        suggestions.append("🎯 Join mock interviews / training")

    return suggestions


def analyze_student(input_data, probability):
    suggestions = skill_gap(input_data)
    
    if probability < 0.5:
        level = "🔴 High Risk"
    elif probability < 0.75:
        level = "🟡 Moderate"
    else:
        level = "🟢 Good Chance"
    
    return level, suggestions

# ---------------- Header ---------------- #
st.markdown("<h1 style='text-align:center;color:#4f46e5;'>🎓 Placement Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Analyze your placement chances 🚀</p>", unsafe_allow_html=True)

# ---------------- Tabs ---------------- #
tab1, tab2, tab3 = st.tabs(["🏠 Home", "📊 Prediction", "📈 Data Insights"])

# ================= HOME ================= #
with tab1:
    st.subheader("📥 Enter Your Details")

    col1, col2 = st.columns(2)

    with col1:
        cgpa = st.slider("CGPA", 0.0, 10.0)
        internships = st.number_input("Internships", 0, 5)
        projects = st.number_input("Projects", 0, 5)
        workshops = st.number_input("Workshops", 0, 5)
        aptitude = st.slider("Aptitude Score", 0, 100)

    with col2:
        softskills = st.slider("Soft Skills", 1, 5)
        extracurricular = st.selectbox("Extracurricular", [0,1])
        training = st.selectbox("Placement Training", [0,1])
        ssc = st.slider("SSC Marks", 0, 100)
        hsc = st.slider("HSC Marks", 0, 100)

    if st.button("🚀 Predict Placement"):

        user_data = np.array([[cgpa, internships, projects, workshops,
                               aptitude, softskills,
                               extracurricular, training,
                               ssc, hsc]])

        user_scaled = scaler.transform(user_data)
        prob = model.predict_proba(user_scaled)[0][1]

        user_dict = {
            'CGPA': cgpa,
            'Internships': internships,
            'Projects': projects,
            'AptitudeTestScore': aptitude,
            'SoftSkillsRating': softskills,
            'PlacementTraining': training
        }

        level, suggestions = analyze_student(user_dict, prob)

        st.session_state.prob = prob
        st.session_state.level = level
        st.session_state.suggestions = suggestions
        st.session_state.inputs = user_dict

        st.success("✅ Prediction done! Go to Prediction tab")

# ================= PREDICTION ================= #
with tab2:

    if st.session_state.prob is None:
        st.warning("⚠️ Please enter data in Home tab first")
    else:
        prob = st.session_state.prob
        level = st.session_state.level
        suggestions = st.session_state.suggestions
        inputs = st.session_state.inputs

        # 🔥 ADVANCED RESULT UI
        st.markdown("## 🎯 Placement Analysis")

        if prob >= 0.75:
            st.success(f"🚀 Excellent! {round(prob*100,2)}% chance of placement")
        elif prob >= 0.5:
            st.warning(f"⚠️ Moderate chance: {round(prob*100,2)}%")
        else:
            st.error(f"❌ Low chance: {round(prob*100,2)}%")

        st.progress(prob)

        # 🔥 WHY THIS RESULT
        st.subheader("📊 Why this prediction?")

        if inputs['CGPA'] < 7:
            st.error("❌ Low CGPA")
        if inputs['Internships'] == 0:
            st.error("❌ No Internship")
        if inputs['Projects'] < 2:
            st.error("❌ Less Projects")
        if inputs['AptitudeTestScore'] < 70:
            st.error("❌ Low Aptitude")

        # 🔥 ROADMAP
        st.subheader("🛠️ Your Personalized Roadmap")
        for i, s in enumerate(suggestions, 1):
            st.write(f"👉 Step {i}: {s}")

        # 🔥 COMPARISON
        st.subheader("🏆 Compare with Top Students")

        top_avg = df[df['PlacementStatus']==1].mean(numeric_only=True)

        st.write("Top CGPA:", round(top_avg['CGPA'],2))
        st.write("Your CGPA:", inputs['CGPA'])

        if inputs['CGPA'] < top_avg['CGPA']:
            st.warning("⚠️ Below top performers")
        else:
            st.success("🔥 Competitive level")

# ================= DATA INSIGHTS ================= #
with tab3:

    st.subheader("📈 Data Analytics Dashboard")

    st.write("### 📊 Placement Distribution")
    st.bar_chart(df['PlacementStatus'].value_counts())

    st.write("### 📊 CGPA Impact")
    st.bar_chart(df.groupby('PlacementStatus')['CGPA'].mean())

    st.write("### 📊 Internship Impact")
    st.bar_chart(df.groupby('Internships')['PlacementStatus'].mean())

    st.write("### 🔥 Important Factors")
    corr = df.corr(numeric_only=True)['PlacementStatus'].sort_values(ascending=False)
    st.bar_chart(corr)