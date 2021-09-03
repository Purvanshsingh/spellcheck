import pkg_resources
from symspellpy import SymSpell, Verbosity

dictionary_path = pkg_resources.resource_filename("symspellpy", "frequency_dictionary_en_82_765.txt")
bigram_path = pkg_resources.resource_filename("symspellpy", "frequency_bigramdictionary_en_243_342.txt")



class SpellCorrector:
    def __init__(self):
        self.sym_spell = SymSpell()
        self.sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
        self.sym_spell.load_bigram_dictionary("data_bigrams.txt", term_index=0, count_index=2)

    async def spellcorrect(self, word: str):
        suggestions = self.sym_spell.lookup_compound(word, max_edit_distance=2)
        return suggestions[0]


"""if __name__ == '__main__':
    obj = SpellCorrector()
    word = (input())
    print(obj.spellcorrect(word))"""