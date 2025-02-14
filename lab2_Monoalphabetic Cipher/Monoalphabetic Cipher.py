# set of variable 1 list
sl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# set of variable 2 list
bt = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 
      'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

def ent(pt):
    ent = ""  # Initialize the encrypted code as an empty string
    for i in pt:
        if i in sl:                             # Matching pt with var 1 list
            ent += bt[sl.index(i)]              # Encoding to bt using index no.
        else:
            ent += i  # Add the character as is if not in the list
    return ent

def dct(cipher_text):
    dct = ""  # Initialize the decrypted code as an empty string
    for i in cipher_text:
        if i in bt:
            dct += sl[bt.index(i)]             # Decoding encrypted text to plain text
        else:
            dct += i  # Add the character as is if not in the list
    return dct

# Input and Output
pt = input("Enter plain text : ")
print("Encoded text is: ", ent(pt))

cipher_text = input("Enter the cipher text: ")
print("Decoded text is :", dct(cipher_text))

