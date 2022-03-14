from pyrogram import Client
import access_creds
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, UsernameInvalid, UsernameNotOccupied
import datetime 
import os

app = Client(session_name='my_session', api_id=access_creds.api_id, api_hash=access_creds.api_hash)

def User_info():
    user_info = input('Enter correct numeric user ID/username/phone number: ')
    try:
        with app:
            print('\n\033[1;90mGetting information...\033[1;00m')
            print('\033[1;90mDownloading profile photo...\033[1;00m\n')
            json_object = app.get_users(user_info)
            count = app.get_profile_photos_count(user_info)
            profile_photo = app.get_profile_photos(user_info)
            item = 0
            while item < count:
                app.download_media(profile_photo[item].file_id, file_name='{0}/profile_photos/{1}/'.format(os.getcwd(), user_info))
                item += 1
            if count == 0:
                print('\033[1;93m\nProfile \033[1;96m{} \033[1;93mhas no photo.\n\033[1;00m'.format(user_info))
            else:
                print('\nOne can find profile photo in \033[1;95m{0}/profile_photos/{1}\033[1;00m directory\n'.format(os.getcwd(), user_info))
    except (KeyError, IndexError, UsernameInvalid, UsernameNotOccupied):
        print("\033[1;91mNot correct input!\033[1;00m")
    except FileExistsError:
        print('\033[1;93mFile already exists!\033[1;00m')
    try:
        print('\033[1;96mid:\033[1;00m', json_object.id)
        print('\033[1;96mis contact:\033[1;00m', json_object.is_contact)
        print("\033[1;96mis mutual contact:\033[1;00m", json_object.is_mutual_contact)
        print('\033[1;96mis deleted:\033[1;00m', json_object.is_deleted)
        print('\033[1;96mis bot:\033[1;00m', json_object.is_bot)
        print('\033[1;96mis verified:\033[1;00m', json_object.is_verified)
        print('\033[1;96mis restricted:\033[1;00m', json_object.is_restricted)
        print('\033[1;96mis scam:\033[1;00m', json_object.is_scam)
        print('\033[1;96mis fake:\033[1;00m', json_object.is_fake)
        print('\033[1;96mfirst name:\033[1;00m', json_object.first_name)
        print('\033[1;96mlast name:\033[1;00m', json_object.last_name)
        print('\033[1;96mstatus:\033[1;00m', json_object.status)
        print('\033[1;96musername:\033[1;00m', json_object.username)
        print('\033[1;96mphone number:\033[1;00m', json_object.phone_number)
        print('\033[1;96mlanguage code:\033[1;00m', json_object.language_code)
        print('\033[1;96mlast online date:\033[1;00m', datetime.datetime.fromtimestamp(json_object.last_online_date).strftime('%Y-%m-%d %H:%M:%S'))
    except UnboundLocalError:
        pass
    except (PeerIdInvalid, UsernameInvalid, UsernameNotOccupied, IndexError):
        print("\033[1;91mNot correct input!\033[1;00m")
    except TypeError:
        pass
