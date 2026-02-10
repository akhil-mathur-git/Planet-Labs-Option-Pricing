from src.pricer import price_call_mc

S0 = 2.8
r = 0.25
sigma = 0.8
T = 0.25
K= 3

for N in [1,10,100,1000,10000,100000]:
    price, std_error = price_call_mc(S0,K,r,sigma,T,N,seed=42)
    print(f"N= {N:>7} | Price= {price:.4f} | Standard Error = {std_error:.4f}")

