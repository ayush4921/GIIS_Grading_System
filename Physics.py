import pandas as pd
df = pd.read_excel("grading.xlsx")
af = pd.read_excel("Physics.xlsx")
af["total"]= 0.4*((af['Physics Test 1']+af['Physics Test 2']+af['Physics Test 3'])/3)+0.6*af['Physics End Term']
df["Physics"]=af["total"]
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

print(df.head())
abc= pd.ExcelWriter('grading.xlsx')
df.to_excel(abc, 'new_sheet')
abc.save()


