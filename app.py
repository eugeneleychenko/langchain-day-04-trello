import streamlit as st
from trello import TrelloClient

def get_trello_cards(client, board_name):
    all_boards = client.list_boards()
    for board in all_boards:
        if board.name == board_name:
            return board.all_cards()
    return []

def main():
    st.title('Trello Board Viewer')

    api_key = st.text_input('Enter your Trello API Key', type='password')
    # api_secret = st.text_input('Enter your Trello API Secret', type='password')
    token = st.text_input('Enter your Trello Token', type='password')
    # token_secret = st.text_input('Enter your Trello Token Secret', type='password')
    board_name = st.text_input('Enter the name of the board you want to view')

    if st.button('Get Cards'):
        client = TrelloClient(
            api_key=api_key,
            # api_secret=api_secret,
            token=token,
            # token_secret=token_secret
        )

        cards = get_trello_cards(client, board_name)
        for card in cards:
            st.write(card.name)

if __name__ == "__main__":
    main()