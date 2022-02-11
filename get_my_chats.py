from pyrogram import Client
import access_creds
import os

my_chats_list = []
app = Client(session_name='my_session', api_id=access_creds.api_id, api_hash=access_creds.api_hash)

def My_chats():
    with app:
        print('\n\033[1;90mGetting information...\033[1;00m')
        for dialog in app.iter_dialogs():
            my_chats_list_row = 'ID:{}'.format(dialog.chat.id), dialog.chat.first_name, dialog.chat.last_name, 'username:{}'.format(dialog.chat.username), 'title:{}'.format(dialog.chat.title)
            if dialog.chat.title is None:
                if dialog.chat.first_name is None:
                    dialog.chat.first_name = ''
                elif dialog.chat.last_name is None:
                    dialog.chat.last_name = ''
                print('\033[1;95m')
                print(dialog.chat.first_name, dialog.chat.last_name, '\033[1;00m=>')
                print('\033[1;96mtype\033[1;00m:', dialog.chat.type)
                print('\033[1;96mid\033[1;00m:', dialog.chat.id)
                print('\033[1;96mis verified\033[1;00m:', dialog.chat.is_verified)
                print('\033[1;96mis restricted\033[1;00m:', dialog.chat.is_restricted)
                print('\033[1;96mis scam\033[1;00m:', dialog.chat.is_scam)
                print('\033[1;96mis fake\033[1;00m:', dialog.chat.is_fake)
                print('\033[1;96musername\033[1;00m:', dialog.chat.username)
            else:
                print('\033[1;95m')
                print(dialog.chat.title, '\033[1;00m=>')
                print('\033[1;96mtype\033[1;00m:', dialog.chat.type)
                print('\033[1;96mid\033[1;00m:', dialog.chat.id)
                print('\033[1;96mis verified\033[1;00m:', dialog.chat.is_verified)
                print('\033[1;96mis restricted\033[1;00m:', dialog.chat.is_restricted)
                print('\033[1;96mis scam\033[1;00m:', dialog.chat.is_scam)
                print('\033[1;96mis fake\033[1;00m:', dialog.chat.is_fake)
                print('\033[1;96musername\033[1;00m:', dialog.chat.username)
                print('\033[1;96mmembers count\033[1;00m:', dialog.chat.members_count)
            my_chats_list.append(list(my_chats_list_row))
        with open("Telegram_scan_results.txt", 'a') as output:
            output.write('MY CHATS => \n')
            for row in my_chats_list:
                output.write(str(row) + '\n')
        
    with app:
        print('\nTotal amount of my chats is\033[1;96m', app.get_dialogs_count(), '\033[1;00m')


    print('One can find scan results in \033[1;95m{}/Telegram_scan_results.txt\033[1;00m file'.format(os.getcwd()))
