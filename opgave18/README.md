

input.txt is mijn overgeschrebven variant van de cirkel. De letters zijn in wijzerzijn opgeschreven van binnen naar buiten

```
l() {grep -o '[A-Z]' | sort | uniq -c | sort -nr}; diff -s <(l < gecoppypasteletters.txt) <(l < input.txt);
Files /proc/self/fd/11 and /proc/self/fd/12 are identical
```
