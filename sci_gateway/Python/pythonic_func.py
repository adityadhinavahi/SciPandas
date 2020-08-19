#Three classes single wrapper approach
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Class 1: Pandas module functions
class Pandas():
    def __init__(self):
        self.data = pd

    def get_func(self):
        return dir(Pandas)
    
    def read_csv(self,file,kwargs=None):
        if kwargs == None:
            df = self.data.read_csv(file)
            return DataFrame(df)
        else:
            df = eval("self.data.read_csv(file,"+kwargs+")")
            return DataFrame(df)
    
    def read_pickle(self,file,kwargs=None):
        if kwargs == None:
            df = self.data.read_pickle(file)
            return DataFrame(df)
        else:
            df = eval("self.data.read_pickle(file,"+kwargs+")")
            return DataFrame(df)
        
    def read_table(self,file,kwargs=None):
        if kwargs == None:
            df = self.data.read_table(file)
            return DataFrame(df)
        else:
            df = eval("self.data.read_pickle(file,"+kwargs+")")
            return DataFrame(df)
    
    def read_fwf(self,file,kwargs=None):
        if kwargs == None:
            df = self.data.read_fwf(file)
            return DataFrame(df)
        else:
            df = eval("self.data.read_fwf(file,"+kwargs+")")
            return DataFrame(df)
    
    def read_excel(self,file,kwargs=None):
        if kwargs == None:
            df = self.data.read_excel(file)
            return DataFrame(df)
        else:
            df = eval("self.data.read_excel(file,"+kwargs+")")
            return DataFrame(df)
        
    def read_json(self,file,kwargs=None):
        if kwargs == None:
            df = self.data.read_json(file)
            return DataFrame(df)
        else:
            df = eval("self.data.read_json(file,"+kwargs+")")
            return DataFrame(df)
        
    def read_parquet(self,file,kwargs=None):
        if kwargs == None:
            df = self.data.read_parquet(file)
            return DataFrame(df)
        else:
            df = eval("self.data.read_parquet(file,"+kwargs+")")
            return DataFrame(df)
    
    def read_orc(self,file,kwargs=None):
        if kwargs == None:
            df = self.data.read_orc(file)
            return DataFrame(df)
        else:
            df = eval("self.data.read_orc(file,"+kwargs+")")
            return DataFrame(df)
    
    def read_sas(self,file,kwargs=None):
        if kwargs == None:
            df = self.data.read_sas(file)
            return DataFrame(df)
        else:
            df = eval("self.data.read_sas(file,"+kwargs+")")
            return DataFrame(df)
    
    def read_spss(self,file,kwargs=None):
        if kwargs == None:
            df = self.data.read_spss(file)
            return DataFrame(df)
        else:
            df = eval("self.data.read_spss(file,"+kwargs+")")
            return DataFrame(df)
    
    def read_sql_table(self,table_name,con,kwargs=None):
        if kwargs == None:
            df = self.data.read_sql_table(table_name,con)
            return DataFrame(df)
        else:
            df = eval("self.data.read_sql_table(table_name,con,"+kwargs+")")
            return DataFrame(df)
        
    def read_sql_query(self,sql_q,con,kwargs=None):
        if kwargs == None:
            df = self.data.read_sql_query(sql_q,con)
            return DataFrame(df)
        else:
            df = eval("self.data.read_sql_query(sql_q,con,"+kwargs+")")
            return DataFrame(df)
    
    def read_sql(self,sql,con,kwargs=None):
        if kwargs == None:
            df = self.data.read_sql(sql,con)
            return DataFrame(df)
        else:
            df = eval("self.data.read_sql(sql,con,"+kwargs+")")
            return DataFrame(df)
    
    def read_stata(self,file,kwargs=None):
        if kwargs == None:
            df = self.data.read_stata(file)
            return DataFrame(df)
        else:
            df = eval("self.data.read_stata(file,"+kwargs+")")
            return DataFrame(df)
    
    def DataFrame(self,df_str):
        df = eval("pd.DataFrame("+df_str+")")
        return DataFrame(df)
    
    def Categorical(self,c_str):
        df = eval("pd.Categorical("+c_str+")")
        return DataFrame(df)
    def cut(self,c_str):
        #To be decided later
        return eval("pd.cut("+c_str+")")

    def qcut(self,c_str):
        #To be decided later
        return eval("pd.qcut("+c_str+")")

    def merge_ordered(self,df1,df2,c_str=None):
        if c_str is None:
            df = pd.merge_ordered(df1,df2)
            return DataFrame(df)
        else:
            df = eval("pd.merge_ordered(df1,df2,"+c_str+")")
            return DataFrame(df)
        
    def merge_asof(self,df1,df2,c_str=None):
        if c_str is None:
            df = pd.merge_asof(df1,df2)
            return DataFrame(df)
        else:
            df = eval("pd.merge_asof(df1,df2,"+c_str+")")
            return DataFrame(df)
        
    def Series(self,c_str):
        ser = eval("pd.Series("+c_str+")")
        return Series(ser)

    def concat(self,s1,s2,c_str=None):
        if c_str is None:
            out = pd.concat(s1,s2)
        else:
            out =  eval("pd.concat(s1,s2,"+c_str+")")
        if isinstance(out,pd.Series) == True:
            return Series(out)
        else:
            return DataFrame(out)
        
    def get_dummies(s,c_str=None):
        if c_str is None:
            df = pd.get_dummies(s)
            return DataFrame(df)
        else:
            df = eval("pd.get_dummies(s,"+c_str+")")
            return DataFrame(df)

    def factorize(self,c_str):
        #To be decided later
        return eval("pd.factorize("+c_str+")")

    def unique(self,c_str):
        #To be decided later
        return eval("pd.unique("+c_str+")")

    def unique_series(self,s):
        #To be decided later
        return pd.unique(s)

    def wide_to_long(self,df,c_str):
        df = eval("pd.wide_to_long(df,"+c_str+")")
        return DataFrame(df)
    
    def to_numeric(self,s,c_str=None):
        #To be decided later
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

