import streamlit as st
import chess
import chess.svg

st.set_page_config(page_title="Streamlit Chess Board")

board = chess.Board()

st.title("Streamlit Chess Board")

move = st.text_input("Enter move in UCI notation (e.g. e2e4):")

if move:
    try:
        board.push_uci(move)
    except ValueError:
        st.error("Invalid move!")
    else:
        st.success("Moved successfully!")

svg = chess.svg.board(board=board)
html = f"<div style='width: 400px; height: 400px;'>{svg}</div>"
st.markdown(html, unsafe_allow_html=True)


