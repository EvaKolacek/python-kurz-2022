import pandas
adopce_zvirat=pandas.read_csv("adopce-zvirat.txt",sep=";",index_col="nazev_cz")
#print(adopce_zvirat.head())
#print(adopce_zvirat.iloc[34,[1,2]])
print(adopce_zvirat.index.is_unique)
#adopce_zvirat.sort_index()
#print(adopce_zvirat.loc["Outloň váhavý"])
print(adopce_zvirat.sort_index().loc["Želva Smithova":"Želva žlutočelá"])
