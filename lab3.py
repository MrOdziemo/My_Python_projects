from collections import Counter

#zad1
print("zad1")
with open("k.txt", 'r') as file:
    content = file.read().split()
    file.close()

counter = Counter(content)

sorted_elements_plus = sorted(counter.items(), key=lambda x: x[1])

sorted_elements_minus = sorted(counter.items(), key=lambda x: x[1], reverse=True)

print("Posortowane według wystąpień rosnąco:")
for item in sorted_elements_plus:
    print(item)

print("\nPosortowane według wystąpień malejąco:")
for items in sorted_elements_minus:
    print(items)


#zad2
print("zad2")
with open("k.txt", 'r') as plik:
    kontent = plik.readlines()
    plik.close()
    
kontent.sort()

sign_one = sorted(kontent, key=len)
sign_two = sorted(kontent, key=len, reverse=True)

print("\nPosortowane alfabetycznie:")
for word in kontent:
    print(word.strip())

print("\nPosortowane według długości znaków rosnąco:")
for words in sign_one:
    print(words.strip())

print("\nPosortowane według długości znaków malejąco:")
for words in sign_two:
    print(words.strip())

def count_vowels(wordss):
    vowels = "aeiouAEIOU"
    return sum(1 for char in wordss if char in vowels)

kontent_alfa = sorted(kontent, reverse=True ,key=lambda x: count_vowels(x))

print("\nPosortowane według samogłosek w napisach")
for wordss in kontent_alfa:
    print(wordss.strip())

vovel = 'a'

kontent_beta_one = sorted(words for words in kontent if words.startswith(vovel))
kontent_beta_two = sorted(words for words in kontent if not words.startswith(vovel))

sorted_words = kontent_beta_one + kontent_beta_two

print("\nPosortowane według początkowej litery 'a', a potem reszty wyrazów:")
for words in sorted_words:
    print(words.split())

#zad3
print("Zad3")
slownik = [{"imie" : "jakub",
            "nazwisko" : "odziemczyk",
            "wiek" : 21,
            "email" : "email1@xd.pl"},
            {"imie" : "klaudia",
            "nazwisko" : "kozioł",
            "wiek" : 20,
            "email" : ["email2@xd.pl", "email2.1@xd.pl"]},
            {"imie" : "karol",
             "nazwisko" : "komorowski",
            "wiek" : 26,
            "email" : "email3@xd.pl"},
            {"imie" : "wiktoria",
             "nazwisko" : "stefańczuk",
            "wiek" : 21,
            "email" : "email4@xd.pl"}]

print("\nWypisanie imion i nazwisk osób pełnoletnich:")
for index in slownik:
    if index["wiek"] >= 18:
        print(index["imie"])

print("\nWypisanie listy osób posortowanych według nazwisk:")
sort_slownik = sorted(slownik, key=lambda x: x['nazwisko'])
print(sort_slownik)

print("\nWypisanie listy osób posortowanych według wieku:")
sort_slowniks = sorted(slownik, key=lambda x: x['wiek'])
print(sort_slowniks)

print("\nWypisanie listy osób posortowanych według osób posiadających więcej niż jeden mail:")
sort_slownik = sorted(slownik, key=lambda osoby: len(osoby["email"]))
for osoby in sort_slownik:
    if len(osoby["email"]) > 1:
        print(sort_slownik)

#zad4
#zad5