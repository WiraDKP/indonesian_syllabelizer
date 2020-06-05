import re
import numpy as np


class Syllabelizer:
    def __init__(self):
        self.DFT_K = ["kh", "ng", "ny", "sy", "dh", "ch", "ph", "th", "gr",
                      "tr", "fr", "pr", "kl", "bl", "pl", "kr", "sw", "dw"]
        self.DFT_K = {a: b for a, b in zip(self.DFT_K, list("¡£¢∞•≠œ®†¥øπ«åß©∆"))}

        self.DFT_V = ["ai", "au", "ei", "oi"]
        self.VOKAL = ["a", "e", "i", "o", "u"]

    def syllabelize(self, query, revert=True):
        query = self._merge_diftong(query)
        suku_kata = self._split_query(query)
        suku_kata = self._fix_vdift(suku_kata)

        if revert:
            suku_kata = [self._revert_diftong(s) for s in suku_kata]
        return suku_kata        
        
    def _merge_diftong(self, text):
        for k, v in self.DFT_K.items():
            text = text.replace(k, v)
        return text

    def _revert_diftong(self, text):
        for k, v in self.DFT_K.items():
            text = text.replace(v, k)
        return text

    def _split_query(self, query):
        symbol = "".join(["v" if char in self.VOKAL else "k" for char in query])

        symbol = symbol.replace("kk", "k|k")
        symbol = symbol.replace("vv", "v|v")
        symbol = symbol.replace("|vkv", "v|kv")
        symbol = symbol.replace("kvv|", "kv|v|")
        symbol = symbol.replace("kvk|", "|kvk|")
        symbol = re.sub("kvk$", "|kvk", symbol)
        symbol = re.sub("^vkv", "v|kv", symbol)    
        symbol = re.sub("\|+", "|", symbol)
        symbols = []
        for s in symbol.split("|"):
            if s != "":
                if len(s) > 3:
                    symbols += s.replace("vk", "v|k").split("|")
                else:
                    symbols += [s]

        idx = np.cumsum([0] + [len(s) for s in symbols])
        suku_kata = [query[a:b] for a, b in zip(idx[:-1], idx[1:])]
        return suku_kata

    def _fix_vdift(self, suku_kata):
        result = []
        skip_v = False
        for i, s in enumerate(suku_kata[:-1]):
            if suku_kata[i+1] in self.VOKAL:
                if (s[-1] + suku_kata[i+1]) in self.DFT_V:
                    result += [s + suku_kata[i+1]]
                    skip_v = True
                else:
                    result += [s]                
            elif s in self.VOKAL and skip_v:
                pass
            else:
                result += [s]
        if (suku_kata[-1] not in self.VOKAL) | (not skip_v):
            result += [suku_kata[-1]]
        return result
