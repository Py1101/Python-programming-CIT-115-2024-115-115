print("chris' Temp Converter:")
print()
# prompt user for temp and scale
fTemp = float(input("Enter a temperature:"))         
sScale = str(input("Is the temp F for Fahrenheit or C for Celsius?"))
# making sure sScale is f or c or at least variant of
if sScale not in ["f" , "F",  "c" , "C"]:
    print(" You must enter a F or C")
# calculations and output according to user input  
elif sScale == "f" or sScale == "F":
    if fTemp > 212:
        print("Temp can not be >212")
    else :
        fCelsius = (5.0 / 9) * (fTemp - 32)
        print(f" Your Celsius equivalent is : {fCelsius:.1f}")
elif sScale == "c" or sScale== "C":
    if fTemp > 100:
        print("Temp can not be > 100")
    else :
        fFahrenheit = ((9.0 / 5.0)* fTemp) + 32
        print(f"The Fahrenheit Equivalent is : {fFahrenheit:.1f}")
    
