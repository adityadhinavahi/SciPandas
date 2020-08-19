//Load SciPandas before execution
pd = pandas();
df = pd.read_csv(".\train.csv") //Load the csv file
disp(df.head()) //Display the head of the dataframe
disp(df.shape) //Display the dimensions of the dataframe
