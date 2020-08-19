import pandas as pd
import numpy as np

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

	def at(self,i_string):
		df = self.df
		return eval("df.at["+i_string+"]")

	def xs(self,i_string):
		df = self.df
		return eval("df.xs("+i_string+")")

	def sub(self,i_string):
		df = self.df
		return eval("df.sub("+i_string+")")

	def mul(self,obj,i_string=None):
		df = self.df
		if i_string is None:
			return df.mul(obj)
		return eval("df.mul(obj,"+i_string+")")

	def ewm(self,c_str,agg_str=None):
		df = self.df
		if agg_str is None:
			return eval("df.ewm("+c_str+")")
		return eval("df.ewm("+c_str+")."+agg_str)

	def replace(self,c_str):
		df = self.df
		return eval("df.replace("+c_str+")")

	def apply(self,c_str):
		df = self.df
		return eval("df.apply("+c_str+")")

	def applymap(self,c_str):
		df = self.df
		return eval("df.applymap("+c_str+")")

	def combine(self,df1,c_str):
		df = self.df
		return eval("df.combine(df1,"+c_str+")")

	def dropna(self,c_str=None):
		df = self.df
		if c_str is None:
			return df.dropna()
		return eval("df.dropna("+c_str+")")

	def fillna(self, c_str):
		df = self.df
		return eval("df.fillna("+c_str+")")

	def drop(self,c_str):
		df = self.df
		return eval("df.drop("+c_str+")")

	def drop_duplicates(self,c_str=None):
		df = self.df
		if c_str is None:
			return df.drop_duplicates()
		return eval("df.drop_duplicates("+c_str+")")

	def agg(self,c_str):
		df = self.df
		return eval("df.agg("+c_str+")")

	def groupby(self,g_str,agg_str=None):
		df = self.df
		if agg_str == None:
			return eval("df.groupby("+g_str+")")
		else:
			return eval("df.groupby("+g_str+")."+agg_str)

	def set_axis(self,c_str):
		df = self.df
		return eval("df.set_axis("+c_str+")")

	def set_index(self,c_str):
		df = self.df
		return eval("df.set_index("+c_str+")")

	def sort_values(self,c_str):
		df = self.df
		return eval("df.sort_values("+c_str+")")

	def sort_index(self,c_str):
		df = self.df
		return eval("df.sort_index("+c_str+")")

	def rank(self,c_str=None):
		df = self.df
		if c_str is None:
			return df.rank()
		return eval("df.rank("+c_str+")")

	def corr(self,c_str):
		df = self.df
		return eval("df.corr("+c_str+")")

	def corrwith(self,obj,c_str=None):
		df = self.df
		if c_str is None:
			return df.corrwith(obj)
		return eval("df.corrwith(obj,"+c_str+")")

	def join(self,obj,c_str=None):
		df = self.df
		if c_str is None:
			return df.join(obj)
		return eval("df.join(obj,"+c_str+")")

	def diff(self,c_str=None):
		df = self.df
		if c_str is None:
			return df.diff()
		return eval("df.diff("+c_str+")")

	def melt(self,m_str):
		df = self.df
		return eval("df.melt("+m_str+")")

	def pivot(self,p_str):
		df = self.df
		return eval("df.pivot"+p_str)

	def pivot_table(self,pt_str):
		df = self.df
		return eval("df.pivot_table("+pt_str+")")

	def merge(self,df_2,mg_str=None):
		df = self.df
		df2 = df_2
		if mg_str is None:
			return df.merge(df2)
		return eval("df.merge(df2,"+mg_str+")")
	
	def append(df1,c_str=None):
		df =self.df
		if c_str is None:
			return df.append(df1)
		return eval("df.append(df1,"+c_str+")")

	def evaluate(self,p_str,c_str=None):
		df = self.df
		if c_str is None:
			return df.eval(p_str)
		return eval("df.eval(p_str,"+c_str+")")



class pd_func():
	def __init__(self):
		pass

	def DataFrame(self,df_str):
		return eval("pd.DataFrame("+df_str+")")

	def Categorical(self,c_str):
		return eval("pd.Categorical("+c_str+")")

	def cut(self,c_str):
		return eval("pd.cut("+c_str+")")	

	
	def qcut(self,c_str):
		return eval("pd.qcut("+c_str+")")

	def merge_ordered(self,df1,df2,c_str=None):
		if c_str is None:
			return pd.merge_ordered(df1,df2)
		return eval("pd.merge_ordered(df1,df2,"+c_str+")")

	def merge_asof(self,df1,df2,c_str=None):
		if c_str is None:
			return pd.merge_ordered(df1,df2)
		return eval("pd.merge_asof(df1,df2,"+c_str+")")

	def series(self,c_str):
		return eval("pd.series("+c_str+")")

	def concat(self,s1,s2,c_str=None):
		if c_str is None:
			return pd.concat(s1,s2)
		return eval("pd.concat(s1,s2,"+c_str+")")

	def get_dummies(s,c_str=None):
		if c_str is None:
			return pd.get_dummies(s)
		return eval("pd.get_dummies(s,"+c_str+")")

	def factorize(self,c_str):
		return eval("pd.factorize("+c_str+")")

	def unique(self,c_str):
		return eval("pd.unique("+c_str+")")

	def unique_series(self,s):
		return pd.unique(s)

	def wide_to_long(self,df,c_str):
		return eval("pd.wide_to_long(df,"+c_str+")")

	def to_numeric(self,s,c_str=None):
		if c_str is None:
			return pd.to_numeric(s)
		return eval("pd.to_numeric(s,"+c_str+")")

	def to_datetime(self,df,c_str=None):
		#For now, we wont support list,tuples and 1-d array
		#int,float,series, or dataframe can be used
		if c_str is None:
			return pd.to_datetime(df)
		return eval("pd.to_datetime(df,"+c_str+")")

	def to_timedelta(self, df,c_str=None):
		if isinstance(df,str) == True:
			eval("a = "+df)
			if c_str is None:
				return pd.to_timedelta(a)
			return eval("pd.to_timedelta(a,"+c_str+")")
		if c_str is None:
			return pd.to_timedelta(df)
		return eval("pd.to_timedelta(df,"+c_str+")")

	def date_range(self,c_str):
		return eval("pd.date_range("+c_str+")")

	def bdate_range(self,c_str):
		return eval("pd.bdate_range("+c_str+")")

	def period_range(self,c_str):
		return eval("pd.period_range("+c_str+")")

	def timedelta_range(self,c_str):
		return eval("pd.timedelta_range("+c_str+")")

	def interval_range(self,c_str):
		return eval("pd.interval_range("+c_str+")")

