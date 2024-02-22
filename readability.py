def get_text():
    return input("Text: ")

def count_letters(text):
    return sum(c.isalpha() for c in text)

def count_words(text):
    return len(text.split())

def count_sentences(text):
    return text.count('.') + text.count('!') + text.count('?')

def main():
    text = get_text()

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")

if __name__ == "__main__":
    main()
