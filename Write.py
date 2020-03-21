from time import sleep
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

# Converts the array into a string so that it can be passed into the card
def arrayToString(arr):
    payload = '\n'.join(arr)
    return payload

# Grabbing inputs from user
def convertToString():
    """
    
    inputs = []
    
    movieNameInput = raw_input('Enter the name of the movie via the directory: ')
    descriptionInput = raw_input('Enter a description for the movie: ')
    releaseDateInput = raw_input('Enter the release year: ')
    
    inputs.append(movieNameInput)
    inputs.append(descriptionInput)
    inputs.append(releaseDateInput)
    return inputs

    """
    inputVar = raw_input('Enter the Directory: ')
    return inputVar
def main():
    moreCards = True
    while moreCards:
        try:
            text = convertToString()
            # text = arrayToString(inputs)
            
            print("Now place your tag to write...")
            print(text)
            reader.write(text)
            print("Data Written Successfully")
            print("==============================\n" * 3)
            creatingMoreCards = raw_input("Would you like to to add more cards? (Y/N) ")
            if creatingMoreCards.upper() == "N":
                moreCards = False
        except KeyboardInterrupt:
            GPIO.cleanup()
            raise

main()
