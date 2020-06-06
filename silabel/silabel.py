import numpy as np
from silabel._fonologi import BaseFonologi


class Syllabelizer(BaseFonologi):
    def __init__(self):
        super().__init__()

    def syllabelize(self, text, revert=True):
        text = text.lower()
        
        if self._is_all_konsonan(text):
            silabel = list(text)
        else:
            text = self._merge_diftong(text)            
            silabel = self._initialize_split(text)
            silabel = self._fix_silabel(silabel)

        if revert:
            silabel = [self._revert_diftong(s) for s in silabel]
        return silabel
    
    def _initialize_split(self, query):
        # Konversi ke fonologi        
        f = self._to_fonologi(query)

        # Pisah konsonan dan vokal
        f = f.replace("kk", "k|k")
        f = f.replace("vv", "v|v")
        
        # Pisah suku diawali vokal
        f = f.replace("|vk|", "|v|k|")
        
        # Pisah 2 suku diawali vokal
        f = f.replace("vkv", "v|kv")
        
        # Pisah 2 suku ganjil konsonan
        f = f.replace("|kvkvk|", "|kv|kvk|")
        
        # Pisah yang berbeda fonologi
        f_list = []
        for item in f.split("|"):
            if item != "":
                if len(item) > 3:
                    f_list += item.replace("vk", "v|k").split("|")
                else:
                    f_list += [item]

        # Kembalikan ke string
        idx = np.cumsum([0] + [len(f) for f in f_list])
        silabel = [query[a:b] for a, b in zip(idx[:-1], idx[1:])]
        return silabel

    def _fix_silabel(self, silabel):
        skip = False
        result = []
        for s_a, s_b in zip(silabel[:-1], silabel[1:]):
            if not skip:
                # Fix single vokal
                if (s_b in self.vokal):
                    if (s_a[-1] + s_b) in self.diftong_vokal:
                        result.append(s_a + s_b)
                        skip = True
                    else:
                        result.append(s_a)
                # Fix single konsonan
                elif (s_a in self.konsonan_kuat) and (s_b[0] in self.konsonan_lemah):
                        result.append(s_a + s_b)
                        skip = True
                # Fix konsonan khusus
                elif (s_a in self.diftong_khusus) and (s_b[0] in self.konsonan_lemah):
                        result.append(s_a + s_b)
                        skip = True      
                else:
                    result.append(s_a)
            else:
                skip = False
                
        # Handle silabel terakhir
        if not skip:
            if s_b in (self.konsonan + self.diftong_konsonan):
                result[-1] += s_b
            else:
                result.append(s_b)
        return result
