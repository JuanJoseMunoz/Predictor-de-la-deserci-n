import streamlit as st
import pandas as pd

from utils.decoder import (
    get_options,
    encode
)

def personal_information():

    st.subheader("👤 Información personal")

    col1, col2 = st.columns(2)

    with col1:

        marital = st.selectbox(
            "Marital status",
            get_options("Marital status"),
            key="marital_status"
        )

        nationality = st.selectbox(
            "Nationality",
            get_options("Nacionality"),
            key="nationality"
        )

        gender = st.selectbox(
            "Gender",
            get_options("Gender"),
            key="gender"
        )

        age = st.number_input(
            "Age at enrollment",
            min_value=15,
            max_value=80,
            value=20,
            key="age"
        )

    with col2:

        displaced = st.selectbox(
            "Displaced",
            get_options("Displaced"),
            key="displaced"
        )

        special = st.selectbox(
            "Educational special needs",
            get_options("Educational special needs"),
            key="special"
        )

        international = st.selectbox(
            "International",
            get_options("International"),
            key="international"
        )

    return {

        "Marital status":
            encode("Marital status", marital),

        "Nacionality":
            encode("Nacionality", nationality),

        "Gender":
            encode("Gender", gender),

        "Age at enrollment":
            age,

        "Displaced":
            encode("Displaced", displaced),

        "Educational special needs":
            encode("Educational special needs", special),

        "International":
            encode("International", international)

    }


def academic_information():

    st.subheader("🎓 Información académica")

    course = st.selectbox(
        "Course",
        get_options("Course"),
        key="course"
    )

    application = st.selectbox(
        "Application mode",
        get_options("Application mode"),
        key="application"
    )

    previous = st.selectbox(
        "Previous qualification",
        get_options("Previous qualification"),
        key="previous"
    )

    application_order = st.number_input(
        "Application order",
        0,
        9,
        1,
        key="application_order"
    )

    admission_grade = st.number_input(
        "Admission grade",
        0.0,
        200.0,
        120.0,
        key="admission_grade"
    )

    previous_grade = st.number_input(
        "Previous qualification grade",
        0.0,
        200.0,
        120.0,
        key="previous_grade"
    )

    attendance = st.selectbox(
        "Attendance",
        get_options("Daytime/evening attendance\t"),
        key="attendance"
    )

    return {

        "Course":
            encode("Course", course),

        "Application mode":
            encode("Application mode", application),

        "Previous qualification":
            encode("Previous qualification", previous),

        "Application order":
            application_order,

        "Admission grade":
            admission_grade,

        "Previous qualification (grade)":
            previous_grade,

        "Daytime/evening attendance\t":
            encode(
                "Daytime/evening attendance\t",
                attendance
            )

    }



def family_information():

    st.subheader("👨‍👩‍👧 Información familiar")

    mother_q = st.selectbox(
        "Mother's qualification",
        get_options("Mother's qualification"),
        key="mother_q"
    )

    father_q = st.selectbox(
        "Father's qualification",
        get_options("Father's qualification"),
        key="father_q"
    )

    mother_occ = st.selectbox(
        "Mother's occupation",
        get_options("Mother's occupation"),
        key="mother_occ"
    )

    father_occ = st.selectbox(
        "Father's occupation",
        get_options("Father's occupation"),
        key="father_occ"
    )

    return {

        "Mother's qualification":
            encode(
                "Mother's qualification",
                mother_q
            ),

        "Father's qualification":
            encode(
                "Father's qualification",
                father_q
            ),

        "Mother's occupation":
            encode(
                "Mother's occupation",
                mother_occ
            ),

        "Father's occupation":
            encode(
                "Father's occupation",
                father_occ
            )

    }


