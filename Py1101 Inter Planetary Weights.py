# named constants
nMERCURY = 0.38
nVENUS = 0.91
nMOON = 0.165
nMARS = 0.38
nJUPITER = 2.34
nSATURN = 0.93
nURANUS = 0.92
nNEPTUNE = 1.12
nPLUTO = 0.066
#prompt user for name and weight
sname = input("What is your name ?")
fweight = float(input("Please enter your weight in lbs :"))
# output with calculation
print(f"{sname}, this is how much you weigh on our solar system's planets :")
print("Weight on Mercury:           " +format(fweight*nMERCURY, '10.2f'))
print("Weight on Venus:             " +format(fweight*nVENUS, '10.2f'))
print("Weight on our Moon:          " +format(fweight*nMOON, '10.2f'))
print("Weight on Mars:              " +format(fweight*nMARS, '10.2f'))
print("Weight on Jupiter:           " +format(fweight*nJUPITER, '10.2f'))
print("weight on Saturn:            " +format(fweight*nSATURN, '10.2f'))
print("Weight on Uranus:            " +format(fweight*nURANUS, '10.2f'))
print("Weight on Neptune:           " +format(fweight*nNEPTUNE, '10.2f'))
print("Weight on Pluto:             " +format(fweight*nPLUTO, '10.2f'))

    
