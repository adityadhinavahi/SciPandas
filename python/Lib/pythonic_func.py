import pandas as pd
import ast

class dframe():
	def __init__(self,df):
		self.df = df
	def loc(self,col_string,df_name):
		df = self.df		
		f_s = col_string.replace(df_name,"df")
		return eval("df.loc["+f_s+"]")

	def iloc(self,i_string):
		df = self.df
		return eval("df.iloc["+i_string+"]")

	def groupby(self,g_str,agg_str=None):
		df = self.df
		if agg_str == None:
			return eval("df.groupby("+g_str+")")
		else:
			return eval("df.groupby("+g_str+")."+agg_str)
		
		#if cond == '==':
			#return df.loc[df[col] == cond_string]
		#elif cond == '!=':
			#return df.loc[df[col] != cond_string]
		#elif cond == '>':
			#return df.loc[df[col] > cond_string]
		#elif cond == '>=':
			#return df.loc[df[col] >= cond_string]
		#elif cond == '<=':
			#return df.loc[df[col] <= cond_string]
		#elif cond == '<':
			#return df.loc[df[col] < cond_string]
		#elif cond == None:
			#return df[col]


	
