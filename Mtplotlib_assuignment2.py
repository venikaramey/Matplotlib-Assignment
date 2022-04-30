import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic = pd.read_csv(url)
titanic.head()

males = titanic[titanic['sex']=='male'].index.value_counts().count()
print("male count is {}".format(males))
females =titanic[titanic['sex']=='female'].index.value_counts().count()
print("female count is {}".format(females))

list_1 = [males,females]
gender = ['male','female']
colors = ['b','y']
plt.pie(list_1,labels=gender,colors=colors,startangle=90,autopct='%.1f%%')
plt.show()

male = titanic[titanic['sex']=='male']
female = titanic[titanic['sex']=='female']
fig = plt.figure(figsize=(18,5))
plt.plot(male.fare, male.age, '.b', label='Male')
plt.plot(female.fare, female.age, '.r', label='Female')
plt.axis('equal')
plt.xlabel('Fare')
plt.ylabel('Age')
leg = plt.legend()

plt.show()