# -*- coding: utf-8 -*-
import pandas as pd
# Country, Energy Supply, Energy Supply per Capita,% Renewable

energy = pd.read_excel("Energy Indicators.xls", skiprows=17, skip_footer=38)
energy = energy.drop('Unnamed: 0',1)
energy = energy.drop('Unnamed: 2',1)
energy = energy.replace("...", "NaN")
energy.columns = ["Country", "Energy Supply","Energy Supply per Capita","%"+" Renewable"]
energy.loc[energy['Energy Supply']!="NaN", 'Energy Supply'] = energy['Energy Supply']*1000000
energy = energy.replace("Republic of Korea", "South Korea")
energy = energy.replace("United States of America", "United States")
energy = energy.replace("United Kingdom of Great Britain and Northern Ireland", "United Kingdom")	
energy = energy.replace("China, Hong Kong Special Administrative Region", "Hong Kong")	
energy = energy.replace("Bolivia (Plurinational State of)", "Bolivia")	
energy = energy.replace("Iran (Islamic Republic of)", "Iran")	
energy = energy.replace("Micronesia (Federated States of)", "Micronesia")	
energy = energy.replace("Venezuela (Bolivarian Republic of)", "Venezuela")	
energy = energy.replace("Falkland Islands (Malvinas)", "Malvinas")
energy = energy.replace("Lao People's Democratic Republic", "Laos")	
energy = energy.replace("The former Yugoslav Republic of Macedonia", "Macedonia")	
energy = energy.replace("United Republic of Tanzania", "Tanzania")
energy = energy.replace("Switzerland17", "Switzerland")	

# print(energy['Country'])

GDP = pd.read_csv("world_bank.csv", skiprows=4)
GDP = GDP.replace("Korea, Rep.", "South Korea")
GDP = GDP.replace("Iran, Islamic Rep.", "Iran")
GDP = GDP.replace("Hong Kong SAR, China", "Hong Kong")
GDP = GDP.replace("Congo, Dem. Rep.", "Congo")
GDP = GDP.replace("Venezuela, RB", "Venezuela")
GDP = GDP.replace("Egypt, Arab Rep.", "Egypt")
GDP = GDP.replace("Gambia, The", "Gambia")
GDP = GDP.replace("Kyrgyz Republic", "Kyrgyzstan")
GDP = GDP.replace("Lao PDR", "Laos")




GDP.drop(GDP.columns[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,
	35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]], axis=1, inplace=True)
GDP = GDP.set_index(['Country Name']);

ScimEn = pd.read_excel("scimagojr-3.xlsx")

newDf1 = ScimEn.merge(energy, on="Country").set_index(['Country'])
los1 = (len(energy) - len(newDf1)) + (len(ScimEn) - len(newDf1));

newDf2 = newDf1.merge(GDP, left_index=True, right_index=True)
los2 = (len(GDP) - len(newDf2)) + (len(newDf1) - len(newDf2))

# newDf = newDf[(newDf['Rank'] >= 1) & ((newDf['Rank'] <= 15))]
# print(GDP_energy.head())

print(newDf2.index.values)


