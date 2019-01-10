
De afbeelding in tekstvorm, met encodering:

 - `-` = grijs
 - `A` = azuurblauw (1 in mijnenveger)
 - `G` = groen (2 in mijnenveger)
 - `O` = oranje (3 in mijnenveger)
 - `D` = donkerblauw (4 in mijnenveger)
 - `B` = bruin (5 in mijnenveger)
 - `C` = cyaan (6 in mijnenveger)
 - `Z` = zwart (7 in mijnenveger)
```
    -----G--O--D---A---G-------D-D--
    -OB-D-A-------G-D---AD--A--Z--O-
    --D-------DDBBO--O-----BG----D-O
    ----A----B-----BB-G------B------
    O-D-AG-B---G-------O----O-------
    GO-O--GB-D-G-----BO----GD---AGOG
    -D-D-O-----------O----GA---DD---
    G-----D----DOD------D-AG------G-
    -O-B-C-B-C-B-OO---AA-O-G--G--BO-
    --O----BG-------O---------AG----
    ----O---A-ODO------AD-D--G-G-D-G
    --C-G-------OO-BZ--O--O--OG--O--
    B----O--G---D------D-----O---G-G
    --C-D-B-GG---D---------A-O--A-G-
    ----O-----O----DBODD-D---D---GGA
    --OG---O---O--C-D-D--D-----O----
    D---D---AGO-B-----------B-D---G-
    -D-G---O-------Z---B-D-G---O-DO-
    ----D-O--D-C-DD----C--DO--A-B--G
    D-D--GAGG---G---D----D--------B-
    --OO-------DOD-C-B-Z-B--O---B---
    ---G---O-B--D----------G-O-B-D-G
    -B-O-----O-O--C---AOO----B--O---
    -B----GO---D-B-OA----O-G-D---OD-
    --O--O----O-----A-G--O---O---G--
    -----B--GO------A---D--A----OGO-
    O-G--D-C-O-DDC-D-O---------O--DO
    ---------O-G-------D-O------O---
    -O--G-----AG--O-----DC---GD--O--
    ---DGGG---GG---D-Z-----CO---B---
    -D---D-G---G-O-O-----Z---O--B--A
    ---G----O----G-O----D-----------
    ------A-AAA----A-OOG-O-----D-DO-
```

board.txt bevat bovenstaand grid met getallen ipv letters
valid input voor https://github.com/madewokherd/mines

unieke oplossing met 407 mines:
python mines/mines.py mines 32 33 407 < board.txt

