#lister til alfabet og morsekode for at definere key og value
morse=['//','.-','-..','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','-.','--','---','.--.','--.-','.-.','...','-','.--','...-','.--','-..-','-.--','--..','.-.-','---.','.--.-','.----','..---','...--','....-','.....','-....','--...','---..','----.','-----','.-.-.-','--..--','---...','..--..','.----.','-....-','-..-.','-.--.','-.--.-','.-..-.','.--.-.']

alfabet=[' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Æ','Ø','Å','1','2','3','4','5','6','7','8','9','0','.',',',':','?',"'",'-','/','(',')','"','@']
print(len(morse))
print(len(alfabet))

# Dictionary til oversættelse fra bogstaver til morsekode
# Dictionary til oversættelse fra morsekode til bogstaver. Tomt oversættes til mellemrum.
morseCode = {}
morseCodeReverse = {}
for i in range(len(alfabet)-1):
    morseCode[alfabet[i]]=morse[i]
    morseCodeReverse[morse[i]]=alfabet[i]


# Denne funktion oversætter et enkelt bogstav (letter) med opslag i dictionay (code) hvis muligt
def translate(letter, code):
    if letter in code:
        return code[letter]


# Denne funktion oversætter en vilkårlig tekststreng til morsekode
# '/' markerer nyt bogstav
# '//' markerer nyt ord
def encodeMessage(message, code):
    pass

# Denne funktion oversætter en korrekt formatteret morsebesked til bogstaver
# '/' markerer nyt bogstav
# '//' markerer nyt ord
def decodeMessage(message, code):
    pass