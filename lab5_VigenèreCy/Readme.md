# Vigenère Cipher Encryption & Decryption

[**Live Demo**](https://colab.research.google.com/drive/1eeHybWrEzEAnIiZinPKc-BltalDHGggR?usp=sharing)

This Python script implements the Vigenère Cipher, a method of encrypting alphabetic text using a series of Caesar ciphers based on the letters of a keyword.

## Features

- Encrypts and decrypts messages using the Vigenère Cipher.
- Supports lowercase alphabetical input.
- Retains non-alphabetic characters without modification.
- Uses a repeating key to shift each letter of the plaintext.

## Prerequisites

- Python 3.x installed on your system.
- Basic knowledge of running Python scripts.

## How It Works

- The plaintext is converted into a series of shifts based on the keyword.
- Each letter is shifted forward (for encryption) or backward (for decryption) by the corresponding letter of the keyword.
- The process repeats cyclically for the entire length of the plaintext.
- **Encryption Process:**
  - Convert each plaintext letter into its corresponding shift value based on the key.
  - Shift the letter forward in the alphabet using the key's character.
  - If the shift exceeds 'z', it wraps around using modulo 26.
- **Decryption Process:**
  - Reverse the shifting process by subtracting the key's shift value.
  - Convert the letter back to its original form.
  - The key cycles through the entire message.

## How to Use

1. Run the Python script.
2. Enter the plaintext you want to encrypt.
3. Enter the keyword for encryption.
4. The program will return:
   - Encrypted text (ciphertext).
   - Decrypted text (original plaintext).

## Example Usage

```
ENTER THE PLAIN TEXT
hello world
ENTER THE KEY FOR CIPHER
test
Encrypted: aessp bsbtd
Decrypted: hello world
```

## Notes

- Only lowercase alphabetic characters are shifted; spaces and symbols remain unchanged.
- The keyword is repeated cyclically to match the plaintext length.

## Future Enhancements

- Add support for uppercase and mixed-case text.
- Improve error handling for invalid inputs.
- Create a GUI for better user interaction.

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to create a pull request or open an issue on GitHub.

## Author

GitHub: [@Ragha8951](https://github.com/Ragha8951)\
Email: [ragha8951@gmail.com](mailto\:ragha8951@gmail.com)

Thank you for visiting ❤️

