#Zad6
def word_reverse(sentence: str) -> str:
    return " ".join([word[::-1] for word in sentence.split(' ')])

print(word_reverse("Ala ma kota"))