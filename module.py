def square_footage(length,width):
    area = length * width
    return area

length_of_house = float(input('What is the length of your house? '))
width_of_house = float(input('What is the width of your house? '))

result = square_footage(length_of_house, width_of_house)
print(f"the total square of your house is {result} foot")