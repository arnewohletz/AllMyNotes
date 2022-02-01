def bmi_calc(sub_num, weight_kg, height_m):
    """Calculate BMI from weight in kg and height in meters"""
    bmi = int(weight_kg / height_m**2)
    subject = 'subject' + str(sub_num)
    print("bmi {} = {}".format(subject, bmi))

# Subject data = [weight_kg, height_m]
subjects =[[1, 80, 1.62], # subject1
           [2, 69, 1.53], # subject2
           [3, 80, 1.66], # subject3
           [4, 80, 1.79], # subject4
           [5, 72, 1.60]] # subject5

for sub in subjects:
    bmi_calc(sub[0], sub[1], sub[2])
