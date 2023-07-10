import streamlit as st
from trello import TrelloClient

def get_trello_boards(client):
    return client.list_boards()

def get_trello_cards(board):
    return board.all_cards()

def main():
    st.title('Trello Board Viewer')

    api_key = st.text_input('Enter your Trello API Key', type='password')
    # api_secret = st.text_input('Enter your Trello API Secret', type='password')
    token = st.text_input('Enter your Trello Token', type='password')

    if api_key  and token:
        client = TrelloClient(
            api_key=api_key,
            # api_secret=api_secret,
            token=token
        )

        boards = get_trello_boards(client)
        board_names = [board.name for board in boards]
        selected_board_name = st.selectbox('Select a board', board_names)

        for board in boards:
            if board.name == selected_board_name:
                selected_board = board
                break

        if st.button('Get Cards'):
            cards = get_trello_cards(selected_board)
            for card in cards:
                st.write(card.name)

if __name__ == "__main__":
    main()