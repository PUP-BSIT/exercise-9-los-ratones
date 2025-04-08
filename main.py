#TODO(JohnPaul Rodriguez): create a function that adds songs to the playlist
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

while True:
    user_choice = int(input("Please Enter your Choice: "))

    match user_choice:
        case 1:
            pass
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