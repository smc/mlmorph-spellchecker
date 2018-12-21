from .suggestion_strategy import SuggestionStrategy


class PhoneticSimilarity(SuggestionStrategy):
    def suggest(self, word):
        confusables = ['കഖഗഘ', 'ചഛജഝ', 'ടഠഡഢ','തഥദധ','പഫബഭ', 'രറ', 'ലള', 'ശഷസ']
        candidates = []
        for confusable in confusables:
            candidates += self.getCandidatesWithReplacements(word, confusable)

        candidates.append(word.replace('ദ്ധ', 'ധ'))
        candidates.append(word.replace('ധ','ദ്ധ'))
        candidates.append(word.replace('ശ്ച', 'ച്ഛ'))
        candidates.append(word.replace('ച്ഛ', 'ശ്ച'))
        candidates.append(word.replace('ഷ', 'ക്ഷ'))
        candidates.append(word.replace('ക്ഷ', 'ഷ')) # പ്രതിക്ഷേധം
        return candidates
