bmi_height = float(input('输入身高：'))
bmi_weight = float(input('输入体重：'))

bmi_key = bmi_weight/(bmi_height*bmi_height)

if bmi_key < 18.5:
	print('too light！')
elif bmi_key < 25:
	print('normal')
elif bmi_key < 28:
	print('a little fat')
elif bmi_key <32:
	print('fat')
else:
	print('tooooo fat')
