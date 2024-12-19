#prompt for user input
nPrincipal =float(input("Enter the starting principal: "))
nInterest =float(input("Enter the annual interest rate: "))
nCompound =float(input("How many times per year is the interest compounded? "))
nYears =int(input("For how many years will the account earn interest? "))
#convert interest rate to decimal
nStatedrate = nInterest/100
#calculate
nAnswer = nPrincipal *(nStatedrate/nCompound+1)**(nCompound*nYears)
#output
print(f"At the end of {nYears} years you will have $ {nAnswer:,.2f}")
