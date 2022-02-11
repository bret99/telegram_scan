from pyrogram import Client
import access_creds
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, UsernameInvalid, UsernameNotOccupied, ChatAdminRequired
import os

chat_members_list = []
chat_administrators_list = []
chat_bots_list = []
app = Client(session_name='my_session', api_id=access_creds.api_id, api_hash=access_creds.api_hash)

def Chat_members():
    chat_members = input("Enter correct numeric chat ID or chat username: ")
    try:
        with app:
            print('\n\033[1;90mGetting information...\n\033[1;00m')
            print("\033[1;95mMembers \033[1;00m=>")
            for member in app.iter_chat_members(chat_members, filter='all'):
                members = 'ID:{}'.format(member.user.id), member.user.first_name, member.user.last_name, 'username:{}'.format(member.user.username), 'phone number:{}'.format(member.user.phone_number)
                print('\033[1;96mid\033[1;00m:', member.user.id, '\033[1;96mfirst name\033[1;00m:', member.user.first_name, '\033[1;96mlast name\033[1;00m:', member.user.last_name, '\033[1;96musername\033[1;00m:', member.user.username, '\033[1;96mphone number\033[1;00m:', member.user.phone_number)
                chat_members_list.append(list(members))
            with open("Telegram_scan_results.txt", 'a') as output:
                output.write('CHAT (id = {}) MEMBERS => \n'.format(chat_members))
                for row in chat_members_list:
                    output.write(str(row) + '\n')
            
            print("\033[1;95mAdministrators \033[1;00m=>")
            for member in app.iter_chat_members(chat_members, filter="administrators"):
                administrators = 'ID:{}'.format(member.user.id), member.user.first_name, member.user.last_name, 'username:{}'.format(member.user.username), 'phone number:{}'.format(member.user.phone_number)
                print('\033[1;96mid\033[1;00m:', member.user.id, '\033[1;96mfirst name\033[1;00m:', member.user.first_name, '\033[1;96mlast name\033[1;00m:', member.user.last_name, '\033[1;96musername\033[1;00m:', member.user.username, '\033[1;96mphone number\033[1;00m:', member.user.phone_number)
                chat_administrators_list.append(list(administrators))
            with open('Telegram_scan_results.txt', 'a') as output:
                output.write('Administrators =>')
                for row in chat_administrators_list:
                    output.write(str(row) + '\n')
    
            print("\033[1;95mBots \033[1;00m=>")
            for member in app.iter_chat_members(chat_members, filter="bots"):
                bots = 'ID:{}'.format(member.user.id), member.user.first_name, member.user.last_name, 'username:{}'.format(member.user.username), 'phone number:{}'.format(member.user.phone_number)
                print('\033[1;96mid\033[1;00m:', member.user.id, '\033[1;96mfirst name\033[1;00m:', member.user.first_name, '\033[1;96mlast name\033[1;00m:', member.user.last_name, '\033[1;96musername\033[1;00m:', member.user.username, '\033[1;96mphone number\033[1;00m:', member.user.phone_number)
                chat_bots_list.append(list(bots))
            with open('Telegram_scan_results.txt', 'a') as output:
                output.write('Bots =>')
                for row in chat_bots_list:
                    output.write(str(row) + '\n')
                
        with app:
            print('\nTotal amount of chat members is\033[1;96m', app.get_chat_members_count(chat_members), '\033[1;00m')
        print('One can find scan results in \033[1;95m{}/Telegram_scan_results.txt\033[1;00m file'.format(os.getcwd()))
    except ChatAdminRequired:
        print('\033[1;93mChat Admin permissions required!\033[1;00m')
    except (PeerIdInvalid, UsernameInvalid, UsernameNotOccupied, IndexError):
        print("\033[91mNot correct input!\033[00m")
