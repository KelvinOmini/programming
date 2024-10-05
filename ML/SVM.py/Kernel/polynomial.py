from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score 

# Load the digits dataset
digits = datasets.load_digits()

# Features (x) and Labels (y)
x = digits.data
y = digits.target

# Split data into training and testing sets (80% train, 20% test)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# scale the data for better performance
scaler =StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Create SVM model with polynomial kernel
svm_poly = SVC(kernel='poly', degree=3, coef0=1, C=1)

# Train the model
svm_poly.fit(x_train, y_train)

# Predict on test data
Y_pred = svm_poly.predict(x_test)

# Evaluate the model
accuracy = accuracy_score(x_test)
print(f'Polynomial kernel SVM Accuracy: {accuracy * 100:2f}%')
