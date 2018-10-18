from sklearn import tree, linear_model, neighbors

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], 
    [166, 65, 40],[190, 90, 47], [175, 64, 39], [177, 70, 40], 
    [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 
    'female','female', 'male', 'male']

test_data = [[155, 67, 33]]

# Decision tree
clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

prediction_tree = clf.predict(test_data)

print(prediction_tree)

#Linear regression
Y_num = []

for gender in Y:
    if gender == 'male':
        Y_num.append(1)
    else:
        Y_num.append(0)

reg = linear_model.LinearRegression()

reg = reg.fit(X, Y_num)

prediction_reg = reg.predict(test_data)

if prediction_reg == 1:
    print('Male')
else:
    print('Female')

# Nearest neighbors classification
neighbor = neighbors.KNeighborsClassifier()

neighbor = neighbor.fit(X, Y)

prediction_neigh = neighbor.predict(test_data)

print(prediction_neigh)
