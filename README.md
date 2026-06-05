SYNTECXHUB PROJECT 2

Project Report: Secure Local Password Manager

As part of my cybersecurity internship and practical learning experience, I developed a Secure Local Password Manager using Python on Kali Linux. The purpose of this project was to create a secure application capable of storing and managing user credentials while protecting sensitive information through encryption.

The project was designed to demonstrate key cybersecurity concepts such as secure data storage, encryption, authentication, and password management.

Project Objectives

The main objectives of the project were:

To develop a local password management system.
 To securely store user credentials on disk.
 To implement a master password for authentication.
 To encrypt stored data using symmetric encryption.
To provide functionality for adding, retrieving, searching, and deleting password entries.
To store data in an encrypted local file format.

<img width="757" height="403" alt="image" src="https://github.com/user-attachments/assets/53045fd8-955e-403a-a14d-32f6f5fcc61e" />

<img width="753" height="455" alt="image" src="https://github.com/user-attachments/assets/844fed88-3ad1-4773-9598-5a184f4590ba" />

Tools and Technologies Used

The following tools and technologies were used during the development of the project:

 Kali Linux
 Python 3
Cryptography Library (Fernet)
JSON File Storage
 Terminal/Command Line Interface (CLI)

System Features

The password manager includes the following features:

1. Master Password Authentication

Users are required to enter a master password before accessing the password vault. This serves as the primary security mechanism for protecting stored credentials.

2. Add Password Entries

Users can securely add website credentials, including usernames and passwords.

3. Retrieve Password Entries

Stored credentials can be viewed when required by searching for the corresponding website.

<img width="753" height="492" alt="image" src="https://github.com/user-attachments/assets/7d607e77-9090-4b83-91df-1eac76f03e35" />

<img width="753" height="277" alt="image" src="https://github.com/user-attachments/assets/d65a2108-982f-4de8-a23d-36aa3947a996" />

4. Search Functionality

Users can search for existing entries within the password vault.

5. Delete Password Entries

Unwanted or outdated credentials can be removed from the vault.

6. Encrypted Storage

<img width="752" height="590" alt="image" src="https://github.com/user-attachments/assets/ab858a7a-ba02-4712-a19b-42712c6d31aa" />

All credential data is encrypted before being saved to disk, ensuring that sensitive information remains protected from unauthorized access.

Implementation Process
The project was implemented in stages:

1. Created a basic password manager using Python dictionaries.
2. Added JSON file storage to save data permanently.
3. Implemented add, retrieve, search, and delete functionalities.
4. Installed and configured the Cryptography library.
5. Integrated master password authentication.
6. Applied symmetric encryption using Fernet to secure stored credentials.
7. Tested the application to ensure data could be securely saved and retrieved.
<img width="752" height="662" alt="image" src="https://github.com/user-attachments/assets/fce9830a-2ea0-442f-89e4-14ea933c467e" />
<img width="756" height="448" alt="image" src="https://github.com/user-attachments/assets/62c3084c-bf60-482d-8e6b-38ae8edc28d0" />

<img width="755" height="382" alt="image" src="https://github.com/user-attachments/assets/a0169432-a411-46d4-baac-528f55b223f5" />
Challenges Encountered

During development, several challenges were encountered, including:

 Python indentation errors caused by inconsistent spacing.
  Package installation restrictions within Kali Linux’s managed Python environment.
  Managing encrypted file storage and retrieval processes.

These challenges were resolved through debugging, code restructuring, and the use of a Python virtual environment for dependency management.

Skills and Knowledge Gained

Through this project, I gained practical experience in:

Python programming
File handling and JSON data management
Encryption and decryption techniques
Symmetric cryptography
Secure password management
Linux command-line operations
Cybersecurity best practices for protecting sensitive information
<img width="752" height="486" alt="image" src="https://github.com/user-attachments/assets/61583e56-8ef5-458c-b423-b8faf1cfa9c5" />

Project Outcome

The project was successfully completed and met all specified requirements. The password manager is capable of securely storing credentials, encrypting sensitive information, authenticating users through a master password, and providing essential password management functions.

Conclusion

This project provided valuable hands-on experience in cybersecurity and secure software development. By implementing encryption, authentication, and secure storage techniques, I developed a practical understanding of how password management systems operate and how sensitive information can be protected from unauthorized access. The project has strengthened my programming, problem-solving, and cybersecurity skills and serves as an important milestone in my learning journey








