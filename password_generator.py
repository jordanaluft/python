# generates a password with a length chose from the user with letters (upper and lowercase) + digits + punctuation
import random, string

length = int(input("Enter the password lenght: "))
while (length < 6):
	length = int(input("Password is too small! Please, try again: "))

def generate_password(length):
	letters = string.ascii_letters
	digits = string.digits
	punctuation = string.punctuation

	word = letters + digits + punctuation
	randon_list = random.sample(word, length)
	password = ''.join(randon_list)
	return password

print(f"The password generated is: {generate_password(length)}")