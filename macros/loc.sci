function loc()
    // Access a group of rows and columns by label(s) or a boolean array.
    //
    // Syntax
    // dfr.loc(input_string,df_name)
    //
    // Parameters
    // input_string : String containing the input labels/conditions
    // df_name : String containing the DataFrame name
    // Returns : dframefunc instance output
    //
    // Description
    // .loc[] is primarily label based, but may also be used with a boolean array.
    // 
    // Examples
    // // Getting the data of passengers who survived
    // dfr.loc("dfr.Survived==1","dfr")
    // 
// Authors
// Aditya Dhinavahi
// Sundeep Akella
endfunction