Collectie van een aantal encodings:
Deze puzzel maakt een reis door acht locaties, soms groot, soms klein. Welke acht locaties?
```
CBDIFBIANCDIOBBEAO
YVKMFCXVEUVTFFIUZERRKZJUWVXFUVUETTTTWSTFUVJJCVLKVCZJUVCFTRKZV
EOKVITARRREIWSVOOKSKEMXBEWWOEJWCILNIGQYLRXREENEGPAMMIE
NTFUESAAMILGGOATAEHEKESDNEEHTRFINEIEECWGG
XRNAKAGNIDVPXGKMTFZOYIONYCM
CBECCCVEQCEOBPQUDAEPCVKKITSVCHCVWXKKCVEPDIPQIDNCHCBYUPHECY
PHNQIDMRUKBVIHCXRASVQVOKHY
```

## Regel 1
Regel 1 bevat letters relatief laag in het alfabet. Als we die omzetten naar cijfers, behalve de N en O dan vinden we `N32.496291 E34.9152251` of volgende locatie op google maps: https://www.google.be/maps/place/32%C2%B029'46.7%22N+34%C2%B054'54.8%22E/@32.4962847,34.9064711,15z/data=!4m5!3m4!1s0x0:0x0!8m2!3d32.496291!4d34.9152251 de caesarea golf club

## Regel 2
Regel 2 kunnen we decoderen volgens de caesar cipher (zie tip in locatie 1). Met een shift van 17 bekomen we:
`HETVOLGENDECOORDINAATISDFEGODEDNCCCCFBCODESSLEUTELISDELOCATIE` Ofwel, het volgende coordinaat is `DFEGODEDNCCCCFBCO` de sleutel is de locatie.

Het coordinaat omzetten levert `N46.570454 E3.333623` op, rue vigenere: https://www.google.com/maps/place/46%C2%B034'13.6%22N+3%C2%B020'01.0%22E/@46.570454,3.333623,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x0!8m2!3d46.570454!4d3.333623 .
 Vigenere cypher voor regel 3 levert niet direct iets op met code moulins oid

## Regel 3
We kunnen regel 3 decoderen met een vigenere cypher met als sleutel ruevigenere. We bekomen dan `NUGAANWENAARCOAGIGFGNIGHABOIAWSLEUTELISHETAANTALHUIZEN` ofwel, Nu gaan we naar `COAGIGFGNIGHABOIAW` sleutel is het aantal huizen.

Nu moeten we naar N30.179767 W97.812091. https://www.google.com/maps/place/30%C2%B010'47.2%22N+97%C2%B048'43.5%22W/@30.1796047,-97.8123076,20z/data=!4m5!3m4!1s0x0:0x0!8m2!3d30.179767!4d-97.812091 . Dit is Rail Fence Cove.

## Regel 4
We weten dat we een cijfer moeten gebruiken als key, dus een rail fence cipher behoort tot de mogelijkheden. Als we daar met 8 rails decoderen, dan bekomen we `NUMAKENWEHETIETSLASTIGERDEGAFAGHNFEGCIEEO` ofwel, Nu maken we het iets lastiger `DEGAFAGHNFEGCIEEO`

## Regel 5
De volgende coordinaat is N45.716178 E6.573955: https://www.google.com/maps/place/45%C2%B042'58.2%22N+6%C2%B034'26.2%22E/@45.716178,6.573955,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x0!8m2!3d45.716178!4d6.573955 . Beaufort cipher met "BEAUFORT" als key geeft `ENNUVOLGTBFFIIHHIZBGHGDGDCO` ofwel, En nu volgt `BFFIIHHIZBGHGDGDCO`.
