#lookup suggestions for multi-word input strings (supports compound splitting & merging)
# library symspellpy
from symspellpy import SymSpell, Verbosity

# initialize
sym_spell = SymSpell()

list_kata = 'Manfaat Apel buat Badan Sehat serta Bebas dari Penyakit. Tidak cuma itu, buah apel juga memilikki antioksidan, semacam flavonoid, serta pektin yang baik untuk kesehatan badan serta menghindari bermacam penyakit. Anda dapat konsumsi buah apel dengan bermacamm cara, baik dimakan langsung, dibuat juice, ataupun dijadikan salad buah. Terdapat beberapa khasiat yang dapat anda peroleh dari komsumsi buah apel, antara llain.'
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
