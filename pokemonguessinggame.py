import requests
import random
from IPython.display import display, Image
class PokemonGuessingGame:
    def __init__(self, num_pokemon=151):
        self.num_pokemon = num_pokemon
        self.score = 0
    def get_random_pokemon(self):
        pokemon_id = random.randint(1, self.num_pokemon)
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
        response = requests.get(url)
        if response.ok:
            data = response.json()
            name = data["name"]
            image_url = data["sprites"]["other"]["official-artwork"]["front_default"]
            return name, image_url
        else:
            return None, None
    def play(self, rounds):
        self.score = 0
        for i in range(rounds):
            name, image_url = self.get_random_pokemon()
            if not name:
                print("OOPS! Couldn’t fetch Pokémon.")
                continue
            print(f"\nRound {i + 1}: Who's that Pokémon?")
            display(Image(url=image_url))
            guess = input("It's: ").strip()

            if guess.lower() == name.lower():
                print("✅ That's Correct!\n")
                self.score += 1
            else:
                print(f"❌ Incorrect! It's {name.title()}.\n")
        print(f"Game over! You got {self.score}/{rounds} correct.")
        if self.score == rounds:
            print("👑 You have become a Pokémon Master! 👑")
        elif self.score >= rounds * 0.7:
            print("🌟 You're a natural! 🌟")
        else:
            print("Keep practicing — you'll be a Pokémon Master soon!")


game = PokemonGuessingGame()
while True:
    choice = input("How many Pokémon do you want to guess? Enter '5' or '10': ").strip()
    if choice in ["5", "10"]:
        game.play(int(choice))
        break
    else:
        print("Please enter '5' or '10'.")
