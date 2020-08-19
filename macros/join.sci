function join()
    //Join columns of another DataFrame.
    // Syntax
    //df.set_index(' ').join(other.set_index(' '))
    //
    // Parameters
    // other: DataFrame, Series, or list of DataFrame
	//lsuffix: str, default ‘’
	//rsuffix: str, default ‘’
	//sort: bool, default False
	//method:{‘pearson’, ‘kendall’, ‘spearman’} or callable
	//dropbool:  default False
    // For additional information on parameters, See https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html
    // Returns : series
    // 
    // Examples
    // If we want to join using the key columns, we need to set key to be the index in both df and other. The joined DataFrame will have key as its index.
    // df.join(other, lsuffix='_caller', rsuffix='_other')
    // Authors
    // Aditya Dhinavahi
   // Sundeep Akella
endfunction
 
    