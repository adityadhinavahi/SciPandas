function melt()
    //Unpivot a DataFrame from wide to long format, optionally leaving identifiers set.
    // Syntax
    //pd.melt(df, id_vars=['A'], value_vars=['B'])
    //
    // Parameters
    //id_vars: tuple, list, or ndarray, optional
	//value_vars: tuple, list, or ndarray, optional
	//var_name: scalar
	//value_name: scalar, default ‘value’
	//
    // For additional information on parameters, See https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html
    // Returns : DataFrame
    // 
    // Examples
    // If we want to join using the key columns, we need to set key to be the index in both df and other. The joined DataFrame will have key as its index.
    // df.join(other, lsuffix='_caller', rsuffix='_other')
    // Authors
    // Aditya Dhinavahi
   // Sundeep Akella
endfunction
 
    