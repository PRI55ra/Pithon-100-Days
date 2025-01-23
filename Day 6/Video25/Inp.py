countries=("Spin","India","Pakisthan")
print(countries)
temp=list(countries)
temp.append("Bangladesh")
temp[2]="Island"
countries=tuple(temp)
print (countries)