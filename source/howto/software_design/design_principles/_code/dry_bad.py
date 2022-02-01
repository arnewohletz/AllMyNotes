# This example has duplications

# Subject data = [weight_kg, height_m]
subject1 = [80, 1.62]
subject2 = [69, 1.53]
subject3 = [80, 1.66]
subject4 = [80, 1.79]
subject5 = [72, 1.60]

bmi_subject1 = int(subject1[0] / subject1[1]**2)
print("bmi {} = {}".format('subject1', bmi_subject1))

bmi_subject2 = int(subject2[0] / subject2[1]**2)
print("bmi {} = {}".format('subject2', bmi_subject2))

bmi_subject3 = int(subject3[0] / subject3[1]**2)
print("bmi {} = {}".format('subject3', bmi_subject3))

bmi_subject4 = int(subject4[0] / subject4[1]**2)
print("bmi {} = {}".format('subject4', bmi_subject4))

bmi_subject5 = int(subject5[0] / subject5[1]**2)
print("bmi {} = {}".format('subject5', bmi_subject5))
