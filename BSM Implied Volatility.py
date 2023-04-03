# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 20:20:03 2023

@author: Mosco
"""

import math
from scipy.stats import norm


def black_scholes_call(S, K, r, T, sigma):
    """
    Calculate the call option price using the Black-Scholes formula.

    Args:
        S (float): The current underlying asset price.
        K (float): The strike price of the option.
        r (float): The risk-free interest rate (annualized).
        T (float): The time to maturity of the option, expressed in years.
        sigma (float): The volatility of the underlying asset.

    Returns:
        float: The call option price.
    """

    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    return call_price


def vega(S, K, r, T, sigma):
    """
    Calculate the Vega of the option, which is the derivative of the option price
    with respect to the volatility of the underlying asset.

    Args:
        S (float): The current underlying asset price.
        K (float): The strike price of the option.
        r (float): The risk-free interest rate (annualized).
        T (float): The time to maturity of the option, expressed in years.
        sigma (float): The volatility of the underlying asset.

    Returns:
        float: The Vega of the option.
    """

    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    return S * norm.pdf(d1) * math.sqrt(T)

def implied_volatility(S, K, r, T, option_price, initial_guess=0.5, max_iterations=100, tolerance=1e-6):
    """
    Calculate the implied volatility using the Black-Scholes model and the Newton-Raphson method.

    Args:
        S (float): The current underlying asset price.
        K (float): The strike price of the option.
        r (float): The risk-free interest rate (annualized).
        T (float): The time to maturity of the option, expressed in years.
        option_price (float): The observed option price.
        initial_guess (float, optional): The initial guess for the implied volatility. Defaults to 0.5.
        max_iterations (int, optional): The maximum number of iterations for the Newton-Raphson method. Defaults to 100.
        tolerance (float, optional): The tolerance for convergence. Defaults to 1e-6.

    Returns:
        float: The implied volatility.
    """

    sigma = initial_guess
    for _ in range(max_iterations):
        call_price = black_scholes_call(S, K, r, T, sigma)
        option_vega = vega(S, K, r, T, sigma)

        # Update the volatility estimate using the Newton-Raphson method
        sigma_new = sigma - (call_price - option_price) / option_vega
    
        # Check for convergence
        if abs(sigma_new - sigma) < tolerance:
            return sigma_new
    
        # Update the volatility estimate for the next iteration
        sigma = sigma_new
    
    # If the function does not converge within the specified maximum iterations, return the latest estimate
    return sigma



S = 100
K = 110
r = 0.02
T = 0.5
option_price = 5.0

implied_vol = implied_volatility(S, K, r, T, option_price)
print(f"The implied volatility is {implied_vol:.4f}.")
