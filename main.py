import re
#Pseudo code

def main():
    # Prompts for a url to a playlist
    url = input("link to a playlist: ")
    if playlist_validator(url):
        print("valid")
    else:
        print("not valid")



def playlist_validator(url):
    pattern = r"^http(s)?://www.youtube.com/(watch\?v|playlist\?list)=[\w\-\_]+"
    if matches := re.match(pattern, url):
        return True
    else:
        return False


# If the link is a valid playlist(find a way to determine this):
# Open youtube (login if necessary)
# Search the playlist
# Find the link of all the songs inside the playlist
# Find a way to download each video as an audio file
# Put them in a folder 
# End


if __name__ == "__main__":
    main()