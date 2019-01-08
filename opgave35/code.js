/*print("31704", "e d i d -es f,knanu 0aioeeeepslankoan2dheatuenl re j   f vkkAaekria eedvirwneresl !dr t  emnipcaembr do e adsa0rjonstlp!ll eft 7eern m ekotn1aTveemeie");
print("28790", "rkrilaen sta m!S!koall  euogvapD i m aene kneu efte!gdepfsakeipcaaWar rde n");
print("40952", "ok oee ! etk oeTin iKee!bo !gdp zpkii");
print("312620", "t. okw nrue2ej g zealgl hemtjae.e n:ae e 9zmenn , enmattnu!av bli ntn5.imni g j aa r lkouukioom9Z reteoaloll eoaiRo.hk sgntwt1 ag ie- prieeneseukrai eeIbkr 4 teoedrmumaarfknl")
print("549218", "rseera otcr:e liPintssb nae siveoeorIapkwf wkgoeduuuotueiho)ddrn ca m n.");
print("720362", "kotira c<kf!ei Dpi3");
print("360184", "zie iruhegnodmHjdlel !Ghllew e km)daap nilka:eel!loj gien aokeleus ");
print("525633536864", "o gnt  ikumtkowaegtnalik)Gtin hi,erao re,s norva !dlbo; a o ");
print("1211", "Uae deleae.keeindgeun tel. oie t rh v jtneh sair ankksebesM .iomu riteleogl.wd rssd.au.l sew rs dgete.");
print("31609639681", "eu s etijsa deHsk u,ojnh ku.evi Dnli aedrh mt: e e");
print("23405634121", "i,l ron ingeo, nAkc m nsaiemeiiehmienoasakeoaed l, k r dmav!");
print('152990', 'avreJtee.,iwda rn sa d rh');*/
//print('165209478', " aev t  zueSem tmue ea,vgi,se  lika kuiiekwg rkeelreN!enosioleG r foask nijb pn  m:gainnad niku");


//dict = getDict();
//testKey(dict, " aev t zueSem  tmue ea,vgi,se lika kuiiekwg rkeelreN!enosioleG r foask nijb pn m:gainnad niku");
//testSpaces("312620", "t. okw nrue2ej g zealgl hemtjae.e n:ae e 9zmenn , enmattnu!av bli ntn5.imni g j aa r lkouukioom9Z reteoaloll eoaiRo.hk sgntwt1 ag ieprieeneseukrai eeIbkr 4 teoedrmumaarfknl")

//permutationGenerator("165209478");

let mods = new Set([14316, 19116, 31704, 47616, 83328, 177792, 295488, 629072, 589786, 294896, 358336, 418904, 366556, 274924, 275444, 243760, 376736, 381028, 285778, 152990, 122410, 97946, 48976, 45946, 22976, 22744, 19916, 17716, ]);
//console.log(permutationGenerator("1211").filter(n => findSequence(n, mods)));
console.log(getPossibleY().filter(n => findSequence(n, mods)));
//findSequence(142109148, mods);

function testKey(dict, text) {
    let max = -1;
    for (let i = 100000000; i < 100000000000; i++) {
        const key = "" + i;
        if (key.length !== (new Set(key.split(""))).size) continue;
        const out = decode(text, key);
        const num = matchingWords(dict, out);
        if (num > max) {
            max = num;
            console.log(i + " (" + max + " hits): " + out);
        }
        if (num >= 4) {
            console.log(i + " (" + num + " hits): " + out);
        }
    }
}

function testSpaces(key, text) {
    const words = text.split(" ");
    let newText = "";
    let msg = "";
    while (!(msg.includes("Ik ga binnenkort trouwen met") && msg.includes("Raar toeval... ik heb ook leuk nieuws:"))) {
        newText = words[0];
        for (let i = 1; i < words.length; i++) {
            while(Math.random() > 0.8) {
                newText += " ";
            }
            newText += " " + words[i];
        }
        msg = decode(newText, key);
    }
    console.log("input: " + newText);
    console.log("output: " + msg);
}

function print(user, msg) {
    console.log(user + ":\t\t" + decode(msg, user));
}

function decode (input, key) {
    const chars =  input.split("");
    const permutation = generatePermutation(input.length, key);
    const output = [];
    permutation.forEach((element, position) => {
       output[element] = input[position]; 
    });
    return output.join('');
}

function generatePermutation(inputLength, key) {
    const input = new Array(inputLength).fill(0).map((v, i) => i);
    const keyLength = key.length;
    const cols = new Array(keyLength).fill(0).map(() => []);
    for (let i = 0; i < input.length; i++) {
        let col = i % keyLength;
        cols[col].push(input[i]);
    }
    return keyToPermutation(key).map(i => cols[i]).flat();
}

function keyToPermutation(key) {
    const chars = key.split('').map(x => +x);
    const output = [];
    for (let i = 0; i < chars.length; i++) {
        const p = positionOfMin(chars);
        output.push(p);
        chars[p] = 10;
    }
    return output;
}

function positionOfMin(array) {
    return array.indexOf(Math.min(...array));
}

function getDict() {
    const fs = require('fs');
    return new Set(fs.readFileSync('woordenlijst.txt').toString().split("\n"));
}

function matchingWords (dict, text) {
    const words = text.replace(/,/g, " ").replace(/!/g, " ").replace(/:/g, " ").replace(/  /g, " ").split(" ").filter(w => w.length > 2);
    let i = 0;
    words.forEach(word => {
        if(dict.has(word)){
            i++;
        }
    });
    return i;
}

function toCols(text, key){
    const input = text.split("");
    const keyLength = key.length;
    const cols = new Array(keyLength).fill(0).map(() => []);
    for (let i = 0; i < input.length; i++) {
        let col = i % keyLength;
        cols[col].push(input[i]);
    }
    return cols;
}

function toShiftedCols(text, key) {
    const cols = (toCols(text, key))
    return keyToPermutation(key).map(i => cols[i]);
}

function permutationGenerator(key) {
    const keyLength = key.length;
    const startKey = Math.pow(10, keyLength - 1);
    const endKey = Math.pow(10, keyLength);
    const keys = [];
    const order = keyToPermutation(key).join('');
    for (let i = startKey; i < endKey; i++) {
        if (keyToPermutation("" + i).join('') === order) {
            //console.log(i);
            keys.push(i);
        }
        
    }
    return keys;
}

function factors(n) {
    const f = [];
    const sqrt = Math.floor(Math.sqrt(n));

    for (let i = 1; i <= sqrt; i++)
        if (n % i === 0) {
            f.push(i);
            q = n / i
            if (q !== i && q !== n) // without itself!
                f.push(q);
        }
    return f;
}

function findSequence(start, mods) {
    console.log("testing " + start);
    let current = start;
    let iterations = new Set();
    for (let i = 0; i < 10000000000; i++) {
        current = factors(current).reduce((a, b) => a + b);
        //console.log(current);
        if (mods.has(current)) {
            console.log(current);
            return true;
        }
        if (iterations.has(current)) {
            //console.log("ended on loop");
            return false;
        }
        if (current === 1) {
            //console.log("ended on 1");
            return false;
        }
        if (current > 10000000000000) {
            //console.log("too big");
            return false;
        }
        iterations.add(current);
    }
    console.log("too many operations");
    return false;
}

function getPossibleY() {
    const fs = require('fs');
    return fs.readFileSync('possible_y.txt').toString().split("\n").map(x => +x);
}
