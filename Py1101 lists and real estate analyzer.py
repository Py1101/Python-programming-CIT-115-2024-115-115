def getFloatInput(prompt):
    while True:
        try:
            fuserinput = float(input(prompt))
            if fuserinput <= 0:
                print("Input a number that is greater than 0.")
            else:
                return fuserinput
        except ValueError:
            print("Input a number that is greater than 0.")

def getMedian(flist):   
    flist.sort()
    middle = len(flist) // 2
    if len(flist) % 2 == 1:
        return flist[middle]
    else:
        return (flist[middle - 1] + flist[middle]) / 2

def main():
    flist = []
    
    while True:
        fSalesPrice = getFloatInput("Enter property sales value: ")
        flist.append(fSalesPrice)
        
        fnewamount = input("Enter another value Y or N: ").upper()
        if fnewamount == "N":
            break
        elif fnewamount != "Y":
            print("Please enter Y or N.")
    
    flist.sort()
    for index, sale in enumerate(flist, start=1):
        print(f"Property {index}: $  {sale:,.2f}")
    
    minimum = min(flist)
    maximum = max(flist)
    total = sum(flist)
    average = total / len(flist)
    median = getMedian(flist)
    commission = total * 0.03
    print(f"Minimum:     $   {minimum:,.2f}")
    print(f"Maximum:     $   {maximum:,.2f}")
    print(f"Total:       $   {total:,.2f}")
    print(f"Average:     $   {average:,.2f}")
    print(f"Median:      $   {median:,.2f}")
    print(f"Commission:  $   {commission:,.2f}")


main()
