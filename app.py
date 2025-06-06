import streamlit as st
import random

st.set_page_config(page_title="Tic Tac Toe AI", page_icon="🌟", layout="centered")
st.markdown("""
    <style>
        .main { background-color: #f0f2f6; }
        .stButton>button { width: 100%; height: 80px; font-size: 28px; }
        .stButton>button:hover { background-color: #d0e1f9; color: black; }
        .title { text-align: center; font-size: 36px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Initialize state
if 'board' not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.result = None

def check_winner(board):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for i,j,k in wins:
        if board[i] and board[i] == board[j] == board[k]:
            return board[i]
    if "" not in board:
        return "Draw"
    return None

def computer_move(board):
    empty = [i for i, val in enumerate(board) if val == ""]
    if empty:
        return random.choice(empty)
    return None

def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.result = None

st.markdown('<div class="title">Tic Tac Toe vs Computer</div>', unsafe_allow_html=True)
st.markdown("---")

if st.session_state.result:
    if st.session_state.result == "Draw":
        st.info("Game Over: It's a Draw! ⚫")
    else:
        emoji = "❌" if st.session_state.result == "X" else "⭕"
        st.success(f"Game Over: {st.session_state.result} wins! {emoji}")
    if st.button("Play Again 🔄"):
        reset_game()
else:
    st.subheader("Your Turn (X):")
    cols = st.columns(3)
    for i in range(9):
        with cols[i % 3]:
            if st.session_state.board[i] == "":
                if st.button(" ", key=i):
                    st.session_state.board[i] = "X"
                    st.session_state.result = check_winner(st.session_state.board)
                    if not st.session_state.result:
                        move = computer_move(st.session_state.board)
                        if move is not None:
                            st.session_state.board[move] = "O"
                        st.session_state.result = check_winner(st.session_state.board)
            else:
                st.markdown(f"<div style='text-align:center;font-size:32px;'>{st.session_state.board[i]}</div>", unsafe_allow_html=True)
