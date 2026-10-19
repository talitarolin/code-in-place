from ai import call_gpt

def main():
    print("Hello! I am an AI joke bot")
    user_choice = input("Do you want to hear a joke? Type yes or no: ")

    while user_choice == "yes":
        joke = call_gpt("Tell me a joke")
        print(joke)

        user_choice = input("Do you want to hear a joke? Type yes or no: ")

if __name__ == "__main__":
    main()