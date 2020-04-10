from gtts import gTTS 
import os 
bidibang = { 'A':'bidibang', 'B':'bangbidibidibidi', 
                    'C':'bangbidibangbidi', 'D':'bangbidibidi', 'E':'bidi', 
                    'F':'bidibidibangbidi', 'G':'bangbangbidi', 'H':'bidibidibidibidi', 
                    'I':'bidibidi', 'J':'bidibangbangbang', 'K':'bangbidibang', 
                    'L':'bidibangbidibidi', 'M':'bangbang', 'N':'bangbidi', 
                    'O':'bangbangbang', 'P':'bidibangbangbidi', 'Q':'bangbangbidibang', 
                    'R':'bidibangbidi', 'S':'bidibidibidi', 'T':'bang', 
                    'U':'bidibidibang', 'V':'bidibidibidibang', 'W':'bidibangbang', 
                    'X':'bangbidibidibang', 'Y':'bangbidibangbang', 'Z':'bangbangbidibidi', 
                    '1':'bidibangbangbangbang', '2':'bidibidibangbangbang', '3':'bidibidibidibangbang', 
                    '4':'bidibidibidibidibang', '5':'bidibidibidibidibidi', '6':'bangbidibidibidibidi', 
                    '7':'bangbangbidibidibidi', '8':'bangbangbangbidibidi', '9':'bangbangbangbangbidi', 
                    '0':'bangbangbangbangbang', ', ':'bangbangbidibidibangbang', 'bidi':'bidibangbidibangbidibang', 
                    '?':'bidibidibangbangbidibidi', '/':'bangbidibidibangbidi', 'bang':'bangbidibidibidibidibang', 
                    '(':'bangbidibangbangbidi', ')':'bangbidibangbangbidibang'} 

def encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ': 
            cipher += bidibang[letter] + ' '
        else: 
            cipher += ' '
    return cipher 

def main(): 
    message = "Bastian"
    result = encrypt(message.upper()) 
    myobj = gTTS(text=result, lang="en", slow=False) 
    myobj.save(message + ".mp3") 


if __name__ == '__main__': 
    main() 