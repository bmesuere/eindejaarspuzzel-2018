
Een aantal getallen heeft een chatgroep opgezet om met elkaar in contact te blijven. Alleen getallen met een speciale relatie tot elkaar zijn toegelaten. Een getal moet tevens kunnen aantonen dat de relatie tot de anderen bestaat. Sommige getallen hebben de relatie niet, of kunnen dit nog niet aantonen. Om het medium verder te beveiligen heeft de eigenaar een vercijfering bedacht op elk berichtje wat er verstuurd wordt. De getallen zelf voor de aanhal- ingstekens zijn niet mee vercijferd. Iedereen in de groep ziet dezelfde berichten, dit is wat er het laatst werd gepost.
```
31704: "e d i d -es f,knanu 0aioeeeepslankoan2dheatuenl re j f vkkAaekria eedvirwneresl !dr t emnipcaembr do e adsa0rjonstlp!ll eft 7eern m ekotn1aTveemeie"
28790: "rkrilaen sta m!S!koall euogvapD i m aene kneu efte!gdepfsakeipcaaWar rde n" 40952: "ok oee ! etk oeTin iKee!bo !gdp zpkii"
312620: "t. okw nrue2ej g zealgl hemtjae.e n:ae e 9zmenn , enmattnu!av bli ntn5.imni g j aa r lkouukioom9Z reteoaloll eoaiRo.hk sgntwt1 ag ie- prieeneseukrai eeIbkr 4 teoedrmumaarfknl"
549218: "rseera otcr:e liPintssb nae siveoeorIapkwf wkgoeduuuotueiho)ddrn ca m n."
720362: "kotira c<kf!ei Dpi3"
360184: "zie iruhegnodmHjdlel !Ghllew e km)daap nilka:eel!loj gien aokeleus " 
525633536864: "o gnt ikumtkowaegtnalik)Gtin hi,erao re,s norva !dlbo; a o "
x: "Uae deleae.keeindgeun tel. oie t rh v jtneh sair ankksebesM .iomu riteleogl.wd rssd.au. l sew rs dgete." 
31609639681: "eu s etijsa deHsk u,ojnh ku.evi Dnli aedrh mt: e e"
23405634121: "i,l ron ingeo, nAkc m nsaiemeiiehmienoasakeoaed l, k r dmav!"
152990: "avreJtee.,iwda rn sa d rh"
y: " aev t zueSem tmue ea,vgi,se lika kuiiekwg rkeelreN!enosioleG r foask nijb pn m:gainnad niku"
```

De tekst is gecodeerd met een standaard transpositie met de username als key.
Bijkomende moeilijkheid is dat opeenvolgende spaties gesquasht werden. Hier en daar moeten dus extra spaties worden toegevoegd om alles te kunnen decoderen.

Hieronder de volledig gedecodeerde tekst:
```
31704:          Allemaal nen dikke proficiat aan de 27 mede-beheerders van dit forum, we kennen elkaar ondertussen al 100 jaar! Tijd voor een feest met veel kippekes!
28790:          Super! Dikke proficiat allemaal! We gaan der een supertof dagske van maken!
40952:          Top! ik ben zot op kiek! Keigoe idee!
312620:         Raar toeval... ik heb ook leuk nieuws: Ik ga binnenkort trouwen met 549219. Ze zit jammer genoeg niet in deze groep, maar jullie mogen allemaal naar het feest komen natuurlijk!
549218:         Inderdaad superleuk nieuws Proficiat van uwe toekomstige schoonbroer. :)
720362:         Dikke proficiat! <3
360184:         Gezondheid allemaal! Hopelijk worden jullie heel gelukkig samen! :)
525633536864:   Goh, maar dat is toevallig, ik ga binnenkort ook trouwen! ;)
1211:           Uw kadoke is reeds besteld se. Maar euh... ik voel me juist nen dwerg hier tussen al die grote getallen...
31609639681:    Hehehe, naast u voele kik mij idd just ne reus. :D
23405634121:    Amai, mannekes, die social media, ik kan ni meer volgen hoor!
152990:         Ja, dat is verwarrend he.
165209478:      Seg, ik ben vanaf morgen op skivakantie, dus moest ik ulle ni meer zien: Gelukkige Nieuwjaar!
```

Voor x en y hebben we een passende volgorde gevonden. Maar let op, voor elke volgorde bestaan er meerdere getallen. Dus wanneer de toelatingsvoorwaarde gevonden is moeten deze getallen hoogstwaarschijnlijk nog aangepast worden.

# Oplossing a
De moderatoren zijn alle elementen uit de aliquot cykel die voor het eerst beschreven werd door Poulet in 1918:
```
2      14316   2E2.3.1193
       19116   2E2.3E4.59
       31704   2E3.3.1321
       47616   2E9.3.31
       83328   2E7.3.7.31
       177792   2E7.3.463
       295488   2E6.3E5.19
       629072   2E4.39317
       589786   2.294893
       294896   2E4.7.2633
       358336   2E6.11.509
       418904   2E3.52363
       366556   2E2.91639
       274924   2E2.13.17.311
       275444   2E2.13.5297
       243760   2E4.5.11.277
       376736   2E5.61.193
       381028   2E2.95257
       285778   2.43.3323
       152990   2.5.15299
       122410   2.5.12241
       97946   2.48973
       48976   2E4.3061
       45946   2.22973
       22976   2E6.359
       22744   2E3.2843
       19916   2E2.13.383
       17716   2E2.43.103
```

De grootste moderator is dus `629072`.

# Oplossing b en c
De niet-moderatoren van de groep zijn getallen waarvoor de opeenvolging van het nemen van de som van de delers uiteindelijk bij een element uit de cykel uitkomt.
Voor x en y weten we al de vorm, we kunnen dus alle getallen genereren die aan de vorm voldoen en voor elk van hun controleren of ze bij een element uit de cykel uitkomen. Merk op dat dit heel lang kan duren. Het bestand possible x bevat de 330 kandidaat x-en.
