out = []
f = open('../woordenlijst.txt')
woorden = f.readlines()
for woord in woorden:
  woord = woord.strip()
  for search in ['ben', 'gelijk', 'hal', 'koek', 'meed', 'pers', 'wend']:
    cont = True
    if len(woord) == len(search):
        for let in search:
            if let not in woord:
                cont = False
                continue
        if cont:
            out.append(woord)

print out

#:TODO filter out wrong words, pidgin hole rule doesn't apply due to double k and ee
#['adem', 'ben', 'boek', 'coke', 'dame', 'demi', 'demo', 'doek', 'doem', 'gelijk', 'hal', 'hemd', 'hoek', 'idem', 'joke', 'koek', 'koel', 'koen', 'koep', 'koer', 'koes', 'koet', 'made', 'mede', 'meed', 'meid', 'mode', 'moed', 'neb', 'oker', 'pers', 'roek', 'soek', 'zoek', 'demp', 'meld', 'pres', 'sper', 'wend']
->
#['ben', 'gelijk', 'hal', 'koek', 'mede', 'meed', 'neb', 'pers', 'pres', 'sper', 'wend']

