import streamlit as st
import random

# Initialize session state
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

st.title("Tic Tac Toe vs Computer")

if st.session_state.result:
    st.success(f"Game Over: {st.session_state.result}")
    if st.button("Play Again"):
        reset_game()
else:
    st.write("Your Turn: X")
    cols = st.columns(3)
    for i in range(9):
        if st.session_state.board[i] == "":
            if cols[i % 3].button(" ", key=i):
                st.session_state.board[i] = "X"
                st.session_state.result = check_winner(st.session_state.board)
                if not st.session_state.result:
                    move = computer_move(st.session_state.board)
                    if move is not None:
                        st.session_state.board[move] = "O"
                    st.session_state.result = check_winner(st.session_state.board)
        else:
            cols[i % 3].write(f"**{st.session_state.board[i]}**")
