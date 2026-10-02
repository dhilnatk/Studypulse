import streamlit as st 
from datetime import date 
st.title("📚studypulse")
st.write("🎯Your Smart Exam Readiness Analyzer")
name = st.text_input("What Is Your Name")
if name:
    st.success(f"Welcome to StudyPulse, {name}! 👏")
subject = st.selectbox(
   "Choose Your Subjects",
   ["Computer Networks","Machine Learning","Robotics","Big Data Analytics","Software Project Management"]
)
progress = st.slider(
   "📖 How Much Of This Subject Have You Completed?",
    0,
    100,
    50
)
study_hours = st.slider(
   "⏰ How Many Hours Do You Study This Subject Per Day?",
       0.0,
       12.0,
       2.0
)
exam_date = st.date_input(
  "🗓️ When is your exam?",
)
test_score = st.slider(
  "📝 What Is Your Latest Test Score?",
  0,
  100,
  50
)
confidence = st.slider(
 "🧠 How Confident Are You In This Subject?",
   0,
   10,
   5
)
readiness_score = ( 
    progress * 0.40 + test_score * 0.30 + confidence * 10* 0.20 + min(study_hours/10*100,100)*0.10
)
st.subheader("🎯Your Exam Readiness Score")
st.metric(
  "Readiness Score",
  f"{readiness_score:.1f}/100"
)
if readiness_score>=80:
   st.success("🟢WELL PREPARED!")
elif readiness_score>=50:
   st.warning("🟡ALMOST READY - keep studying!")
else:
   st.error("🔴 NEEDS MORE PREPARATION")
st.subheader("💡YOUR STUDY RECOMMENDATION")
if progress<50:
  st.info("📖FOCUS ON COMPLETING MORE OF YOUR SYLLABUS")
elif test_score<50:
  st.info("📝 FOCUS MORE ON PRACTICE AND SOLVING TEST")
elif confidence<5:
  st.info("🧠 REVISE THE TOPICS YOU FEEL LESS CONFIDENT ABOUT")
else:
  st.success("✨YOU'RE DOING WELL! KEEP MAINTAINING YOUR CURRENT STUDY ROUTINE")
days_remaining=(exam_date-date.today()).days
st.subheader("🗓️ EXAM COUNTDOWN")
if days_remaining>=0:
   st.metric("DAYS UNTIL EXAM",days_remaining)
else:
   st.warning("⚠️THE EXAM DATE HAS ALREADY PASSED")

























