from src.pricer import price_call_mc
from src.black_scholes import black_scholes_call
import matplotlib.pyplot as plt


S0 = 2.8
r = 0.05
sigma = 0.8
T = 0.25
K= 3
N=100000

mc_price, mc_err = price_call_mc(S0,K,r,sigma,T,N,seed=42)
bs_price = black_scholes_call(S0,K,r,sigma,T)

print(f"Monte Carlo price: {mc_price:.4f} +- {1.96*mc_err:.4f}")
print(f"Black-Scholes price: {bs_price:.4f}")

Ns = [10,100,1000,5000,10000,50000,100000]
mc_prices = []

for N in Ns:
    price,_ = price_call_mc(S0,K,r,sigma,T,N,seed=42)
    mc_prices.append(price)

plt.plot(Ns,mc_prices, marker = "o", label = "Monte Carlo")
plt.axhline(bs_price, color = "red", linestyle = "--", label = "Black-Scholes")
plt.xscale("log")
plt.xlabel("Number of simulations")
plt.ylabel("Call option price")
plt.title("Monte Carlo convergence to Black-Scholes")
plt.legend()
plt.show()
