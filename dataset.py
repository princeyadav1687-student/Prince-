from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(
    page_title="AI-Powered Student Analytics",
    page_icon="🎓",
    layout="wide"
)

with st.sidebar:

    st.image("https://img.icons8.com/color/96/artificial-intelligence.png", width=80)

    st.markdown(
        """
        <h2 style='text-align:center;color:#4F8BF9;'>
        🎓 AI Student Analytics
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    menu = option_menu(
        menu_title="Navigation",
        options=[
            "Home",
            "Dataset Overview",
            "Exploratory Data Analysis",
            "Student Demographics",
            "AI Usage Analysis",
            "Academic Performance",
            "Study Habits",
            "Mental Health Analysis",
            "Correlation Analysis",
            "Key Insights",
            "Technologies Used",
            "Conclusion",
            "About"
        ],

        icons=[
            "house-fill",
            "database-fill",
            "bar-chart-fill",
            "people-fill",
            "robot",
            "graph-up-arrow",
            "book-fill",
            "emoji-smile-fill",
            "diagram-3-fill",
            "cpu-fill",
            "magic",
            "lightbulb-fill",
            "clipboard-check-fill",
            "person-circle"
        ],

        menu_icon="mortarboard-fill",
        default_index=0,
        styles={
            "container":{
                "padding":"5!important",
                "background-color":"#F8F9FA"
            },
            "icon":{
                "color":"#4F8BF9",
                "font-size":"18px"
            },
            "nav-link":{
                "font-size":"15px",
                "text-align":"left",
                "margin":"2px",
                "--hover-color":"#D6EAF8",
            },
            "nav-link-selected":{
                "background-color":"#4F8BF9",
                "color":"white",
            },
        }
    )

    st.divider()

if menu == "Home":
 st.set_page_config(
    page_title="AI Impact on Students",
    page_icon="🤖",
    layout="wide"
)

 st.markdown("""
<div style="
padding:18px;
border-radius:12px;
background:#f4f6fb;
border-left:6px solid #4F46E5;
margin-bottom:25px;">
<h1 style="margin:0;color:#222;">🎓 AI Impact on Students </h1>
<p style="margin-top:8px;color:#555;font-size:17px;">
Explore how Artificial Intelligence influences students' learning, academic performance and study habits.
</p>
</div>
""", unsafe_allow_html=True)
 

 image = Image.open("ai.jpg")
 st.image(image)
 
 left,right=st.columns([2,1])

 with left:

    st.markdown("## 📖 About This Project")

    st.info("""
• Explore the growing influence of Artificial Intelligence on students' learning behavior.

• Analyze how AI impacts academic performance, study habits, and time management.

• Evaluate the balance between AI-assisted learning and independent critical thinking.

• Identify trends related to stress levels, learning efficiency, and digital education.

• Transform real-world student data into meaningful insights through interactive dashboards and visual analytics.

• Provide evidence-based observations that encourage responsible and effective use of AI in education.
""")
 with right:

    st.markdown("## 🎯 Objectives")

    st.success("""
✅ Analyze AI Usage

✅ Study Behaviour

✅ Academic Performance

✅ Mental Health

✅ Learning Efficiency

✅ Responsible AI Adoption

✅ Data-driven Insights
""")
    st.divider()
# -----------------------------
# Progress
# -----------------------------

 left,right=st.columns(2)

 with left:

    st.markdown("### 📈 Dataset")

    st.progress(100)

    st.success("Dataset is Clean and Ready for Analysis")

    st.metric("Data Quality","100%")

 with right:

    st.markdown("### 🤖 AI Learning Insights")

    st.info("""
✔ 50,000 Student Records

✔ AI Usage Analysis

✔ Academic Performance

✔ Mental Health Impact

✔ Personalized Learning

✔ Interactive Visualizations
 """)

 st.write("")

 st.markdown("## 🚀 What You Can Explore")

 c1, c2, c3 = st.columns(3)

 with c1:
    with st.container(border=True):
        st.subheader("📊 Exploratory Analysis")
        st.success("✔ Dataset Overview")
        st.info("✔ Missing Values")
        st.info("✔ Summary Statistics")
        st.success("✔ Correlation Analysis")

 with c2:
    with st.container(border=True):
        st.subheader("📈 Interactive Charts")
        st.warning("✔ Pie Charts")
        st.success("✔ Histograms")
        st.info("✔ Heatmaps")
        st.warning("✔ Scatter Plots")

 with c3:
    with st.container(border=True):
        st.subheader("🤖 AI Analytics")
        st.success("✔ AI Usage Analysis")
        st.info("✔ GPA Prediction")
        st.warning("✔ Student Clustering")
        st.success("✔ Performance Analysis")
 st.write("")


 st.markdown("## 🌍 Why This Project Matters")

 st.markdown("""
###### Artificial Intelligence is transforming education worldwide. This dashboard helps educators, researchers, and students understand:

- 🤖 AI adoption in education
- 📚 Learning outcomes
- 🎯 Student engagement
- 💡 Personalized learning
- 📈 Academic performance
- ⚠️ Challenges and ethical concerns
""")

 st.write("")
 st.write("")

elif menu =="Dataset Overview":
  st.title("📊 Dataset Overview")
  st.markdown("Explore the structure and quality of the **AI Impact on Students** dataset.")

  st.divider()

# Load dataset
  df = pd.read_csv(r"ai_student_impact.csv") 

  col1, col2, col3, col4 = st.columns(4)

  with col1:
    st.metric("📄 Total Records", f"{len(df):,}")

  with col2:
    st.metric("📌 Features", df.shape[1])

  with col3:
    st.metric("❌ Missing Values", int(df.isnull().sum().sum()))

  with col4:
    st.metric("🔁 Duplicate Rows", int(df.duplicated().sum()))

  st.divider()
  
  left, right = st.columns([2,1])

  with left:

    st.subheader("📋 Dataset Preview")

    rows = st.slider(
        "Select number of rows",
        5,
        30,
        10
    )

    st.dataframe(
        df.head(rows),
        use_container_width=True,
        height=350
    )

  with right:

    st.subheader("📂 Dataset Shape")

    st.info(f"""
Rows : **{df.shape[0]}**

Columns : **{df.shape[1]}**
""")

    st.subheader("💾 Memory Usage")

    memory = df.memory_usage(deep=True).sum()/1024**2

    st.success(f"{memory:.2f} MB")

    st.divider()

   

# ==========================
# MISSING VALUES
# ==========================

    st.subheader("🚨 Missing Values")

    missing = df.isnull().sum().reset_index()

    missing.columns=["Column","Missing"]

    missing = missing[missing["Missing"]>0]

    if len(missing)==0:

     st.success("✅ No Missing Values Found!")

    
    st.divider()


    st.set_page_config(
    page_title="AI Impact on Students",
    layout="wide"
)
  st.subheader("📑 Feature Summary")

  summary = pd.DataFrame({

    "Column":df.columns,

    "Datatype":df.dtypes,

    "Unique":df.nunique()

})

  st.dataframe(summary,use_container_width=True)

  st.divider()
  with st.expander("💡 Quick Dataset Insights", expanded=True):

     st.write(f"• Number of observations: **{df.shape[0]}**")

     st.write(f"• Number of variables: **{df.shape[1]}**")
  
     st.write(f"• Numerical features: **{len(df.select_dtypes('number').columns)}**")

     st.write(f"• Categorical features: **{len(df.select_dtypes('object').columns)}**")

     st.write(f"• Missing values: **{df.isnull().sum().sum()}**")

     st.write(f"• Duplicate rows: **{df.duplicated().sum()}**")

elif menu =="Exploratory Data Analysis":
 st.set_page_config(page_title="Exploratory Data Analysis",
                   page_icon="🤖",
                   layout="wide")

 df = pd.read_csv(r"ai_student_impact.csv")
 st.markdown("""
## 🧠 AI Exploratory Data Analysis
""")

 st.subheader("📑 Dataset Statistics")

 st.dataframe(df.describe(include="all"),use_container_width=True)

 st.divider()

 col1,col2=st.columns([2,1])

 with col1:

    st.markdown(f"""
    <div class="insight">

### 🧠 AI Dataset Report

✅ <b>Total Records</b> : {df.shape[0]}<br><br>

✅ <b>Total Features</b> : {df.shape[1]}<br><br>

⚠️ <b>Missing Values</b> : {df.isnull().sum().sum()}<br><br>

🔁 <b>Duplicate Rows</b> : {df.duplicated().sum()}<br><br>

📈 <b>Dataset Quality Score</b> :
{"🟢 Excellent" if df.isnull().sum().sum()==0 else "🟡 Needs Cleaning"}

</div>
 """,unsafe_allow_html=True)

 with col2:

    st.subheader("🔍 Feature Explorer")
    feature=st.selectbox("Select Feature",df.columns)
    left, right = st.columns([1, 1])

    with left:
     st.info("📈 Summary Statistics")
     st.dataframe(
        df[feature].describe().to_frame(name="Value"),
        use_container_width=True
    )

    with right:
     st.info("📊 Value Distribution")
     st.dataframe(
        df[feature].value_counts().reset_index().rename(
            columns={"index": feature, feature: "Count"}
        ),
        use_container_width=True
    )
 st.divider()

# ---------------- Expandable AI Summary ---------------- #

 with st.expander("🤖 Click to View Summary"):

    st.success("""
### Observations

✔ Dataset loaded successfully.

✔ Ready for preprocessing and visualization.

✔ Numeric and categorical features are identified.

✔ Missing values should be handled before model training.

✔ Duplicate records should be removed to improve accuracy.
""")
    
#Student Demographics
elif menu =="Student Demographics":
 st.title("👨‍🎓 Student Demographics")
 st.markdown("### Explore the demographic profile of students")

# Load Dataset
 df = pd.read_csv(r"ai_student_impact.csv") 

 
 Prompt_Engineering_Skill = st.multiselect(
    "🎯 Prompt Engineering Skill",
    options=df["Prompt_Engineering_Skill"].unique(),
    default=df["Prompt_Engineering_Skill"].unique()
)

 Major_Category = st.multiselect(
    "🎓 Major Category",
    options=df["Major_Category"].unique(),
    default=df["Major_Category"].unique()
)

 filtered_df = df[
    (df["Prompt_Engineering_Skill"].isin(Prompt_Engineering_Skill)) &
    (df["Major_Category"].isin(Major_Category))
]
 col1, col2, col3 = st.columns(3)

 with col1:
    st.metric("👥 Students", len(filtered_df))

 with col2:
    st.metric("🎓 Major Category",
              filtered_df["Major_Category"].nunique())

 with col3:
    st.metric("🌍 Weekly GenAI Hours",
              filtered_df["Weekly_GenAI_Hours"].nunique())

 st.divider()

 left, right = st.columns(2)

 with left:
    st.subheader("🤖 GenAI Usage by Primary Purpose")

 
    purpose_count = (
    filtered_df["Primary_Use_Case"]
    .value_counts()
    .reset_index()
)

    purpose_count.columns = ["Primary_Use_Case", "Count"]

    fig = px.pie(
    purpose_count,
    names="Primary_Use_Case",
    values="Count",
    hole=0.4
)

    st.plotly_chart(fig, use_container_width=True)

 with right:
    st.subheader("📚 Weekly AI Hours vs Traditional Study Hours")

    fig = px.scatter(
    filtered_df,
    x="Weekly_GenAI_Hours",
    y="Traditional_Study_Hours",
    color="Burnout_Risk_Level",
    template="simple_white"
)
    st.plotly_chart(fig, use_container_width=True)

 st.divider()

 left, right = st.columns(2)

 with left:
 
    st.subheader("🎓 Education Level")

    edu = filtered_df["Prompt_Engineering_Skill"].value_counts().reset_index()

    edu.columns = ["Education", "Students"]

    fig = px.bar(
        edu,
        x="Education",
        y="Students",
        color="Students",
        text="Students",
        color_continuous_scale="Turbo"
    )

    st.plotly_chart(fig, use_container_width=True)

 with right:

    st.subheader("📚 Field of Study")

    field = filtered_df["Major_Category"].value_counts().reset_index()

    field.columns = ["Field", "Students"]

    fig = px.treemap(
        field,
        path=["Field"],
        values="Students",
        color="Students",
        color_continuous_scale="Viridis"
    )

    st.plotly_chart(fig, use_container_width=True)

 st.divider()

# ---------------- COUNTRY ----------------
 
 st.subheader("🔥Burnout Risk Level")

 Burnout_Risk_Level = filtered_df["Burnout_Risk_Level"].value_counts().reset_index()

 Burnout_Risk_Level.columns = ["Burnout_Risk_Level", "Students"]

 fig = px.bar(
    Burnout_Risk_Level,
    x="Burnout_Risk_Level",
    y="Students",
    color="Students",
    text="Students",
    color_continuous_scale="Rainbow"
)

 st.plotly_chart(fig, use_container_width=True)

 st.divider()

# AI usuage analysis
elif menu =="AI Usage Analysis":
  st.header("⚡📊AI Usage Analysis")

  st.subheader("🤖 AI Usage by Primary Purpose")

  df = pd.read_csv(r"ai_student_impact.csv")
  filtered_df = df.copy()
  
  purpose = (
    filtered_df["Primary_Use_Case"]
    .value_counts()
    .reset_index()
)

  purpose.columns = ["Primary_Use_Case", "Students"]

  fig = px.bar(
    purpose,
    x="Primary_Use_Case",
    y="Students",
    color="Students",
    text="Students",
    color_continuous_scale="Turbo"
)

  fig.update_traces(
    textposition="outside",
    marker_line_width=2
)

  fig.update_layout(
    xaxis_title="Primary Use Case",
    yaxis_title="Number of Students",
    height=500
)

  st.plotly_chart(fig, use_container_width=True)

  st.subheader("📊 Weekly AI Usage Analysis")

  fig = px.scatter(
    filtered_df,
    x="Weekly_GenAI_Hours",
    y="Traditional_Study_Hours",
    color="Perceived_AI_Dependency",
    template="plotly_white"
)

  fig.update_layout(
    height=500
)

  st.plotly_chart(fig, use_container_width=True)

  st.subheader("🤖 Student AI Dependency Distribution")

# Create dependency categories
  filtered_df["AI_Dependency_Level"] = pd.cut(
    filtered_df["Perceived_AI_Dependency"],
    bins=[0, 3, 7, 10],
    labels=["Low", "Moderate", "High"]
)

# Count students in each category
  dependency = (
    filtered_df["AI_Dependency_Level"]
    .value_counts()
    .reset_index()
)

  dependency.columns = ["Dependency Level", "Students"]

  fig = px.pie(
    dependency,
    names="Dependency Level",
    values="Students",
    hole=0.45,
    color="Dependency Level",
    color_discrete_sequence=px.colors.qualitative.Set2,
  )

  fig.update_traces(
    textposition="inside",
    textinfo="percent+label",
    hovertemplate="<b>%{label}</b><br>Students: %{value}<br>Percentage: %{percent}<extra></extra>"
)

  fig.update_layout(
    height=500,
    legend_title="Dependency Level"
)

  st.plotly_chart(fig, use_container_width=True)

  st.subheader("🔥 Relationship Between AI Use Cases and Prompt Engineering Skills")

  heat = filtered_df.pivot_table(
    values="Weekly_GenAI_Hours",
    index="Prompt_Engineering_Skill",
    columns="Primary_Use_Case",
    aggfunc="mean"
)

  fig = px.imshow(
    heat,
    text_auto=".1f",
    color_continuous_scale="Turbo",
    aspect="auto"
)

  fig.update_layout(height=500)

  st.plotly_chart(fig, use_container_width=True)
  st.markdown("""
              <h3 style="color:#1A237E;">📊 Key Observations</h3>

<ul style="font-size:17px; line-height:1.8; color:#333;">
<li>🔧 <b>Debugging/Troubleshooting</b> is the most common AI use, with <b>12,295 students</b>.</li>
<li>✍️ <b>Copywriting/Drafting</b> follows closely, used by <b>12,011 students</b>.</li>
<li>💡 <b>Ideation</b> is also popular, helping <b>10,721 students</b> generate creative ideas.</li>
<li>📖 <b>Summarizing & Reading</b> is used by <b>8,633 students</b> for faster learning.</li>
<li>💬 <b>Direct Answer Generation</b> has the lowest usage (<b>6,340 students</b>), showing students prefer AI as a learning assistant rather than just receiving answers.</li>
<li>🚀 Overall, AI is primarily used to improve productivity, problem-solving, and learning efficiency.</li>

</ul>
</div>
""", unsafe_allow_html=True)
#Academic Performance
elif menu =="Academic Performance":
  st.header("🎓 Academic Performance Comparison")
  st.subheader("📊 Average Academic Performance")
  df = pd.read_csv(r"ai_student_impact.csv")
  filtered_df = df.copy()
  gpa = {
    "Semester": ["Pre Semester GPA", "Post Semester GPA"],
    "Average GPA": [
        filtered_df["Pre_Semester_GPA"].mean(),
        filtered_df["Post_Semester_GPA"].mean()
    ]
}

  gpa_df = pd.DataFrame(gpa)

  fig = px.bar(
    gpa_df,
    x="Semester",
    y="Average GPA",
    text="Average GPA",
    color="Semester",
    color_discrete_sequence=[
        "#6C63FF",   # Purple
        "#FF6B6B"    # Coral Red
    ]
)

  fig.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside",
    marker_line_color="white",
    marker_line_width=3
)
  fig.update_traces(
    textfont=dict(size=16)
)
  fig.update_layout(
    
    height=520,
    xaxis_title="📚Semester",
    yaxis_title="📈Average GPA",
    yaxis=dict(range=[0, 4.5]),
    template="plotly_white",
    showlegend=False,
    font=dict(size=15)
)

  st.plotly_chart(fig, use_container_width=True)
  st.subheader("📈 Average GPA by Year of Study")

  trend = (
    filtered_df
    .groupby("Year_of_Study")[["Pre_Semester_GPA","Post_Semester_GPA"]]
    .mean()
    .reset_index()
)

  fig = px.line(
    trend,
    x="Year_of_Study",
    y=["Pre_Semester_GPA","Post_Semester_GPA"],
    markers=True,
    template="plotly_white"
)

  fig.update_layout(height=500)

  st.plotly_chart(fig, use_container_width=True)
  
  st.subheader("🔥🤖 Student Academic & AI Behavior Correlation")

  corr = filtered_df[
    [
        "Pre_Semester_GPA",
        "Post_Semester_GPA",
        "Weekly_GenAI_Hours",
        "Traditional_Study_Hours",
        "Tool_Diversity",
        "Perceived_AI_Dependency"
    ]
  ].corr()

  fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    aspect="auto"
)

  fig.update_layout(height=550)

  st.plotly_chart(fig, use_container_width=True)
  st.subheader("🎈 AI Usage vs Academic Performance")

  fig = px.scatter(
    filtered_df,
    x="Weekly_GenAI_Hours",
    y="Post_Semester_GPA",
    color="Year_of_Study",
    template="plotly_white"
)

  fig.update_traces(marker=dict(size=8))

  fig.update_layout(
    height=500
)

  st.plotly_chart(fig, use_container_width=True)
  st.subheader("📦 GPA Distribution by Prompt Engineering Skill")

  fig = px.box(
    filtered_df,
    x="Prompt_Engineering_Skill",
    y="Post_Semester_GPA",
    color="Prompt_Engineering_Skill",
    points="all",
    color_discrete_sequence=px.colors.qualitative.Bold
)

  fig.update_layout(height=500)

  st.plotly_chart(fig, use_container_width=True)
  st.markdown("""
              <h3 style="color:#1B5E20;">🎓 Academic Performance Insights</h3>

<ul style="font-size:17px; line-height:1.8; color:#333;">
<li>📈 The average GPA increased from <b>3.15</b> to <b>3.35</b>, showing an overall improvement in academic performance.</li>
<li>🚀 Students achieved a <b>0.20-point increase</b> in average GPA after the semester.</li>
<li>📚 The upward trend indicates better learning outcomes and consistent academic progress.</li>
<li>💡 The results suggest that effective study practices and academic support may have contributed to improved performance.</li>
<li>🌟 Overall, the comparison reflects positive growth in students' academic achievement.</li>
</ul>

</div>
""", unsafe_allow_html=True)
# study habits
elif menu == "Study Habits":
  st.header("📚 Study Habits of Students")
  df = pd.read_csv(r"ai_student_impact.csv")
  filtered_df = df.copy()
  study = (
    filtered_df.groupby("Year_of_Study")["Traditional_Study_Hours"]
    .mean()
    .reset_index()
)

  st.subheader("🔥 Study Habits Correlation")

  corr = filtered_df[
    [
        "Traditional_Study_Hours",
        "Weekly_GenAI_Hours",
        "Pre_Semester_GPA",
        "Post_Semester_GPA",
        "Tool_Diversity",
        "Perceived_AI_Dependency"
    ]
  ].corr()

  fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="Turbo",
    aspect="equal"
)

  fig.update_traces(
    hovertemplate="<b>%{x}</b> vs <b>%{y}</b><br>Correlation: %{z:.2f}<extra></extra>"
)

  fig.update_layout(
    height=600,
    template="plotly_white",
    coloraxis_colorbar=dict(
        title="Correlation",
        thickness=20,
        len=0.75
    ),
    font=dict(size=14),
    margin=dict(l=50, r=50, t=80, b=50)
)

  st.plotly_chart(fig, use_container_width=True)
  
  st.subheader("📚 Distribution of Traditional Study Hours")

  fig = px.histogram(
    filtered_df,
    x="Traditional_Study_Hours",
    nbins=20,
    color="Prompt_Engineering_Skill",
    marginal="box",
    opacity=0.85,
    color_discrete_sequence=px.colors.qualitative.Bold,
    hover_data=[
        "Weekly_GenAI_Hours",
        "Post_Semester_GPA"
    ]
)

  fig.update_layout(
    title="Traditional Study Hours Distribution",
    xaxis_title="Study Hours per Week",
    yaxis_title="Number of Students",
    height=550,
    template="plotly_white"
)

  st.plotly_chart(fig, use_container_width=True)
  st.subheader("📈 Study Hours Trend")

  trend = (
    filtered_df.groupby("Year_of_Study")
    .agg({
        "Traditional_Study_Hours":"mean",
        "Weekly_GenAI_Hours":"mean"
    })
    .reset_index()
)

  fig = px.line(
    trend,
    x="Year_of_Study",
    y=["Traditional_Study_Hours","Weekly_GenAI_Hours"],
    markers=True,
    template="plotly_white"
)

  fig.update_layout(height=500)

  st.plotly_chart(fig, use_container_width=True)
  st.subheader("🥧 Prompt Engineering Skill Distribution")

  skill = (
    filtered_df["Prompt_Engineering_Skill"]
    .value_counts()
    .reset_index()
)

  skill.columns = ["Skill Level", "Students"]

  fig = px.pie(
    skill,
    names="Skill Level",
    values="Students",
    hole=0.55,
    color="Skill Level",
    color_discrete_sequence=px.colors.qualitative.Vivid
)

  fig.update_traces(
    textposition="inside",
    textinfo="percent+label",
    pull=[0.04] * len(skill),
    hovertemplate="<b>%{label}</b><br>Students: %{value}<br>Percentage: %{percent}"
)

  fig.update_layout(
    title="Prompt Engineering Skill Levels",
    height=550,
    legend_title="Skill Level"
)

  st.plotly_chart(fig, use_container_width=True)
  st.subheader("📦 Study Hours by Burnout Level")

  fig = px.box(
    filtered_df,
    x="Burnout_Risk_Level",
    y="Traditional_Study_Hours",
    color="Burnout_Risk_Level",
    points="all",
    color_discrete_sequence=px.colors.qualitative.Bold
)

  fig.update_layout(height=500)

  st.plotly_chart(fig, use_container_width=True)
  st.info("""
🔍 **Study Habits Observations**

• 📚 Students show different study patterns across years of study, reflecting changes in academic workload.

• 🤖 Weekly GenAI usage varies alongside traditional study hours, indicating that many students combine AI tools with conventional learning.

• 🎓 Students maintaining balanced study routines generally achieve more consistent academic performance.

• 🔥 The correlation heatmap highlights how study hours, AI usage, and GPA are related, helping identify positive or weak relationships.

• ⚖️ Higher AI usage does not always correspond to higher or lower GPA, suggesting that effective study strategies matter more than tool usage alone.

• 💡 These insights can help educators and students develop balanced learning habits that integrate AI while preserving strong study practices.
""")
  
#mental health analysis 
elif menu == "Mental Health Analysis":
  st.header("🧠 Mental Health Analysis")
  df = pd.read_csv(r"ai_student_impact.csv")
  filtered_df = df.copy()
  anxiety = (
    filtered_df["Anxiety_Level_During_Exams"]
    .value_counts()
    .reset_index()
)

  anxiety.columns = ["Anxiety Level", "Students"]

  fig = px.bar(
    anxiety,
    x="Anxiety Level",
    y="Students",
    color="Students",
    text="Students",
    color_continuous_scale="Turbo"
)

  fig.update_traces(
    textposition="outside",
    marker_line_color="white",
    marker_line_width=2
)

  fig.update_layout(
    height=500,
    template="plotly_white",
    title="📊 Distribution of Anxiety Levels"
)

  st.plotly_chart(fig, use_container_width=True)
  st.subheader("🔥 Burnout Risk Distribution")

  burnout = (
    filtered_df["Burnout_Risk_Level"]
    .value_counts()
    .reset_index()
)

  burnout.columns = ["Risk Level", "Students"]

  fig = px.pie(
    burnout,
    names="Risk Level",
    values="Students",
    hole=0.55,
    color="Risk Level",
    color_discrete_sequence=px.colors.qualitative.Bold
)

  fig.update_traces(
    textinfo="percent+label",
    pull=[0.04]*len(burnout)
)

  fig.update_layout(height=500)

  st.plotly_chart(fig, use_container_width=True)
  st.subheader("📈 AI Usage vs Anxiety")

  trend = (
    filtered_df.groupby("Perceived_AI_Dependency")
    ["Weekly_GenAI_Hours"]
    .mean()
    .reset_index()
)

  fig = px.area(
    trend,
    x="Perceived_AI_Dependency",
    y="Weekly_GenAI_Hours",
    color_discrete_sequence=["#6C63FF"]
)

  fig.update_traces(line=dict(width=4))

  fig.update_layout(
    template="plotly_white",
    height=500
)

  st.plotly_chart(fig, use_container_width=True)
  st.subheader("🎈 AI Dependency vs Weekly AI Usage")

  fig = px.scatter(
    filtered_df,
    x="Perceived_AI_Dependency",
    y="Weekly_GenAI_Hours",
    color="Burnout_Risk_Level",
    template="plotly_white"
)

  fig.update_traces(
    marker=dict(size=8)
)

  fig.update_layout(
    height=500,
    xaxis_title="Perceived AI Dependency",
    yaxis_title="Weekly AI Usage (Hours)"
)

  st.plotly_chart(fig, use_container_width=True)
  st.subheader("🔥 Mental Health Correlation")

  corr = filtered_df[
    [
        "Weekly_GenAI_Hours",
        "Traditional_Study_Hours",
        "Perceived_AI_Dependency",
        "Anxiety_Level_During_Exams",
        "Pre_Semester_GPA",
        "Post_Semester_GPA"
    ]
  ].corr()

  fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="Turbo",
    aspect="equal"
)

  fig.update_layout(
    height=600,
    template="plotly_white"
)

  st.plotly_chart(fig, use_container_width=True)
  st.success("""
🧠 Mental Health Insights

• 💡 Anxiety levels vary among students, showing that academic pressure is experienced differently by each individual.

• 📚 Balanced study habits are often associated with more consistent academic performance and improved well-being.

• 🤖 AI serves as a valuable learning aid, but its effectiveness depends on how students use it alongside traditional study methods.

• 🔥 Students with higher burnout risk may also experience higher anxiety during exams, highlighting the importance of maintaining a healthy routine.

• 📊 Correlation analysis helps uncover relationships between study hours, AI usage, anxiety, burnout risk, and academic performance.

• 🎯 A balanced approach to studying, technology use, and mental wellness can contribute to a more positive learning experience.
""")
  
# correlatiom
elif menu == "Correlation Analysis":
  st.header("🔗 Correlation Analysis")
  st.subheader("🔥 Correlation Matrix")
  df = pd.read_csv(r"ai_student_impact.csv")
  filtered_df = df.copy()
  corr = filtered_df[
    [
        "Weekly_GenAI_Hours",
        "Traditional_Study_Hours",
        "Pre_Semester_GPA",
        "Post_Semester_GPA",
        "Tool_Diversity",
        "Perceived_AI_Dependency"
    ]
  ].corr()

  fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="Viridis",
    aspect="equal"
)
  fig.update_layout(
    template="plotly_white",
    height=600
)

  st.plotly_chart(fig, use_container_width=True)
  st.subheader("😓 Weekly AI Usage vs Burnout Risk")

  fig = px.scatter(
    filtered_df,
    x="Weekly_GenAI_Hours",
    y="Burnout_Risk_Level",
    color="Year_of_Study",
    template="plotly_white"

)

  fig.update_layout(
    height=500,
)

  st.plotly_chart(fig, use_container_width=True)
  st.subheader("📦 GPA Distribution by Burnout Risk")

  fig = px.box(
    filtered_df,
    x="Burnout_Risk_Level",
    y="Post_Semester_GPA",
    color="Burnout_Risk_Level",
    points="all",
    color_discrete_sequence=px.colors.qualitative.Bold
)

  fig.update_layout(
    height=550,
    template="plotly_white"
)

  st.plotly_chart(fig, use_container_width=True)
  st.subheader("📊 Scatter Matrix")

  burnout_counts = filtered_df["Burnout_Risk_Level"].value_counts().reset_index()
  burnout_counts.columns = ["Burnout_Risk_Level", "Count"]

  fig = px.pie(
    burnout_counts,
    names="Burnout_Risk_Level",
    values="Count",
    hole=0.4,
    color_discrete_sequence=px.colors.qualitative.Set2
)

  fig.update_traces(
    textinfo="percent+label",
    hovertemplate="<b>%{label}</b><br>Students: %{value}<br>Percentage: %{percent}"
)

  fig.update_layout(
    height=600
)

  st.plotly_chart(fig, use_container_width=True)
  st.info("""
### 🔍 Correlation Analysis Observations

• 📊 The correlation heatmap provides a quick overview of how numerical variables are related.

• 🎈 The bubble scatter plot helps compare AI usage, GPA, and tool diversity in a single interactive view.

• 📦 The box plot highlights the variation in academic performance across different burnout risk levels.

• 🌈 The parallel coordinates chart allows readers to follow patterns across multiple variables simultaneously.

• 📈 The scatter matrix makes it easy to identify clusters, trends, and possible relationships between pairs of variables.

• 💡 Correlation indicates the strength of association between variables but does not by itself establish a cause-and-effect relationship.
""")
#key insight 
elif menu == "Key Insights":
  st.markdown("""
<h1 style='text-align:center;color:#6C63FF;'>
🌟 Key Insights Dashboard
</h1>
""", unsafe_allow_html=True)

  st.markdown("---")
  df = pd.read_csv(r"ai_student_impact.csv")
  filtered_df = df.copy()
  col1, col2, col3, col4 = st.columns(4)

  with col1:
    st.metric(
        "🤖 Avg AI Hours",
        f"{filtered_df['Weekly_GenAI_Hours'].mean():.1f} hrs"
    )

  with col2:
    st.metric(
        "📚 Avg Study Hours",
        f"{filtered_df['Traditional_Study_Hours'].mean():.1f} hrs"
    )

  with col3:
    st.metric(
        "🎓 Avg GPA",
        f"{filtered_df['Post_Semester_GPA'].mean():.2f}"
    )

  with col4:
    st.metric(
        "🛠 Avg AI Tools",
        f"{filtered_df['Tool_Diversity'].mean():.1f}"
    )
  col1, col2 = st.columns(2)

  with col1:
     st.success("""
### 🤖 AI Usage

✅ Students actively use Generative AI tools to support learning.

✅ AI is commonly used for writing, summarizing, debugging, and brainstorming.

✅ Students with greater tool diversity explore multiple AI platforms.
""")
  with col2:
     st.info("""
### 📚 Study Habits

📖 Students balance traditional study methods with AI-assisted learning.

📖 Weekly study hours vary, indicating different learning approaches.

📖 Combining AI with regular study may help students learn more efficiently.
""")
  col3, col4 = st.columns(2)

  with col3:
     st.warning("""
### 🧠 Mental Well-being

⚠ Anxiety and burnout levels vary among students.

⚠ High AI dependency does not necessarily indicate better academic outcomes.

⚠ Maintaining a balanced study routine is important for long-term well-being.
""")
  with col4:
     st.error("""
### 🎓 Academic Performance

🏆 Academic performance differs across students with different study habits and AI usage.

🏆 Multiple factors influence GPA, including study hours, AI usage, and learning strategies.

🏆 The prediction model demonstrates how machine learning can identify patterns in educational data.
""")

# technologies used
elif menu == "Technologies Used":
  st.markdown("""
<h1 style="
text-align:center;
font-size:42px;
font-weight:bold;
background: linear-gradient(90deg,#ff4b4b,#ff8c00,#ffd700,#00c853,#00bcd4,#3f51b5,#9c27b0);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
margin-bottom:20px;">
🛠 Technologies Used
</h1>
""", unsafe_allow_html=True)

  st.write("")
  col1, col2 = st.columns(2)

  with col1:

    st.success("""
### 🐍 Python

✔ Core programming language

✔ Data processing & machine learning

✔ Easy integration with libraries
""")

    st.info("""
### 🎈 Streamlit

✔ Interactive web dashboard

✔ User-friendly interface

✔ Dynamic filters and charts
""")

    st.warning("""
### 🐼 Pandas

✔ Data cleaning

✔ Data preprocessing

✔ Data analysis & manipulation
""")

  with col2:

    st.error("""
### 📊 Plotly

✔ Interactive charts

✔ Beautiful visualizations

✔ Zoom, hover & filtering
""")

    st.success("""
### 💻 Visual Studio Code

✔ Code development

✔ Project management

✔ Debugging support
""")

    st.info("""
### 🖼 Pillow (PIL)

✔ Display project images

✔ Image processing

✔ Dashboard graphics
""")
#conclusion
elif menu == "Conclusion":
  df = pd.read_csv(r"ai_student_impact.csv")
  filtered_df = df.copy()
  st.markdown("""
# 📌 Project Summary
""")

  st.success("""
### 🎯 What This Project Achieved

✅ Explored how students use Generative AI in their academic journey through an interactive dashboard.

✅ Analyzed AI usage patterns, study habits, academic performance, and mental well-being using real-world educational data.

✅ Applied data preprocessing, exploratory data analysis (EDA), interactive visualizations, and machine learning techniques to uncover meaningful patterns.

✅ Built a user-friendly Streamlit dashboard that enables users to explore insights through dynamic charts and filters.

✅ Demonstrated how data science can transform raw educational data into valuable and easy-to-understand insights.
""")
  st.markdown("""
# 🌟 Project Impact
""")

  st.success("""
### 🚀 Why This Project Matters

🎓 Helps students better understand their study habits and AI usage patterns.

📊 Provides educators and researchers with visual insights into educational data.

🤖 Demonstrates the practical use of Artificial Intelligence and Machine Learning in education analytics.

💡 Encourages data-driven decision-making through interactive dashboards and visualizations.

🌍 Shows how technology can be used to analyze educational trends and support informed learning strategies.
""")
elif menu == "About":
  st.markdown("""
<div style="
background:linear-gradient(90deg,#A18CD1,#FBC2EB);
padding:25px;
border-radius:18px;
text-align:center;
color:#2D2D2D;
box-shadow:0px 6px 15px rgba(0,0,0,0.2);
">

<h2>🤖 Thank You for Exploring Our Project!</h2>

<p style="font-size:18px; line-height:1.8;">

🌟 Every chart tells a story, and every insight brings us closer to understanding the evolving role of AI in education.

📊 We hope this dashboard helped you explore meaningful patterns and inspired new perspectives on student learning.

🚀 Thank you for your time, curiosity, and interest in our project!

</p>

<h3>✨ Keep Learning • Keep Exploring • Keep Growing ✨</h3>

</div>
""", unsafe_allow_html=True)
  
