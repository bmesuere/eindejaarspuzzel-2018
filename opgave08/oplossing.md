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
Regel 1 bevat letters relatief laag in het alfabet. Als we die omzetten naar cijfers, behalve de N en O dan vinden we `N32.496291 E34.902251` of `N32.496291 E34.902251` als we `O` door `0` vervangen wat de volgende locatie geeft op google maps: https://www.google.be/maps/place/32%C2%B029'46.7%22N+34%C2%B054'08.1%22E/@32.4985403,34.9069791,16.7z/data=!4m5!3m4!1s0x0:0x0!8m2!3d32.496291!4d34.902251 de caesarea golf club of het dorpje caesarea

## Regel 2
Regel 2 kunnen we decoderen volgens de caesar cipher (zie tip in locatie 1). Met een shift van 17 bekomen we:
`HETVOLGENDECOORDINAATISDFEGODEDNCCCCFBCODESSLEUTELISDELOCATIE` Ofwel, het volgende coordinaat is `DFEGODEDNCCCCFBCO` de sleutel is de locatie.

Het coordinaat omzetten levert `N46.570454 E3.333623` op, rue vigenere: https://www.google.com/maps/place/46%C2%B034'13.6%22N+3%C2%B020'01.0%22E/@46.570454,3.333623,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x0!8m2!3d46.570454!4d3.333623 .

## Regel 3
We kunnen regel 3 decoderen met een vigenere cypher met als sleutel `ruevigenere`. We bekomen dan `NUGAANWENAARCOAGIGFGNIGHABOIAWSLEUTELISHETAANTALHUIZEN` ofwel, Nu gaan we naar `COAGIGFGNIGHABOIAW` sleutel is het aantal huizen.

Nu moeten we naar `N30.179767 W97.812091`. https://www.google.com/maps/place/30%C2%B010'47.2%22N+97%C2%B048'43.5%22W/@30.1796047,-97.8123076,20z/data=!4m5!3m4!1s0x0:0x0!8m2!3d30.179767!4d-97.812091 . Dit is Rail Fence Cove waar 8 huizen staan.

## Regel 4
We kunnen regel 4 decoderen met een rail fence cipher met sleutel 8, dan bekomen we `NUMAKENWEHETIETSLASTIGERDEGAFAGHNFEGCIEEO` ofwel, Nu maken we het iets lastiger `DEGAFAGHNFEGCIEEO`.

Het coordinaat levert `N45.716178 E6.573955` op, het dorpje beaufort: https://www.google.com/maps/place/45%C2%B042'58.2%22N+6%C2%B034'26.2%22E/@45.716178,6.5717663,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x0!8m2!3d45.716178!4d6.573955

## Regel 5
We kunnen regel 5 dedoceren met de Beaufort cipher met `BEAUFORT` als key geeft `ENNUVOLGTBFFIIHHIZBGHGDGDCO` ofwel, En nu volgt `BFFIIHHIZBGHGDGDCO`.

Het coordinaat levert `S26.699889 E27.874743` op, playfair boulevard: https://www.google.com/maps/place/26%C2%B041'59.6%22S+27%C2%B052'29.1%22E/@-26.699889,27.8725543,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x0!8m2!3d-26.699889!4d27.874743

## Regel 6
We kunnen regel 6 docoderen met het playfair cypher, met `playfairboulevard` als key. We stellen hierbij I en J gelijk aan elkaar en splitsen geen dubbele letters. We bekomen `DOGDBBEGNGCIIAGFBWISDEEERSTEENDETWEEDEISEBFHBECONEOAIFEIOX`ofwel `DOGDBBEGNGCIIAGFBW` is de eerste en de tweede is `EBFHBECONEOAIFEIOX`

Het eerste coordinaat levert `N40.742257 W73.991762` op, een plaats in Manhattan: https://www.google.com/maps/place/40%C2%B044'32.1%22N+73%C2%B059'30.3%22W/@40.7421444,-74.0267542,13z/data=!4m5!3m4!1s0x0:0x0!8m2!3d40.742257!4d-73.991762 

Het tweede coordinaat eindigt op een X wat raar is. Als we die weglaten bekomen we `N52.682530 E5.019659`, de straat Vierkant: https://www.google.com/maps/place/52%C2%B040'57.1%22N+5%C2%B001'10.8%22E/@52.6825332,5.0174703,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x0!8m2!3d52.68253!4d5.019659

## Regel 7
Four-square cipher? Geen idee van de key.