De mijnen uit de oplossing kunnen als braille gelezen worden:
```
·☻ ☻☻ ☻☻ ·· ☻☻ ☻☻ ☻☻ ·☻ ☻☻ ☻☻ ☻· ☻· ·· ☻☻ ☻☻ ☻· 
·· ·☻ ·☻ ·· ☻☻ ·☻ ☻☻ ·· ·☻ ·· ·· ☻☻ ·· ☻· ☻☻ ·☻ 
·☻ ·· ·· ·· ·☻ ·· ·· ·· ☻· ·· ·· ☻· ·· ☻☻ ☻· ·· 

☻☻ ☻· ·· ☻· ☻· ☻· ☻☻ ☻· ·☻ ·· ☻· ☻· ☻· ☻· ·· ☻☻ 
·☻ ·☻ ·· ☻· ☻☻ ·· ·· ☻☻ ☻☻ ·· ☻· ·☻ ·☻ ☻· ·· ☻☻ 
·· ·· ·· ·· ☻· ·· ·· ·· ☻· ·· ☻☻ ·· ·· ☻· ·· ·· 

☻· ☻· ☻· ☻· ☻· ·☻ ☻☻ ☻· ☻· ☻☻ ☻· ·· ☻☻ ☻· ·☻ ·· 
·☻ ☻☻ ·☻ ·☻ ☻☻ ☻· ·· ☻☻ ·· ·☻ ·☻ ·· ·· ·☻ ☻☻ ·· 
·· ·· ☻· ☻· ☻· ☻· ·· ·· ·· ·· ·· ·· ☻· ·· ☻· ·· 

☻· ·☻ ☻☻ ☻· ·· ☻☻ ☻· ☻· ·· ·· ·☻ ☻· ·☻ ·· ☻☻ ·☻ 
·☻ ☻· ·· ☻☻ ·· ·· ·☻ ·☻ ☻☻ ·· ·☻ ·· ☻· ·· ·· ☻· 
☻☻ ·· ·· ·· ·· ☻· ·· ·· ·☻ ·· ☻☻ ·· ·· ·· ☻· ·· 

·☻ ☻☻ ☻· ☻☻ ·· ☻☻ ·☻ ☻☻ ☻☻ ☻· ☻☻ ·· ☻· ☻☻ ·· ☻· 
☻☻ ·☻ ·☻ ·☻ ·· ☻☻ ☻· ·☻ ☻☻ ·☻ ·☻ ·· ·· ☻· ·· ·☻ 
·· ☻· ·· ☻· ·· ·· ·· ☻· ·· ·· ☻· ·· ·· ·· ·· ·· 

☻☻ ·· ☻· ☻· ·· ☻· ☻☻ ·☻ ·☻ ·☻ ☻· ☻☻ ☻☻ ☻· ☻☻ ·· 
·☻ ·· ·☻ ·☻ ·· ·☻ ·☻ ☻☻ ☻· ☻☻ ·☻ ·☻ ·☻ ·☻ ·☻ ·· 
☻· ·· ☻☻ ☻· ·· ☻· ☻· ☻· ☻· ☻· ☻· ☻· ·· ·· ☻· ·· 

·☻ ☻· ·☻ ·· ☻· ☻· ☻· ·☻ ☻· ☻· ·☻ ·· ·· ·☻ ·☻ ☻· 
·☻ ·· ☻· ·· ·· ☻☻ ·· ☻☻ ·☻ ☻☻ ☻· ☻☻ ·· ·· ☻☻ ·☻ 
☻☻ ·· ·· ·· ☻· ☻· ·· ☻· ·· ☻· ☻· ·☻ ·· ·☻ ·☻ ·· 

☻· ☻· ☻· ·· ☻· ·☻ ·☻ ☻☻ ☻· ☻· ☻☻ ·· ☻· ☻· ☻· ☻· 
☻· ·· ·☻ ·· ☻· ☻· ☻☻ ·☻ ·· ·· ·· ·· ·· ☻☻ ·☻ ·☻ 
☻· ☻· ·· ·· ·· ·· ·· ☻· ·· ·· ☻· ·· ☻· ☻· ·· ·· 

☻☻ ·· ☻· ☻· ☻· ·☻ ☻· ☻· ·· ·☻ ☻· ☻· ·· ☻☻ ☻· ☻☻ 
☻☻ ·· ·· ☻☻ ·· ☻☻ ·☻ ☻☻ ·· ·☻ ·· ·· ·· ·☻ ·· ·☻ 
·· ·· ☻· ☻· ·· ☻· ·· ☻· ·· ☻☻ ·· ·· ·· ☻· ·· ·· 

☻· ·☻ ·· ☻☻ ☻· ·· ☻☻ ☻· ·☻ ☻· ☻· ☻· ·· ☻· ·☻ ☻☻ 
·· ☻☻ ·· ·☻ ·☻ ·· ·☻ ·· ☻☻ ·· ·· ☻☻ ·· ·☻ ☻· ·· 
·· ☻· ·· ·· ·· ·· ☻· ·· ☻· ☻☻ ☻☻ ☻· ·· ☻☻ ·· ·· 

☻· ·· ☻· ☻· ☻☻ ·· ☻· ☻· ☻☻ ☻☻ ☻· ☻☻ ☻· ·☻ ·☻ ·· 
☻☻ ·· ☻☻ ·· ·☻ ·· ·· ·· ·☻ ☻☻ ·☻ ☻· ·· ☻· ☻☻ ☻· 
·· ·· ·· ·· ·· ·· ·· ·· ☻· ·· ·· ☻· ·· ☻· ☻· ·☻ 
```

Na ontcijferen krijgen we `Dd ïdg_ncar çqede bracht veel gehoorschade met zich mee. 19 mijnen gingen af en zo ontstonden 19 kraters. Welke bijnaam kreeg krater 11 nadat de natuur zich had aangepast?`. De eerste regel van de oplossing is dus vermoedelijk fout.

Het antwoord is dus `Pool of peace`.
