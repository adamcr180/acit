songs = []
def add_song(song_list):
    """Ask for song details, convert duration to seconds, and append a new dictionary."""
    title = input("Enter song title: ").strip()
    artist = input("Enter artist: ").strip()
    try:
        minutes = int(input("Enter duration (minutes): "))
        seconds = int(input("Enter duration (seconds): "))
    except ValueError:
        print("Invalid input for duration. Please enter numbers.")
        return
    total_duration = (minutes * 60) + seconds

    new_song = {
        "title": title,
        "artist": artist,
        "duration": total_duration,
        "plays": 0
    }
    song_list.append(new_song)
    print(f"\nSuccessfully added '{title}' by {artist}!")
def record_listen(song_list):
    """Search for a song by title (ignoring case/spacing) and increment its plays."""
    if not song_list:
        print("\nYour song library is empty! Add a song first.")
        return

    search_title = input("Enter song title to record a listen: ").strip().lower()
    found = False
    for song in song_list:
        if song["title"].strip().lower() == search_title:
            song["plays"] += 1
            found = True
            print(f"\nRecorded a listen for '{song['title']}'! Total plays: {song['plays']}")
            break
        if not found:
            print(f"\nError: Song not found in your library.")
    total_songs = len(song_list)
    total_plays = sum(song["plays"] for song in song_list)
    total_seconds = sum(song["duration"] * song["plays"] for song in song_list)
    total_minutes = total_seconds // 60
    most_played = song_list[0]
    for song in song_list:
        if song["plays"] > most_played["plays"]:
            most_played = song
    print("\n========== YOUR SPOTIFY WRAPPED ==========")
    print(f"\nTotal Songs: {total_songs}")
    print(f"Total Plays: {total_plays}")
    print(f"Total Listening Time: {total_minutes} minutes")
    print("\nYour Most Played Song:")
    print(f"{most_played['title']} - {most_played['artist']} ({most_played['plays']} plays)")
    print("\n==========================================")