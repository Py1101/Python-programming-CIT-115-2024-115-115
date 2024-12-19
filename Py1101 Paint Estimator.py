import math
#check for correct user input
def getFloatInput(prompt):
    while True:
        try:
            userinput = float(input(prompt))
            if userinput <= 0:
                print("Please enter a positive number.")
            else:
                return userinput 
        except ValueError:
            print("Please enter a positive number.")
# function parameters
def main():
    fSquareFeet = getFloatInput("Enter wall space in square feet: ")
    fGallonPrice = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGallon = getFloatInput("Enter feet per gallon: ")
    fLaborHoursPer = getFloatInput("How many labor hours per gallon: ")
    fLaborPerHour = getFloatInput("Labor charge per hour: ")
    strState = input("State job is in: ").upper()
    strUserName = input("Customer last name: ")
    taxrates = {"CT": 0.06, "MA": 0.0625, "ME": 0.085, "NH": 0.0, "RI": 0.07, "VT": 0.06} 
    if strState in taxrates:
        fSalesTax = taxrates[strState]
    else:
        fSalesTax = 0.0
#calculating...
    intgetGallonsofpaint = math.ceil(fSquareFeet / fFeetPerGallon)
    fLaborHours = intgetGallonsofpaint * fLaborHoursPer
    fPaintCharges = intgetGallonsofpaint * fGallonPrice
    fLaborCharges = fLaborHours * fLaborPerHour
    fTotaltaxamount = (fPaintCharges + fLaborCharges) * fSalesTax
    fTotalCost = fPaintCharges + fLaborCharges + fTotaltaxamount
    stroutputfile = f"{strUserName}_PaintJobOutput.txt"
    # Open output file and write to it
    with open(stroutputfile, "w") as file:
        file.write(f"Gallons of Paint: {intgetGallonsofpaint}\n")
        file.write(f"Hours of Labor: {fLaborHours:.2f}\n")
        file.write(f"Paint Charges: ${fPaintCharges:,.2f}\n")
        file.write(f"Labor Charges: ${fLaborCharges:,.2f}\n")
        file.write(f"Tax: ${fTotaltaxamount:.2f}\n")
        file.write(f"Total Cost: ${fTotalCost:,.2f}\n")
#printing output to screen       
    print(f"Gallons of Paint: {intgetGallonsofpaint}")
    print(f"Hours of Labor: {fLaborHours:.2f}")
    print(f"Paint Charges: ${fPaintCharges:,.2f}")
    print(f"Labor Charges: ${fLaborCharges:,.2f}")
    print(f"Tax: ${fTotaltaxamount:.2f}")
    print(f"Total Cost: ${fTotalCost:,.2f}")
    print(f"File: {stroutputfile} was created.")

main()

