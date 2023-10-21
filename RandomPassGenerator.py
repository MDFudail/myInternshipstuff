import random
import string


# Define a function to generate a random password
def generate_random_password(length):
    """Generates a random password of the specified length.

    Args:
      length: The length of the password.

    Returns:
      A random password.
    """

    # Create a list of all possible characters for the password.
    characters = (
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
        + string.punctuation
    )

    # Generate a random password.
    password = ""
    for i in range(length):
        password += random.choice(characters)

    # Return the random password.
    return password


# Define a function to validate the user inputs
def validate_user_inputs(password_length, number_of_passwords):
    """Validates the user inputs for password length and number of passwords.

    Args:
      password_length: The length of the password.
      number_of_passwords: The number of passwords required.

    Returns:
      True if the user inputs are valid, False otherwise.
    """

    # Check if the password length is between 8 and 64 characters.
    if not 8 <= password_length <= 64:
        return False

    # Check if the number of passwords is less than or equal to 10.
    if not number_of_passwords <= 10:
        return False

    # Return True if the user inputs are valid.
    return True


# Prompt the user to input the password length
password_length = int(
    input("Enter the password length (between 8 and 64 characters): ")
)

# Prompt the user to input the number of passwords required
number_of_passwords = int(
    input("Enter the number of passwords required (less than or equal to 10): ")
)


# Generate a list of random passwords with rumming serial number in prefix
passwords = []
for i in range(number_of_passwords):
    password = str(i + 1) + "\t" + generate_random_password(password_length)

    # Check if the password contains at least one upper case letter, at least one lower case letter, at least one number, and at least one special character.
    if not (
        any(char.isupper() for char in password)
        and any(char.islower() for char in password)
        and any(char.isdigit() for char in password)
        and any(char in string.punctuation for char in password)
    ):
        i -= 1
    passwords.append(password)

    # Display the generated passwords
    print(password)