#Class 2: DataFrame module functions
class DataFrame():


    def __init__(self,df):
        if isinstance(df,pd.DataFrame):
            self.data = df
            self.index = self.data.index
            self.dtypes = Series(self.data.dtypes)
            self.values = self.data.values
            self.columns = Index(self.data.columns)
            self.axes = self.data.axes
            self.ndim = self.data.ndim
            self.size = self.data.size
            self.shape = self.data.shape
            self.empty = self.data.empty
            self.index = self.data.index
            
    def get_func(self):
        return dir(DataFrame)


    def select_dtypes(self,kwargs=None):
        if kwargs is None:
            return DataFrame(self.data.select_dtypes())
        else:
            return DataFrame(eval("self.data.select_dtypes("+kwargs+")"))


    def memory_usage(self,kwargs=None):
        if kwargs==None:
            return Series(self.data.memory_usage())
        else:
            out = eval("self.data.memory_usage("+kwargs+")")
            return Series(out)
    
    def astype(self,c_str,kwargs=None):
        if kwargs == None:
            out = self.data.astype(c_str)

        else:
            out = eval("self.data.astype(c_str,"+kwargs+")")
        if isinstance(out,pd.DataFrame):
            return DataFrame(out)
        elif isinstance(out,pd.Series):
            return Series(out)
        else:
            return out
    
    def convert_dtypes(self,kwargs=None):
        if kwargs == None:
            out = self.data.convert_dtypes()
        else:
            out = eval("self.data.convert_dtypes("+kwargs+")")
        if isinstance(out,pd.DataFrame):
            return DataFrame(out)
        else:
            return Series(out)
    
    def infer_objects(self):
        return self.data.infer_objects()
    
    def copy(self,kwargs=None):
        if kwargs == None:
            return DataFrame(self.data.copy())
        
        else:
            out = eval("self.data.copy("+kwargs+")")
            return DataFrame(out)
    def isna(self):
        return DataFrame(self.data.isna())
    
    def notna(self):
        return DataFrame(self.data.notna())
    
    def bool(self):
        return self.data.bool()
    
    def loc(self,col_string,df_name):
        df = self.data
        f_s = col_string.replace(df_name,"df")
        out = eval("df.loc["+f_s+"]")
        if isinstance(out,pd.DataFrame):
            return DataFrame(out)
        elif isinstance(out,pd.Series):
            return Series(out)
        else:
            return out
        

    def iloc(self,i_string):
        df = self.data
        out = eval("df.iloc["+i_string+"]")
        if isinstance(out,pd.DataFrame):
            return DataFrame(out)
        elif isinstance(out,pd.Series):
            return Series(out)
        else:
            return out

    def at(self,i_string):
        df = self.data
        return eval("df.at["+i_string+"]")

    def iat(self,i_string):
        df = self.data
        return eval("df.iat["+i_string+"]")

    def xs(self,i_string):
        df = self.data
        out = eval("df.xs("+i_string+")")
        if isinstance(out,pd.DataFrame):
            return DataFrame(out)
        elif isinstance(out,pd.Series):
            return Series(out)        

    def sub(self,obj,i_string=None):
        df = self.data
        if isinstance(obj,DataFrame) == True or isinstance(obj,Series) == True:
            obj = obj.data
        else:
            obj = obj
        if i_string == None:
            return DataFrame(df.sub(obj))
        else:
            return DataFrame(eval("df.sub(obj,"+i_string+")"))

    def mul(self,obj,i_string=None):
        df = self.data
        if isinstance(obj,DataFrame) == True or isinstance(obj,Series) == True:
            obj = obj.data
        else:
            obj = obj
        if i_string is None:
            return DataFrame(df.mul(obj))
        return DataFrame(eval("df.mul(obj,"+i_string+")"))

    def ewm(self,c_str,agg_str=None):
        df = self.data
        if agg_str is None:
            return DataFrame(eval("df.ewm("+c_str+")"))
        return DataFrame(eval("df.ewm("+c_str+")."+agg_str))

    def replace(self,c_str):
        df = self.data
        return DataFrame(eval("df.replace("+c_str+")"))

    def apply(self,c_str):
        df = self.data
        out = eval("df.apply("+c_str+")")
        if isinstance(out,pd.DataFrame):
            return DataFrame(out)
        else:
            return Series(out)
        

    def applymap(self,c_str):
        df = self.data
        return DataFrame(eval("df.applymap("+c_str+")"))

    def combine(self,df1,c_str):
        df = self.data
        return eval("df.combine(df1,"+c_str+")")

    def dropna(self,c_str=None):
        df = self.data
        if c_str is None:
            return DataFrame(df.dropna())
        return DataFrame(eval("df.dropna("+c_str+")"))

    def fillna(self, c_str):
        df = self.data
        if "inplace=True" in c_str:
            eval("df.fillna("+c_str+")")
        return DataFrame(eval("df.fillna("+c_str+")"))

    def drop(self,c_str):
        df = self.data
        return DataFrame(eval("df.drop("+c_str+")"))

    def drop_duplicates(self,c_str=None):
        df = self.data
        if c_str is None:
            return DataFrame(df.drop_duplicates())
        if "inplace=True" in c_str:
            eval("df.drop_duplicates("+c_str+")")
            return 0
        return DataFrame(eval("df.drop_duplicates("+c_str+")"))

    def agg(self,c_str):
        df = self.data
        out  = eval("df.agg("+c_str+")")
        if isinstance(out,pd.DataFrame):
            return DataFrame(out)
        elif isinstance(out,pd.Series):
            return Series(out)
        else:
            return out
    def groupby(self,g_str,agg_str=None):
        df = self.data
        if agg_str == None:
            return eval("df.groupby("+g_str+")")
        else:
            return DataFrame(eval("df.groupby("+g_str+")."+agg_str))

    def set_axis(self,c_str):
        df = self.df
        return DataFrame(eval("df.set_axis("+c_str+")"))

    def set_index(self,c_str):
        df = self.data
        return DataFrame(eval("df.set_index("+c_str+")"))

    def sort_values(self,c_str):
        df = self.data
        return DataFrame(eval("df.sort_values("+c_str+")"))

    def rank(self,c_str=None):
        df = self.data
        if c_str is None:
            out =  df.rank()
        else:
            out = eval("df.rank("+c_str+")")
        if isinstance(out,pd.DataFrame):
            return DataFrame(out)
        elif isinstance(out,pd.Series):
            return Series(out)
        else:
            return out

    def corr(self,c_str):
        df = self.data
        return DataFrame(eval("df.corr("+c_str+")"))

    def corrwith(self,obj,c_str=None):
        df = self.data
        obj = obj.data
        if c_str is None:
            return Series(df.corrwith(obj))
        return Series(eval("df.corrwith(obj,"+c_str+")"))

    def join(self,obj,c_str=None):
        df = self.data
        if c_str is None:
            return DataFrame(df.join(obj))
        return DataFrame(eval("df.join(obj,"+c_str+")"))

    def diff(self,c_str=None):
        df = self.data
        if c_str is None:
            return DataFrame(df.diff())
        return DataFrame(eval("df.diff("+c_str+")"))

    def melt(self,m_str):
        df = self.data
        return DataFrame(eval("df.melt("+m_str+")"))

    def pivot(self,p_str):
        df = self.data
        return DataFrame(eval("df.pivot("+p_str+")"))

    def pivot_table(self,pt_str):
        df = self.data
        return DataFrame(eval("df.pivot_table("+pt_str+")"))

    def merge(self,df_2,mg_str=None):
        df = self.data
        df2 = df_2.data
        if mg_str is None:
            return DataFrame(df.merge(df2))
        return DataFrame(eval("df.merge(df2,"+mg_str+")"))
    
    def append(df1,c_str=None):
        df =self.data
        if c_str is None:
            return DataFrame(df.append(df1))
        return Dataframe(eval("df.append(df1,"+c_str+")"))

    def eval(self,p_str,c_str=None):
        df = self.df
        if c_str is None:
            out = df.eval(p_str)
        else:
            out = eval("df.eval(p_str,"+c_str+")")
        if isinstance(out,pd.DataFrame):
            return DataFrame(out)
        elif isinstance(out,pd.Series):
            return Series(out)
        else:
            return out

    def view(self):
        return self.data
        
    def head(self,num=None):
        if num == None:
            return DataFrame(self.data.head())
        else:
            return DataFrame(self.data.head(num))
    
    def tail(self,num=None):
        if num == None:
            return DataFrame(self.data.tail())
        else:
            return DataFrame(self.data.tail(num))
    
    def describe(self,kwargs=None):
        if kwargs == None:
            return DataFrame(self.data.describe())
        else:
            df = eval("self.data.describe("+kwargs+")")
            return DataFrame(df)
    
    def sel_column(self,col_name):
        if col_name in self.data.columns:
            return Series(self.data[col_name])
        else:
            return -1
    
    def change_col(self,col_name,ser_obj):
        if col_name in self.data.columns:
            self.data[col_name] = ser_obj.data
            self.view()
        else:
            self.data[col_name] = ser_obj.data
            self.view()
    
    def sum(self,kwargs=None):
        if kwargs == None:
            out = self.data.sum()
        else:
            out = eval("self.data.sum("+kwargs+")")
        if instance(out,pd.DataFrame) == True:
            return DataFrame(out)
        elif isinstance(out,pd.Series):
            return Series(out)
        else:
            return out
    
    def add(self,obj,kwargs=None):
        if isinstance(obj,Series) == True or isinstance(obj,DataFrame) == True:
            obj = obj.data
        else:
            obj = obj
        if kwargs is None:
            return DataFrame(self.data.add(obj))
        else:
            return DataFrame(eval("self.data.add(obj,"+kwargs+")"))
    
    def min(self,kwargs=None):
        if kwargs == None:
            out = self.data.min()
        else:
            out = eval("self.data.min("+kwargs+")")
        if instance(out,pd.DataFrame) == True:
            return DataFrame(out)
        else:
            return Series(out)
    
    def max(self,kwargs=None):
        if kwargs == None:
            out = self.data.max()
        else:
            out = eval("self.data.max("+kwargs+")")
        if instance(out,pd.DataFrame) == True:
            return DataFrame(out)
        else:
            return Series(out)
    
    def idxmin(self,kwargs=None):
        if kwargs==None:
            return Series(self.data.idxmin())
        else:
            out = eval("self.data.idxmin("+kwargs+")")
            return Series(out)
    def idxmax(self,kwargs=None):
        if kwargs==None:
            return Series(self.data.idxmax())
        else:
            out = eval("self.data.idxmax("+kwargs+")")
            return Series(out)

    def pct_change(self,kwargs=None):
        if kwargs is None:
            return Dataframe(self.data.pct_change())
        else:
            return DataFrame(eval("self.data.pct_change("+kwargs+")"))


    def info(self,kwargs=None):
        if kwargs is None:
            self.data.info()
            return 0
        else:
            eval("self.data.info("+kwargs+")")
            return 0

    def add_col(self,*args):
        out = None
        for a in args:
            if a in self.data.columns:
                if out is None:
                    out = self.data[a]
                else:
                    out = out + self.data[a]
        if out is not None:
            return Series(out)

    def insert(self,loc,column,value,kwargs=None):
        if isinstance(value,Series):
            value = value.data
        else:
            value = value
        if kwargs is None:
            out = self.data.insert(loc,column,value)
        else:
            out = eval("self.data.insert(loc,column,value,"+kwargs+")")

    def keys(self):
        return self.data.keys()

    def pop(self, key):
        if key in self.data.columns:
            return Series(self.data.pop(key))

    def get(self, key,kwargs=None):
        if key in self.data.columns:
            if kwargs is not None:
                return self.data.get(self.data.columns[key])
            else:
                return eval("self.data.get(self.data.columns[key],"+kwargs+")")
        else:
            return "Column not found"

    def div(self,obj,kwargs=None):
        if isinstance(obj,DataFrame) == True or isinstance(obj,Series):
            obj = obj.data
        else:
            obj = obj
        if kwargs is None:
            return DataFrame(self.data.div(obj))
        else:
            return DataFrame(eval("self.data.div(obj,"+kwargs+")"))

    def truediv(self,obj,kwargs=None):
        if isinstance(obj,DataFrame) == True or isinstance(obj,Series) == True:
            obj = obj.data
        else:
            obj = obj
        if kwargs is None:
            return DataFrame(self.data.truediv(obj))
        else:
            return DataFrame(eval("self.data.truediv(obj,"+kwargs+")"))

    def floordiv(self,obj,kwargs=None):
        if isinstance(obj,DataFrame) == True or isinstance(obj,Series) == True:
            obj = obj.data
        else:
            obj = obj
        if kwargs is None:
            return DataFrame(self.data.floordiv(obj))
        else:
            return DataFrame(eval("self.data.floordiv(obj,"+kwargs+")"))

    def mod(self,obj,kwargs=None):
        if isinstance(obj,DataFrame) == True or isinstance(obj,Series) == True:
            obj = obj.data
        else:
            obj = obj
        if kwargs is None:
            return DataFrame(self.data.mod(obj))
        else:
            return DataFrame(eval("self.data.mod(obj,"+kwargs+")"))

    def pow(self,obj,kwargs=None):
        if isinstance(obj,DataFrame) == True or isinstance(obj,Series) == True:
            obj = obj.data
        else:
            obj = obj
        if kwargs is None:
            return DataFrame(self.data.mod(obj))
        else:
            return DataFrame(eval("self.data.mod(obj,"+kwargs+")"))

    def dot(self,obj,kwargs=None):
        if isinstance(obj,DataFrame) == True or isinstance(obj,Series) == True:
            obj = obj.data
            if kwargs is None:
                return DataFrame(self.data.dot(obj))
            else:
                return DataFrame(eval("self.data.dot(obj,"+kwargs+")"))

    def transform(self,i_string,kwargs=None):
        if kwargs is None:
            return DataFrame(eval("self.data.transform("+i_string+")"))
        else:
            return DataFrame(eval("self.data.transform("+i_string+","+kwargs+")"))

    def kurtosis(self,kwargs=None):
        if kwargs == None:
            out = self.data.kurtosis()
        else:
            out = eval("self.data.kurtosis("+kwargs+")")
        if isinstance(out,pd.DataFrame):
            return DataFrame(out)
        elif isinstance(out,pd.Series):
            return Series(out)
        else:
            return out

    def var(self,kwargs=None):
        if kwargs == None:
            out = self.data.var()
        else:
            out = eval("self.data.var("+kwargs+")")
        if isinstance(out,pd.DataFrame):
            return DataFrame(out)
        elif isinstance(out,pd.Series):
            return Series(out)
        else:
            return out



    def to_parquet(self,path,kwargs=None):
        if kwargs is None:
            self.data.to_parquet(path)
        else:
            eval("self.data.to_parquet(path,"+kwargs+")")

    def to_pickle(self,path,kwargs=None):
        if kwargs is None:
            self.data.to_pickle(path)
        else:
            eval("self.data.to_pickle(path,"+kwargs+")")

    def to_csv(self,path,kwargs=None):
        if kwargs is None:
            self.data.to_csv(path)
        else:
            eval("self.data.to_csv(path,"+kwargs+")")


    def to_dict(self,kwargs=None):
        if kwargs is None:
            return self.data.to_dict()
        else:
            return eval("self.data.to_dict("+kwargs+")")

    def to_excel(self,path,kwargs=None):
        if kwargs is None:
            self.data.to_excel(path)
        else:
            eval("self.data.to_excel(path,"+kwargs+")")

    def to_json(self,kwargs=None):
        if kwargs == None:
            return self.data.to_json()
        else:
            return eval("self.data.to_json("+kwargs+")")

    def to_html(self,kwargs=None):
        if kwargs == None:
            return self.data.to_html()
        else:
            return eval("self.data.to_html("+kwargs+")")

    def to_feather(self,path):
        return self.data.to_feather(path)

    def to_latex(self,kwargs=None):
        if kwargs == None:
            return self.data.to_latex()
        else:
            return eval("self.data.to_latex("+kwargs+")")

    def to_string(self,kwargs=None):
        if kwargs == None:
            return self.data.to_string()
        else:
            return eval("self.data.to_string("+kwargs+")")

    def to_clipboard(self,kwargs=None):
        if kwargs == None:
            return self.data.to_clipboard()
        else:
            return eval("self.data.to_clipboard("+kwargs+")")




    
    
    
    
