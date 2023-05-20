# File Encryptor App 💠!
Welcome to the File Encryptor App! 😊🔐

What can this application do? 📝🔒
This application allows you to encrypt and decrypt files using the cryptography module in Python. 🔑

Encryption: You can encrypt a file of your choice, which will be secured with a generated encryption key. This ensures that the file contents are protected and unreadable without the key. 🔒
Decryption: You can decrypt an encrypted file using the corresponding encryption key. Only with the correct key can you retrieve the original file contents. 🔓
How to use the app? 💻🔧
Choose an option from the menu:

1) Encrypt data: Encrypt a file by providing a password and the filename.
2) Decrypt data: Decrypt an encrypted file using the encryption key and password.
3) Exit: Quit the program.


Encryption Process:

- Set a password to encrypt the file. 🔑 
- Provide the filename to be encrypted. 
- The file will be encrypted using a randomly generated encryption key.
- The encryption key will be saved in a separate file (.key) alongside the encrypted file.
- The password used for encryption will be saved in a separate file (.pwd) for decryption purposes.

Decryption Process:

Enter the filename of the encrypted file to be decrypted.
Provide the password that was used for encryption.
The program will check if the provided password matches the saved password.
If the passwords match, the file will be decrypted and the original content will be restored.
The encryption key and password files will be deleted after successful decryption.
That's it! 🎉 You can now encrypt and decrypt files using this simple and secure File Encryptor App. Enjoy protecting your sensitive data! 🔐

Feel free to contribute, provide feedback, or report any issues on GitHub. Happy coding! 😄🐙
