import pandas
filename = "indians-diabetes.data.csv"
hnames = ['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe = pandas.read_csv(filename, names=hnames)

#dimensions of your data
print("dataframe.shape:", dataframe.shape)
print("-*-"*20)

#peek at your data
#review the first 10 rows of your data using the heads() function on the pandas dataframe
print(dataframe.head(10))
print("-*-"*20)
print(dataframe.tail(10))
print("-*-"*20)
print(dataframe.sample(10))
print("-*-"*20)

#datatype for each attribute
print(dataframe.dtypes)
print("-*-"*20)

#descriptive statistics
pandas.set_option('display.width', 1000)
pandas.set_option('precision', 2)

print("description=\n",dataframe.describe())
print("-*-"*20)

#class distribution(classification only)
print()
class_counts=dataframe.groupby('class').size()
print(class_counts)
print("-*-"*20)

#correlations between attributes
correlations=dataframe.corr(method='pearson')
print(correlations)