from pyrogram import Client
import access_creds
import os
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, UsernameInvalid, UsernameNotOccupied, ChatAdminRequired
import datetime 

app = Client(session_name='my_session', api_id=access_creds.api_id, api_hash=access_creds.api_hash)
last_100_messages_list = []

def Search_last_100_messages():
    try:
        chat_creds = input('Enter correct numeric chat ID or chat username: ')
        with app:
            print('\n\033[1;90mGetting information...\n\033[1;00m')
            for message in app.get_history(chat_id=chat_creds):
                print('\033[1;94m' + datetime.datetime.fromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S')+ '\033[1;00m')
                print(message.text)
                last_100_messages_list.append(datetime.datetime.fromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S'))
                last_100_messages_list.append(message.text)
            with open("Telegram_scan_results.txt", 'a') as output:
                output.write('CHAT (id = {}) LAST 100 MESSAGES => \n'.format(chat_creds))
                for row in last_100_messages_list:
                    output.write(str(row) + '\n')
    except ChatAdminRequired:
        print('\033[1;93mChat Admin permissions required!\033[1;00m')
    except (PeerIdInvalid, UsernameInvalid, UsernameNotOccupied, IndexError, TypeError):
        print('\033[1;91mNot correct input!\033[1;00m')        
    print('\nOne can find results in \033[1;95m{}/Telegram_scan_results.txt\033[1;00m file'.format(os.getcwd()))
