### Monte Carlo Simulation

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

This Python script performs a Monte Carlo simulation to estimate the value of π.

## Features

- Monte Carlo simulation algorithm
- Estimation of the value of π

#### Installation

You can install the script using pip:

```bash
pip install pymontecarlo

#### Example

```python
# Import the Monte Carlo simulation function
from monte_carlo_simulation import monte_carlo_simulation

# Set the number of random points to generate
num_points = 10000

# Run the Monte Carlo simulation to estimate the value of π
result = monte_carlo_simulation(num_points)

# Display the result
print(f"Estimated value of π using {num_points} random points: {result}")