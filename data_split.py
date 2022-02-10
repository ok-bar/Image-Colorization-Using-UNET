def split_data(inputs,labels,test_size=0.2):
    labels=np.array(labels)
    inputs=np.array(inputs)
    x_train, x_test, y_train, y_test = train_test_split(inputs, labels, test_size=test_size)
    x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train, test_size=0.05)
    return x_train, x_valid,x_test ,y_train, y_valid,y_test
