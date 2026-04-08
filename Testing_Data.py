
test_start = len(scaled_data) - 300 
test_data = scaled_data[test_start - time_step:] 

X_test = []
for i in range(time_step, len(test_data)):
    X_test.append(test_data[i-time_step:i, 0])

X_test = np.array(X_test)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

print("Testing Data Shape:", X_test.shape)