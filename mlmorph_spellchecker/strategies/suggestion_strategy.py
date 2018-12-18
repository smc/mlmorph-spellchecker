import abc
import re
from itertools import product


class SuggestionStrategy(metaclass=abc.ABCMeta):
    """
    Declare an interface common to all supported algorithms. Context
    uses this interface to call the algorithm defined by a
    ConcreteStrategy.
    """

    @abc.abstractmethod
    def suggest(self):
        pass

    def isConsonant(self, char):
        return re.compile(r'([ക-ഹ])').search(char) != None

    def getCandidatesWithReplacements(self, word, letters):
        candidates = []
        for replacement, pos in product(letters, range(len(word))):
            s = list(word)
            original = s[pos]
            if original in letters:
                s[pos] = replacement
                candidates.append(''.join(s))
        return candidates
