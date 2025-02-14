# Caesar Cipher Encryption & Decryption

This Python script implements the Caesar Cipher, a simple encryption technique where each letter in the text is shifted by a fixed number of positions.

## Features
- Encrypts and decrypts uppercase and lowercase letters.
- Handles digits (0-9) with modular arithmetic.
- Preserves spaces and special characters without modification.
- User-friendly input and output format.

## Prerequisites
- Python 3.x installed on your system.
- Basic knowledge of running Python scripts.

## How It Works
- Encoding: Each character is shifted forward by a given number (k).
- Decoding: Each character is shifted backward by the same number (k).

### Formula Used
For letters:
```
Encrypted = (ASCII value - base + k) % 26 + base
Decrypted = (ASCII value - base - k) % 26 + base
```
For digits:
```
Encrypted = (ASCII value - 48 + k) % 10 + 48
Decrypted = (ASCII value - 48 - k) % 10 + 48
```

## How to Use
1. Run the Python script.
2. Enter the text you want to encrypt.
3. Provide a shift value (k).
4. The program will return:
   - Encoded message (encrypted text).
   - Decoded message (original text).

## Example Usage
```
Enter a string: Hello 123
Enter the value to be shifted: 3

YOUR ENTERED TEXT: Hello 123
The encoded message is: Khoor 456
The decoded message is: Hello 123
```

## Notes
- Works for both uppercase and lowercase letters.
- Numbers cycle through 0-9 instead of stopping at 9.
- Symbols, spaces, and special characters remain unchanged.

## Future Enhancements
- Add support for negative shift values.
- Extend the cipher to handle Unicode characters.
- Implement a GUI version for better usability.

## Contribution
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to create a pull request or open an issue on GitHub.

## Author
Developed by [Raghavendra]  
GitHub: [Your GitHub Profile](https://github.com/Ragha8951)

If you found this helpful, give it a star on GitHub.

