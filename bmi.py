

# FUNCTIONS
def get_height_inp():
    inp = input("Enter height as feet, inches: ")
    return inp

def split_inp(inp):
    inp1, inp2 = inp.split(", ")
    return inp1, inp2

def calc_height_in_inches(feet, inches):
    feet = int(feet)
    inches = int(inches)
    return (feet * 12) + inches

def calc_height_in_meters(inches):
    return inches * 0.0254

def get_weight_inp():
    inp = input("Enter weight in lbs: ")
    return inp

def calc_weight_in_kg(weight):
    weight = int(weight)
    return weight * 0.453592

def calculate_bmi(height, weight):
    height_squared = height ** 2
    return weight / height_squared

def find_bmi_label(bmi):
    if bmi < 18.5:
        return 'Underweight'
    if bmi > 18.5 and bmi < 24.9:
        return 'Normal weight'
    if bmi > 25 and bmi < 29.9:
        return 'Overweight'
    if bmi >= 30:
        return 'Obese'

# MAIN
if __name__ == '__main__':
    height = get_height_inp()
    feet, inches = split_inp(height)
    height = calc_height_in_inches(feet, inches)
    height = calc_height_in_meters(height)
    weight = get_weight_inp()
    weight = calc_weight_in_kg(weight)
    bmi = calculate_bmi(height, weight)
    print(bmi)
    print(find_bmi_label(bmi))