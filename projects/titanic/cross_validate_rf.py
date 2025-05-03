import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import make_scorer, f1_score

# Load data
df = pd.read_csv('C:/Users/73045/Documents/ml_product_leader_2025/projects/titanic/data/titanic_cleaned.csv')
X = df.drop('Survived', axis=1)
y = df['Survived']

# Initialize model
model = RandomForestClassifier(n_estimators=100, random_state=41)

# Use F1 score as the evaluation metric
f1 = make_scorer(f1_score)

# Run 5-fold cross-validation
scores = cross_val_score(model, X, y, cv=5, scoring=f1)

print("F1 Scores per fold:", scores)
print("Average F1 Score:", scores.mean())
