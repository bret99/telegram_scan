import sys
import os
from get_user_info import User_info
from get_my_chats import My_chats
from get_chat_info import Chat_info 
from get_chat_members import Chat_members
from get_chat_animations import Search_animations
from get_chat_photos import Search_photos
from get_chat_audios import Search_audios
from get_chat_videos import Search_videos
from get_chat_voice_notes import Search_voice_notes
from get_chat_documents import Search_documents
from get_chat_urls import Search_urls
from get_chat_contacts import Search_contacts
from get_chat_location import Search_locations
from search_query import Search_query
from search_user_messages import Search_user_messages
from get_last_100_messages import Search_last_100_messages

def main_menu():
    print("\n\033[1;96mTelegram Scanner \033[1;00mmodules:\n\n[\033[1;96m1\033[1;00m] Get user info\n[\033[1;96m2\033[1;00m] Get my chats info\n\033[1;00m[\033[1;96m3\033[1;00m] Get chat info\n\033[1;00m[\033[1;96m4\033[1;00m] Get chat members\n\033[1;00m[\033[1;96m5\033[1;00m] Get chat animations\033[1;00m\n[\033[1;96m6\033[1;00m] Get chat photos\033[1;00m\n[\033[1;96m7\033[1;00m] Get chat audios\n[\033[1;96m8\033[1;00m] Get chat videos\n[\033[1;96m9\033[1;00m] Get chat chat voice notes\n\033[1;00m[\033[1;96m10\033[1;00m] Get chat documents\n\033[1;00m[\033[1;96m11\033[1;00m] Get chat urls\033[1;00m\n[\033[1;96m12\033[1;00m] Get chat contacts\n\033[1;00m[\033[1;96m13\033[1;00m] Get chat locations\n\033[1;00m[\033[1;96m14\033[1;00m] Search query\033[1;00m\n[\033[1;96m15\033[1;00m] Get user messages\n\033[1;00m[\033[1;96m16\033[1;00m] Get last 100 chat messages\033[1;00m\n\033[1;00m[\033[1;96m99\033[1;00m]\033[1;90m Exit\033[1;00m\n")
    choose_module = input("Enter module number: ")
    if choose_module == "1":
        User_info()
        main_menu()
    elif choose_module == "2":
        My_chats()
        main_menu()
    elif choose_module == "3":
        Chat_info()
        main_menu()
    elif choose_module == "4":
        Chat_members()
        main_menu()
    elif choose_module == "5":
        Search_animations()
        main_menu()
    elif choose_module == "6":
        Search_photos()
        main_menu()
    elif choose_module == "7":
        Search_audios()
        main_menu()
    elif choose_module == "8":
        Search_videos()
        main_menu()
    elif choose_module == "9":
        Search_voice_notes()
        main_menu()
    elif choose_module == "10":
        Search_documents()
        main_menu()
    elif choose_module == "11":
        Search_urls()
        main_menu()
    elif choose_module == "12":
        Search_contacts()
        main_menu()
    elif choose_module == "13":
        Search_locations()
        main_menu()
    elif choose_module == "14":
        Search_query()
        main_menu()
    elif choose_module == "15":
        Search_user_messages()
        main_menu()
    elif choose_module == "16":
        Search_last_100_messages()
        main_menu()
    elif choose_module == "99":
        sys.exit()
    else:
        sys.exit("\033[1;91mWrong input!\033[1;00m")


main_menu()
