
predictions = model.predict(X_test)

predictions = scaler.inverse_transform(predictions)

actual_prices = scaler.inverse_transform(scaled_data[test_start:])