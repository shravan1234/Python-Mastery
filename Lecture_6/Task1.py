Options = """
1.January         7.July   
2.February        8.August
3.March           9.September
4.April           10.October
5.May             11.November
6.June            12.December
"""
print(Options)
Options = int(input("Please enterr a number for what moth you would like to choose: "))
match Options:
    case 1:
        print("January!")
    case 2:
        print("February!")
    case 3:
        print("March!!")
    case 4:
        print("April!")
    case 5:
        print("May!")
    case 6:
        print("June!")
    case 7:
        print("July!")
    case 8:
        print("August!")
    case 9:
        print("September!")
    case 10:
        print("October!")
    case 11:
        print("November!")
    case 12:
        print("December!")
    case _:
        print("Invalid month...")