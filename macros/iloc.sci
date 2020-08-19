function iloc()
    // Purely integer-location based indexing for selection by position.
    //
    // Syntax
    // dfr.iloc(input_string)
    //
    // Parameters
    // input_string : String containing the input integers/slices/lists of integers
    // Returns : DataFrame
    //
    // Description
    // .iloc[] is primarily integer position based (from 0 to length-1 of the axis), but may also be used with a boolean array.
    // 
    // Examples
    // // Getting the data of the first passenger
    // dfr.iloc("0,:")
    // 
// Authors
// Aditya Dhinavahi
// Sundeep Akella
endfunction