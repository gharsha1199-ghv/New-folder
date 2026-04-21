class User:
    def __init__(self, name, mobile_no):
        self.name = name
        self.mobile_no = mobile_no
# songs=["Shape of You","Happy","Uptown Funk","Let Her Go","Someone Like You","Fix You","Believer","Stronger","Numb"]
user_account = []
My_playlist = []
My_Favorites = []



def login():
    name = input("Enter your name: ")
    mobile_no = input("Enter your mobile no.: ")
    user_account.append(User(name, mobile_no))
    print("Account created successfully 🎧")


def show_all_songs():
    print('''
    1. 🎧  Shape of You        ⏮  ▶  ⏭
    2. 🎧  Happy               ▶
    3. 🎧  Uptown Funk         ▶
    4. 🎧  Let Her Go          ▶
    5. 🎧  Someone Like You    ▶     
    6. 🎧  Fix You             ▶
    7. 🎧  Believer            ▶
    8. 🎧  Stronger            ▶
    9. 🎧  Numb                ▶
''')

def search_by_mood():
    mood = input("Enter your mood(happy / sad / angry): ")
    if mood.lower() == "happy":
        print('''    
🎵 Happy Songs:
                         
🎧  Shape of You     ⏮  ▶  ⏭
🎧  Happy            ▶
🎧  Uptown Funk      ▶
''')
    elif mood.lower() == "sad":
        print('''
🎵 Sad Songs:
              
🎧  Let Her Go       ⏮  ▶  ⏭
🎧  Someone Like You ▶
🎧  Fix You          ▶
''')
    elif mood.lower() == "angry":
        print('''
🎵 Angry Songs:
              
🎧  Believer         ⏮  ▶  ⏭
🎧  Stronger         ▶
🎧  Numb             ▶
''')
    else:
        print("No song found for this mood!")
    

def playlist():
    add_to_playlist = input("Add to Playlist (or press Enter to skip): ")
    
    if add_to_playlist:  
        My_playlist.append(add_to_playlist)
        print("Playlist Added ✅")

    if not My_playlist:
        print("No songs in playlist !")
    else:
        print("My Playlists:", My_playlist)


def fav_songs():
    add_fav_song = input("Type song name (or press Enter to skip): ")
    
    if add_fav_song:  
        My_Favorites.append(add_fav_song)
        print("song Added to Favorites ✅\n")

    if not My_Favorites:
        print("No favorites !")
    else:
        print("My Favorites:")
        for i,songs in enumerate(My_Favorites):
            if i==0:
                # print(f"\n🎧  {songs[0]}       ⏮  ▶  ⏭")
                print(f"\n🎧  {songs}      ⏮  ▶  ⏭")

            else:
                # print(f"\n🎧  {songs[0,]}      ▶")
                print(f"🎧  {songs}      ▶")

               
            # print("My Favorites:", songs)

        # print("My Favorites:", My_Favorites)


    # if not My_Favorites:
    #     add_fav_songs = input("Type song name: ")
    #     My_Favorites.append(add_fav_songs)
    #     print(My_Favorites)

    # else:
    #     print(My_Favorites)







while True:  
         
    show_name=user_account[0].name if user_account else "Guest"
    # print(f"Welcome to Mood-Based Music App 🎧\n1. Login\n2. Show All Songs\n3. Search by Mood\n4. My Playlist\n5. Favorites\n6. Exit\n7. Choose valid option")
   
    if not user_account:
        print(f"\nWelcome to Mood-Based Music App 🎧, {show_name}")
        print("1. Login")
        print("2. Show All Songs")
        print("3. Search by Mood")
        print("4. Exit")
    else:
        print(f"\nWelcome to Mood-Based Music App 🎧, {show_name}")
        print("1. Show All Songs")
        print("2. Search by Mood")
        print("3. My Playlist")
        print("4. Favorites")
        print("5. Logout")
    
    choice=int(input("Enter your choice: "))
    if not user_account:
        if choice == 1:
            login()
        elif choice == 2:
            show_all_songs()
        elif choice == 3:
            search_by_mood()
        elif choice == 4:
            # user_account.clear()
            print("Login to the app to see more Features !!\nThanks for using our app! 🎧")
            break
        else:
            print("Choose valid option !!")
    else:
        if choice == 1:
             show_all_songs()
        elif choice == 2:
             search_by_mood()
        elif choice == 3:
             playlist()
        elif choice == 4:
             fav_songs()
        elif choice == 5:
             print("Logged out !\nThanks for using our app!  🎧 \nGive us a rating! \n★ ★ ☆ ☆ ☆")
             break
        else:
            print("Choose valid option !!")
      





