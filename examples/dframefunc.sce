//Load SciPandas before execution
pd = pandas();
df = pd.read_csv(".\train.csv")
t_df = dframefunc(df)
disp(t_df.loc("t_df.Survived == 1","t_df") //Access label string, dataframe name(t_df in this case because t_df.Survived is passed in the label string)
disp(t_df.groupby("by=["+""'Age''"+","+""'Survived''"+"]","sum()") //equivalent to df.groupby(by=['Age','Survived']).sum()
