#lookup suggestions for multi-word input strings (supports compound splitting & merging)
# library symspellpy
from symspellpy import SymSpell, Verbosity

# initialize
sym_spell = SymSpell()

#lookup suggestions for multi-word input strings (supports compound splitting & merging)
list_kata = 'Bhasa merupakan alat komonikasi yang sunguh penting. Melalui bhasa manusia dpat menyampaikan isi hatii kepda sesamanya, mewarisi dan mewariskan, menerimo dan memberi pengtahuan kepada sesamanya. Bahkn dengn bahsa pula mnusia dapat mengekspresokan jiwah seninya. Dengn demikian jelaslah bhwa bahasab nerupakan sarana komunikasi yang sngat penting dlam kehidupan manusio.'
sentence = list_kata.split()

for kata in sentence:
    maxEditDistanceLookup = 2
    include_unknown = True
    suggestion = sym_spell.lookup(kata, Verbosity.TOP, maxEditDistanceLookup, include_unknown)

#display term and edit distance
    for s in suggestion:
      print(s.term, end=' ')


# create dictionary
path_corpus = "kompas.txt"
sym_spell.create_dictionary(path_corpus)
