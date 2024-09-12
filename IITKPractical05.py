import pandas
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_column', None)
pandas.set_option('display.width', 1000)
filename="indians-diabetes.data.csv"
hnames=['preg','plas','pres','skin','test','mass','pedi','age','class']
df= pandas.read_csv(filename, names=hnames)
print("Size of training data=",df.shape)
print(df.dtypes)
print("\n\n")
print(df)
print(df.describe())
print(df.describe(include="all"))
class_counts=df.groupby('class').size()
print(class_counts)
correlations= df.corr(method='pearson')
print(correlations)