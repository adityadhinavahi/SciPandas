function convert_dtypes()
    // Convert columns to best possible dtypes using dtypes supporting pd.NA.
    //
    // Syntax
    //pd.DataFrame(data=d)
    //
    // Parameters
    // nfer_objects: bool, default True
	//convert_string: bool, default True
    // convert_integer: bool, default True
	//convert_boolean: bool, defaults True
    // For additional information on parameters, See  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.convert_dtypes.html
    // Returns : Series or DataFrame
    // 
    // Examples
    // //Cast all columns to int32:
    // d = {'col1': [1, 2], 'col2': [3, 4]}
    //df = pd.DataFrame(data=d)
    //df.dtypes
    // 
    // Authors
    // Aditya Dhinavahi
   // Sundeep Akella
endfunction
 
    