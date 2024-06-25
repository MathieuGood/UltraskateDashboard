from fuzzywuzzy import fuzz


class FuzzyWuzzyMatcher:
    def __init__(self):
        self.ratio = 0

    def match(self, string1, string2):
        ratio = fuzz.ratio(string1, string2)
        return ratio

    def get_ratio(self):
        return self.ratio