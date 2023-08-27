# This file was generated using OpenAI's ChatGPT.

import argparse
import string
import random

def generate_password(length=8, use_uppercase=False, use_digits=False, use_symbols=False):
    """
    Generate a random password based on specified criteria.

    Args:
        length (int): Length of the password.
        use_uppercase (bool): Whether to include uppercase letters.
        use_digits (bool): Whether to include digits.
        use_symbols (bool): Whether to include symbols.

    Returns:
        str: The generated password.
    """

    # Define the character sets to be used.
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Generate the password until it includes the required characters.
    password = ''
    if use_uppercase:
        password += random.choice(string.ascii_uppercase)
    if use_digits:
        password += random.choice(string.digits)
    if use_symbols:
        password += random.choice(string.punctuation)

    remaining_length = max(length - len(password), 0)
    password += ''.join(random.choice(characters) for _ in range(remaining_length))

    # Shuffle the characters to generate the final password.
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def main():
    parser = argparse.ArgumentParser(description='Generate a password with specified options')
    parser.add_argument('-l', '--length', type=int, default=8, help='Length of the password (default: 8)')
    parser.add_argument('-u', '--uppercase', action='store_true', help='Include uppercase letters (default: False)')
    parser.add_argument('-d', '--digits', action='store_true', help='Include digits (default: False)')
    parser.add_argument('-s', '--symbols', action='store_true', help='Include symbols (default: False)')

    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        use_uppercase=args.uppercase,
        use_digits=args.digits,
        use_symbols=args.symbols
    )

    print("Generated password:", password)

if __name__ == '__main__':
    main()
