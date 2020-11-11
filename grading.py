import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image 


df = pd.read_excel("grading.xlsx")

df['Total Maths']= df['Mathematics']+df['Math Project']
df['Total English']=df['English Theory']+df['Language Lab']
df['Total Physics']=df['Physics']+df['Physics Lab']
df['Total Chemistry']=df['Chemistry']+df['Chemistry Lab']
df['Total Computers']=df['Computer']+df['Computer Lab']

df['Average marks']= (df['Total Maths']+df['Total English']+df['Total Physics']+df['Total Chemistry']+df['Total Computers'])/5

def thegrade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else : return "E"

df['Grade'] = df['Average marks'].apply(thegrade)

df = df.sort_values(by=['Average marks'], ascending=False)
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
abcd=len(df)
a_list = list(range(1, abcd+1))
df['Rank']=a_list
df = df[['Rank','Names','Total Maths','Total Physics','Total Chemistry','Total English','Total Computers','Average marks','Grade']]

abc= pd.ExcelWriter('final_report.xlsx')
df.to_excel(abc, 'new_sheet')
abc.save()
averagemarksofclass = df['Average marks'].to_list()
averagemarksofclass2 = df['Total Maths'].to_list()
averagemarksofclass3 = df['Total English'].to_list()
averagemarksofclass4 = df['Total Physics'].to_list()
averagemarksofclass5 = df['Total Chemistry'].to_list()
averagemarksofclass6 = df['Total Computers'].to_list()

averagemarksofclass11 = int(sum(averagemarksofclass)/len(averagemarksofclass))
averagemarksofclass22 = int(sum(averagemarksofclass2)/len(averagemarksofclass2))
averagemarksofclass33 = int(sum(averagemarksofclass3)/len(averagemarksofclass3))
averagemarksofclass44 = int(sum(averagemarksofclass4)/len(averagemarksofclass4))
averagemarksofclass55 = int(sum(averagemarksofclass5)/len(averagemarksofclass5))
averagemarksofclass66 = int(sum(averagemarksofclass6)/len(averagemarksofclass6))


topper = df['Names'].to_list()
print("GIIS AUTO GRADING SYSTEM DEVELOPED BY AYUSH GARG")
print("\n")

print("The Class topper is",topper[0])
print("\n")

print("The average marks of class is",averagemarksofclass11)
print("The average marks of class in Mathematics is",averagemarksofclass22)
print("The average marks of class in English is",averagemarksofclass33)
print("The average marks of class in Physics is",averagemarksofclass44)
print("The average marks of class in Chemistry is",averagemarksofclass55)
print("The average marks of class in Computers is",averagemarksofclass66)
print("\n")

print("Combined result has been created at final_report.xlsx")

df.plot.bar(x='Names', y='Average marks', rot=0)
plt.ylim(70, 95)
plt.xticks(rotation=50)
plt.savefig('Analysis_Overall.png')

df.plot.bar(x='Names', y='Total Maths', rot=0)
plt.ylim(70, 95)
plt.xticks(rotation=50)
plt.savefig('Analysis_Maths.png')

df.plot.bar(x='Names', y='Total English', rot=0)
plt.ylim(70, 95)
plt.xticks(rotation=50)
plt.savefig('Analysis_English.png')

df.plot.bar(x='Names', y='Total Physics', rot=0)
plt.ylim(70, 95)
plt.xticks(rotation=50)
plt.savefig('Analysis_Physics.png')

df.plot.bar(x='Names', y='Total Chemistry', rot=0)
plt.ylim(70, 95)
plt.xticks(rotation=50)
plt.savefig('Analysis_Chemistry.png')

df.plot.bar(x='Names', y='Total Computers', rot=0)
plt.ylim(70, 95)
plt.xticks(rotation=50)
plt.savefig('Analysis_Computers.png')

im = Image.open(r"New Project.jpg")  
im.show()



