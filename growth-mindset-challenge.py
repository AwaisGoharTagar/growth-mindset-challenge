import streamlit as st
import random
import time

# Apply Custom CSS for styling and animations
def apply_custom_css():
    st.markdown(
        """
        <style>
            body {
                background-color: #121212;
                color: #FFFFFF;
                font-family: 'Arial', sans-serif;
            }
            .stButton>button {
                background-color: #007ACC;
                color: white;
                border-radius: 10px;
                padding: 12px;
                font-size: 18px;
                font-weight: bold;
                border: none;
                transition: background-color 0.3s ease, transform 0.2s ease;
            }
            .stButton>button:hover {
                background-color: #005A99;
                transform: scale(1.08);
            }
            .stTextInput>div>div>input {
                border-radius: 8px;
                padding: 10px;
                border: 2px solid #007ACC;
                font-size: 16px;
                background-color: #222;
                color: white;
            }
            .title {
                font-size: 36px;
                font-weight: bold;
                color: #F4A261;
                text-align: center;
                margin-bottom: 20px;
                animation: fadeIn 1.5s ease-in-out;
            }
            .card {
                background: #1E1E1E;
                padding: 15px;
                border-radius: 12px;
                box-shadow: 3px 3px 15px rgba(0, 122, 204, 0.5);
                margin-bottom: 10px;
            }
            .leaderboard-table {
                width: 100%;
                border-collapse: collapse;
            }
            .leaderboard-table th, .leaderboard-table td {
                padding: 12px;
                text-align: left;
                border-bottom: 2px solid #007ACC;
            }
            .leaderboard-table th {
                background-color: #007ACC;
                color: white;
                font-weight: bold;
            }
            .leaderboard-table tr:hover {
                background-color: rgba(0, 122, 204, 0.2);
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to fetch a random motivational quote
def get_motivational_quote():
    quotes = [
        "Your only limit is your mind.",
        "Failure is not the opposite of success; it's part of success.",
        "Don't stop when you're tired. Stop when you're done!",
        "Push yourself, because no one else is going to do it for you.",
        "Dream big, work hard, and stay focused.",
        "Success is the sum of small efforts repeated daily.",
        "Believe in yourself and all that you are."
    ]
    return random.choice(quotes)

# Function to fetch a random daily challenge
def get_daily_challenge():
    challenges = [
        "Write down 3 things you learned today.",
        "Try something new and reflect on your experience.",
        "Help a friend solve a problem today.",
        "Read an inspiring story and share what you learned.",
        "Practice positive self-talk for 5 minutes.",
        "Step outside your comfort zone today."
    ]
    return random.choice(challenges)

# Quiz Section with a progress bar
def quiz_section():
    st.subheader("🎯 Growth Mindset Quiz")
    
    questions = {
        "What is a growth mindset?": ["A fixed way of thinking", "The belief that abilities can grow", "Avoiding challenges", "Not making mistakes"],
        "What should you do when you fail?": ["Give up", "Learn from it", "Blame others", "Ignore it"],
        "How do you develop a growth mindset?": ["Practice and effort", "Innate talent only", "Avoiding hard tasks", "Never seeking feedback"],
        "Why is perseverance important?": ["It builds resilience", "It's unnecessary", "It guarantees instant success", "It shows weakness"],
        "How should you approach challenges?": ["As opportunities to grow", "By avoiding them", "With fear", "By quitting"]
    }

    score = 0
    user_answers = {}
    total_questions = len(questions)

    progress_bar = st.progress(0)
    progress = 0

    for question, options in questions.items():
        user_answers[question] = st.radio(f"**{question}**", options, index=None)
        progress += 100 / total_questions
        progress_bar.progress(int(progress))
        time.sleep(0.1)

    if st.button("✅ Submit Answers"):
        correct_answers = {
            "What is a growth mindset?": "The belief that abilities can grow",
            "What should you do when you fail?": "Learn from it",
            "How do you develop a growth mindset?": "Practice and effort",
            "Why is perseverance important?": "It builds resilience",
            "How should you approach challenges?": "As opportunities to grow"
        }

        for question, correct_answer in correct_answers.items():
            if user_answers.get(question) == correct_answer:
                score += 1

        st.success(f"🎉 You scored {score}/{len(questions)}! Keep up the great work! 🚀")

# Dynamic Leaderboard Section
def leaderboard():
    st.subheader("🏆 Leaderboard - Top Achievers")

    leaders = {
        "Awais": random.randint(80, 100),
        "Maaz": random.randint(80, 100),
        "Bachal": random.randint(80, 100),
        "Ayesha": random.randint(80, 100),
        "Zain": random.randint(80, 100)
    }

    sorted_leaders = dict(sorted(leaders.items(), key=lambda item: item[1], reverse=True))

    leaderboard_html = "<table class='leaderboard-table'><tr><th>Name</th><th>Points</th></tr>"
    for name, points in sorted_leaders.items():
        leaderboard_html += f"<tr><td>{name}</td><td>{points}</td></tr>"
    leaderboard_html += "</table>"

    st.markdown(leaderboard_html, unsafe_allow_html=True)

# Growth Mindset Challenge Page
def growth_mindset_page():
    apply_custom_css()
    st.markdown("<p class='title'>🚀 Growth Mindset Challenge</p>", unsafe_allow_html=True)
    st.subheader("✨ Learn, Improve, and Grow")

    st.markdown("""
    A **growth mindset** is the belief that abilities and intelligence can be developed.  
    With **hard work, learning, and persistence**, you can improve your skills.  
     """  )

    # User Input
    name = st.text_input("📌 Enter your name:")
    if name:
        st.write(f"👋 Welcome, {name}! Ready to build a growth mindset?")

    # Start Button
    if st.button("🚀 Click to Start"):
        st.success("🔥 Great! Keep learning and growing!")

    # Motivational Quote
    st.markdown(f"<div class='card'>💡 **Inspirational Quote:** {get_motivational_quote()}</div>", unsafe_allow_html=True)

    # Daily Challenge
    st.markdown(f"<div class='card'>📌 **Today's Challenge:** {get_daily_challenge()}</div>", unsafe_allow_html=True)

    # Quiz Section
    quiz_section()

    # Leaderboard
    leaderboard()

# Run the Streamlit App
if __name__ == "__main__":
    growth_mindset_page()


# import streamlit as st
# import random
# import time

# # Custom CSS for improved UI and animations
# def apply_custom_css():
#     st.markdown(
#         """
#         <style>
#             body {
#                 background-color: #121212;
#                 color: #FFFFFF;
#                 font-family: 'Arial', sans-serif;
#             }
#             .stButton>button {
#                 background-color: #007ACC;
#                 color: white;
#                 border-radius: 10px;
#                 padding: 12px;
#                 font-size: 18px;
#                 font-weight: bold;
#                 border: none;
#                 transition: background-color 0.3s ease, transform 0.2s ease;
#             }
#             .stButton>button:hover {
#                 background-color: #005A99;
#                 transform: scale(1.08);
#             }
#             .stTextInput>div>div>input {
#                 border-radius: 8px;
#                 padding: 10px;
#                 border: 2px solid #007ACC;
#                 font-size: 16px;
#                 background-color: #222;
#                 color: white;
#             }
#             .title {
#                 font-size: 36px;
#                 font-weight: bold;
#                 color: #F4A261;
#                 text-align: center;
#                 margin-bottom: 20px;
#                 animation: fadeIn 1.5s ease-in-out;
#             }
#             .card {
#                 background: #1E1E1E;
#                 padding: 15px;
#                 border-radius: 12px;
#                 box-shadow: 3px 3px 15px rgba(0, 122, 204, 0.5);
#                 margin-bottom: 10px;
#             }
#             .leaderboard-table {
#                 width: 100%;
#                 border-collapse: collapse;
#             }
#             .leaderboard-table th, .leaderboard-table td {
#                 padding: 12px;
#                 text-align: left;
#                 border-bottom: 2px solid #007ACC;
#             }
#             .leaderboard-table th {
#                 background-color: #007ACC;
#                 color: white;
#                 font-weight: bold;
#             }
#             .leaderboard-table tr:hover {
#                 background-color: rgba(0, 122, 204, 0.2);
#             }
#             @keyframes fadeIn {
#                 from { opacity: 0; }
#                 to { opacity: 1; }
#             }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # Fetch random motivational quote
# def get_motivational_quote():
#     quotes = [
#         "Your only limit is your mind.",
#         "Failure is not the opposite of success; it's part of success.",
#         "Don't stop when you're tired. Stop when you're done!",
#         "Push yourself, because no one else is going to do it for you.",
#         "Dream big, work hard, and stay focused."
#     ]
#     return random.choice(quotes)

# # Daily Challenge Section
# def get_daily_challenge():
#     challenges = [
#         "Write down 3 things you learned today.",
#         "Try something new and reflect on your experience.",
#         "Help a friend solve a problem today.",
#         "Read an inspiring story and share what you learned.",
#         "Practice positive self-talk for 5 minutes."
#     ]
#     return random.choice(challenges)

# # Quiz Section
# def quiz_section():
#     st.subheader("🎯 Growth Mindset Quiz")
#     questions = {
#         "What is a growth mindset?": ["A fixed way of thinking", "The belief that abilities can grow", "Avoiding challenges", "Not making mistakes"],
#         "What should you do when you fail?": ["Give up", "Learn from it", "Blame others", "Ignore it"],
#         "How do you develop a growth mindset?": ["Practice and effort", "Innate talent only", "Avoiding hard tasks", "Never seeking feedback"],
#         "Why is perseverance important?": ["It builds resilience", "It's unnecessary", "It guarantees instant success", "It shows weakness"],
#         "How should you approach challenges?": ["As opportunities to grow", "By avoiding them", "With fear", "By quitting"]
#     }

#     score = 0
#     user_answers = {}
#     total_questions = len(questions)

#     progress_bar = st.progress(0)
#     progress = 0

#     for question, options in questions.items():
#         user_answers[question] = st.radio(f"**{question}**", options, index=None)
#         progress += 100 / total_questions
#         progress_bar.progress(int(progress))
#         time.sleep(0.1)  # Slight delay for smooth progress bar animation

#     if st.button("✅ Submit Answers"):
#         correct_answers = {
#             "What is a growth mindset?": "The belief that abilities can grow",
#             "What should you do when you fail?": "Learn from it",
#             "How do you develop a growth mindset?": "Practice and effort",
#             "Why is perseverance important?": "It builds resilience",
#             "How should you approach challenges?": "As opportunities to grow"
#         }

#         for question, correct_answer in correct_answers.items():
#             if user_answers.get(question) == correct_answer:
#                 score += 1

#         st.success(f"🎉 You scored {score}/{len(questions)}! Keep up the great work! 🚀")

# # Leaderboard Section
# def leaderboard():
#     st.subheader("🏆 Leaderboard - Top Achievers")
#     leaders = {"Awais": 95, "Maaz": 90, "Bachal": 88, "Ayesha": 85, "Zain": 82}
#     sorted_leaders = dict(sorted(leaders.items(), key=lambda item: item[1], reverse=True))

#     leaderboard_html = "<table class='leaderboard-table'><tr><th>Name</th><th>Points</th></tr>"
#     for name, points in sorted_leaders.items():
#         leaderboard_html += f"<tr><td>{name}</td><td>{points}</td></tr>"
#     leaderboard_html += "</table>"

#     st.markdown(leaderboard_html, unsafe_allow_html=True)

# # Growth Mindset Challenge Page
# def growth_mindset_page():
#     apply_custom_css()
#     st.markdown("<p class='title'>🚀 Growth Mindset Challenge</p>", unsafe_allow_html=True)
#     st.subheader("✨ Learn, Improve, and Grow")

#     st.markdown("""
#     A **growth mindset** is the belief that abilities and intelligence can be developed.  
#     With **hard work, learning, and persistence**, you can improve your skills.  
#     """)

#     # User Input
#     name = st.text_input("📌 Enter your name:")
#     if name:
#         st.write(f"👋 Welcome, {name}! Ready to build a growth mindset?")

#     # Start Button
#     if st.button("🚀 Click to Start"):
#         st.success("🔥 Great! Keep learning and growing!")

#     # Motivational Quote
#     st.markdown(f"<div class='card'>💡 **Inspirational Quote:** {get_motivational_quote()}</div>", unsafe_allow_html=True)

#     # Daily Challenge
#     st.markdown(f"<div class='card'>📌 **Today's Challenge:** {get_daily_challenge()}</div>", unsafe_allow_html=True)

#     # Quiz Section
#     quiz_section()

#     # Leaderboard
#     leaderboard()

# # Run the Streamlit App
# if __name__ == "__main__":
#     growth_mindset_page()



# import streamlit as st
# import random
# import time

# # Custom CSS for improved UI and animations
# def apply_custom_css():
#     st.markdown(
#         """
#         <style>
#             body {
#                 background-color: #1E1E1E;
#                 color: #FFFFFF;
#                 font-family: Arial, sans-serif;
#             }
#             .stButton>button {
#                 background-color: #007ACC;
#                 color: white;
#                 border-radius: 10px;
#                 padding: 10px;
#                 font-size: 18px;
#                 border: none;
#                 transition: background-color 0.3s ease, transform 0.2s ease;
#             }
#             .stButton>button:hover {
#                 background-color: #005A99;
#                 transform: scale(1.05);
#             }
#             .stTextInput>div>div>input {
#                 border-radius: 10px;
#                 padding: 10px;
#                 border: 1px solid #007ACC;
#             }
#             .title {
#                 font-size: 32px;
#                 font-weight: bold;
#                 color: #F4A261;
#                 text-align: center;
#                 opacity: 0;
#                 animation: fadeIn 2s forwards;
#             }
#             @keyframes fadeIn {
#                 from { opacity: 0; }
#                 to { opacity: 1; }
#             }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # Fetch random motivational quote
# def get_motivational_quote():
#     quotes = [
#         "Your only limit is your mind.",
#         "Failure is not the opposite of success; it's part of success.",
#         "Don't stop when you're tired. Stop when you're done!",
#         "Push yourself, because no one else is going to do it for you.",
#         "Dream big, work hard, and stay focused."
#     ]
#     return random.choice(quotes)

# # Daily Challenge Section
# def get_daily_challenge():
#     challenges = [
#         "Write down 3 things you learned today.",
#         "Try something new and reflect on your experience.",
#         "Help a friend solve a problem today.",
#         "Read an inspiring story and share what you learned.",
#         "Practice positive self-talk for 5 minutes."
#     ]
#     return random.choice(challenges)

# # Quiz Section
# def quiz_section():
#     st.subheader("Growth Mindset Quiz")
#     questions = {
#         "What is a growth mindset?": ["A fixed way of thinking", "The belief that abilities can grow", "Avoiding challenges", "Not making mistakes"],
#         "What should you do when you fail?": ["Give up", "Learn from it", "Blame others", "Ignore it"],
#         "How do you develop a growth mindset?": ["Practice and effort", "Innate talent only", "Avoiding hard tasks", "Never seeking feedback"],
#         "Why is perseverance important?": ["It builds resilience", "It's unnecessary", "It guarantees instant success", "It shows weakness"],
#         "How should you approach challenges?": ["As opportunities to grow", "By avoiding them", "With fear", "By quitting"]
#     }

#     score = 0
#     user_answers = {}
#     total_questions = len(questions)

#     progress_bar = st.progress(0)
#     progress = 0

#     for question, options in questions.items():
#         user_answers[question] = st.radio(question, options, index=0)
#         progress += 100 / total_questions
#         progress_bar.progress(int(progress))
#         time.sleep(0.2)  # Slight delay for smooth progress bar animation

#     if st.button("Submit Answers"):
#         correct_answers = {
#             "What is a growth mindset?": "The belief that abilities can grow",
#             "What should you do when you fail?": "Learn from it",
#             "How do you develop a growth mindset?": "Practice and effort",
#             "Why is perseverance important?": "It builds resilience",
#             "How should you approach challenges?": "As opportunities to grow"
#         }

#         for question, correct_answer in correct_answers.items():
#             if user_answers.get(question) == correct_answer:
#                 score += 1

#         st.success(f"You scored {score}/{len(questions)}! Keep up the great work!")

# # Leaderboard Section (Static Example)
# def leaderboard():
#     st.subheader("Leaderboard - Top Achievers")
#     leaders = {"Awais": 95, "Maaz": 90, "Bachal": 88, "Ayesha": 85, "Zain": 82}
#     sorted_leaders = dict(sorted(leaders.items(), key=lambda item: item[1], reverse=True))
#     for name, points in sorted_leaders.items():
#         st.write(f"{name}: {points} points")

# # Growth Mindset Challenge Page
# def growth_mindset_page():
#     apply_custom_css()
#     st.markdown("<p class='title'>Growth Mindset Challenge</p>", unsafe_allow_html=True)
#     st.subheader("Learn, Improve, and Grow")

#     st.write("""
#     A growth mindset is the belief that abilities and intelligence can be developed.  
#     With hard work, learning, and persistence, you can improve your skills.
#     """)

#     # User Input
#     name = st.text_input("Enter your name:")
#     if name:
#         st.write(f"Welcome, {name}! Ready to build a growth mindset?")

#     # Start Button
#     if st.button("Click to Start"):
#         st.success("Great! Keep learning and growing!")

#     # Motivational Quote
#     st.info(f"Inspirational Quote: {get_motivational_quote()}")

#     # Daily Challenge
#     st.warning(f"Today's Challenge: {get_daily_challenge()}")

#     # Quiz Section
#     quiz_section()

#     # Leaderboard
#     leaderboard()

# # Run the Streamlit App
# if __name__ == "__main__":
#     growth_mindset_page()
