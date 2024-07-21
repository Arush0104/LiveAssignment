from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data and preprocess once
df = pd.read_csv('mushrooms.csv')
categorical_data = ['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat']
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False).set_output(transform='pandas')
X_encoded = encoder.fit_transform(df[categorical_data])
df = pd.concat([df.drop(columns=categorical_data), X_encoded], axis=1)

# Separate features (X) and target variable (y)
X = df.drop('class', axis=1)
y = df['class']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42)

# Create and train logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Print model accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home_page.html')

@app.route('/predict', methods=['GET', 'POST'])
def index():
    form_data = {}
    prediction = None
    if request.method == 'POST':
        form_data = {
            'cap-shape': [request.form['cap-shape']],
            'cap-surface': [request.form['cap-surface']],
            'cap-color': [request.form['cap-color']],
            'bruises': [request.form['bruises']],
            'odor': [request.form['odor']],
            'gill-attachment': [request.form['gill-attachment']],
            'gill-spacing': [request.form['gill-spacing']],
            'gill-size': [request.form['gill-size']],
            'gill-color': [request.form['gill-color']],
            'stalk-shape': [request.form['stalk-shape']],
            'stalk-root': [request.form['stalk-root']],
            'stalk-surface-above-ring': [request.form['stalk-surface-above-ring']],
            'stalk-surface-below-ring': [request.form['stalk-surface-below-ring']],
            'stalk-color-above-ring': [request.form['stalk-color-above-ring']],
            'stalk-color-below-ring': [request.form['stalk-color-below-ring']],
            'veil-type': [request.form['veil-type']],
            'veil-color': [request.form['veil-color']],
            'ring-number': [request.form['ring-number']],
            'ring-type': [request.form['ring-type']],
            'spore-print-color': [request.form['spore-print-color']],
            'population': [request.form['population']],
            'habitat': [request.form['habitat']]
        }
        X_example = pd.DataFrame(form_data)
        X_example_encoded = encoder.transform(X_example)
        X_example_encoded = X_example_encoded.reindex(columns=X.columns, fill_value=0)
        prediction = model.predict(X_example_encoded)[0]
    
    return render_template('index.html', prediction=prediction, form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
