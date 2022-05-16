import pandas

teplota=pandas.read_csv("temperature.csv")

#print(teplota.head())

teplotaPraha=(teplota[teplota["City"]=="Prague"])
teplotaVyssi80=(teplota[teplota["AvgTemperature"]>80])
teplotaVyssi60=teplota["AvgTemperature"]>60
teplotaEvropa=teplota["Region"]=="Europe"
teplotaEvropaVyssi60=teplota[teplotaVyssi60&teplotaEvropa]
extremniHodnoty = teplota[(teplota["AvgTemperature"]>80)|(teplota["AvgTemperature"]<(-20))]

print(extremniHodnoty)
