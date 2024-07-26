#IITI SOC 2024
<h1>Cybersecurity Suite for Enhanced Digital Security </h1>
Overview
This cybersecurity suite comprises three essential tools designed to enhance digital security: Password Checker, Malicious Mail Identifier, and Keylogger. Each tool is crafted to address specific security vulnerabilities and ensure a safer digital environment.

Tools
Password Checker
The Password Checker evaluates the strength of passwords entered by users based on various factors such as length, complexity, and the inclusion of special characters. It provides feedback to help users create strong and secure passwords.

Malicious Mail Identifier
The Malicious Mail Identifier scans emails to detect potentially harmful content. It analyzes email headers, content, and attachments to identify phishing attempts, malware, and suspicious links, thereby safeguarding users from malicious emails.

Keylogger
The Keylogger captures keyboard inputs to monitor user activity. It demonstrates how keylogging can be used to retrieve sensitive data by cloning a login page of a well-known website and capturing user inputs.

Installation
To install the necessary dependencies, run the following command:

bash
Copy code
pip install pynput flask
Running the Project
To run the project, execute the following command:

bash
Copy code
python app.py
Team Members
Shiv Patel
Yogesh Patidar
Vishal
Roshan Saini
Mentors
Siddhesh Waje
Satvik Desai
Project Structure
arduino
Copy code
Cybersecurity-Suite/
├── password_checker/
│   ├── checker.py
│   ├── templates/
│   └── static/
├── malicious_mail_identifier/
│   ├── scanner.py
│   ├── templates/
│   └── static/
├── keylogger/
│   ├── keylogger.py
│   ├── templates/
│   └── static/
├── app.py
├── requirements.txt
└── README.md
How to Use
Password Checker: Navigate to the password_checker directory and run the checker.py script. Enter a password to check its strength.

Malicious Mail Identifier: Navigate to the malicious_mail_identifier directory and run the scanner.py script. Enter the details of the email to scan for malicious content.

Keylogger: Navigate to the keylogger directory and run the keylogger.py script. The keylogger will start capturing keyboard inputs.

Disclaimer
The tools provided in this suite are for educational purposes only. The use of the Keylogger tool to capture sensitive data without permission is illegal and unethical. Users are responsible for ensuring that their use of these tools complies with applicable laws and regulations.

Contact
For any questions or inquiries, please contact the project team members.
