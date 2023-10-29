import re

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








if __name__ == "__main__":
    main()