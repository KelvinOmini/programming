import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

digits = datasets.load_digits()

plt.figure(figsize=(10, 4))
for index, (image, label) in enumerate(list(zip(digits.images, digits.target))[:5]):
    plt.subplot(1, 5, index + 1)
    plt.imshow(image, cmap='gray')
    plt.title(f'Target: {label}')
    plt.axis('off')
plt.tight_layout()
plt.show()

# Flatten the images
n_samples = len(digits.images)
x = digits.images.reshape(n_samples, -1)
y = digits.target

# Split into training and test sets (70% training, 30% test)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=42, stratify=y)

# Feature scaling
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Create and train the linear kernel SVM classifier
svm_classifier = SVC(kernel='linear',C=1.0)
svm_classifier.fit(x_train_scaled, y_train)

y_pred = svm_classifier.predict(x_test_scaled)

# Confusion Matrix
print(f'Çonfusion Matrix: \n{confusion_matrix(y_test, y_pred)}')

# Classification Report 
print(f'\nClassification Report: \n{classification_report(y_test, y_pred)}')

# Accuracy Score
Accuracy = accuracy_score(y_test, y_pred)
print(f'\nAccuracy: {Accuracy * 100:2f}%')

# Display some predictions alongside actual labels
plt.figure(figsize=(10,4))
for index, (image, prediction, label) in enumerate( list(zip(x_test, y_pred, y_test))[:5]):
    
    # Undo the scaling so we can display the original image
    original_image = scaler.inverse_transform(image).reshape(8,8)
    plt.subplot(1, 5, index + 1)
    plt.imshow(original_image, cmap='gray')
    plt.imshow(f'P: {prediction}\nT:{label}')
    plt.axis('off')
plt.tight_layout()
plt.show()

