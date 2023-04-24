def calculate_bmi(height, weight):

    bmi = str(weight / (height * height))

    print("Height = " + str(height))
    print("Weight = " + str(weight))
    print("Your bmi is: " + bmi)

calculate_bmi(height = 1.73, weight = 57.0)
def calculate_bmi(height, weight):
    bmi = str(weight / (height ** 2))


    print("Height = " + str(height))
    print("Weight = " + str(weight))
    print("Your bmi is: " + bmi)

    if bmi <str(18.5):
        print("You are overweight")
    elif str(18.5)<=bmi<=str(25):
        print("You are normal weight")
    elif bmi>str(25):
        print("You are under weight")


calculate_bmi(height=1.73, weight=57.0)








