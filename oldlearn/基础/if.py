height = input('Please tell me your height: ')
weight = input('please tell me your weight: ')
height = float(height)
weight = float(weight)
bmi = weight / (height * height)
print(bmi)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
elif bmi > 32:
    print('严重肥胖')
