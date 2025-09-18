import re

def symbol_count(text):
    count = len(text)
    print("Символов: ", count)
    return count

def word_count(text):
    word = text.split()
    count = sum(1 for i in word if i)
    print("Слов: ", count)
    return count

def sentences_count(text):
    sentences = re.split(r"[.!?]", text)
    count = sum(1 for s in sentences if s.strip())
    print("Предложений: ", count)
    return count

def longest_word(text):
    words_list = text.split()
    word = max(words_list, key=len)
    print("Самое длинное слово: ", word)
    return word

def save_report(save, filename):
    try:
        with open(filename, 'a') as f:
            f.write(save)
    except IOError as e:
        print(f"Error saving report: {e}")


def main():
    while True:
        text = input("Введите текст для анализа: ") 

        symbol = symbol_count(text)
        word = word_count(text)
        sentences = sentences_count(text)
        longest = longest_word(text)

        save_log = (
            f"\n-------------------\n"
            f"Текст для анализа:\n{text}\n\n"
            f"Символов: {symbol}\n"
            f"Слов: {word}\n"
            f"Предложений: {sentences}\n"
            f"Самое длинное слово: {longest}\n"
        )
        save_report(save_log, "text_report.txt")

        r = input("Хотите продолжить? (y/n): ")
        if r not in ["y", "Y"]:
            print("До свидания!")
            break

if __name__ == "__main__":
    main()