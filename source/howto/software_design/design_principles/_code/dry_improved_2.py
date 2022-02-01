def bmi_calc(sub_num, weight_kg, height_m):
    """Calculate BMI from weight in kg and height in meters"""
    bmi = int(weight_kg / height_m**2)
    subject = 'subject' + str(sub_num)
    print("bmi {} = {}".format(subject, bmi))

# Subject data = [weight_kg, height_m]
subject1 = [80, 1.62]
subject2 = [69, 1.53]
subject3 = [80, 1.66]
subject4 = [80, 1.79]
subject5 = [72, 1.60]

bmi_subject1 = bmi_calc(1, subject1[0], subject1[1])
bmi_subject2 = bmi_calc(2, subject2[0], subject2[1])
bmi_subject3 = bmi_calc(3, subject3[0], subject3[1])
bmi_subject4 = bmi_calc(4, subject4[0], subject4[1])
bmi_subject5 = bmi_calc(5, subject5[0], subject5[1])
