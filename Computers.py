import pandas as pd
df = pd.read_excel("grading.xlsx")
af = pd.read_excel("Computers.xlsx")
af["total"]= 0.4*((af['Computer Test 1']+af['Computer Test 2']+af['Computer Test 3'])/3)+0.6*af['Computer End Term']
df["Computer"]=af["total"]
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

print(df.head())
abc= pd.ExcelWriter('grading.xlsx')
df.to_excel(abc, 'new_sheet')
abc.save()


