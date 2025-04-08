def add_song(song_id):
    new_song = {}
    
    new_song['song_id'] = song_id
    new_song['song_name'] = input("Enter Song Name: ").title()
    new_song['artist_name'] = input("Enter Artist Name: ").title()
    new_song['song_genre'] = input("Enter Song Genre: ").upper()
    new_song['release_year'] = int(input("Enter Release Year: "))
    playlist.append(new_song)

    print("Record added successfully.")

#TODO(Kenji Enishi Campos): create a function that updates a song in the playlist
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

#TODO(Jedi Duncan Gonot): create a function that displays all songs in the playlist
#TODO(Paul Benidict Reduta): create a function that searches for a specific son
#TODO(Dion Manicio): create a function that deletes a song in the playlist

#temporary playlist
playlist = [
    {
        "song_id": 1,
        "song_name": "Marilag",
        "song_artist": "Dionela",
        "song_genre": "R&B/SOUL",
        "release_year": 2024
    },
    {
        "song_id": 2,
        "song_name": "Plastic Love",
        "song_artist": "Mariya Takeuchi",
        "song_genre": "CITY POP",
        "release_year": 1968
    }
]

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
            song_id += 1
            add_song(song_id)
            input("Press any key to continue...")
        case 2:
            print(" ")
            update_playlist()
            input("Press any key to continue...")
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            break
        case _:
            print(f"\n({user_choice}) is not a valid input. ",
                  "Please try again...")    