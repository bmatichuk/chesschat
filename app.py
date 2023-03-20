import streamlit as st
import chess
import chess.svg
from IPython.display import SVG, display
from streamlit.components.v1 import html

# Define your javascript
my_js = """
console.log("Hola mundo");
"""

# Wrapt the javascript as html code
my_html = f"<script>{my_js}</script>"

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

svg = chess.svg.board(board=board)

root = ET.fromstring(svg)
pieces = list(board.fen().split()[0])

for i, piece in enumerate(pieces):
    x = i % 8
    y = i // 8
    square = get_square(x, y)
    symbol = get_piece(piece)
    if symbol:
        rect = root.find(f".//*[@id='{square}']")
        rect.set('onclick', f"handle_click('{square}')")
        rect.set('cursor', 'pointer')

svg = ET.tostring(root, encoding='unicode')

def handle_click(square):
    st.write(f"Selected square: {square}")
    
html = f"<div style='width: 400px; height: 400px;'>{svg}</div>"
st.markdown(html, unsafe_allow_html=True)

