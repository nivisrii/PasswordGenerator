import random

def generate_password(lengths):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    generated_passwords = []

    for length in lengths:
        password = ""
        for _ in range(length):
            random_index = random.randrange(len(alphabet))
            password += alphabet[random_index]

        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)

        generated_passwords.append(password)

    return generated_passwords


def replace_with_number(password):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(password) // 2)
        password = password[:replace_index] + str(random.randrange(10)) + password[replace_index + 1:]
    return password


def replace_with_uppercase_letter(password):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(password) // 2, len(password))
        password = password[:replace_index] + password[replace_index].upper() + password[replace_index + 1:]
    return password


def main():
    num_passwords = int(input("How many passwords do you want to generate? "))

    print(f"Generating {num_passwords} passwords")

    password_lengths = []

    print("Minimum length of a password should be 3")

    for i in range(num_passwords):
        length = int(input(f"Enter the length of Password #{i + 1}: "))
        if length < 3:
            length = 3
        password_lengths.append(length)

    passwords = generate_password(password_lengths)

    for i, password in enumerate(passwords, start=1):
        print(f"Password #{i} = {password}")


main()
