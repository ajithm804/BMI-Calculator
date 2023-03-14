#Inputting the height and weight values
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#Converting height and weight values into float and string
weight_in_float= int(weight)
height_in_float= float(height)
#Calculating BMI by dividing weight by height and multiplying the number with 2
BMI=  weight_in_float/height_in_float ** 2
#Converting the BMI value into integer
BMI_in_float=int(BMI)
#printing the value of calculated BMI
print(BMI_in_float)
