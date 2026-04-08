from sklearn.metrics import mean_squared_error

rmse = np.sqrt(mean_squared_error(actual_prices, predictions))
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")