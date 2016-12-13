# -*- coding: utf-8 -*-

import pandas as pd

census_df = pd.read_csv('census.csv')

# question-5
# mostCounty_df = pd.DataFrame(census_df.groupby(['STNAME']).sum())
# mostCounty_df['COUNTY'].argmax()

# question-6
mask = census_df['SUMLEV'].isin([40])
df = pd.DataFrame(census_df[~mask]);
df_sorted = df.sort_values("CENSUS2010POP", ascending=False);
unique_stname = df_sorted.STNAME.unique();
result_dict = dict();
for i in range(0,len(unique_stname)):
	stname = unique_stname[i];
	count = 0;
	maxPop = 0;
	for index, row in df_sorted.iterrows():
		if(row['STNAME'] == stname):
			maxPop = maxPop + float(row['CENSUS2010POP']);
			count = count + 1;
			if(count > 2):
				break;
	result_dict[stname]= maxPop;			
stList = sorted(result_dict,key=result_dict.__getitem__, reverse=True);
print(stList[0:3])


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

# fin = list();
# fin = ["POPESTIMATE2010", "POPESTIMATE2011", "POPESTIMATE2012", "POPESTIMATE2013", "POPESTIMATE2014", "POPESTIMATE2015"]	
# maxDiffList = list();
# for index, row in census_df.iterrows():
# 	max = 0;
# 	for i in range(0, len(fin)):
# 		comp = float(row[fin[i]]);
# 		for j in range(0, len(fin)):
# 			if(abs(comp-float(row[fin[j]])) > max):
# 				max = abs(comp-row[fin[j]])
# 	maxDiffList.append(max);
# census_df['maxDiff'] = maxDiffList;
# countyName = census_df.groupby(['CTYNAME']).sum().sort_values("maxDiff", ascending=False);
# print(countyName["maxDiff"].argmax())


# question-8
# Washington


# df_filtered = census_df[(census_df['CTYNAME'].str.startswith('Washington')) & 
# (census_df['POPESTIMATE2015'] > census_df['POPESTIMATE2014']) & 
# (census_df['REGION'] != 3) & (census_df['REGION'] != 4)]

# df_result = df_filtered[['STNAME','CTYNAME']]

# print(df_result)
# print(len(df_filtered))