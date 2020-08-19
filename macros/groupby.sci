function groupby()
    // Group DataFrame using a mapper or by a Series of columns.
    //
    // Syntax
    // dfr.groupby(input_string,agg_str)
    //
    // Parameters
    // input_string : String containing the parameters to group
    // agg_str : String containing any agg function to aggregate the resulting groups(optional)
    // // For additional information on parameters, see https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html?#pandas.DataFrame.groupby
    // Returns : DataFrame
    // 
    // Examples
    // // Group by the Survived column and aggregate the results by sum
    // dfr.groupby("by = ["+""'Survived''"+"]","sum()")
    // 
// Authors
// Aditya Dhinavahi
// Sundeep Akella
endfunction