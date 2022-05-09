import pandas
adopce_zvirat=pandas.read_csv("adopce-zvirat.txt",sep=";",index_col="nazev_cz")
#print(adopce_zvirat.head())
#print(adopce_zvirat.iloc[34,[1,2]])
print(adopce_zvirat.index.is_unique)
#print(adopce_zvirat.sort_index())
#print(adopce_zvirat.loc["Outloň váhavý"])
print(adopce_zvirat.loc["Želva Smithova":"Želva žlutočelá"])
#True
#Empty DataFrame
#Columns: [id, nazev_en, trida_cz, cena, k_prohlidce]
#Index: []