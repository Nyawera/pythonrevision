from os import remove


x = ['a','b',1 , 42 , True, False]
x.reverse()
print(x)

y = (10,20,30,40,50)
for number in y:print(number%3)

a = [150,250,350,450,550]
b = []
b= [ num//9 for num in a ]
print(b)


country_codes = {"kenya":254 , "Uganda":256, "Rwanda":250}
country_codes["Burundi"]=257
print(country_codes)

country_codes["Morocco"]=234
print(country_codes)

country_codes["somali"]=234
print(country_codes)

country_codes.pop("somali")
print(country_codes)
print((country_codes))