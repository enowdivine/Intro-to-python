#Name: Isong Mbah
#Date: Fri July 1 2022
#Project: python program to calculate the date of Easter for any year in the twentieth or twenty-first centuries for Western dates.

while True:
    #prompting the user for a positive year
    year = int(input("Enter a positive year: "))

    #condition checking if entered year is negative
    if year < 0:
        break

    #mathematical computation when a valid year is entered
    valueD = year - 1900

    valueR = valueD % 19

    valueP = (7 * valueR + 1) // 19

    valueS = (11 * valueR + 4 - valueP) % 29

    valueQ = valueD // 4

    valueT = (valueD + valueQ + 31 - valueS) % 7

    Easter = 25 - valueS - valueT

    if Easter >  0:
        print(f"(Weatern) Easter Sunday - {Easter}th April, {year}")
    elif Easter <= 0:
        Easter = 31 + Easter
        print(f"(Weatern) Easter Sunday - {Easter}th March, {year}")

#print statement when a negative year is entered
print("Bye...")
