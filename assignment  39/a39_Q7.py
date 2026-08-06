new_student = [[5, 4, 3]]

prediction = model.predict(new_student)

if prediction[0] == 1:
    print("Predicted Result: Pass")
else:
    print("Predicted Result: Fail")