# Fiestel_Cypher Encryption & Decryption

[**Live Demo**](https://colab.research.google.com/drive/1ZY9uMrAma54j3qTggcRKD0iICZjRhZmU?usp=sharing)

This Python script converts a string into its binary equivalent and performs encryption using bitwise operations and a key.

## Features

- Converts a string into an 8-bit binary representation.
- Splits the binary string into two halves for processing.
- Uses a key to perform binary addition and XOR operations.
- Swaps the halves and applies the transformation again for encryption.
- Converts the final binary result back into a readable plaintext format.

## Prerequisites

- Python 3.x installed on your system.
- Basic knowledge of running Python scripts.

## How It Works

1. **Convert to Binary**: The input string is converted into an 8-bit binary representation.
2. **Split into Halves**: The binary string is divided into two equal halves: `left` and `right`.
3. **Convert Key to Binary**: The input key is also converted into an 8-bit binary format.
4. **First Round of Encryption**:
   - Perform binary addition of `right` half and the key.
   - XOR the result with `left` half to generate a new `right`.
   - Swap `left` and `right` halves.
5. **Second Round of Encryption**:
   - Repeat the previous steps with the swapped halves.
   - The final `left` and `right` halves are concatenated to form the encrypted binary string.
6. **Convert Back to Text**: The binary result is converted back into a readable text format.

## How to Use

1. Run the Python script.
2. Enter the string you want to encrypt.
3. Provide a key for encryption.
4. The program will return:
   - Encrypted binary text.
   - Decrypted plaintext.

## Example Usage

```
Enter a string: Hello
Result: 0100100001100101011011000110110001101111
Enter a key: key
Cipher: 01110000011101110110101101111010
Plaintext: Hello
```

## Notes

- The key should be of appropriate length to ensure proper encryption.
- Works with standard ASCII characters.
- Binary transformations ensure bitwise security.

## Future Enhancements

- Implement support for Unicode characters.
- Improve the key expansion method.
- Create a GUI for a more user-friendly experience.

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to create a pull request or open an issue on GitHub.

## Author

GitHub: [@Ragha8951](https://github.com/Ragha8951)  
Email: [ragha8951@gmail.com](mailto:ragha8951@gmail.com)

Thank you for visiting ❤️

