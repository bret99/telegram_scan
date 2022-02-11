from pyrogram import Client
import access_creds
import os
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, UsernameInvalid, UsernameNotOccupied, ChatAdminRequired
import datetime 

app = Client(session_name='my_session', api_id=access_creds.api_id, api_hash=access_creds.api_hash)
photos_list = []
from_users_list = []

def Search_photos():
    try:
        chat_creds = input('Enter correct numeric chat ID or chat username: ')
        try:
            with app:
                print('\n\033[1;90mGetting information...\n\033[1;00m')
                for message in app.search_messages(chat_id=chat_creds, filter='photo'):
                    print('\033[1;94m', datetime.datetime.fromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S') + '\033[1;00m from user ID:\033[1;94m' + str(message.from_user.id) + '\033[00m')
                    from_users_list.append(datetime.datetime.fromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S') + ' from user ID:' + str(message.from_user.id))
                    photos_list.append(message.photo.file_id)
        except AttributeError:
            print('')
        with open("Telegram_scan_results.txt", 'a') as output:
            output.write('CHAT (id = {}) PHOTOS => \n'.format(chat_creds))
            for row in from_users_list:
                output.write(str(row) + '\n')

        if len(photos_list) == 0:
            print('There are no photos one can get.')
        else:
            print('\nTotal amount of photos is \033[1;96m{}\033[1;00m'.format(len(photos_list)))
            download_photos = input("Enter how many photos to download (press \033[1;93m<Enter>\033[1;00m to skip): ")
            
            if download_photos == '' or download_photos == '0':
                print('One can find scan results in \033[1;95m{}/Telegram_scan_results.txt\033[1;00m file'.format(os.getcwd()))
            else:
                print('\n\033[1;90mDownloading...\033[1;00m\n')
                try:
                    count = 0
                    with app:
                        while count < int(download_photos):
                            app.download_media(photos_list[count], file_name='{0}/photos/{1}/'.format(os.getcwd(), chat_creds))
                            count += 1
                    print('One can find photos in \033[1;95m{0}/photos/{1}\033[1;00m directory'.format(os.getcwd(), chat_creds))
                except (TypeError, ValueError):
                    print('\033[1;91mNot correct input or smth went wrong!\033[1;00m\n')
                print('One can find scan results in \033[1;95m{}/Telegram_scan_results.txt\033[1;00m file'.format(os.getcwd()))
    except ChatAdminRequired:
        print('\033[1;93mChat Admin permissions required!\033[1;00m')
    except (PeerIdInvalid, UsernameInvalid, UsernameNotOccupied, IndexError, TypeError):
        print('\033[1;91mNot correct input!\0331;00m')
