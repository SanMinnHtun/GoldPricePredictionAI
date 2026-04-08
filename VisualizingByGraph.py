import matplotlib.pyplot as plt

plt.figure(figsize=(14, 5))
plt.plot(actual_prices, color='blue', label='Actual Gold Price (USD)')
plt.plot(predictions, color='red', label='Predicted Gold Price (USD)')
plt.title('Gold Price Prediction Test')
plt.xlabel('Days')
plt.ylabel('USD Price')
plt.legend()
plt.show()