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
  ["Home", "My Notes", "Quiz", "Study Planner", "AI Study Assistant"]
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
    st.write("Test your Python knowledge!")

    questions = [
        {
            "question": "What does print() do in Python?",
            "options": [
                "Deletes a file",
                "Displays information",
                "Creates a website automatically",
                "Turns off the computer"
            ],
            "answer": "Displays information",
            "explanation": "print() displays text or other values on the screen."
        },
        {
            "question": "Which symbol starts a comment in Python?",
            "options": ["//", "#", "/*", "$"],
            "answer": "#",
            "explanation": "A # symbol starts a single-line comment in Python."
        },
        {
            "question": "Which of these is a string in Python?",
            "options": ["25", '"Hello"', "True", "3.14"],
            "answer": '"Hello"',
            "explanation": "A string is text. Text is commonly written inside quotes."
        },
        {
            "question": "Which keyword is used to define a function?",
            "options": ["func", "function", "def", "make"],
            "answer": "def",
            "explanation": "Python uses the def keyword to define a function."
        },
        {
            "question": "What is the result of 3 + 2?",
            "options": ["32", "5", "6", "1"],
            "answer": "5",
            "explanation": "The + operator adds the two numbers: 3 + 2 = 5."
        }
    ]

    with st.form("python_quiz"):
        answers = []

        for i, q in enumerate(questions):
            st.subheader(f"Question {i + 1}")
            st.write(q["question"])

            selected = st.radio(
                "Choose your answer:",
                q["options"],
                key=f"quiz_question_{i}",
                index=None
            )
            answers.append(selected)

        submitted = st.form_submit_button("Check My Score")

    if submitted:
        score = 0

        for i, q in enumerate(questions):
            st.write(f"**Question {i + 1}: {q['question']}**")

            if answers[i] == q["answer"]:
                score += 1
                st.success("Correct! " + q["explanation"])
            else:
                st.error(
                    f"Correct answer: {q['answer']}. "
                    + q["explanation"]
                )

        st.subheader(f"Your score: {score}/{len(questions)}")

        if score == len(questions):
            st.balloons()
            st.success("Perfect score! Excellent work!")
        elif score >= 3:
            st.success("Good job! Keep practising.")
        else:
            st.info("Keep learning and try again!")


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





elif page == "AI Study Assistant":
    st.header("🤖 AI Study Assistant")
    st.write("Ask a study question and get a simple explanation!")

    topic = st.text_input("Enter your question")

    if st.button("Explain"):
        if topic.strip():
            question = topic.strip().lower()

            answers = {
                "photosynthesis": (
                    "Photosynthesis is how green plants make "
                    "food using sunlight, water, and carbon dioxide. "
                    "They release oxygen."
                ),
                "python": (
                    "Python is a beginner-friendly programming "
                    "language used to build apps, automate tasks, "
                    "and work with AI."
                ),
                "gravity": (
                    "Gravity attracts objects toward each other. "
                    "Earth's gravity pulls objects toward the ground."
                ),
                "water cycle": (
                    "The water cycle includes evaporation, "
                    "condensation, and precipitation."
                ),
            }

            matched_answer = None

            for keyword, answer in answers.items():
                if keyword in question:
                    matched_answer = answer
                    break

            if matched_answer:
                st.success(matched_answer)
            else:
                st.info(
                    "I don't have an answer for that topic yet. "
                    "Try photosynthesis, Python, gravity, "
                    "or water cycle."
                )
        else:
            st.warning("Please enter a question first.")
