import streamlit as st
import chess
import chess.svg
import xml.etree.ElementTree as ET
import re

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

piece_map = {
    'P': '♙',
    'N': '♘',
    'B': '♗',
    'R': '♖',
    'Q': '♕',
    'K': '♔',
    'p': '♟',
    'n': '♞',
    'b': '♝',
    'r': '♜',
    'q': '♛',
    'k': '♚'
}

def get_piece(symbol):
    return piece_map.get(symbol, '')

def get_square(x, y):
    file = chess.FILE_NAMES[x]
    rank = chess.RANK_NAMES[7 - y]
    return file + rank

square = st.text_input("Enter square to select (e.g. e2):")
if st.button("Select square"):
    if chess.SQUARE_NAMES.count(square) > 0:
        st.write(f"Selected square: {square}")
    else:
        st.error("Invalid square!")

svg = chess.svg.board(board=board)

html = f"<div style='width: 400px; height: 400px;'>{svg}</div>"
st.markdown(html, unsafe_allow_html=True)