def financial_information():

    st.subheader("💰 Información financiera")

    col1, col2, col3 = st.columns(3)

    with col1:

        debtor = st.selectbox(
            "Debtor",
            get_options("Debtor"),
            key="debtor"
        )

    with col2:

        tuition = st.selectbox(
            "Tuition fees up to date",
            get_options("Tuition fees up to date"),
            key="tuition"
        )

    with col3:

        scholarship = st.selectbox(
            "Scholarship holder",
            get_options("Scholarship holder"),
            key="scholarship"
        )

    return {

        "Debtor":
            encode("Debtor", debtor),

        "Tuition fees up to date":
            encode(
                "Tuition fees up to date",
                tuition
            ),

        "Scholarship holder":
            encode(
                "Scholarship holder",
                scholarship
            )

    }


def first_semester():

    st.subheader("📚 Rendimiento académico - Primer semestre")

    c1, c2, c3 = st.columns(3)

    with c1:

        credited = st.number_input(
            "Credited",
            0,
            30,
            0,
            key="credited1"
        )

        enrolled = st.number_input(
            "Enrolled",
            0,
            30,
            6,
            key="enrolled1"
        )

    with c2:

        evaluations = st.number_input(
            "Evaluations",
            0,
            30,
            6,
            key="evaluations1"
        )

        approved = st.number_input(
            "Approved",
            0,
            30,
            5,
            key="approved1"
        )

    with c3:

        grade = st.number_input(
            "Average grade",
            0.0,
            20.0,
            12.0,
            key="grade1"
        )

        without_eval = st.number_input(
            "Without evaluations",
            0,
            30,
            0,
            key="without1"
        )

    return {

        "Curricular units 1st sem (credited)": credited,

        "Curricular units 1st sem (enrolled)": enrolled,

        "Curricular units 1st sem (evaluations)": evaluations,

        "Curricular units 1st sem (approved)": approved,

        "Curricular units 1st sem (grade)": grade,

        "Curricular units 1st sem (without evaluations)": without_eval

    }



def second_semester():

    st.subheader("📖 Rendimiento académico - Segundo semestre")

    c1, c2, c3 = st.columns(3)

    with c1:

        credited = st.number_input(
            "Credited",
            0,
            30,
            0,
            key="credited2"
        )

        enrolled = st.number_input(
            "Enrolled",
            0,
            30,
            6,
            key="enrolled2"
        )

    with c2:

        evaluations = st.number_input(
            "Evaluations",
            0,
            30,
            6,
            key="evaluations2"
        )

        approved = st.number_input(
            "Approved",
            0,
            30,
            5,
            key="approved2"
        )

    with c3:

        grade = st.number_input(
            "Average grade",
            0.0,
            20.0,
            12.0,
            key="grade2"
        )

        without_eval = st.number_input(
            "Without evaluations",
            0,
            30,
            0,
            key="without2"
        )

    return {

        "Curricular units 2nd sem (credited)": credited,

        "Curricular units 2nd sem (enrolled)": enrolled,

        "Curricular units 2nd sem (evaluations)": evaluations,

        "Curricular units 2nd sem (approved)": approved,

        "Curricular units 2nd sem (grade)": grade,

        "Curricular units 2nd sem (without evaluations)": without_eval

    }



def economic_information():

    st.subheader("🌍 Contexto económico")

    c1, c2, c3 = st.columns(3)

    with c1:

        unemployment = st.number_input(
            "Unemployment rate",
            value=10.8,
            step=0.1,
            key="unemployment"
        )

    with c2:

        inflation = st.number_input(
            "Inflation rate",
            value=1.4,
            step=0.1,
            key="inflation"
        )

    with c3:

        gdp = st.number_input(
            "GDP",
            value=0.3,
            step=0.1,
            key="gdp"
        )

    return {

        "Unemployment rate": unemployment,

        "Inflation rate": inflation,

        "GDP": gdp

    }

def build_dataframe():

    student = {}

    student.update(personal_information())

    student.update(academic_information())

    student.update(family_information())

    student.update(financial_information())

    student.update(first_semester())

    student.update(second_semester())

    student.update(economic_information())

    from utils.config import FEATURE_COLUMNS

    df = pd.DataFrame([student])

    df = df.reindex(columns=FEATURE_COLUMNS)

    return df
