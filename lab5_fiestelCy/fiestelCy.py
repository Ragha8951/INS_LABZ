# Taking user input as a string
s = input("Enter a string : ")

# Convert the string to ASCII and then to 8-bit binary representation
# Each character is converted to its ASCII value and then to an 8-bit binary format
result = "".join(format(ord(i), '08b') for i in s) 
print("Binary Representation : ", result)

# Splitting the binary string into two halves: Left and Right
l = int(len(result) / 2)  # Finding the midpoint of the binary string
left = result[:l]  # Left half of the binary string
right = result[l:]  # Right half of the binary string

# Taking user input as the key
k = input("Enter a key : ")

# Convert the key to its binary equivalent (each character as an 8-bit binary)
key = "".join(format(ord(i), '08b') for i in k)

# Perform Feistel-like encryption: Right part + Key, then XOR with Left part
s = bin(int(right, 2) + int(key, 2))  # Convert right part and key to integer, add, and convert back to binary
answer = bin(int(s[2:], 2) ^ int(left, 2))  # XOR result with left part

# Swapping Left and Right halves for next round
newr = answer[2:]  # New Right part after XOR operation
newl = right  # Old Right part becomes new Left part
newr, newl = newl, newr  # Swap Left and Right

# Second round of Feistel-like encryption
s = bin(int(newr, 2) + int(key, 2))  # New Right + Key in binary
ans = bin(int(s[2:], 2) ^ int(newl, 2))  # XOR with new Left part

# Final swap of Left and Right parts after second round
nl = newr  # New Left
nr = ans[2:]  # New Right
nl, nr = nr, nl  # Final swap

# Concatenating the final Left and Right parts to get the cipher text in binary
cipher = nl + nr  

# Ensuring the cipher text length matches the original binary string
if len(cipher) != len(result):
    while len(cipher) != len(result):
        cipher = "0" + cipher  # Padding with 0s if necessary

print("Cipher (Binary):", cipher)

# Converting binary cipher text back to characters to get the encrypted string
plainText = ""
for i in range(0, len(cipher), 8):  # Process 8 bits at a time
    temp = cipher[i:i + 8]  # Extract 8-bit segment
    d = int(temp, 2)  # Convert binary to decimal (ASCII)
    plainText = plainText + chr(d)  # Convert ASCII to character

# Output the encrypted text
print("Cipher (Text) :", plainText)
