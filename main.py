#Define Alphabet
Alphabet = {'A': '.-',
			'B': '-...',
			'C': '-.-.',
			'D': '-..',
			'E': '.',
			'F': '..-.',
			'G': '--.',
			'H': '....',
			'I': '..',
			'J': '.---',
			'K': '-.-',
			'L': '.-..',
			'M': '--',
			'N': '-.',
			'O': '---',
			'P': '.--.',
			'Q': '--.-',
			'R': '.-.',
			'S': '...',
			'T': '-',
			'U': '..-',
			'V': '...-',
			'W': '.--',
			'X': '-..-',
			'Y': '-.--',
			'Z': '--..',
			'1': '.----',
			'2': '..---',
			'3': '...--',
			'4': '....-',
			'5': '.....',
			'6': '-....',
			'7': '--...',
			'8': '---..',           
			'9': '----.',
            '0': '-----'} 

#Define Morse Var
Morse = {'.': 'Short',
         '-': 'Long'}

#Function to send message, initializes the main function


#Main function to mask message
def mask(request):
    if (request and request != ''):
        message = ''
        upperRequest = request.upper()
        for character in upperRequest:
            if (character and character != ' '):
                message += Alphabet[character] + ' '
            else:
                message += ' '
        return message
    else:
        return('ERROR')

#Main function to unmask message
def unmask(request):
    if (request and request != ''):
        upperRequest = request.upper()
        request += ' '
        message = ''
        secondary = ''
        for character in upperRequest:
            if (character and character != ' '):
                cindex = 0
                secondary += character
            else:
                cindex += 1
                if cindex == 2:
                    message += ' '
                else:
                    message += list(Alphabet.keys())[list(Alphabet.values()).index(secondary)]
        return message
    else:
        return('ERROR')


prompt = input('Would you like to encrypt your message or decrypt? ')
if (prompt.upper() == 'ENCRYPT'):
    request = input('Please enter the message you would like to encrypt? ')
    print('Your message is: ' + mask(request))
elif (prompt.upper() == 'DECRYPT'):
    request = input('Please enter the message you would like to decrypt? ')
    print('Your message is: ' + unmask(request))
else:
    print('Command invalid, please try again')

