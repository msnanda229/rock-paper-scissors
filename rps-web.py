# Importing necessary libraries
import streamlit as st
import random

# Setting the page configuration
st.set_page_config(
    page_title="Rock, Paper, Scissors Game 🎮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Game title
st.title("🪨 📄 ✂️ Rock, Paper, Scissors Game")

# Game instructions
st.markdown("""
Select your move by clicking on one of the names below.  
The computer will randomly make its choice, and the result will be displayed.  
**Rules**:  
- Rock beats Scissors 🪨 > ✂️  
- Paper beats Rock 📄 > 🪨  
- Scissors beat Paper ✂️ > 📄  
---
""")

# Placeholder for showing the game result
result_placeholder = st.empty()

# Buttons for user selection
st.write("### Make your move:")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Rock 🪨", key="rock"):
        user_choice = 'r'
        computer_choice = random.choice(['r', 'p', 's'])
        result_placeholder.markdown(f"**Your choice:** Rock 🪨")
        result_placeholder.markdown(f"**Computer's choice:** {'Rock 🪨' if computer_choice == 'r' else 'Paper 📄' if computer_choice == 'p' else 'Scissors ✂️'}")

        if user_choice == computer_choice:
            st.success("🤝 It's a draw!")
        elif computer_choice == 's':
            st.success("🎉 You win! Rock crushes Scissors.")
        else:
            st.error("😅 Computer wins! Paper wraps Rock.")

with col2:
    if st.button("Paper 📄", key="paper"):
        user_choice = 'p'
        computer_choice = random.choice(['r', 'p', 's'])
        result_placeholder.markdown(f"**Your choice:** Paper 📄")
        result_placeholder.markdown(f"**Computer's choice:** {'Rock 🪨' if computer_choice == 'r' else 'Paper 📄' if computer_choice == 'p' else 'Scissors ✂️'}")

        if user_choice == computer_choice:
            st.success("🤝 It's a draw!")
        elif computer_choice == 'r':
            st.success("🎉 You win! Paper covers Rock.")
        else:
            st.error("😅 Computer wins! Scissors cut Paper.")

with col3:
    if st.button("Scissors ✂️", key="scissors"):
        user_choice = 's'
        computer_choice = random.choice(['r', 'p', 's'])
        result_placeholder.markdown(f"**Your choice:** Scissors ✂️")
        result_placeholder.markdown(f"**Computer's choice:** {'Rock 🪨' if computer_choice == 'r' else 'Paper 📄' if computer_choice == 'p' else 'Scissors ✂️'}")

        if user_choice == computer_choice:
            st.success("🤝 It's a draw!")
        elif computer_choice == 'p':
            st.success("🎉 You win! Scissors cut Paper.")
        else:
            st.error("😅 Computer wins! Rock crushes Scissors.")

# Footer
st.markdown("""
---
**Made by M.S.NANDA** 
""")
