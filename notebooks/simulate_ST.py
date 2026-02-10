from src.gbm import simulate_terminal_prices
import numpy
import matplotlib.pyplot as plt

S0 = 2.8
r = 0.25
sigma = 0.8
T = 0.25
N= 100000

ST = simulate_terminal_prices(S0,r,sigma,T,N, seed=42)

plt.hist(ST, bins = 100)
plt.xlabel("Terminal stock price")
plt.ylabel("Frequency")
plt.title("Simulated Terminal Prices for Planet Labs")
plt.show()

