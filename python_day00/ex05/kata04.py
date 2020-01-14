def main():
    t = (0, 4, 132.42222, 10000, 12345.67)
    print("day_0{0}, ex_0{1} : {2}, {3}, {4}".format(t[0], t[1], round(t[2], 2), format(t[3], "10.2e"), format(t[4], "10.2e")))

main()
