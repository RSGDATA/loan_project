

def test_classification_model(model, data, folder):
    from time import time
    
    start = time()
    X_train_scaled, X_test_scaled, y_train, y_test = data

    reg = model.fit(X_train_scaled, y_train)
    print(f'Model: {type(reg).__name__}')
    print(f'Train score: {reg.score(X_train_scaled, y_train)}')
    print(f'Test Score: {reg.score(X_test_scaled, y_test)}\n')
#     plt.show()    
    y_true = y_test
    y_pred = model.predict(X_test_scaled)
    print('Confusion Matrix:\n',confusion_matrix(y_true, y_pred), '\n\n')
    confusion_score(y_true, y_pred)
    end = time()
    print(f'Process time: {round(end-start, 2)} seconds.')

    
    
    filename = f'{folder}/{type(reg).__name__}.sav'
    pickle.dump(model, open(filename, 'wb'))
    print(f'{getsize(filename):,} bytes')
    
    print('~'*80)
    
#     return(y_true, y_pred)
    
    
    
def confusion_score(y_true, y_pred):
    from sklearn.metrics import confusion_matrix
    [[TP, FN],[FP,TN]] = confusion_matrix(y_true, y_pred)

    accuracy = round((TP + TN) / (TP + FP + TN + FN),4) # (111 + 128) / (111 + 5 + 128 + 6)
#     print(f"Accuracy: {accuracy.round(4)}")
    precision = round((TP / (TP + FP)),4)
#     print(f'Precision: {precision.round(4)}')
    sensitivity = round(TP / (TP + FN),4)
#     print(f'Sensitivity: {sensitivity.round(4)}')
    specificity = round(TN / (TN + FP),4)
#     print(f'Specificity: {specificity.round(4)}')

    neg_predictive_value = round(TN / (TN + FN),4)
    
    matrix = [
#         ['','Predicted Class','Predicted Class',''],
        ['CONFUSION','Pred. Pos.','Pred. Neg.',''],
        ['MATRIX','_'*50],
        ['Act. Positive',TP,FN,sensitivity,'sensitivity'],
        ['Act. Negative',FP,TN,specificity,'specificity'],
        ['',precision,neg_predictive_value,accuracy,'accuracy'],
        ['','precision','neg. pred. value']
    ]
    
    for i in matrix:
        for j in i:
            print(f'{j:^16}|', end='')
        print("")
        
        
        
        
# IN CASE OF 3x3 CONFUSION MATRIX:

def confusion_score2(y_true, y_pred):
    from sklearn.metrics import confusion_matrix
    [[a1, a2, a3],[b1,b2, b3],[c1,c2,c3]] = confusion_matrix(y_true, y_pred)
    TP = a1
    FN = a2 + a3
    FP = b1 + c1
    TN = b2 + b3 + c2 + c3

    accuracy = (TP + TN) / (TP + FP + TN + FN) # (111 + 128) / (111 + 5 + 128 + 6)
    print(f"Accuracy: {accuracy.round(3)}")
    precision = TP / (TP + FP)
    print(f'Precision: {precision.round(3)}')
    sensitivity = TP / (TP + FN)
    print(f'Sensitivity: {sensitivity.round(3)}')
    specificity = TN / (TN + FP)
    print(f'Specificity: {specificity.round(3)}')