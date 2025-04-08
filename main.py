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
            pass
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