import streamlit as st

st.set_page_config(
    page_title="StudyBuddy AI",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 StudyBuddy AI")
st.caption("Learn • Practice • Grow")

st.sidebar.title("📚 StudyBuddy")
page = st.sidebar.radio(
    "Choose a page",
    ["Home", "My Notes", "Quiz", "Study Planner"]
)

if page == "Home":
    st.header("Welcome to StudyBuddy AI! 👋")
    st.write(
        "Your personal study companion. "
        "Learn new things, practise questions, "
        "and organize your study time."
    )

    col1, col2 = st.columns(2)
    col1.info("📚 **My Notes**\n\nKeep your learning notes together.")
    col2.success("📝 **Quiz**\n\nTest what you have learned.")

    st.subheader("Today's reminder")
    st.write("Small steps today, big dreams tomorrow! 🚀")

elif page == "My Notes":
    st.header("📚 My Python Notes")

    st.markdown("""
    ### What is Python?
    Python is a high-level, general-purpose programming
    language created by Guido van Rossum and first
    released in 1991.

    ### Core data types
    - `str`: text
    - `int`: whole numbers
    - `float`: decimal numbers
    - `bool`: True or False
    - `list`: changeable collection
    - `tuple`: unchangeable collection
    - `set`: collection of unique items
    - `dict`: key-value pairs

    ### Key concepts
    - `print()` displays information.
    - `input()` gets information from the user.
    - `if` and `else` make decisions.
    - `for` and `while` repeat instructions.

    ### Popular uses
    - Artificial intelligence
    - Data science
    - Web development
    - Automation
    """)

elif page == "Quiz":
    st.header("📝 Python Quiz")

    question = st.radio(
        "What does print() do in Python?",
        [
            "Deletes a file",
            "Displays information",
            "Creates a website automatically",
            "Turns off the computer"
        ]
    )

    if st.button("Check my answer"):
        if question == "Displays information":
            st.success("Correct! Great job! 🎉")
        else:
            st.error("Not quite. Try again!")

elif page == "Study Planner":
    st.header("📅 My Study Planner")

    task = st.text_input("What do you want to study?")
    minutes = st.number_input(
        "Study time (minutes)",
        min_value=5,
        max_value=240,
        value=30,
        step=5
    )

    if st.button("Add study task"):
        if task.strip():
            st.success(f"Task added: {task} — {minutes} minutes")
        else:
            st.warning("Please enter a task first.")

st.divider()
st.caption("StudyBuddy AI • Better Study Habits, Brighter Future 💙")

elif page == "AI Study Assistant":
    st.header("🤖 AI Study Assistant")
    st.write("Ask a study question and get a simple explanation!")

    topic = st.text_input("Enter your question")

    if st.button("Explain"):
        if topic.strip():
            st.info(
                "Your question: " + topic +
                "\n\nNext, we'll connect an AI model "
                "to generate real answers!"
            )
        else:
            st.warning("Please enter a question first.")

