# Syllabelizer for Indonesian Language in Python
This is a rule-based syllabelizer for Indonesian Language. Please note that this project does not aim to replicate rules in Ejaan yang Disempurnakan (EYD).

## Installation :zap:
```
pip install silabel
```

## Example Usage :robot:
```python
from silabel import Syllabelizer

s = Syllabelizer()
s.syllabelize("menggunakan") # ['meng', 'gu', 'na', 'kan']
s.syllabelize("memperkirakan") # ['mem', 'per', 'ki', 'ra', 'kan']
```

## Quick Check :mag:
Here are some results to check if this package suits your interest
```
BSD                       : b-s-d
SMP                       : s-m-p
main                      : ma-in
april                     : ap-ril
swasta                    : swas-ta
instan                    : in-stan
dengan                    : de-ngan
pandai                    : pan-dai
makhluk                   : makh-luk
saudara                   : sau-da-ra
menyapu                   : me-nya-pu
etiopia                   : e-ti-o-pi-a
masyhur                   : masy-hur
biografi                  : bi-o-gra-fi
instrumen                 : in-stru-men
pengarang                 : pe-nga-rang
reboisasi                 : re-boi-sa-si
musyawarah                : mu-sya-wa-rah
dramatisasi               : dra-ma-ti-sa-si
memproklamasikan          : mem-pro-kla-ma-si-kan
berkesinambungan          : ber-ke-si-nam-bu-ngan
mempertanggungjawabkan    : mem-per-tang-gung-ja-wab-kan
```

## Known Issue :persevere:
There are words with vocal diphthong that would not be syllabelize, such as `re-boi-sa-si`, but it is good enough for my use case so I prefer to let it be.

## End notes :heart:
There is no reference used in this project. I simply create a set of rules based on indonesian vocal, consonant, and diphthong to syllabelize indonesian words.

I made this repo for educational purposes so it might need further tweaking to reach production level. <br>
Feel free to create an issue if you need help, and I hope I'll have the time to help you. Thank you.

:heart: from Indonesia