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
prompt = imput('Would you like to encrypt your message or decrypt?')
if (prompt.upper() == 'ENCRYPT'):
    request = input('Please enter the message you would like to encrypt')
    print('Your message is: ' + mask(request))
else:
    request = input('Please enter the message you would like to decrypt')
    print('Your message is: ' + unmask(request))

#Main function to mask message
def mask(request):
    if (request and request != ''):
        message == ""
        for character in request:
            if (character and character != ''):
            
                
        return message
    else:
        return('ERROR')
        print('Message is invalid, please try again')

#Main function to unmask message
def unmask(request):
    if (request && request != ''):
        message == ""
        for character in request:
            if (character && character != ''):


        return message
    else:
        return('ERROR')
        print('Message is invalid, please try again')

