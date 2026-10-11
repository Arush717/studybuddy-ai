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
    import random

    st.header("🧠 StudyBuddy Quiz")
    st.write("Choose a subject and test your knowledge!")

    quiz_data = {
        "Python": [
            {
                "q": "What does print() do?",
                "options": [
                    "Deletes files", "Displays information",
                    "Creates folders", "Shuts down the computer"
                ],
                "answer": "Displays information",
                "why": "print() displays text and values."
            },
            {
                "q": "Which symbol starts a Python comment?",
                "options": ["//", "#", "$", "&"],
                "answer": "#",
                "why": "Python uses # for single-line comments."
            },
            {
                "q": "Which keyword defines a function?",
                "options": ["func", "make", "def", "loop"],
                "answer": "def",
                "why": "The def keyword defines a function."
            },
            {
                "q": "What is the result of 4 * 3?",
                "options": ["7", "12", "43", "1"],
                "answer": "12",
                "why": "* multiplies numbers, so 4 * 3 = 12."
            },
            {
                "q": "Which data type stores True or False?",
                "options": ["str", "int", "bool", "list"],
                "answer": "bool",
                "why": "The bool type represents True or False."
            }
        ],
        "Science": [
            {
                "q": "Which gas do plants absorb for photosynthesis?",
                "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"],
                "answer": "Carbon dioxide",
                "why": "Plants use carbon dioxide during photosynthesis."
            },
            {
                "q": "What is the SI unit of force?",
                "options": ["Joule", "Watt", "Newton", "Pascal"],
                "answer": "Newton",
                "why": "Force is measured in newtons (N)."
            },
            {
                "q": "Which organ pumps blood around the body?",
                "options": ["Lungs", "Brain", "Kidneys", "Heart"],
                "answer": "Heart",
                "why": "The heart pumps blood through the circulatory system."
            },
            {
                "q": "What is the chemical formula for water?",
                "options": ["CO2", "H2O", "O2", "NaCl"],
                "answer": "H2O",
                "why": "A water molecule contains two hydrogen atoms and one oxygen atom."
            },
            {
                "q": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Jupiter", "Mars", "Mercury"],
                "answer": "Mars",
                "why": "Iron-rich dust gives Mars its reddish appearance."
            }
        ],
        "Maths": [
            {
                "q": "What is 15 + 27?",
                "options": ["32", "42", "41", "52"],
                "answer": "42",
                "why": "15 + 27 = 42."
            },
            {
                "q": "What is 9 squared?",
                "options": ["18", "72", "81", "99"],
                "answer": "81",
                "why": "9 squared means 9 × 9 = 81."
            },
            {
                "q": "What is the perimeter of a square with side 5 cm?",
                "options": ["10 cm", "20 cm", "25 cm", "15 cm"],
                "answer": "20 cm",
                "why": "A square has four equal sides: 4 × 5 = 20 cm."
            },
            {
                "q": "Solve: x + 7 = 12",
                "options": ["3", "4", "5", "6"],
                "answer": "5",
                "why": "Subtract 7 from both sides: x = 12 - 7 = 5."
            },
            {
                "q": "What is 3/4 as a percentage?",
                "options": ["25%", "50%", "75%", "80%"],
                "answer": "75%",
                "why": "3 ÷ 4 × 100 = 75%."
            }
        ]
    }

    subject = st.selectbox(
        "Choose your subject",
        list(quiz_data.keys())
    )
    difficulty = st.selectbox(
    "Choose difficulty",
    ["Easy", "Medium", "Hard"]
)
    question_count = st.slider(
        "Number of questions",
        min_value=3,
        max_value=5,
        value=5
    )

    
if st.button("🎲 Start New Quiz"):
    all_questions = quiz_data[subject]

    if difficulty == "Easy":
        available_questions = all_questions[:3]
    elif difficulty == "Medium":
        available_questions = all_questions[1:4]
    else:
        available_questions = all_questions[2:]

    actual_count = min(question_count, len(available_questions))

    selected_questions = random.sample(
        available_questions, actual_count
    )

    st.session_state.quiz_questions = selected_questions
    st.session_state.quiz_subject = subject
    st.session_state.quiz_difficulty = difficulty

    if (
        "quiz_questions" in st.session_state
        and st.session_state.quiz_subject == subject
    ):
        questions = st.session_state.quiz_questions

        with st.form("advanced_quiz"):
            answers = []

            for i, q in enumerate(questions):
                st.subheader(f"Question {i + 1}")
                st.write(q["q"])

                options = q["options"][:]
                random.Random(i + 100).shuffle(options)

                selected = st.radio(
                    "Choose your answer:",
                    options,
                    index=None,
                    key=f"advanced_{subject}_{i}"
                )
                answers.append(selected)

            submitted = st.form_submit_button("✅ Submit Quiz")

        if submitted:
            score = sum(
                answers[i] == q["answer"]
                for i, q in enumerate(questions)
            )

            percentage = round(score / len(questions) * 100)

            st.subheader("📊 Your Results")
            st.metric("Score", f"{score}/{len(questions)}")
            st.progress(percentage / 100)
            st.write(f"**Percentage: {percentage}%**")

            for i, q in enumerate(questions):
                st.write(f"**Q{i + 1}: {q['q']}**")

                if answers[i] == q["answer"]:
                    st.success("Correct! " + q["why"])
                else:
                    st.error(
                        f"Your answer: {answers[i] or 'Not answered'}"
                    )
                    st.info(
                        f"Correct answer: {q['answer']}. {q['why']}"
                    )

            if percentage == 100:
                st.balloons()
                st.success("Perfect score! Outstanding work!")
            elif percentage >= 60:
                st.success("Good job! Keep practising.")
            else:
                st.info("Review the explanations and try again.")




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