#Class 3: Series module functions
class Series():

    def __init__(self,ser):
        if isinstance(ser,pd.Series):
            self.data = ser
            self.index = self.data.index
            self.array  = self.data.array
            self.values = self.data.values
            self.dtype = self.data.dtype
            self.shape = self.data.shape
            self.nbytes = self.data.nbytes
            self.ndim = self.data.ndim
            self.size = self.data.size
            self.T = self.data.T
            self.hasnans = self.data.hasnans
            self.empty = self.data.empty
            self.dtypes = self.data.dtypes
            self.name = self.data.name


    def memory_usage(self,kwargs=None):
        if kwargs == None:
            return self.data.memory_usage()
        else:
            return eval("self.data.memory_usage("+kwargs+")")

    def astype(self,c_str,kwargs=None):
        if kwargs == None:
            out = self.data.astype(c_str)

        else:
            out = eval("self.data.astype(c_str,"+kwargs+")")
        if isinstance(out,pd.DataFrame):
            return DataFrame(out)
        elif isinstance(out,pd.Series):
            return Series(out)
        else:
            return out

    def get_func(self):
        return dir(Series)
            
    def view(self):
        return self.data
        
    def head(self,num=None):
        if num == None:
            return Series(self.data.head())
        else:
            return Series(self.data.head(num))
    
    def tail(self,num=None):
        if num == None:
            return Series(self.data.tail())
        else:
            return Series(self.data.tail(num))
    
    def describe(self,kwargs=None):
        if kwargs == None:
            return Series(self.data.describe())
        else:
            ser = eval("self.data.describe("+kwargs+")")
            return Series(ser)
    
    def sum(self,kwargs=None):
        if kwargs==None:
            out = self.data.sum()
        else:
            out = eval("self.data.sum("+kwargs+")")
        if isinstance(out,pd.Series) == True:
            return Series(out)
        else:
            return out
    
    def min(self,kwargs=None):
        if kwargs == None:
            out = self.data.min()
        else:
            out = eval("self.data.min("+kwargs+")")
        if isinstance(out,pd.Series) == True:
            return Series(out)
        else:
            return out

    def max(self,kwargs=None):
        if kwargs == None:
            out = self.data.max()
        else:
            out = eval("self.data.max("+kwargs+")")
        if instance(out,pd.DataFrame) == True:
            return DataFrame(out)
        elif isinstance(out,pd.Series):
            return Series(out)
        else:
            return out

    def apply(self,c_str):
        df = self.data
        out = eval("df.apply("+c_str+")")
        if isinstance(out,pd.DataFrame):
            return DataFrame(out)
        else:
            return Series(out)

    def agg(self,c_str):
        df = self.data
        out  = eval("df.agg("+c_str+")")
        if isinstance(out,pd.DataFrame):
            return DataFrame(out)
        elif isinstance(out,pd.Series):
            return Series(out)
        else:
            return out


    def at(self,i_string):
        df = self.data
        return eval("df.at["+i_string+"]")

    def iat(self,i_string):
        df = self.data
        return eval("df.iat["+i_string+"]")

    def loc(self,col_string,df_name):
        df = self.data
        f_s = col_string.replace(df_name,"df")
        out = eval("df.loc["+f_s+"]")
        if isinstance(out,pd.DataFrame):
            return DataFrame(out)
        elif isinstance(out,pd.Series):
            return Series(out)
        else:
            return out


    def iloc(self,i_string):
        df = self.data
        out = eval("df.iloc["+i_string+"]")
        if isinstance(out,pd.DataFrame):
            return DataFrame(out)
        elif isinstance(out,pd.Series):
            return Series(out)
        else:
            return out

    def pop(self, key):
        return Series(self.data.pop(key))

    def item(self):
        return self.data.item()

    def xs(self,i_string):
        df = self.data
        out = eval("df.xs("+i_string+")")
        if isinstance(out,pd.DataFrame):
            return DataFrame(out)
        elif isinstance(out,pd.Series):
            return Series(out)    

    def add(self,obj,kwargs=None):
        if isinstance(obj,Series) == True or isinstance(obj,DataFrame) == True:
            obj = obj.data
        else:
            obj = obj
        if kwargs is None:
            return Series(self.data.add(obj))
        else:
            return Series(eval("self.data.add(obj,"+kwargs+")")) 

    def sub(self,obj,i_string=None):
        df = self.data
        if isinstance(obj,DataFrame) == True or isinstance(obj,Series) == True:
            obj = obj.data
        else:
            obj = obj
        if i_string == None:
            return Series(df.sub(obj))
        else:
            return Series(eval("df.sub(obj,"+i_string+")"))

    def mul(self,obj,i_string=None):
        df = self.data
        if isinstance(obj,DataFrame) == True or isinstance(obj,Series) == True:
            obj = obj.data
        else:
            obj = obj
        if i_string is None:
            return Series(df.mul(obj))
        return Series(eval("df.mul(obj,"+i_string+")"))

    def div(self,obj,kwargs=None):
        if isinstance(obj,DataFrame) == True or isinstance(obj,Series):
            obj = obj.data
        else:
            obj = obj
        if kwargs is None:
            return Series(self.data.div(obj))
        else:
            return Series(eval("self.data.div(obj,"+kwargs+")"))

    def truediv(self,obj,kwargs=None):
        if isinstance(obj,DataFrame) == True or isinstance(obj,Series) == True:
            obj = obj.data
        else:
            obj = obj
        if kwargs is None:
            return Series(self.data.truediv(obj))
        else:
            return Series(eval("self.data.truediv(obj,"+kwargs+")"))

    def floordiv(self,obj,kwargs=None):
        if isinstance(obj,DataFrame) == True or isinstance(obj,Series) == True:
            obj = obj.data
        else:
            obj = obj
        if kwargs is None:
            return Series(self.data.floordiv(obj))
        else:
            return Series(eval("self.data.floordiv(obj,"+kwargs+")"))

    def mod(self,obj,kwargs=None):
        if isinstance(obj,DataFrame) == True or isinstance(obj,Series) == True:
            obj = obj.data
        else:
            obj = obj
        if kwargs is None:
            return Series(self.data.mod(obj))
        else:
            return Series(eval("self.data.mod(obj,"+kwargs+")"))

    def pow(self,obj,kwargs=None):
        if isinstance(obj,DataFrame) == True or isinstance(obj,Series) == True:
            obj = obj.data
        else:
            obj = obj
        if kwargs is None:
            return Series(self.data.mod(obj))
        else:
            return Series(eval("self.data.mod(obj,"+kwargs+")"))

    def dot(self,obj,kwargs=None):
        if isinstance(obj,DataFrame) == True or isinstance(obj,Series) == True:
            obj = obj.data
            if kwargs is None:
                return Series(self.data.dot(obj))
            else:
                return Series(eval("self.data.dot(obj,"+kwargs+")"))

    def transform(self,i_string,kwargs=None):
        if kwargs is None:
            return Series(eval("self.data.transform("+i_string+")"))
        else:
            return Series(eval("self.data.transform("+i_string+","+kwargs+")"))

    def kurtosis(self,kwargs=None):
        if kwargs == None:
            out = self.data.kurtosis()
        else:
            out = eval("self.data.kurtosis("+kwargs+")")
        if isinstance(out,pd.DataFrame):
            return DataFrame(out)
        elif isinstance(out,pd.Series):
            return Series(out)
        else:
            return out

    def pct_change(self,kwargs=None):
        if kwargs is None:
            return Series(self.data.pct_change())
        else:
            return Series(eval("self.data.pct_change("+kwargs+")"))



    def divide(self,num):
        return Series(self.data/num)




    def multiply(self,num):
        return Series(self.data*num)

