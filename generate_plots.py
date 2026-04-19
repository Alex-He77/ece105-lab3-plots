"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
import numpy as np

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.

def generate_data(seed: int = 6412):
    """Generate synthetic sensor temperature data.

    Parameters
    ----------
    seed : int
        Seed for NumPy's random number generator (last 4 digits of Drexel ID).
        Defaults to 6412.

    Returns
    -------
    sensor_a : numpy.ndarray
        1-D array of shape (200,) containing Sensor A temperature readings (°C).
    sensor_b : numpy.ndarray
        1-D array of shape (200,) containing Sensor B temperature readings (°C).
    timestamps : numpy.ndarray
        1-D array of shape (200,) containing timestamps uniformly sampled in [0, 10] seconds.

    Notes
    -----
    Sensor A: mean 25 C, std 3 C.
    Sensor B: mean 27 C, std 4.5 C.
    """
    rng = np.random.default_rng(seed)
    n = 200
    # timestamps uniformly in [0, 10]
    timestamps = rng.uniform(0.0, 10.0, size=n)

    # two sensors with requested means and stddevs
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=n)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=n)

    return sensor_a, sensor_b, timestamps
