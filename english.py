import pandas as pd
df = pd.read_excel("grading.xlsx")
af = pd.read_excel("English.xlsx")
af["total"]= 0.4*((af['English Test 1']+af['English Test 2']+af['English Test 3'])/3)+0.6*af['English End Term']
df["English Theory"]=af["total"]
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

print(df.head())
abc= pd.ExcelWriter('grading.xlsx')
df.to_excel(abc, 'new_sheet')
abc.save()


