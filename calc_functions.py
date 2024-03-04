from math import exp
import numpy as np

def eurcall_explicit(S: float, K: float, r: float, sigma: float, T: float, M: int =4, N: int =3):
    '''
    S: current price of underlying asset,
    K: strike price of option,
    r: annual risk-free interest rate in decimal form,
    sigma: standard deviation of underlying asset in decimal form,
    T: time to maturity in years,
    M: number of price steps,
    N: number of time steps.

    Assumptions:
    1. S_max < 2 * K
    2. Underlying asset does not pay dividends
    '''
    # Step 1: Calculate the time step, dt, and the price step, ds.
    S_max = 2*K
    dt, ds = T/N, S_max/M

    # Step 2a: Initialise the matrix to store option prices over time.
    option_prices = np.zeros((M+1, N+1))

    # Step 2b: Update the option prices at time T.
    option_prices[:, N] = np.maximum(np.arange(0, M+1) * ds - K, 0)

    # Step 3: Compute option price at time i and at asset price S_j where S_j = j * ds
    for i in range(N-1, -1, -1):
        # Set option price when j = 0 (asset price S_j = 0)
        option_prices[0, i] = 0

        # Set option price when j = M (asset price S_j = S_max)
        option_prices[M, i] = S_max - K * exp(- r * (N-i) * dt)

        # Calculate option price for all other S_j at time i
        for j in range(1, M):
            a = 0.5 * dt * (sigma ** 2 * j ** 2 - r * j)
            b = 1 - (sigma ** 2 * j ** 2 + r) * dt
            c = 0.5 * dt * (sigma ** 2 * j ** 2 + r * j)
            
            opPrice_down = option_prices[j-1, i+1]
            opPrice_mid = option_prices[j, i+1]
            opPrice_up = option_prices[j+1, i+1]

            opPrice_curr = a * opPrice_down + b * opPrice_mid + c * opPrice_up

            option_prices[j, i] = opPrice_curr

    # Step 4: Find value of k such that k * ds <= S < (k+1) * ds
    k = int(S // ds)
    
    # Step 5: Compute option price using linear interpolation 
    opPrice_at_k = option_prices[k, 0]
    opPrice_at_kplus1 = option_prices[k+1, 0]
    
    option_price = opPrice_at_k + ((opPrice_at_kplus1 - opPrice_at_k) / ds) * (S - k * ds)
    
    return option_price

def eurput_explicit(S: float, K: float, r: float, sigma: float, T: float, M: int =4, N: int =3):
    '''
    S: current price of underlying asset,
    K: strike price of option,
    r: annual risk-free interest rate in decimal form,
    sigma: standard deviation of underlying asset in decimal form,
    T: time to maturity in years,
    M: number of price steps,
    N: number of time steps.

    Assumptions:
    1. S_max < 2 * K
    2. Underlying asset does not pay dividends
    '''
    # Step 1: Calculate the time step, dt, and the price step, ds.
    S_max = 2*K
    dt, ds = T/N, S_max/M

    # Step 2a: Initialise the matrix to store option prices over time.
    option_prices = np.zeros((M+1, N+1))

    # Step 2b: Update the option prices at time T.
    option_prices[:, N] = np.maximum(np.arange(0, M+1) * ds - K, 0)

    # Step 3: Compute option price at time i and at asset price S_j where S_j = j * ds
    for i in range(N-1, -1, -1):
        # Set option price when j = 0 (asset price S_j = 0)
        option_prices[0, i] = K * exp(- r * (N-i) * dt)

        # Set option price when j = M (asset price S_j = S_max)
        option_prices[M, i] = 0

        # Calculate option price for all other S_j at time i
        for j in range(1, M):
            a = 0.5 * dt * (sigma ** 2 * j ** 2 - r * j)
            b = 1 - (sigma ** 2 * j ** 2 + r) * dt
            c = 0.5 * dt * (sigma ** 2 * j ** 2 + r * j)
            
            opPrice_down = option_prices[j-1, i+1]
            opPrice_mid = option_prices[j, i+1]
            opPrice_up = option_prices[j+1, i+1]

            opPrice_curr = a * opPrice_down + b * opPrice_mid + c * opPrice_up

            option_prices[j, i] = opPrice_curr

    # Step 4: Find value of k such that k * ds <= S < (k+1) * ds
    k = int(S // ds)
    
    # Step 5: Compute option price using linear interpolation 
    opPrice_at_k = option_prices[k, 0]
    opPrice_at_kplus1 = option_prices[k+1, 0]
    
    option_price = opPrice_at_k + ((opPrice_at_kplus1 - opPrice_at_k) / ds) * (S - k * ds)
    
    return option_price

def amrcall_explicit(S: float, K: float, r: float, sigma: float, T: float, M: int =4, N: int =3):
    '''
    S: current price of underlying asset,
    K: strike price of option,
    r: annual risk-free interest rate in decimal form,
    sigma: standard deviation of underlying asset in decimal form,
    T: time to maturity in years,
    M: number of price steps,
    N: number of time steps.

    Assumptions:
    1. S_max < 2 * K
    2. Underlying asset does not pay dividends
    '''
    # Step 1: Calculate the time step, dt, and the price step, ds.
    S_max = 2*K
    dt, ds = T/N, S_max/M

    # Step 2a: Initialise the matrix to store option prices over time.
    option_prices = np.zeros((M+1, N+1))

    # Step 2b: Update the option prices at time T.
    option_prices[:, N] = np.maximum(np.arange(0, M+1) * ds - K, 0)

    # Step 3: Compute option price at time i and at asset price S_j where S_j = j * ds
    for i in range(N-1, -1, -1):
        # Set option price when j = 0 (asset price S_j = 0)
        option_prices[0, i] = 0

        # Set option price when j = M (asset price S_j = S_max)
        option_prices[M, i] = S_max - K * exp(- r * (N-i) * dt)

        # Calculate option price for all other S_j at time i
        for j in range(1, M):
            a = 0.5 * dt * (sigma ** 2 * j ** 2 - r * j)
            b = 1 - (sigma ** 2 * j ** 2 + r) * dt
            c = 0.5 * dt * (sigma ** 2 * j ** 2 + r * j)
            
            opPrice_down = option_prices[j-1, i+1]
            opPrice_mid = option_prices[j, i+1]
            opPrice_up = option_prices[j+1, i+1]

            opPrice_curr = a * opPrice_down + b * opPrice_mid + c * opPrice_up

            opPrice_exercised = j * ds - K

            option_prices[j, i] = max(opPrice_curr, opPrice_exercised)

    # Step 4: Find value of k such that k * ds <= S < (k+1) * ds
    k = int(S // ds)
    
    # Step 5: Compute option price using linear interpolation 
    opPrice_at_k = option_prices[k, 0]
    opPrice_at_kplus1 = option_prices[k+1, 0]
    
    option_price = opPrice_at_k + ((opPrice_at_kplus1 - opPrice_at_k) / ds) * (S - k * ds)
    
    return option_price

# Test case for european call option
# Result: Same as QF101 ans apart from some rounding differences
x = eurcall_explicit(50, 50, 0.1, 0.4, 1, 4, 3)
print(x)

    
    
    
    

