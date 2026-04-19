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

def plot_scatter(sensor_a: np.ndarray, sensor_b: np.ndarray, timestamps: np.ndarray, ax):
    """Draw a scatter plot of two sensors on the provided Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        1-D array of shape (N,) containing Sensor A temperature readings in °C.
    sensor_b : numpy.ndarray
        1-D array of shape (N,) containing Sensor B temperature readings in °C.
    timestamps : numpy.ndarray
        1-D array of shape (N,) containing timestamps in seconds.
    ax : matplotlib.axes.Axes
        Matplotlib Axes object to draw the scatter plot on. The function
        modifies this Axes in place.

    Returns
    -------
    None
        The function modifies the provided Axes object in place and does not
        return a value.

    Notes
    -----
    - Sensor A points are plotted in blue and Sensor B points in orange.
    - Axis labels, title, legend, grid, and tight layout are set on the Axes.
    """
    # Plot points for each sensor
    ax.scatter(timestamps, sensor_a, s=30, c='tab:blue', alpha=0.8, label='Sensor A')
    ax.scatter(timestamps, sensor_b, s=30, c='tab:orange', alpha=0.8, label='Sensor B')

    # Labels and title
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Sensor temperature readings vs Time')

    # Legend and grid
    ax.legend()
    ax.grid(True, which='both', axis='both', linestyle='-', alpha=0.3)

    # No return; modifies ax in place
    return None

def plot_histogram(sensor_a: np.ndarray, sensor_b: np.ndarray, ax, bins=30):
    """Draw overlaid histograms for two sensors on the provided Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        1-D array of shape (N,) containing Sensor A temperature readings in °C.
    sensor_b : numpy.ndarray
        1-D array of shape (N,) containing Sensor B temperature readings in °C.
    ax : matplotlib.axes.Axes
        Matplotlib Axes object to draw the histograms on. Modified in place.
    bins : int or sequence, optional
        Number of bins (int) or bin edges (sequence). If int, a shared range
        across both sensors is used. Default is 30.

    Returns
    -------
    None
        The function modifies the provided Axes object in place and returns None.
    """
    # Determine shared bin edges if bins is an int
    if isinstance(bins, int):
        lo = min(np.min(sensor_a), np.min(sensor_b))
        hi = max(np.max(sensor_a), np.max(sensor_b))
        bin_edges = np.linspace(lo, hi, bins + 1)
    else:
        bin_edges = bins

    # Plot histograms
    ax.hist(sensor_a, bins=bin_edges, color='tab:blue', alpha=0.5, label='Sensor A',
            edgecolor='black', linewidth=0.2)
    ax.hist(sensor_b, bins=bin_edges, color='tab:orange', alpha=0.5, label='Sensor B',
            edgecolor='black', linewidth=0.2)

    # Vertical dashed lines at each sensor mean
    mean_a = np.mean(sensor_a)
    mean_b = np.mean(sensor_b)
    ax.axvline(mean_a, color='tab:blue', linestyle='--', linewidth=2, label='Mean A')
    ax.axvline(mean_b, color='tab:orange', linestyle='--', linewidth=2, label='Mean B')

    # Labels, title, legend, and grid
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Count')
    ax.set_title('Histogram of sensor temperature readings')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    return None

def plot_boxplot(sensor_a: np.ndarray, sensor_b: np.ndarray, ax):
    """Draw side-by-side box plots for two sensors on the provided Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        1-D array of shape (N,) containing Sensor A temperature readings in °C.
    sensor_b : numpy.ndarray
        1-D array of shape (N,) containing Sensor B temperature readings in °C.
    ax : matplotlib.axes.Axes
        Matplotlib Axes object to draw the box plots on. Modified in place.

    Returns
    -------
    None
        The function modifies the provided Axes object in place and returns None.

    Notes
    -----
    - Boxes are colored to match the scatter/histogram colors used elsewhere.
    - A horizontal dashed line is drawn at the overall mean across both sensors.
    """
   
    # Prepare data
    data = [sensor_a, sensor_b]
    labels = ['Sensor A', 'Sensor B']

    # Create boxplot with notches and colored boxes
    bp = ax.boxplot(data, labels=labels, patch_artist=True, notch=True,
                    flierprops=dict(marker='o', markerfacecolor='gray', markersize=5, alpha=0.6))

    # Color the boxes
    colors = ['tab:blue', 'tab:orange']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)

    # Plot mean markers
    means = [np.mean(d) for d in data]
    ax.scatter([1, 2], means, color=colors, marker='D', edgecolor='black', zorder=3, label='Mean')

    # horizontal dashed line at overall mean across both sensors
    overall_mean = np.mean(np.concatenate(data))
    ax.axhline(overall_mean, color='gray', linestyle='--', linewidth=1.5, label='Overall mean')

    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Box plot of sensor temperature readings')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    return None

def main(seed: int = 6412):
    """Generate data, create plots, and save a combined figure.

    Parameters
    ----------
    seed : int
        Seed passed to generate_data for reproducible random data. Defaults to
        6412.

    Returns
    -------
    None
        Saves a PNG file named 'sensor_analysis.png' and does not return a value.
    """
    import matplotlib.pyplot as plt

    # Generate data
    sensor_a, sensor_b, timestamps = generate_data(seed)

    # Create a 1x3 subplot figure
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Scatter plot (left)
    plot_scatter(sensor_a, sensor_b, timestamps, axes[0])

    # Histogram (middle)
    plot_histogram(sensor_a, sensor_b, axes[1], bins=30)

    # Box plot (right)
    plot_boxplot(sensor_a, sensor_b, axes[2])

    # Adjust layout and save
    plt.tight_layout()
    fig.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')
    print("Saved 'sensor_analysis.png'")


if __name__ == '__main__':
    main()