import numpy
import string


NL_HIST = {'a':7, '2':1, 'c':1, 'd':6, 'e': 19, 'f':1, 'g': 3, 'h': 2, 'i': 6, 'j': 1, 'k': 2, 'l': 4, 'm': 2, 'n':
        10, 'o': 6, 'p': 1, 'q': 0, 'r': 6, 's': 4, 't': 7, 'u': 2, 'v': 3, 'w': 2, 'x': 0, 'y': 0, 'z': 1}

NL_HIST = {'a': 7.486, 'b': 1.584, 'c': 1.242, 'd': 5.933, 'e': 18.91, 'f': .0805, 'g': 3.403,
        'h': 2.380, 'i': 6.499, 'j': 1.46, 'k': 2.248, 'l': 3.568, 'm': 2.213, 'n': 10.032,
        'o': 6.063, 'p': 1.57, 'q': .009, 'r': 6.411, 's': 3.73, 't': 6.79, 'u':1.99,
        'v': 2.85, 'w': 1.52, 'x': .036, 'y': .035, 'z': .0139}

def histogram(text):
    """create a histogram of the given text"""
    hist = {}
    for i in text:
        hist[i] = hist.pop(i, 0) + 1
    return hist


def analyzelanguage(languagestring):
    """returns the histogram (in %) of characters used in the given language"""
    # todo: use n-grams for more then 1 letter? in extra function
    hist = histogram(languagestring)
    total = len(languagestring)
    for i, j in hist.iteritems():
        hist[i] = j*100/total
    return hist

def dictcorrelation(dict1, dict2):
    """Calculate the correlation between two dicts"""
    keys = set(dict1.keys() + dict2.keys())
    return numpy.corrcoef(
        [dict1.get(x, 0) for x in keys],
        [dict2.get(x, 0) for x in keys])[0, 1]

def scorelanguage(languagestring, language_hist=None):
    """
    give a score of how well the given input matches the histogram of characters used in that language (between 0 and 1)
    this works on indiviual letters, so you can give slices without worrying about ngrams
    """
    if not language_hist:
        language_hist = NL_HIST.copy()
    hist = histogram(languagestring)

    # calculate the correlation
    return dictcorrelation(language_hist, hist)

def rot(a, b):
    """
    rotate string a with letters of string b resp
    stops after shortest string is processed
    """
    c = ''
    for i in range(0,min(len(a),len(b))):
        c = c + chr(((ord(a[i]) - 2*ord('a') + ord(b[i])) % 26) + ord('a'))
    return c


def crack(inputstring, decrypt_cipher, language_hist=NL_HIST, confidence=.5, pw_length=1):
    """
    Crack the key and return it and the plaintext for cipher given a
    We start with one char pw's only
    """
    bestscore = 0
    bestkey = ''
    bestenglish = ''
    #for key in itertools.combinations_with_replacement(ascii_lowercase, pw_length):
    for letter in string.ascii_letters:
        key = letter * len(inputstring)
        try:
            # do the xorhex for a long string of char, decode it to hex to score our language
            decrypted = decrypt_cipher(inputstring, "".join(key))
        except TypeError:
            # result wasn't hex, so lets skip
            continue
        english = scorelanguage(decrypted, language_hist)
        if english > bestscore:
            bestscore = english
            bestkey = key
            bestenglish = decrypted
        if english > confidence:
            yield "".join(key), decrypted, english
    # if nothing was found, lets still return our best finding
    if bestscore <= confidence:
        yield "".join(bestkey), bestenglish,bestscore


# it's cbc so we can crack 1 char at a time
def cbccrack(blocklen, decrypt, inputstring, lang_hist, confidence=0.7):
    for i in range(blocklen):
        print('next block')
        inp = inputstring[i::blocklen]
        for guess in crack(inp, decrypt, lang_hist, confidence,len(inputstring)//blocklen):
            print(i, guess)

# no good on short texts
cbccrack(9, rot, """OTNMFRSVGNLTWIQQJLDJASUBWNVARPEKVAABQGTINKAAJOBXSGRQAMYTAAJPKAKMGRQBBIHXQGJMXXGRZAOIYIMQCWJAKFWEYVIINYAWNFCMOMUHPTLRXFPBLYUZQEZTFNPQGCKDCXKNKVGLQZNHSCNMD""", lang_hist=NL_HIST, confidence=0.4)

#TODO: dictinonary attack instead of cbc cryptanalyse


def dictcrack(inputstring, decrypt_cipher, wordlist, lang_hist=NL_HIST, confidence=.5):
    bestscore = 0
    bestkey = ''
    bestenglish = ''
    for key in wordlist:
        try:
            # do the xorhex for a long string of char, decode it to hex to score our language
            decrypted = decrypt_cipher(inputstring, key * (len(inputstring)//len(key)))
        except TypeError:
            # result wasn't hex, so lets skip
            continue
        english = scorelanguage(decrypted, lang_hist)
        if english > bestscore:
            bestscore = english
            bestkey = key
            bestenglish = decrypted
            print("".join(key), decrypted, english)
        if english > confidence:
            yield "".join(key), decrypted, english
    if bestscore <= confidence:
        yield "".join(bestkey), bestenglish,bestscore


def getscore(tup):
    return tup[2]

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def wordlistcrack(wordlistfile, decrypt, inputstring, lang_hist, confidence=0.7):
    output = []
    words = [word.strip() for word  in open(wordlistfile).readlines()]
    for guess in dictcrack(inputstring, rot, words, lang_hist, confidence):
            output.append(guess)
    print("\n".join(x[0] + " " + " ".join(chunks(x[1],9)) + " " + str(x[2]) for x in sorted(output,
        key=getscore)))

#wordlistcrack('woordenlijst_l9.txt', rot,
#        """OTNMFRSVGNLTWIQQJLDJASUBWNVARPEKVAABQGTINKAAJOBXSGRQAMYTAAJPKAKMGRQBBIHXQGJMXXGRZAOIYIMQCWJAKFWEYVIINYAWNFCMOMUHPTLRXFPBLYUZQEZTFNPQGCKDCXKNKVGLQZNHSCNMD""".lower(), lang_hist=NL_HIST, confidence=0.5)


