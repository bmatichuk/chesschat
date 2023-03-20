import streamlit as st
import chess
import stchess

@st.cache(allow_output_mutation=True)
def get_board():
    return chess.Board()

board = get_board()

st.title("Streamlit Chess Board")

move = st.text_input("Enter move in UCI notation (e.g. e2e4):")

if move:
    try:
        board.push_uci(move)
    except ValueError:
        st.error("Invalid move!")
    else:
        st.success("Moved successfully!")

last_move = board.peek() if board.move_stack else None
selected_move = stchess.chessboard(board.fen(), last_move=last_move)

if selected_move is not None:
    try:
        move = chess.Move.from_uci(selected_move)
        if move in board.legal_moves:
            board.push(move)
        else:
            st.error("Invalid move!")
    except ValueError:
        st.error("Invalid move!")
