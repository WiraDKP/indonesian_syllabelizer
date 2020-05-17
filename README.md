# Syllabelizer for Indonesian Language in Python
This is a rule-based syllabelizer for Indonesian Language. Please note that this project does not aim to replicate rules in Ejaan yang Disempurnakan (EYD), but focuses on a simple way to split indonesian words into common sub-words because it is good enough for my purposes.

## Installation
```
pip install silabel
```

## Example Usage
```python
from silabel import Syllabelizer

s = Syllabelizer()
s.syllabelize("menggunakan") # ['meng', 'gu', 'na', 'kan']
s.syllabelize("memperkirakan") # ['mem', 'per', 'ki', 'ra', 'kan']
```

## End notes :heart:
There is no reference used in this project. I simply create a set of rules based on indonesian vocal, consonant, and diftong to syllabelize indonesian words.

I made this repo for educational purposes so it might need further tweaking to reach production level. <br>
Feel free to create an issue if you need help, and I hope I'll have the time to help you. Thank you.

:heart: from Indonesia