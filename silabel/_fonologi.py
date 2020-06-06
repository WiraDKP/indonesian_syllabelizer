from string import ascii_lowercase


class BaseFonologi:
    def __init__(self):
        self.diftong_konsonan_map = {"kh": "å", "ng": "ß", "ny": "©", "sy": "∆"}
        self.diftong_konsonan = ["å", "ß", "©", "∆"]
        self.diftong_vokal = ["ai", "au", "ei", "oi"]
        self.vokal = ["a", "e", "i", "o", "u"]
        self.konsonan = [char for char in ascii_lowercase if char not in self.vokal]

        self.konsonan_kuat = list("bcdfgjkmnpqstvz")
        self.konsonan_lemah = list("hlrw")
        self.diftong_khusus = ["st"]
        
    def _merge_diftong(self, text):
        for k, v in self.diftong_konsonan_map.items():
            text = text.replace(k, v)
        return text

    def _revert_diftong(self, text):
        for k, v in self.diftong_konsonan_map.items():
            text = text.replace(v, k)
        return text

    def _to_fonologi(self, text):
        return "".join(["v" if char in self.vokal else "k" for char in text])
    
    def _is_all_konsonan(self, text):
        all_cons = True
        for char in text:
            if char in self.vokal:
                all_cons = False
        return all_cons
