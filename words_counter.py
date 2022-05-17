#zapytanie do użytkownika o wprowadzenie tekstu
text = input("Wprowadź tekst: ")

#podział tekstu na słowa, gdzie znakiem oddzielającym jest spacja
words = text.split(" ")

#zliczanie zestawów słów po podziale
sets_words = set(words)

#wyświetlanie w pętli słów oraz liczby ich wystąpień:
for word in sets_words:
    print(f"'{word}' occurs {words.count(word)} times.")