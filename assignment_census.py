# -*- coding: utf-8 -*-

import pandas as pd

census_df = pd.read_csv('census.csv')

# question-5
# mostCounty_df = pd.DataFrame(census_df.groupby(['STNAME']).sum())
# mostCounty_df['COUNTY'].argmax()

# question-6
# mostPopulous_df = census_df.groupby(['STNAME']).sum().sort_values("CENSUS2010POP", ascending=False).head(3)
# print(mostPopulous_df.index.values) 

# question-7
# def getMaxDifferenceForEachRow(row):
# 	fin = list();
# 	fin = ["POPESTIMATE2010", "POPESTIMATE2011", "POPESTIMATE2012", "POPESTIMATE2013", "POPESTIMATE2014", "POPESTIMATE2015"]	
# 	max = 0.0;
# 	for i in range(0, len(fin)):
# 		comp = float(row[fin[i]]);
# 		for j in range(0, len(fin)):
# 			if(abs(comp-float(row[fin[j]])) > max):

# 				max = abs(comp-row[fin[j]])
# 	return max;

# maxDiffList = list();
# for index, row in census_df.iterrows():
# 	maxDiff= getMaxDifferenceForEachRow(row)
# 	maxDiffList.append(maxDiff);
# census_df['maxDiff'] = maxDiffList;
# countyName = census_df.groupby(['CTYNAME']).sum().sort_values("maxDiff", ascending=False);
# print(countyName["maxDiff"].argmax())




# def getMaxDifferenceForEachRow(row):
# 	fin = list();
# 	fin = ["POPESTIMATE2010", "POPESTIMATE2011", "POPESTIMATE2012", "POPESTIMATE2013", "POPESTIMATE2014", "POPESTIMATE2015"]	
# 	max = 0.0;
# 	for i in range(0, len(fin)):
# 		comp = float(row[fin[i]]);
# 		for j in range(0, len(fin)):
# 			if(abs(comp-float(row[fin[j]])) > max):

# 				max = abs(comp-row[fin[j]])
# 	return max;

fin = list();
fin = ["POPESTIMATE2010", "POPESTIMATE2011", "POPESTIMATE2012", "POPESTIMATE2013", "POPESTIMATE2014", "POPESTIMATE2015"]	
maxDiffList = list();
for index, row in census_df.iterrows():
	max = 0;
	for i in range(0, len(fin)):
		comp = float(row[fin[i]]);
		for j in range(0, len(fin)):
			if(abs(comp-float(row[fin[j]])) > max):
				max = abs(comp-row[fin[j]])
	maxDiffList.append(max);
census_df['maxDiff'] = maxDiffList;
countyName = census_df.groupby(['CTYNAME']).sum().sort_values("maxDiff", ascending=False);
print(countyName["maxDiff"].argmax())


# question-8
# Washington


# df_filtered = census_df[(census_df['CTYNAME'].str.startswith('Washington')) & 
# (census_df['POPESTIMATE2015'] > census_df['POPESTIMATE2014']) & 
# (census_df['REGION'] != 3) & (census_df['REGION'] != 4)]

# df_result = df_filtered[['STNAME','CTYNAME']]

# print(df_result)
# print(len(df_filtered))