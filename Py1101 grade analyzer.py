#added to stop exit program prompt after exit
import sys
#prompt user for name and test grades
#hoping i remembered to cover all of the parameters given
strName = str(input("Name of person that we are calculating the grades for:"))
intTest1 = int(input("Test 1:"))
intTest2 = int(input("Test 2:"))
intTest3 = int(input("Test 3:"))
intTest4 = int(input("Test 4:"))
#make sure test grades above 0
if intTest1 <= 0 or intTest2 <= 0 or intTest3 <= 0 or intTest4 <= 0:
    print("The test scores must be greater than 0")
    sys.exit()    
#check to see if user wants to drop low score    
strDropscore = str(input("Do you want to drop the lowest grade Y or N?"))   
if strDropscore not in ["Y","y","N","n"]:
    print("Enter Y or N to drop the lowest grade.")
    sys.exit()
#finding lowest score
intLowestgrade = intTest1
if intTest2 < intLowestgrade:
    intLowestgrade = intTest2
if intTest3 < intLowestgrade:
    intLowestgrade = intTest3
if intTest4 < intLowestgrade:
    intLowestgrade = intTest4
#calculate average according to user input    
if strDropscore == "y":
    intAverage = (intTest1 + intTest2 + intTest3 + intTest4 - intLowestgrade)/3
    print(f"{strName} test average is: {intAverage:.1f}")
else:
    strDropscore == "N"
    intAverage = (intTest1 + intTest2 + intTest3 + intTest4)/4
    print(f"{strName} test average is: {intAverage:.1f}")
#finding letter grade 
if intAverage >= 97.0 :
    strLettergrade ="A+"
elif intAverage >= 94.0:
    strLettergrade ="A"  
elif intAverage >= 90.0:
    strLettergrade ="A-"   
elif intAverage >= 87.0:
    strLettergrade ="B+"
elif intAverage >= 84.0:
    strLettergrade ="B"     
elif intAverage >= 80.0:
    strLettergrade ="B-"   
elif intAverage >= 7.0:
    strLettergrade ="C+"    
elif intAverage >= 74.0:
    strLettergrade ="C"
elif intAverage >= 70.0:
    strLettergrade ="C-"     
elif intAverage >= 67.0:
    strLettergrade ="D+"   
elif intAverage >= 64.0:
    strLettergrade ="D"    
elif intAverage >= 60.0:
    strLettergrade ="D-"
else:
    intAverage <=59.9
    strLettergrade ="F"     
print (f"Your letter grade for the test is: {strLettergrade}")  

    
    

