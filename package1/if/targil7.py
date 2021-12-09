day=int(input("enter day: "))


if day>0 and day<=31:
    month = int(input("enter month: "))
    if month>=1 and month<=12:
        year = int(input("enter year: "))
        if year>=1950 and year<=2020:

            if day<10 and month<10:
                print(f"0{day}/0{month}/{year//10%10}{year%10}")
            elif day>=10 and month<10:
                print(f"{day}/0{month}/{year//10%10}{year%10}")
            elif day<10 and month>=10:
                print(f"0{day}/{month}/{year // 10 % 10}{year % 10}")
            else:
                print(f"{day}/{month}/{year // 10 % 10}{year % 10}")
        else:
            print("year isnt right")
    else:
        print("month isnt right")
else:
    print("day isnt right")

