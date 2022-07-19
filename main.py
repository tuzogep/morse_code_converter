from playsound import playsound
import time

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def play_sound(morse_code):
    for symbol in morse_code:
        if symbol == ".":
            playsound("DIT.wav")
        elif symbol == "-":
            playsound("DAH.wav")
        else:
            time.sleep(0.5)


# Listing the characters we can translate:
key_list = [key for key in MORSE_CODE_DICT]
keys = ""
for char in key_list:
    keys += char + ", "


print("""
    \                                            \  |                         
   _ \ \ \  \ /  -_) (_-<   _ \   ` \    -_)    |\/ |   _ \   _| (_-<   -_)   
 _/  _\ \_/\_/ \___| ___/ \___/ _|_|_| \___|   _|  _| \___/ _|   ___/ \___|   
                                                                              
   __|            |           __|                           |                 
  (      _ \   _` |   -_)    (      _ \    \ \ \ /  -_)   _| _|   -_)   _|    
 \___| \___/ \__,_| \___|   \___| \___/ _| _| \_/ \___| _| \__| \___| _|      
                                                                              """)
print("Welcome to the Awesome Morse Code Converter!")
app_on = True
while app_on:
    text = input("Enter the text to encode: ")
    text = text.upper().replace(" ", "")
    code = ""
    # Check if it the translation will be possible:
    problems = ""
    for letter in text:
        if letter not in MORSE_CODE_DICT:
            problems += letter + ", "
    if problems:
        print(f"Problematic letters: {problems}")
        print(f"I can accept only these letters:\n{keys}")
    else:
        for letter in text:
            if letter in MORSE_CODE_DICT:
                code += MORSE_CODE_DICT[letter] + " "
        print(code)
        play_sound(code)
    again = input("Do you want to encode another text? (y/n): ")
    if again == "n":
        print("Goodbye!")
        app_on = False
