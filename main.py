def add_song(song_id):
    new_song = {}
    
    new_song['song_id'] = song_id
    new_song['song_name'] = input("Enter Song Name: ").title()
    new_song['artist_name'] = input("Enter Artist Name: ").title()
    new_song['song_genre'] = input("Enter Song Genre: ").upper()
    new_song['release_year'] = int(input("Enter Release Year: "))
    playlist.append(new_song)

    print("Record added successfully.")

def update_playlist():
    song_id = int(input("Enter the song ID to update: "))
    song_to_update = None

    for song in playlist:
        if song["song_id"] == song_id:
            song_to_update = song
            break

    if song_to_update:
        print(
            f"Are you sure you want to update: " 
            f"{song_to_update['song_name']}?"
            )

        choice = input("Enter Y to update or N to cancel: ").upper()

        if choice == "Y":
            new_song_name = input("Enter the new song name: ").title()
            new_artist_name = input("Enter the new artist name: ").title()
            new_song_genre = input("Enter the new song genre: ").upper()
            new_release_year = int(input("Enter the new release year: "))

            song_to_update["song_name"] = new_song_name
            song_to_update["artist_name"] = new_artist_name
            song_to_update["song_genre"] = new_song_genre
            song_to_update["release_year"] = new_release_year

            print("Song updated successfully.")
        else:
            print("Update cancelled.")
    else:
        print("Song ID not found.")

def display_playlist():
    if not playlist:
        print("There are no songs in the Playlist.")
        return
    
    print("\nCurrent Playlist:")
    print("=" * 50)
    for song in playlist:
        print(f"Song ID      : {song['song_id']}")
        print(f"Song Name    : {song['song_name']}")
        print(f"Artist Name  : {song['artist_name']}")
        print(f"Song Genre   : {song['song_genre']}")
        print(f"Release Year : {song['release_year']}")
        print("-" * 50)

def search_song():
    if not playlist:
        print("The are no songs in the Playlist.")
        return
    
    song_name = input("Please Enter the Song Name: ").title()

    print("=" * 50)
    for song in playlist:
        if song["song_name"] == song_name:
            print(f"Song ID      : {song['song_id']}")
            print(f"Song Name    : {song['song_name']}")
            print(f"Artist Name  : {song['artist_name']}")
            print(f"Song Genre   : {song['song_genre']}")
            print(f"Release Year : {song['release_year']}")
            print("-" * 50)
            return
        
    print(f"There is no song named '{song_name}' found..")

def delete_song():
    song_id = int(input("Enter the Song ID to delete: "))

    for record in playlist:
        if record['song_id'] == song_id:
            playlist.remove(record)
            print("Record deleted successfully.")
            return
        
    print("Record not found.")

playlist = []
song_id_counter = 0

while True:
    print(
        "\n===========================\n" 
        + "Welcome To LR Music Station\n" 
        + "===========================\n" 
        + "1. Add a Song\n" 
        + "2. Update a Song\n" 
        + "3. Display All Songs\n" 
        + "4. Search a Song\n" 
        + "5. Delete a Song\n" 
        + "6. Exit\n"
        + "==========================="
        )
    
    user_choice = int(input("Please Enter your Choice: "))

    match user_choice:
        case 1:
            print(" ")
            song_id_counter += 1
            add_song(song_id_counter)
            input("Press any key to continue...")
        case 2:
            print(" ")
            update_playlist()
            input("Press any key to continue...")
        case 3:
            print(" ")
            display_playlist()
            input("Press any key to continue...")
        case 4:
            print(" ")
            search_song()
            input("Press any key to continue...")
        case 5:
            print(" ")
            delete_song()
            input("Press any key to continue...")
        case 6:
            break
        case _:
            print(f"\n({user_choice}) is not a valid input. ",
                  "Please try again...")    