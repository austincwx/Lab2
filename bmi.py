
def calculate_bmi(height, weight):
    bmi = str(weight / (height ** 2))


    print("Height = " + str(height))
    print("Weight = " + str(weight))
    print("Your bmi is: " + bmi)

    if bmi <str(18.5):
        num=-1
        return(num)
    elif str(18.5)<=bmi<=str(25):
        num=0
        return(num)
    elif bmi>str(25):
        num=1
        return(num)


calculate_bmi(height=1.73, weight=57.0)








