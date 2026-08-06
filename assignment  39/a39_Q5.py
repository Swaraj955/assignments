train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)

print(f"Training Accuracy: {train_accuracy * 100:.2f}%")
print(f"Testing Accuracy: {test_accuracy * 100:.2f}%")

if train_accuracy > test_accuracy + 0.10:
    print("Model is Overfitting")
elif train_accuracy < test_accuracy:
    print("Model is Underfitting")
else:
    print("Model is Well Fitted")