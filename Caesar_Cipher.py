pt = str(input("Enter a string: "))
k = int(input("Enter the value to be shifted: "))
ent = ""  # Encrypted text
dct = ""  # Decrypted text

# Encoding
for i in range(len(pt)):
    ch = pt[i]
    if ch.isalpha():  # Checks for alphabets
        if ch.isupper():
            ent += chr((ord(ch) - 65 + k) % 26 + 65)  # For uppercase letters
        else:
            ent += chr((ord(ch) - 97 + k) % 26 + 97)  # For lowercase letters
    elif ch.isdigit():  # Checks for digits
        ent += chr((ord(ch) - 48 + k) % 10 + 48)  # For digits
    else:
        ent += ch  # Keeps spaces and special characters unchanged

# Decoding
for i in range(len(ent)):
    ch = ent[i]
    if ch.isalpha():
        if ch.isupper():
            dct += chr((ord(ch) - 65 - k) % 26 + 65)  # For uppercase letters
        else:
            dct += chr((ord(ch) - 97 - k) % 26 + 97)  # For lowercase letters
    elif ch.isdigit():
        dct += chr((ord(ch) - 48 - k) % 10 + 48)  # For digits
    else:
        dct += ch  # Keeps spaces and special characters unchanged

# Output
print("\nYOUR ENTERED TEXT: " + pt)
print("The encoded message is: " + ent)
print("The decoded message is: " + dct)
