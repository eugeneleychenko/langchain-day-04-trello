import streamlit as st
import requests
from trello import TrelloClient

def get_trello_boards(client):
    return client.list_boards()

def get_trello_cards(board):
    return board.all_cards()

def get_list_from_card(board, card):
    return board.get_list(card.list_id)

def get_members_from_card(api_key, token, card_id):
    url = f"https://api.trello.com/1/cards/{card_id}/members"
    query = {
        'key': api_key,
        'token': token
    }
    response = requests.request("GET", url, params=query)
    return response.json()

def main():
    st.title('Trello Board Viewer')

    api_key = st.text_input('Enter your Trello API Key', type='password')
    token = st.text_input('Enter your Trello Token', type='password')

    if api_key and token:
        client = TrelloClient(
            api_key=api_key,
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
                st.write(f"**Card Name:** {card.name}")
                st.write(f"**Card Description:** {card.description}")
                list = get_list_from_card(selected_board, card)
                st.write(f"**Card List:** {list.name}")
                st.write("**Card Members:**")
                members = get_members_from_card(api_key, token, card.id)
                for member in members:
                    st.write(member['fullName'])
                st.write("**Card Comments:** ")
                for comment in card.comments:
                    st.write(comment['data']['text'])
                st.markdown("---")  # This adds a horizontal line

if __name__ == "__main__":
    main()