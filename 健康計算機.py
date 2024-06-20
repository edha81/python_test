#健康計算機

def print_bmi():
    w = float(input('請輸入體重(KG):'))
    h = float(input('請輸入身高(M):'))
    bmi = w/h**2
    print(f'你的BMI為:{bmi:.2f}')

def print_bmr():
    sex = int(input('請輸入性別:1(男)、2(女):'))
    w = float(input('請輸入體重(KG):'))
    h = float(input('請輸入身高(CM):'))
    age = int(input('請輸入年齡:'))
    if sex == 1 :
        bmr = 13.7 * w + 5.0 * h -6.8 * age +66
    elif sex == 2 :
        bmr = 9.6 * w + 1.8 * h -4.7 *age +655
    else:
        print('性別輸入有誤!')
    print(f'你的BMR為:{bmr:.2f}')
    return bmr

def print_tdee():
    bmr = print_bmr()

    activity_level = int(input('請輸入活動量:\n1.無活動\n2.輕量活動(每周運動1-3天)\n3.中度活動(每周活動3-5天)\n4.高度活動(每周活動6-7天)\n5.非常高度活動(無時無刻在運動、幾乎整天都在做高強度運動)\n'))
    if activity_level == 1:
        tdee = bmr * 1.2
    elif activity_level == 2:
        tdee = bmr * 1.375
    elif activity_level == 3: 
        tdee = bmr * 1.55
    elif activity_level == 4:
        tdee = bmr * 1.725
    elif activity_level == 5:
        tdee = bmr *1.9
    else:
        print('活動量請輸入1~5之間')
    print(tdee)

Pj = int(input('歡迎使用綜合健康計算機\n(1)計算BMI\n(2)計算基礎代謝率(BMR)\n(3)計算總熱號消耗(TDEE)\n請選擇要計算的項目'))
if Pj == 1:
    print_bmi()
elif Pj ==2:
    print_bmr()
elif Pj ==3:
    print_tdee()
else:
    print('請輸入介於1~3之間的正整數')
    