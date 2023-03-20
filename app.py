import streamlit as st
import chess
import chess.svg

@st.cache(allow_output_mutation=True)
def get_board():
    return chess.Board()

board = get_board()
st.title("Streamlit Chess Board")

start_square = st.session_state.get("start_square", None)
end_square = st.session_state.get("end_square", None)

def square_name_to_coord(square_name):
    file, rank = square_name
    x = chess.FILE_NAMES.index(file)
    y = 7 - chess.RANK_NAMES.index(rank)
    return x, y

def render_board(board):
    rows = 8
    cols = 8
    for row in range(rows):
        cols_list = st.beta_columns(cols)
        for col in range(cols):
            square_name = chess.FILE_NAMES[col] + chess.RANK_NAMES[row]
            x, y = square_name_to_coord(square_name)
            piece = board.piece_at(chess.square(x, y))

            if piece:
                piece_unicode = piece.unicode_symbol()
            else:
                piece_unicode = " "

            is_dark_square = (row + col) % 2 == 1
            square_color = "#d18b47" if is_dark_square else "#ffce9e"

            with cols_list[col]:
                if st.button(piece_unicode, key=square_name, on_click=handle_click, args=(square_name,)):
                    pass

def handle_click(square_name):
    if not start_square:
        st.session_state.start_square = square_name
    else:
        st.session_state.end_square = square_name

        move = chess.Move.from_uci(st.session_state.start_square + st.session_state.end_square)

        if move in board.legal_moves:
            board.push(move)
            st.success("Moved successfully!")
        else:
            st.error("Invalid move!")

        st.session_state.start_square = None
        st.session_state.end_square = None

# Custom CSS style for the buttons
st.markdown(
    """
    <style>
        .chess-btn {
            background-color: transparent !important;
            border: none !important;
            color: black !important;
            font-size: 32px !important;
            width: 75px !important;
            height: 75px !important;
            line-height: 75px !important;
            text-align: center !important;
            padding: 0 !important;
        }
        .chess-btn:active {
            background-color: rgba(0, 0, 0, 0.1) !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

render_board(board)
