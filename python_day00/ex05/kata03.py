def main():
    phrase = "The right format"
    final_phrase = ""
    i = 42 - len(phrase)
    while i > 1:
        final_phrase += '-'
        i -= 1
    final_phrase += phrase
    print(final_phrase)

main()
