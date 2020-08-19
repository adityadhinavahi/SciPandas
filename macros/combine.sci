function combine()
    // Perform column-wise combine with another DataFrame.
    //
    // Syntax
    // dfr.combine(obj,input_string)
    //
    // Parameters
    // obj : DataFrame object
    // input_string : String containing the function to be passed. Scilab functions are not supported as of now. Additional parameters supported can be passed
    // // For additional information on parameters, see https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine.html?#pandas.DataFrame.combine
    // Returns : DataFrame
    // 
    // Examples
    // // Combine another DataFrame with this DataFrame by using np.sqrt function
    // dfr.combine(df1.age,"np.sqrt") // 
    // // Lambda functions are also supported.
    // 
// Authors
// Aditya Dhinavahi
// Sundeep Akella
endfunction