import pandas as pd
df = pd.read_excel("grading.xlsx")
af = pd.read_excel("Chemistry.xlsx")
af["total"]= 0.4*((af['Chemistry Test 1']+af['Chemistry Test 2']+af['Chemistry Test 3'])/3)+0.6*af['Chemistry End Term']
df["Chemistry"]=af["total"]
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

print(df.head())
abc= pd.ExcelWriter('grading.xlsx')
df.to_excel(abc, 'new_sheet')
abc.save()


