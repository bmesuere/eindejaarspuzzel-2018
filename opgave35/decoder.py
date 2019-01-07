import itertools
import time

messages = [
        #(31704, "e d i d -es f,knanu 0aioeeeepslankoan2dheatuenl re j   f vkkAaekria eedvirwneresl !dr t  emnipcaembr do e adsa0rjonstlp!ll eft 7eern m ekotn1aTveemeie"),
        #(28790, "rkrilaen sta m!S!koall  euogvapD i m aene kneu efte!gdepfsakeipcaaWar rde n"),
        #(40952, "ok oee ! etk oeTin iKee!bo !gdp zpkii"),
        (312620, "t. okw nrue2ej g zealgl hemtjae.e n:ae e 9zmenn , enmattnu!av bli ntn5.imni g j aa r lkouukioom9Z reteoalolleoaiRo.hk sgntwt1 ag ie- prieeneseukrai eeIbkr 4 teoedrmumaarfknl"),
        #(549218, "rseera otcr:e liPintssb nae siveoeorIapkwf wkgoeduuuotueiho)ddrn ca m n."),
        #(720362, "kotira c<kf!ei Dpi3"),
        #(360184, "zie iruhegnodmHjdlel !Ghllew e km)daap nilka:eel!loj gien aokeleus "),
        #(525633536864, "o gnt  ikumtkowaegtnalik)Gtin hi,erao re,s norva !dlbo; a o "),
        #(31609639681, "eu s etijsa deHsk u,ojnh ku.evi Dnli aedrh mt: e e"),
        #(23405634121, "i,l ron ingeo, nAkc m nsaiemeiiehmienoasakeoaed l,  k r dmav!"),
        #(1211, "Uae deleae.keeindgeun  tel. oie t  rh v jtneh sair ankksebesM .iomu  riteleogl.wd rssd.au. l sew rs dgete."),
        #(152990, "avreJtee.,iwda rn sa d rh"),
        #(132103, " aev t zueSem tmue ea,vgi,se lika kuiiekwg rkeelreN!enosioleG r foask nijb pn m:gainnad niku")
        ]

def transpose(matrix):
    return list(map(list, zip(*matrix)))

def decode(getal, tekst):
    columns = len(str(getal))
    rows = len(tekst) // columns
    numColumnsWithExtra = len(tekst) % columns

    vals = sorted(map(lambda x: (x[0], int(x[1])), enumerate(str(getal))), key=lambda x: x[1])
    read = 0
    res = [[] for i in range(columns)]
    for i, (j, k) in enumerate(vals):
        if j < numColumnsWithExtra:
            res[j].extend(tekst[read:read+rows+1])
            read += rows + 1
        else:
            res[j].extend(tekst[read:read+rows])
            res[j] += ' '
            read += rows
    res = transpose(res)
    return "".join(map(lambda l: "".join(l), res))

for num, tekst in messages:
    spaces = [i for i, x in enumerate(tekst) if x == ' ']
    for i in range(10, 20):
        for positions in itertools.combinations_with_replacement(spaces, i):
            positions = positions[::-1]
            ntekst = tekst[:]
            for pos in positions:
                ntekst = ntekst[:pos] + ' ' + ntekst[pos:]
            print(decode(num, ntekst))
            print(positions[::-1])
