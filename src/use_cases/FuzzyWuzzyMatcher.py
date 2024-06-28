from fuzzywuzzy import fuzz


class FuzzyWuzzyMatcher:
    @staticmethod
    def match(string1, string2):
        return fuzz.ratio(string1, string2)