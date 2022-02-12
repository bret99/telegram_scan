from pyrogram import Client
import access_creds
import os
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, UsernameInvalid, UsernameNotOccupied, ChatAdminRequired
import datetime 

app = Client(session_name='my_session', api_id=access_creds.api_id, api_hash=access_creds.api_hash)
search_query_results_list = []

def Search_query():
    try:
        chat_creds = input('Enter correct numeric chat ID or chat username: ')
        search_query = input('Enter search query: ')
        with app:
            print('\n\033[1;90mGetting information...\n\033[1;00m')
            for message in app.search_messages(chat_id=chat_creds, query=search_query):
                messages = datetime.datetime.fromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S') + ' from user ID:{}'.format(message.from_user.id) + '\n' + message.text
                message = '\033[1;94m' + datetime.datetime.fromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S') + '\033[1;00m from user ID:\033[1;94m{}\033[1;00m'.format(message.from_user.id) + '\n' + message.text
                print(message)
                search_query_results_list.append(messages)
            with open("Telegram_scan_results.txt", 'a') as output:
                output.write('CHAT (id = {0}) QUERY ({1}) => \n'.format(chat_creds, search_query))
                for row in search_query_results_list:
                    output.write(str(row) + '\n')
        if len(search_query_results_list) == 0:
            print("There are no posts one can get")
        print('\nOne can find scan results in \033[1;95m{}/Telegram_scan_results.txt\033[1;00m file'.format(os.getcwd()))
    except ChatAdminRequired:
        print('\033[1;93mChat Admin permissions required!\033[1;00m')
    except (PeerIdInvalid, UsernameInvalid, UsernameNotOccupied, IndexError, TypeError, AttributeError):
        with open("Telegram_scan_results.txt", 'a') as output:
            output.write('CHAT (id = {0}) QUERY ({1}) => \n'.format(chat_creds, search_query))
            for row in search_query_results_list:
                output.write(str(row) + '\n')
        print('\033[1;91mNot correct input or smth went wrong!\033[1;00m')
        print('\nOne can find scan results in \033[1;95m{}/Telegram_scan_results.txt\033[1;00m file'.format(os.getcwd()))
