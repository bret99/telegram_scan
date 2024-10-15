from pyrogram import Client
import access_creds
import os
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, UsernameInvalid, UsernameNotOccupied, ChatAdminRequired
import sys

app = Client('my_session', api_id=access_creds.api_id, api_hash=access_creds.api_hash)
chat_messages_list = []

def get_chat_messages():
    try:
        chat_creds = input('Enter correct numeric chat ID or chat username: ')
        messages_amount = input("Enter the number of messages to get (press \033[1;93m<Enter>\033[1;00m to get all ones): ")
        with app:
            print('\n\033[1;90mGetting information...\n\033[1;00m')
            try:
                for message in app.get_chat_history(chat_id=chat_creds, limit=int(messages_amount)):
                    print('\033[1;94m' + message.date.strftime('%Y-%m-%d %H:%M:%S')+ '\033[1;00m')
                    print(message.text)
                    chat_messages_list.append(message.date.strftime('%Y-%m-%d %H:%M:%S'))
                    chat_messages_list.append(message.text)
            except ValueError:
                sys.exit("\033[1;91mNot correct input!\033[1;00m\n")
            with open("Telegram_scan_results.txt", 'a') as output:
                output.write('CHAT (id = {}) LAST 100 MESSAGES => \n'.format(chat_creds))
                for row in chat_messages_list:
                    output.write(str(row) + '\n')
        print('\nOne can find results in \033[1;95m{}/Telegram_scan_results.txt\033[1;00m file'.format(os.getcwd()))
    except ChatAdminRequired:
        print('\033[1;93mChat Admin permissions required!\033[1;00m')
    except (PeerIdInvalid, UsernameInvalid, UsernameNotOccupied, IndexError, TypeError):
        print('\033[1;91mNot correct input!\033[1;00m')
    except KeyboardInterrupt:
        with open("Telegram_scan_results.txt", 'a') as output:
            output.write('CHAT (id = {}) MESSAGES => \n'.format(chat_creds))
            for row in chat_messages_list:
                output.write(str(row) + '\n')
        print('\nOne can find results in \033[1;95m{}/Telegram_scan_results.txt\033[1;00m file'.format(os.getcwd()))
        sys.exit("\n")
