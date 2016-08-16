# Imports
import random
import sys

def get_length():
	if len(sys.argv) > 1:
		return int(sys.argv[1])
	else: 
		return 1

def mimsmind0_game():
	print("Let's play mimsmind0 game.")
	length = get_length()
	correct_num = random.randint(0,10 ** length - 1)
	#print("Correct Answer is: " + str(correct_num))

	count = 1
	while(True):
		try: 
			if count == 1:
				usr_input = int(input("Guess a {} digit number: ".format(length)))
			else: 
				usr_input = int(input(msg))
		except: 
			print("Please enter a valid number")
			continue
		if usr_input == correct_num:
			print ("Congratulations. You guessed the correct number in {} tries.".format(count))
			break
		elif usr_input < correct_num:
			msg = "Try again. Guess a higher number: "
			count += 1
		else: 
			msg = "Try again. Guess a lower number: "
			count += 1




def main():
	mimsmind0_game()


if __name__ == '__main__':
    main()
