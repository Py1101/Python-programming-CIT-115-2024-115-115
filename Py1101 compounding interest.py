# setup for def main input
# fGoal accepting 0 without prompting stumped me for a bit
def promptforinput(sPrompt):
    fInput = 0
    while fInput <= 0:  
        try:
            fInput = float(input(sPrompt))
      
        except ValueError:
            print("input must be a positive numeric value")
    return fInput       
#getting user input
def main():
    fDeposit = promptforinput("What is the original deposit (Positive value):")
    fInterestrate = promptforinput("What is the Interest Rate (Positive Value) :")
    intMonths = int(promptforinput("What is the number of months (Positive Value) :"))
    fGoal = float(input("What is the Goal Amount (can enter 0 but not negative) :"))
#calculate interest payment  
    fltMonthlyInterestRate = fInterestrate / 12 /100
    FirstDeposit = fDeposit
#listing months and account balances  
    for Month in range (1, intMonths + 1):
        fInterest = FirstDeposit * fltMonthlyInterestRate
        FirstDeposit += fInterest
        print(f"Month: {Month} Account Balance is : $ {FirstDeposit:,.2f}")
#calculate how many months to reach goal w/goal amount
    if fGoal > 0:
        HowManyMonths = 0
        FirstDeposit = fDeposit
        while FirstDeposit  < fGoal:
            fInterest =FirstDeposit  * fltMonthlyInterestRate
            FirstDeposit += fInterest
            HowManyMonths += 1
        print(f"It will take: {HowManyMonths} months to reach the goal of $ {fGoal:,.2f}")
    

main() 
                  
