from pyrogram import Client
import access_creds
import os
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, UsernameInvalid, UsernameNotOccupied, ChatAdminRequired
import datetime 

app = Client(session_name='my_session', api_id=access_creds.api_id, api_hash=access_creds.api_hash)
urls_list = []

def Search_urls():
    try:
        chat_creds = input('Enter correct numeric chat ID or chat username: ')
        search_query_1 = 'http://'
        with app:
            print('\n\033[1;90mGetting information...\n\033[1;00m')
            for message in app.search_messages(chat_id=chat_creds, query=search_query_1):
                messages = datetime.datetime.fromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S') + ' from user ID:{}'.format(message.from_user.id) + '\n' + message.text
                message = '\033[1;94m' + datetime.datetime.fromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S') + '\033[1;00m from user ID:\033[1;94m{}\033[1;00m'.format(message.from_user.id) + '\n' + message.text
                print(message)
                urls_list.append(messages)
        search_query_2 = 'https://'
        with app:
            for message in app.search_messages(chat_id=chat_creds, query=search_query_2):
                messages = datetime.datetime.fromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S') + ' from user ID:{}'.format(message.from_user.id) + '\n' + message.text
                message = '\033[1;94m' + datetime.datetime.fromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S') + '\033[1;00m from user ID:\033[1;94m{}\033[1;00m'.format(message.from_user.id) + '\n' + message.text
                print(message)
                urls_list.append(messages)
            with open("Telegram_scan_results.txt", 'a') as output:
                output.write('CHAT (id = {}) URLS => \n'.format(chat_creds))
                for row in urls_list:
                    output.write(str(row) + '\n')
            print('\nOne can find scan results in \033[1;95m{}/Telegram_scan_results.txt\033[1;00m file'.format(os.getcwd()))
    except ChatAdminRequired:
        print('\033[1;93mChat Admin permissions required!\033[1;00m')
    except (PeerIdInvalid, UsernameInvalid, UsernameNotOccupied, IndexError, TypeError, AttributeError):
        with open("Telegram_scan_results.txt", 'a') as output:
            output.write('CHAT (id = {}) URLS => \n'.format(chat_creds))
            for row in urls_list:
                output.write(str(row) + '\n')
        print('\033[1;91mNot correct input or smth went wrong!\033[1;00m')
        print('\nOne can find scan results in \033[1;95m{}/Telegram_scan_results.txt\033[1;00m file'.format(os.getcwd()))