#Class 4: Index class
class Index():
    def __init__(self,Index):
        if isinstance(Index,pd.Index):
            self.data = Index
            self.values = self.data.values
            self.is_monotonic = self.data.is_monotonic
            self.is_monotonic_increasing = self.data.is_monotonic_increasing
            self.is_monotonic_decreasing = self.data.is_monotonic_decreasing
            self.is_unique = self.data.is_unique
            self.has_duplicates = self.data.has_duplicates
            self.hasnans = self.data.hasnans
            self.dtype = self.data.dtype
            self.inferred_type = self.data.inferred_type
            self.is_all_dates = self.data.is_all_dates
            self.shape = self.data.shape
            self.name = self.data.name
            self.names = self.data.names
            self.nbytes = self.data.nbytes
            self.ndim = self.data.ndim
            self.size = self.data.size
            self.empty = self.data.empty
            self.T = self.data.T

    def memory_usage(self,kwargs=None):
        if kwargs == None:
            return self.data.memory_usage()
        else:
            return eval("self.data.memory_usage("+kwargs+")")

    def argmin(self,kwargs=None):
        if kwargs == None:
            return self.data.argmin()
        else:
            return eval("self.data.argmin("+kwargs+")")

    def argmax(self,kwargs=None):
        if kwargs == None:
            return self.data.argmax()
        else:
            return eval("self.data.argmax("+kwargs+")")

    def all(self, kwargs=None):
        if kwargs == None:
            return self.data.all()
        else:
            return eval("self.data.all("+kwargs+")")

    def any(self,kwargs=None):
        if kwargs == None:
            return self.data.any()
        else:
            return eval("self.data.any("+kwargs+")")

    def delete(self,loc):
        return Index(self.data.delete(loc))



    def view(self):
        return self.data

    def copy(self,kwargs=None):
        if kwargs == None:
            return Index(self.data.copy())
        else:
            return Index(eval("self.data.copy("+kwargs+")"))

    def get_func(self):
        return dir(Index)