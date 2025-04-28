import pandas as pd

df = pd.read_csv('data/titanic.csv')

# Drop columns we won't use
df = df.drop(columns=['Name', 'Ticket', 'Cabin'])

# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna('S')

# Convert categorical columns to numeric
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True).astype(int)


print("Cleaned Dataset Preview:")
print(df.head())
print("\nData Types:")
print(df.dtypes)

# Save cleaned version
df.to_csv('data/titanic_cleaned.csv', index=False)
print("\nCleaned data saved to: data/titanic_cleaned.csv")
