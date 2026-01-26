'''
print("Hello Python!")

name = "Levente"
age = 30
height =182.5
is_learning_python = True

print(name)
print(age)
print(height)
print(is_learning_python)


a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print("My name is", name)
print("Next year I will be", age + 1)

daily_steps = 12000
training_hours = 1.5
calories = 1850

print("Daily steps:", daily_steps)
print("Training hours:", training_hours)
print("Daily calories eaten:", calories)
print("Calories per training hours:", round(calories / training_hours, 2))
'''

'''
x = 10
y = 2.5
name = "Python"
learning = True

print(x, type(x))
print(y, type(y))
print(name, type(name))
print(learning, type(learning))
'''

a = "10"
b = int(a)

print(a, type(a))
print(b, type(b))

int("5")
float("3.14")
str(100)

text = "Python"
print(len(text))

#indexing
print(text[0])
print(text[-1])

name = "Levente"

print(name.upper())
print(name.lower())
print(name.replace("e", "E"))

print("Lev" in name)

age = 30
print("I am", age, "years old.")

weight = "71.5"
height = "182"

weight_n = float(weight)
height_n = float(height)

BMI = weight_n / ((height_n/100)**2)

print(BMI, type(BMI))


