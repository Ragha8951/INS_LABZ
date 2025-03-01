# Function to encrypt the plaintext using Vigenère Cipher
def vige_encrypt(pt, key):
    key = key.lower()  # Convert the key to lowercase to ensure consistency
    cp = ""  # Initialize an empty string to store the encrypted text
    key_index = 0  # Keeps track of which letter of the key to use

    # Iterate through each character of the plaintext
    for char in pt.lower():  # Convert plaintext to lowercase for uniformity
        if char.isalpha():  # Process only alphabetic characters
            shift = ord(key[key_index]) - ord('a')  # Compute the shift value from the key
            # Encrypt the character using the shift value
            cp += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            # Move to the next character in the key (cyclically)
            key_index = (key_index + 1) % len(key)
        else:
            cp += char  # Keep non-alphabetic characters unchanged
    return cp  # Return the encrypted text


# Function to decrypt the ciphertext using Vigenère Cipher
def vige_decrypt(ct, key):
    key = key.lower()  # Convert the key to lowercase for consistency
    pt = ""  # Initialize an empty string to store the decrypted text
    key_index = 0  # Keeps track of which letter of the key to use

    # Iterate through each character of the ciphertext
    for char in ct.lower():  # Convert ciphertext to lowercase for uniformity
        if char.isalpha():  # Process only alphabetic characters
            shift = ord(key[key_index]) - ord('a')  # Compute the shift value from the key
            # Decrypt the character using the shift value
            pt += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            # Move to the next character in the key (cyclically)
            key_index = (key_index + 1) % len(key)
        else:
            pt += char  # Keep non-alphabetic characters unchanged
    return pt  # Return the decrypted text


# Input from the user
pt = input("ENTER THE PLAIN TEXT\n")  # Take plaintext input from user
key = input("ENTER THE KEY FOR CIPHER\n")  # Take key input from user

# Encrypt the plaintext
encrypted_text = vige_encrypt(pt, key)
print("Encrypted:", encrypted_text)  # Print the encrypted text

# Decrypt the ciphertext
decrypted_text = vige_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)  # Print the decrypted text (should match original plaintext)
