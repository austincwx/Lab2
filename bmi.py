
def calculate_bmi(height, weight):
    bmi = str(weight / (height ** 2))


    print("Height = " + str(height))
    print("Weight = " + str(weight))
    print("Your bmi is: " + bmi)

    if bmi <str(18.5):
        num1=-1
        return(num1)
    elif str(18.5)<=bmi<=str(25):
        num2=0
        return(num2)
    elif bmi>str(25):
        num3=1
        return(num3)


calculate_bmi(height=1.73, weight=57.0)








