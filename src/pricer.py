import numpy as np
from src.gbm import simulate_terminal_prices

def price_call_mc(S0, K, r, sigma, T, N, seed=None):
    """
    Monte Carlo price of a call option
    """
    ST = simulate_terminal_prices(S0,r,sigma,T,N, seed)
    payoff = np.maximum(ST-K, 0)
    discounted_payoffs = payoff * np.exp(-r*T)
    price = np.mean(discounted_payoffs)
    std_error = np.std(discounted_payoffs)/np.sqrt(N)

    return price, std_error




