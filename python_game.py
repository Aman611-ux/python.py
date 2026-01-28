import random

def guess_the_number():
    # 1 se 20 ke beech ek random number generate karega
    secret_number = random.randint(1, 20)
    attempts = 0

    print("--- Number Guessing Game ---")
    print("Main 1 se 20 ke beech ek number soch raha hoon. Kya aap bata sakte hain wo kya hai?")

    while True:
        try:
            # User se input lena
            guess = int(input("Apna guess likhiye: "))
            attempts += 1

            if guess < secret_number:
                print("Thoda bada number try karein! (Too Low)")
            elif guess > secret_number:
                print("Thoda chota number try karein! (Too High)")
            else:
                print(f"Mubarak ho! Aapne {attempts} koshishon mein sahi pehchana.")
                break
        except ValueError:
            print("Pehle ek sahi number toh likhiye!")

# Game shuru karne ke liye function call karein
guess_the_number()