import numpy as np
import matplotlib.pyplot as plt

def simulate_terminal_prices(S0, r, sigma, T, N, seed=None):
    """
    Simulate N terminal stock prices under Geometric Brownian Motion
    """
    if seed is not None:
        np.random.seed(seed)

    Z = np.random.normal(0,1, N)
    ST = S0*np.exp((r-0.5*sigma**2)*T + sigma* np.sqrt(T)*Z)

    return ST

