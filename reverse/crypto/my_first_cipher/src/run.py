from random import randint
import argparse


def encrypt(clear_text):
    """
    Encrypt function used to obtain cipher text using custom prfne algorithm.
    """
    cipher_text = ""
    padding = randint(0, 12)
    for i in range(len(clear_text)):
        cipher_text += chr(ord(clear_text[i]) + padding)
    return cipher_text


def decrypt(cipher_text):
    """
    Decrypt function, not implemented yet.
    """
    clear_text = cipher_text
    return clear_text


def parseArgs():
    description = "Encryption tool using custom prfne algorithm."
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("-c", "--clear_file", required=True, help="Clear text file to encrypt.")
    parser.add_argument("-o", "--output", help="Output file for the encryted text.")

    return parser.parse_args()


if __name__ == "__main__":
    # Init
    args = parseArgs()
    print(f"\n\033[32;1m[+]\033[0m \033[1mClear file: {args.clear_file}\033[0m")
    if args.output:
        print(f"\033[32;1m[+]\033[0m \033[1mOutput file: {args.output}\033[0m")

    # Getting clear text
    try:
        with open(file=args.clear_file, mode="r") as file:
            clear_text = file.read()
    except:
        print("\033[31;1m=== OPENING ERROR ===\033[0m\n")

    # Encrypt
    cipher_text = encrypt(clear_text).encode()
    print(f"\033[32;1m[+]\033[0m \033[1mCipher text: {cipher_text}\033[0m")

    # Save output
    print("\033[32;1m[+]\033[0m \033[1mSaving...\033[0m")
    if args.output:
        try:
            with open(file=args.output, mode="wb") as file:
                file.write(cipher_text)
        except:
            print("\033[31;1m=== SAVING ERROR ===\033[0m\n")
            exit(0)
    else:
        with open(file="cipher.txt", mode="wb") as file:
            file.write(cipher_text)
    print("\033[32;1m[+]\033[0m \033[1mDone.\n\033[0m")
