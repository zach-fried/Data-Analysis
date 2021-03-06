# Basic machine learning, learning. Practice makes perfect. Siraj Raval coding challenge.

from sklearn import tree, linear_model, neighbors

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], 
    [166, 65, 40],[190, 90, 47], [175, 64, 39], [177, 70, 40], 
    [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 
    'female','female', 'male', 'male']

# Trying to allow user input of test data and split string input and convert to float for machine learning algorithms
test_data = input('Please enter a height (cm), weight (kg), and shoe size (cm) separated by commas: ')#[[182.88, 81.65, 25]]
test_data = test_data.split(',')

for i in range(0, len(test_data)):
    test_data[i] = float(test_data[i])

# Decision tree
clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

prediction_tree = clf.predict([test_data])

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

prediction_reg = reg.predict([test_data])

if prediction_reg == 1:
    print('Male')
else:
    print('Female')

# Nearest neighbors classification
neighbor = neighbors.KNeighborsClassifier()

neighbor = neighbor.fit(X, Y)

prediction_neigh = neighbor.predict([test_data])

print(prediction_neigh)
