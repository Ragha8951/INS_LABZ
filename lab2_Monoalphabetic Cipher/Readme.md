# Mono Alphabet Substitution Cipher

[**Live Demo**](https://colab.research.google.com/drive/1VQv8Dp0BcxIMqHCkeJvRnS0qsmSUItXg?usp=sharing)

This Python script implements an Alphabet Substitution Cipher, where each letter in the plaintext is substituted with a corresponding letter from a second predefined list. It can encode and decode messages based on this substitution rule.

## Features

- Encrypts and decrypts lowercase letters based on a custom substitution rule.
- Handles characters that are not in the substitution lists by keeping them unchanged.
- User-friendly input and output format for encoding and decoding.

## Prerequisites

- Python 3.x installed on your system.
- Basic knowledge of running Python scripts.

## How It Works

- **Encoding**: Each character in the plaintext (pt) is matched with its corresponding character in the second list (bt) using the index position.
- **Decoding**: Each character in the ciphertext is matched with its corresponding character in the first list (sl) to retrieve the original letter.

### Formula Used

For encoding:
Encoded Character = bt[sl.index(pt)]

---

For decoding:
Decoded Character = sl[bt.index(cipher_text)]

---

## How to Use

1. Run the Python script.
2. Enter the plaintext you want to encode.
3. The program will output the encoded message.
4. Enter the encoded (cipher) text to decode it back to the original plaintext.

## Example Usage

Enter plain text : hello world  
Encoded text is: Qhhpo pwtp  

Enter the cipher text: Qhhpo pwtp  
Decoded text is : hello world

## Notes

- The substitution is case-sensitive, so it only works for lowercase letters in the input.
- Non-alphabetical characters, such as spaces or punctuation, remain unchanged.

## Future Enhancements

- Add support for both uppercase and lowercase letters.
- Include error handling for unsupported characters or incorrect inputs.
- Enhance user interface for better interaction.

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to create a pull request or open an issue on GitHub.

## Author

 
GitHub: [@Ragha8951](https://github.com/Ragha8951)  
Email: [ragha8951@gmail.com](mailto:ragha8951@gmail.com)  

Thank you for visiting ❤️

