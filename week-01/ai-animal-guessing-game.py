from ai import call_gpt

def main():
    animal = input("Name an animal: ")
    description = input("Describe it in a few words: ")

    prompt = f"The user is thinking of an animal. Here is a description: {description}. Guess the animal. Respond in a single word, nothing else."
    guess = call_gpt(prompt)

    if guess == animal:
        print(f"Wahoo! GPT guessed {guess}!")
    else:
        print(f"Aww! GPT guessed {guess}, but you were thinking of {animal}.")

if __name__ == "__main__":
    main()
