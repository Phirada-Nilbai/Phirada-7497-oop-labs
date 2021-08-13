#Phirada Nilbai
#ID 633040749-7
patients = [[70, 1.80], [58, 1.55], [100, 1.90]]


def calculate_bmi(_weight, _height):
    return _weight / (_height **2)


for i,patient in enumerate(patients):
    weight, height = patient
    bmi = calculate_bmi(weight,height)
    print(f"Patient's BMI is: {bmi:0.02f}")
