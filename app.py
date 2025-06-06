import streamlit as st
import random
import time

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
    st.session_state.username = ""
    st.session_state.level = "Easy"
    st.session_state.ready = False

def check_winner(board):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for i,j,k in wins:
        if board[i] and board[i] == board[j] == board[k]:
            return board[i]
    if "" not in board:
        return "Draw"
    return None

def easy_ai(board):
    empty = [i for i, val in enumerate(board) if val == ""]
    return random.choice(empty) if empty else None

def medium_ai(board):
    # Try to win or block
    for mark in ["O", "X"]:
        for i in range(9):
            if board[i] == "":
                board_copy = board[:]
                board_copy[i] = mark
                if check_winner(board_copy) == mark:
                    return i
    return easy_ai(board)

def computer_move(board, level):
    if level == "Easy":
        return easy_ai(board)
    elif level == "Medium":
        return medium_ai(board)
    else:
        return easy_ai(board)  # Placeholder for future Hard AI

def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.result = None

# Setup screen
if not st.session_state.ready:
    st.markdown('<div class="title">Welcome to Tic Tac Toe</div>', unsafe_allow_html=True)
    st.session_state.username = st.text_input("Enter your name:", value=st.session_state.username)
    st.session_state.level = st.selectbox("Choose difficulty:", ["Easy", "Medium"])
    if st.button("Start Game") and st.session_state.username.strip():
        st.session_state.ready = True
        st.rerun()
else:
    st.markdown(f'<div class="title">Tic Tac Toe vs Computer ({st.session_state.level})</div>', unsafe_allow_html=True)
    st.subheader(f"Player: {st.session_state.username} (X)")
    st.markdown("---")

    if st.session_state.result:
        if st.session_state.result == "Draw":
            st.info("Game Over: It's a Draw! ⚫")
        else:
            emoji = "❌" if st.session_state.result == "X" else "⭕"
            winner = "You" if st.session_state.result == "X" else "Computer"
            st.success(f"{winner} Wins! {emoji}")
        if st.button("Play Again 🔄"):
            reset_game()
            st.rerun()
    else:
        cols = st.columns(3)
        for i in range(9):
            with cols[i % 3]:
                if st.session_state.board[i] == "":
                    if st.button(" ", key=i):
                        st.session_state.board[i] = "X"
                        st.session_state.result = check_winner(st.session_state.board)
                        if not st.session_state.result:
                            move = computer_move(st.session_state.board, st.session_state.level)
                            if move is not None:
                                time.sleep(0.3)
                                st.session_state.board[move] = "O"
                            st.session_state.result = check_winner(st.session_state.board)
                        st.rerun()
                else:
                    st.markdown(f"<div style='text-align:center;font-size:32px;'>{st.session_state.board[i]}</div>", unsafe_allow_html=True)
