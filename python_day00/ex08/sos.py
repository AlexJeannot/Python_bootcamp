import sys

def main():

    morse_dict = { 'A':'.-', 'B':'-...',
                'C':'-.-.', 'D':'-..', 'E':'.',
                'F':'..-.', 'G':'--.', 'H':'....',
                'I':'..', 'J':'.---', 'K':'-.-',
                'L':'.-..', 'M':'--', 'N':'-.',
                'O':'---', 'P':'.--.', 'Q':'--.-',
                'R':'.-.', 'S':'...', 'T':'-',
                'U':'..-', 'V':'...-', 'W':'.--',
                'X':'-..-', 'Y':'-.--', 'Z':'--..',
                '1':'.----', '2':'..---', '3':'...--',
                '4':'....-', '5':'.....', '6':'-....',
                '7':'--...', '8':'---..', '9':'----.',
                '0':'-----', ', ':'--..--', '.':'.-.-.-',
                '?':'..--..', '/':'-..-.', '-':'-....-',
                '(':'-.--.', ')':'-.--.-'}

    final_str = ""
    list = sys.argv
    del list[0]
    i = 1
    for elem in list:
        x = 1
        for letter in elem:
            try:
                final_str += morse_dict[letter.upper()]
                if (x < len(elem) or i < len(list)):
                    final_str += ' '
            except:
                print("ERROR")
                return 0
            x += 1
        if (i < len(list)):
            final_str += "/ "
        i += 1
    print(final_str)
    return 0

main()
