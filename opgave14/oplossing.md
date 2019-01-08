Eric speelt graag met getallen. Hij maakte dit overzicht van getallen en Belgische vlagget- jes. Welke reeks komt op de plaats van de vraagtekens? Als je een Belgische vlag wil noteren, schrijf dan een "B".

Vervolgens hebben we een rooster met getallen waarin sommige getallen vervangen zijn door een vlag.

**Wat weten we?**
* Er bestaat iets als Belgian numbers (vroeger Eric numbers, hint opgave). Alle Belgian numbers worden als vlag weergegeven, de andere worden integraal getoond
* De getallen in elke rij zijn strikt stijgend
* De eerste kolom bevat waarschijnlijk de getallen 3 tot 20
* In de rij waar 10 in de eerste kolom zou kunnen staan komen de eerste 10 niet-belgian numbers voor
* De franstalige opgave is identiek, dus vermoedelijk niet tekstueel.

**Wat merken we op?**
* Naast de standaard belgian numbers (ook wel belgian-0 numbers genoemd) bestaan er ook 1-9 numbers. Er zijn echter geen aanwijzigen dat deze gebruikt worden.
* De bovenste rij bevat veel gaten, met een hoge waarde rechtsboven tot gevolg. De onderste rij bevat amper gaten.

**oplossing**
Iedere rij bevat de eerste 10 non Belgian Numbers, maar uitgedrukt in een andere basis. De basissen zijn oplopen 3,4,...,20. Daarom dat op rij 10 de non Belgian Numbers staan. Om te weten of een getal n op de rij van basis b staat moet de volgende procedure toegepast worden:

- Zet n om naar basis b
- Pas de zelfde procedure als bij de belgian numbers toe, maar nu in basis b

**Voorbeeld n=15, b = 8**

15 in basis 8 is gelijk aan 17

Voor ons voorbeeld is de rij dan
0,1,10,11,20,...

17 staat die in die rij en staat dus wel op de rij van basis 8

**voorbeeld n=20, b=16**

20 in basis 16 is 14

De rij wordt
0,1,5,6,A,B,F,10,14,...

14 duikt wel op in deze rij en dus staat 20 niet op de rij van basis 16

Het volledig ingevuld rooster is dan

3	5	7	11	17	19	29	34	43	46	47
4	7	11	13	14	19	23	31	37	41	43
5	9	13	17	19	21	23	29	33	34	35
6	8	11	13	16	17	22	23	26	27	29
7	10	13	19	20	22	25	26	31	33	37
8	11	12	15	19	22	23	25	26	29	31
9	11	13	14	17	19	21	22	25	26	29
10	14	15	16	19	23	25	28	29	32	34
11	14	16	17	18	21	27	28	31	32	34
12	14	15	17	18	19	20	23	25	28	29
13	17	19	20	21	22	25	29	31	33	34
**14	18	20	21	22	23	24	27	31	33	35**
15	17	18	19	20	22	23	24	25	26	29
16	19	21	23	24	25	26	27	28	31	38
17	22	23	25	26	27	28	29	30	33	39
18	20	22	23	24	26	27	28	29	30	31
19	22	23	25	26	28	29	30	31	32	33
20	23	24	26	27	29	30	31	32	33	34

En rekening houdend met de vlaggetjes

14	B	B	B	B	23 B	B	B	B	B

