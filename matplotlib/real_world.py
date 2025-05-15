#!/usr/bin/env python3
"""
Matplotlib Real-World Examples

This script demonstrates practical applications of Matplotlib
in various domains like data science, finance, and scientific visualization.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.dates import DateFormatter
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Set a seed for reproducibility
np.random.seed(42)

def data_science_example():
    """Example of data visualization for data science."""
    print("\n=== Data Science Visualization ===")
    
    # Create sample data (simulating a dataset)
    categories = ['Category A', 'Category B', 'Category C', 'Category D']
    values = [15, 34, 23, 28]
    
    # Create a horizontal bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot horizontal bars
    bars = ax.barh(categories, values, color='skyblue', edgecolor='navy')
    
    # Add data labels
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 1, bar.get_y() + bar.get_height()/2, 
                f'{width}', ha='left', va='center')
    
    # Add title and labels
    ax.set_title('Sample Data Distribution by Category', fontsize=14)
    ax.set_xlabel('Value', fontsize=12)
    ax.set_ylabel('Category', fontsize=12)
    
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Add grid lines
    ax.grid(True, axis='x', linestyle='--', alpha=0.7)
    
    # Show plot
    plt.tight_layout()
    plt.show()
    
    print("Data science visualization example completed.")

def financial_data_example():
    """Example of financial data visualization."""
    print("\n=== Financial Data Visualization ===")
    
    # Generate sample stock price data
    days = 100
    dates = pd.date_range(start='2023-01-01', periods=days)
    
    # Simulate stock prices with random walk
    price_a = 100 + np.cumsum(np.random.normal(0.1, 1, days))
    price_b = 80 + np.cumsum(np.random.normal(0.05, 1.2, days))
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot stock prices
    ax.plot(dates, price_a, 'b-', linewidth=1.5, label='Stock A')
    ax.plot(dates, price_b, 'r-', linewidth=1.5, label='Stock B')
    
    # Add title and labels
    ax.set_title('Stock Price Comparison', fontsize=14)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Price ($)', fontsize=12)
    
    # Format x-axis date labels
    date_format = DateFormatter('%Y-%m-%d')
    ax.xaxis.set_major_formatter(date_format)
    plt.xticks(rotation=45)
    
    # Add grid
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Add legend
    ax.legend()
    
    # Highlight specific events
    event_date = dates[50]
    ax.axvline(x=event_date, color='green', linestyle='--', alpha=0.7)
    ax.text(event_date, max(price_a.max(), price_b.max()) + 5, 
            'Market Event', rotation=90, va='top')
    
    # Show plot
    plt.tight_layout()
    plt.show()
    
    print("Financial data visualization example completed.")

def scientific_visualization_example():
    """Example of scientific data visualization."""
    print("\n=== Scientific Visualization ===")
    
    # Create sample data for a heatmap (e.g., temperature distribution)
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2)) * np.exp(-0.1 * (X**2 + Y**2))
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create heatmap
    im = ax.imshow(Z, extent=[-5, 5, -5, 5], origin='lower', 
                  cmap='viridis', aspect='auto')
    
    # Add contour lines
    contours = ax.contour(X, Y, Z, colors='white', alpha=0.5, linewidths=0.5)
    ax.clabel(contours, inline=True, fontsize=8, fmt='%.1f')
    
    # Add colorbar
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label('Value', rotation=270, labelpad=15)
    
    # Add title and labels
    ax.set_title('2D Field Visualization', fontsize=14)
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    
    # Show plot
    plt.tight_layout()
    plt.show()
    
    print("Scientific visualization example completed.")

def geographic_data_example():
    """Example of geographic data visualization."""
    print("\n=== Geographic Data Visualization ===")
    print("(Note: This is a simplified example without actual map data)")
    
    # Create sample data for cities (longitude, latitude, population)
    cities = {
        'City A': (-74.0, 40.7, 8.4),  # lon, lat, pop (millions)
        'City B': (-118.2, 34.0, 3.9),
        'City C': (-87.6, 41.8, 2.7),
        'City D': (-95.4, 29.8, 2.3),
        'City E': (-122.4, 37.8, 0.9)
    }
    
    # Extract data
    lons = [city[0] for city in cities.values()]
    lats = [city[1] for city in cities.values()]
    pops = [city[2] for city in cities.values()]
    names = list(cities.keys())
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create scatter plot
    scatter = ax.scatter(lons, lats, s=[p*50 for p in pops], 
                        c=pops, cmap='YlOrRd', alpha=0.7)
    
    # Add city labels
    for i, name in enumerate(names):
        ax.annotate(name, (lons[i], lats[i]), 
                   xytext=(5, 5), textcoords='offset points')
    
    # Add colorbar
    cbar = fig.colorbar(scatter)
    cbar.set_label('Population (millions)')
    
    # Add title and labels
    ax.set_title('City Population Distribution', fontsize=14)
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)
    
    # Set aspect ratio to be equal
    ax.set_aspect('equal')
    
    # Add grid
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Show plot
    plt.tight_layout()
    plt.show()
    
    print("Geographic data visualization example completed.")

def time_series_analysis_example():
    """Example of time series data analysis visualization."""
    print("\n=== Time Series Analysis Visualization ===")
    
    # Generate sample time series data
    days = 365
    dates = pd.date_range(start='2023-01-01', periods=days)
    
    # Create seasonal data with trend and noise
    t = np.arange(days)
    trend = 0.05 * t
    seasonal = 10 * np.sin(2 * np.pi * t / 365)
    noise = np.random.normal(0, 1, days)
    data = trend + seasonal + noise
    
    # Create figure with subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
    
    # Plot original time series
    ax1.plot(dates, data, 'b-', linewidth=1, alpha=0.7)
    ax1.set_title('Time Series Data', fontsize=14)
    ax1.set_ylabel('Value', fontsize=12)
    ax1.grid(True, linestyle='--', alpha=0.7)
    
    # Calculate and plot moving average
    window_size = 30
    moving_avg = np.convolve(data, np.ones(window_size)/window_size, mode='valid')
    ma_dates = dates[window_size-1:]
    
    ax2.plot(dates, data, 'b-', linewidth=1, alpha=0.3, label='Original')
    ax2.plot(ma_dates, moving_avg, 'r-', linewidth=2, label=f'{window_size}-Day Moving Average')
    ax2.set_title('Time Series with Moving Average', fontsize=14)
    ax2.set_xlabel('Date', fontsize=12)
    ax2.set_ylabel('Value', fontsize=12)
    ax2.grid(True, linestyle='--', alpha=0.7)
    ax2.legend()
    
    # Format x-axis date labels
    date_format = DateFormatter('%Y-%m-%d')
    ax2.xaxis.set_major_formatter(date_format)
    plt.xticks(rotation=45)
    
    # Show plot
    plt.tight_layout()
    plt.show()
    
    print("Time series analysis visualization example completed.")

def main():
    """Main function to run all examples."""
    print("Matplotlib Real-World Examples")
    print("=============================")
    print("This script demonstrates practical applications of Matplotlib.")
    print("Close each plot window to proceed to the next example.")
    
    # Run examples
    data_science_example()
    financial_data_example()
    scientific_visualization_example()
    geographic_data_example()
    time_series_analysis_example()
    
    print("\nAll examples completed!")

if __name__ == "__main__":
    main()