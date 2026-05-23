import streamlit as st

st.set_page_config(
    page_title="Arvind Alewad | Portfolio",
    page_icon="📊",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #f8fafc, #eff6ff);
        color: #0f172a;
        font-family: 'Segoe UI', sans-serif;
    }

    .hero {
        background: linear-gradient(135deg, #2563eb, #7c3aed, #ec4899);
        padding: 70px 60px;
        border-radius: 30px;
        color: white;
        margin-bottom: 35px;
        box-shadow: 0px 15px 40px rgba(0,0,0,0.15);
    }

    .hero h1 {
        font-size: 64px;
        margin-bottom: 10px;
        color: white;
    }

    .hero h3 {
        font-size: 28px;
        font-weight: 500;
        margin-bottom: 20px;
        color: #fdf4ff;
    }

    .hero p {
        font-size: 20px;
        line-height: 1.8;
        color: #f8fafc;
    }

    .card {
        background: white;
        padding: 30px;
        border-radius: 24px;
        margin-bottom: 25px;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.08);
        border: 1px solid #e2e8f0;
    }

    .skill-box {
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
        color: white;
        padding: 12px 18px;
        border-radius: 30px;
        text-align: center;
        margin-bottom: 12px;
        font-weight: 600;
        box-shadow: 0px 4px 12px rgba(59,130,246,0.25);
    }

    .metric-card {
        background: white;
        border-radius: 22px;
        padding: 25px;
        text-align: center;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.08);
        border: 1px solid #e2e8f0;
    }

    .metric-card h2 {
        font-size: 38px;
        color: #2563eb;
        margin-bottom: 5px;
    }

    .metric-card p {
        color: #475569;
        font-size: 16px;
    }

    .project-card {
        background: linear-gradient(to bottom right, #ffffff, #f8fafc);
        border-radius: 24px;
        padding: 28px;
        border: 1px solid #e2e8f0;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.06);
        height: 100%;
    }

    .footer {
        text-align: center;
        padding: 30px;
        color: #64748b;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HERO SECTION ----------------

st.markdown(
    """
    <div class="hero">
        <h1>Arvind Alewad</h1>
        <h3>Data Analyst | Python Developer | BI Analyst</h3>
        <p>
        Data Analyst with 3 years of experience in HRMS and Financial Domain Analytics.
        Skilled in Python, SQL, Power BI, Tableau, Snowflake, Excel, ETL, and Data Visualization.
        Passionate about transforming data into meaningful business insights.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- METRICS ----------------

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
    <div class='metric-card'>
        <h2>3+</h2>
        <p>Years Experience</p>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class='metric-card'>
        <h2>10+</h2>
        <p>Projects Completed</p>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class='metric-card'>
        <h2>15+</h2>
        <p>Technical Skills</p>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class='metric-card'>
        <h2>3</h2>
        <p>Awards & Recognitions</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------------- ABOUT ----------------

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("About Me")

st.write(
    """
    Passionate Data Analyst experienced in claims analytics, HRMS reporting, workflow automation,
    dashboard development, statistical analysis, and ETL processes.

    I enjoy solving business problems using Python, SQL, Power BI, Tableau, and data visualization.
    Currently learning advanced analytics, machine learning, and building real-world analytics projects.
    """
)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- SKILLS ----------------

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("Technical Skills")

c1, c2, c3 = st.columns(3)

with c1:
    st.subheader("Programming")
    for skill in ["Python", "SQL", "Pandas", "NumPy", "ETL", "Data Cleaning"]:
        st.markdown(f'<div class="skill-box">{skill}</div>', unsafe_allow_html=True)

with c2:
    st.subheader("Visualization")
    for skill in ["Power BI", "Tableau", "Plotly", "Matplotlib", "Seaborn", "Excel Dashboards"]:
        st.markdown(f'<div class="skill-box">{skill}</div>', unsafe_allow_html=True)

with c3:
    st.subheader("Tools & Cloud")
    for skill in ["Snowflake", "AWS", "Workflow Automation", "Agile", "Data Validation", "Reporting"]:
        st.markdown(f'<div class="skill-box">{skill}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- EXPERIENCE ----------------

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("Professional Experience")

st.subheader("Data Analyst — Bajaj Finance Limited")
st.caption("March 2024 - Present | Pune")

st.write(
    """
    • Analyzed claims and HRMS data using Python, SQL, Pandas, and Excel.

    • Built Power BI dashboards and KPI reports for business insights.

    • Performed data cleaning, transformation, and validation.

    • Improved reporting processes and data quality.
    """
)

st.subheader("Graduate Engineer Trainee — Vodafone Intelligent Solutions")
st.caption("August 2023 - March 2024 | Pune")

st.write(
    """
    • Automated CSV workflows using Python and SQL.

    • Processed and validated large datasets using Pandas.

    • Developed Power BI and Excel dashboards.

    • Improved workflow reliability and reporting accuracy.
    """
)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PROJECTS ----------------

st.header("Projects & Portfolio")

p1, p2 = st.columns(2)

with p1:
    st.markdown(
        """
        <div class="project-card">
            <h3>Analytics & Dashboard Projects</h3>
            <p>
            Worked on multiple analytics projects including Sales Analysis,
            Customer Churn Analysis, HRMS Analytics, Claims Analysis,
            KPI Reporting, Retail Analysis, and Workflow Automation.
            </p>
            <p>
            Created dashboards, EDA notebooks, and visualization projects using Python,
            Power BI, Tableau, Plotly, and Excel.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with p2:
    st.markdown(
        """
        <div class="project-card">
            <h3>Learning & Portfolio Journey</h3>
            <p>
            Continuously learning Statistics, Machine Learning, Advanced Python,
            SQL Optimization, and Data Visualization.
            </p>
            <p>
            10+ projects and analytics work are available on GitHub, LinkedIn,
            and Kaggle profiles.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- PROFILE LINKS ----------------

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("Explore My Work")

l1, l2, l3 = st.columns(3)

with l1:
    st.link_button("GitHub Projects", "https://github.com/AGALEWAD")

with l2:
    st.link_button("LinkedIn Profile", "https://www.linkedin.com/in/arvind-alewad-3471a1219/")

with l3:
    st.link_button("Kaggle Portfolio", "https://www.kaggle.com/agakaggle2022")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- EDUCATION ----------------

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("Education")

st.subheader("Bachelor of Technology — Electronics & Telecommunication Engineering")

st.write("Shri Guru Gobind Singhji Institute of Engineering, Nanded")
st.write("Graduated: May 2023")
st.write("GPA: 7.78")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- ACHIEVEMENTS ----------------

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("Awards & Achievements")

st.success("🏆 Star of the Month — Recognized for strong performance in data analysis and reporting")
st.success("🏆 Superstar Award — Awarded for excellence in analytics and process improvement")
st.success("🏆 Kudos Recognition — Appreciated for contributions to claims and HRMS analytics")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CONTACT ----------------

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("Contact")

c1, c2, c3 = st.columns(3)

with c1:
    st.info("📍 Pune, Maharashtra")

with c2:
    st.info("📧 alewadarvind22@gmail.com")

with c3:
    st.info("📞 9765828004")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------

st.markdown(
    """
    <div class="footer">
        © 2026 Arvind Alewad | Data Analyst Portfolio
    </div>
    """,
    unsafe_allow_html=True
)
