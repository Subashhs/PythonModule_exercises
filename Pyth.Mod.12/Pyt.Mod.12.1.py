import requests

def get_random_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        joke_data = response.json()
        return joke_data.get("value")
    else:
        return None

def main():
    joke = get_random_chuck_norris_joke()

    if joke:
        print("Chuck Norris Joke:")
        print(joke)
    else:
        print("Failed to fetch Chuck Norris joke. Please try again.")

if __name__ == "__main__":
    main()
