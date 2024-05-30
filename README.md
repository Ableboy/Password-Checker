# Password Checker Project

## Description

A tool to check the strength and security of user passwords, providing feedback and checking against known breached passwords.

## Libraries Used

- requests (for checking against breached passwords using an API like "Have I Been Pwned")
- hashlib (changes values to glibberish value)

## Key Features

- Evaluate password strength based on length, use of uppercase/lowercase letters, numbers, and special characters.
- Check passwords against known breached password databases.
- Provide feedback to users on how to improve password strength.

## Use Case

Enhances security by ensuring users create strong and secure passwords.

## Installation
``` bash
# Clone the repository
git clone https://github.com/Ableboy/Password-Checker.git
```
``` bash
# Navigate into the project directory
cd password-checker
```
``` bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
``` bash
# Install dependencies
pip install -r requirements.txt
``` 

## Usage

``` bash
# Example command to run the project
python checkmypass.py
```

## Contributing

We welcome contributions! Please fork the repository, create a feature branch, and submit a pull request.

## License

MIT License