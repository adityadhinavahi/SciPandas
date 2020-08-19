function [df] = qcut()
    // Calls and initializes qcut function
    //
    // Syntax
    // df = qcut()
    //
    // Parameters
    //df: qcut input
    //
    // Description
//The pandas documentation describes qcut as a “Quantile-based discretization function.” This basically means that qcut tries to divide up the underlying data into equal sized bins. The function defines the bins using percentiles based on the distribution of the data, not the actual numeric edges of the bins.
    // Examples
    // //Constructing qcut from a dictionary.
    //df = pd_f.cut("+c_str+")
// Authors
// Aditya Dhinavahi
// Sundeep Akella
endfunction