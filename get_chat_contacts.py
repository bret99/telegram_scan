from pyrogram import Client
import access_creds
import os
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, UsernameInvalid, UsernameNotOccupied, ChatAdminRequired
import datetime 

app = Client(session_name='my_session', api_id=access_creds.api_id, api_hash=access_creds.api_hash)
contacts_list = []

def Search_contacts():
    try:
        chat_creds = input('Enter correct numeric chat ID or chat username: ')
        try:
            with app:
                print('\n\033[1;90mGetting information...\n\033[1;00m')
                for message in app.search_messages(chat_id=chat_creds, filter='contact'):
                    print('\033[1;94m' + datetime.datetime.fromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S') + '\033[1;00m from user ID:\033[1;94m' + str(message.from_user.id) + '\n\033[1;00m' + message.contact.phone_number + ' ' + message.contact.first_name + ' ' + message.contact.last_name)
                    contacts_list.append(datetime.datetime.fromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S') + ' from user ID:' + str(message.from_user.id))
                    contacts_list.append(message.contact.phone_number + ' ' + message.contact.first_name + ' ' + message.contact.last_name)
        except AttributeError:
            print('')
        with open("Telegram_scan_results.txt", 'a') as output:
            output.write('CHAT (id = {}) CONTACTS => \n'.format(chat_creds))
            for row in contacts_list:
                output.write(str(row) + '\n')
        if len(contacts_list) == 0:
            print('There are no contacts one can get.')
        else:
            print('\nTotal amount of contacts is \033[1;94m{}'.format(len(contacts_list)/2))
            print('One can find scan results in \033[1;95m{}/Telegram_scan_results.txt\033[1;00m file'.format(os.getcwd()))
    except ChatAdminRequired:
        print('\033[1;93mChat Admin permissions required!\033[1;00m')
    except (PeerIdInvalid, UsernameInvalid, UsernameNotOccupied, IndexError, TypeError):
        print('\033[1;91mNot correct input or smth went wrong!\033[1;00m')
