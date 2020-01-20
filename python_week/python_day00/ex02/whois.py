import sys

def main():
    list = sys.argv

    if len(list) > 2:
        print("ERROR")
        return 0
    try:
        list[1] = int(list[1])
    except:
        print("ERROR")
        return 0
    if list[1] == 0:
        print("I'm zero.")
    elif list[1] % 2 == 0:
        print("I'm even.")
    elif list[1] % 2 != 0:
        print("I'm odd.")
    return 0
    
main()
