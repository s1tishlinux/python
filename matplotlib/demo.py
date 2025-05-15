#!/usr/bin/env python3
"""
Matplotlib Demo Script

This script demonstrates the core functionality of Matplotlib,
from basic plotting to advanced features.
"""

import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

def basic_line_plot():
    """Create a basic line plot with labels and grid."""
    print("\n=== Basic Line Plot ===")
    
    # Create data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title('Sine Wave')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.grid(True)
    
    # Show plot
    plt.tight_layout()
    plt.show()
    
    print("Basic line plot demonstrated.")

def multiple_lines():
    """Plot multiple lines with a legend."""
    print("\n=== Multiple Lines ===")
    
    # Create data
    x = np.linspace(0, 10, 100)
    
    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, np.sin(x), label='sin(x)')
    plt.plot(x, np.cos(x), label='cos(x)')
    plt.plot(x, np.sin(x+np.pi/4), label='sin(x+π/4)')
    plt.title('Multiple Sine Waves')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    
    # Show plot
    plt.tight_layout()
    plt.show()
    
    print("Multiple lines demonstrated.")

def line_styles_and_markers():
    """Demonstrate different line styles and markers."""
    print("\n=== Line Styles and Markers ===")
    
    # Create data
    x = np.linspace(0, 10, 20)  # Fewer points to see markers better
    
    # Create plot
    plt.figure(figsize=(12, 8))
    
    # Different line styles
    plt.plot(x, np.sin(x), 'r-', linewidth=2, label='Solid red')
    plt.plot(x, np.sin(x)+0.5, 'g--', linewidth=2, label='Dashed green')
    plt.plot(x, np.sin(x)+1.0, 'b-.', linewidth=2, label='Dash-dot blue')
    plt.plot(x, np.sin(x)+1.5, 'k:', linewidth=2, label='Dotted black')
    
    # Different markers
    plt.plot(x, np.sin(x)-0.5, 'co-', linewidth=1, markersize=8, label='Circles')
    plt.plot(x, np.sin(x)-1.0, 'ms-', linewidth=1, markersize=8, label='Squares')
    plt.plot(x, np.sin(x)-1.5, 'y^-', linewidth=1, markersize=8, label='Triangles')
    plt.plot(x, np.sin(x)-2.0, 'gD-', linewidth=1, markersize=8, label='Diamonds')
    
    plt.title('Line Styles and Markers')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.grid(True)
    
    # Show plot
    plt.tight_layout()
    plt.show()
    
    print("Line styles and markers demonstrated.")

def scatter_plot():
    """Create a scatter plot with color mapping."""
    print("\n=== Scatter Plot ===")
    
    # Create data
    x = np.random.rand(100)
    y = np.random.rand(100)
    colors = np.random.rand(100)
    sizes = 1000 * np.random.rand(100)
    
    # Create plot
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
    plt.colorbar(scatter, label='Color Value')
    plt.title('Scatter Plot with Color Mapping')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, alpha=0.3)
    
    # Show plot
    plt.tight_layout()
    plt.show()
    
    print("Scatter plot demonstrated.")

def bar_chart():
    """Create a simple bar chart."""
    print("\n=== Bar Chart ===")
    
    # Create data
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [3, 7, 2, 5, 9]
    
    # Create plot
    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color='skyblue', edgecolor='navy')
    plt.title('Simple Bar Chart')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.grid(True, axis='y', alpha=0.3)
    
    # Add value labels on top of bars
    for i, v in enumerate(values):
        plt.text(i, v + 0.1, str(v), ha='center')
    
    # Show plot
    plt.tight_layout()
    plt.show()
    
    print("Bar chart demonstrated.")

def histogram():
    """Create a histogram."""
    print("\n=== Histogram ===")
    
    # Create data
    data = np.random.normal(0, 1, 1000)
    
    # Create plot
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title('Histogram of Normal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    
    # Add mean and std lines
    plt.axvline(data.mean(), color='red', linestyle='dashed', linewidth=1, label=f'Mean: {data.mean():.2f}')
    plt.axvline(data.mean() + data.std(), color='green', linestyle='dashed', linewidth=1, label=f'Mean + Std: {data.mean() + data.std():.2f}')
    plt.axvline(data.mean() - data.std(), color='green', linestyle='dashed', linewidth=1, label=f'Mean - Std: {data.mean() - data.std():.2f}')
    plt.legend()
    
    # Show plot
    plt.tight_layout()
    plt.show()
    
    print("Histogram demonstrated.")

def pie_chart():
    """Create a pie chart."""
    print("\n=== Pie Chart ===")
    
    # Create data
    labels = ['A', 'B', 'C', 'D', 'E']
    sizes = [15, 30, 45, 10, 25]
    explode = (0, 0.1, 0, 0, 0.1)  # explode 2nd & 5th slice
    
    # Create plot
    plt.figure(figsize=(10, 8))
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, colors=plt.cm.Paired.colors)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title('Pie Chart')
    
    # Show plot
    plt.tight_layout()
    plt.show()
    
    print("Pie chart demonstrated.")

def subplots_demo():
    """Create multiple subplots in one figure."""
    print("\n=== Subplots ===")
    
    # Create data
    x = np.linspace(0, 10, 100)
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [3, 7, 2, 5, 9]
    
    # Create figure and subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    
    # First subplot - Line plot
    axs[0, 0].plot(x, np.sin(x))
    axs[0, 0].set_title('Sine Wave')
    axs[0, 0].set_xlabel('x')
    axs[0, 0].set_ylabel('sin(x)')
    axs[0, 0].grid(True)
    
    # Second subplot - Scatter plot
    axs[0, 1].scatter(x[::5], np.cos(x[::5]), c=x[::5], cmap='plasma')
    axs[0, 1].set_title('Scatter Plot')
    axs[0, 1].set_xlabel('x')
    axs[0, 1].set_ylabel('cos(x)')
    
    # Third subplot - Bar chart
    axs[1, 0].bar(categories, values, color='lightgreen', edgecolor='darkgreen')
    axs[1, 0].set_title('Bar Chart')
    axs[1, 0].set_xlabel('Categories')
    axs[1, 0].set_ylabel('Values')
    axs[1, 0].grid(True, axis='y', alpha=0.3)
    
    # Fourth subplot - Histogram
    data = np.random.normal(0, 1, 1000)
    axs[1, 1].hist(data, bins=20, color='lightblue', edgecolor='blue')
    axs[1, 1].set_title('Histogram')
    axs[1, 1].set_xlabel('Value')
    axs[1, 1].set_ylabel('Frequency')
    axs[1, 1].grid(True, alpha=0.3)
    
    # Adjust layout
    fig.tight_layout()
    plt.show()
    
    print("Subplots demonstrated.")

def three_d_plot():
    """Create a 3D surface plot."""
    print("\n=== 3D Plot ===")
    
    # Create data
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    
    # Create 3D plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot surface
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    
    # Add labels and title
    ax.set_title('3D Surface Plot')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # Add colorbar
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    
    # Show plot
    plt.tight_layout()
    plt.show()
    
    print("3D plot demonstrated.")

def animation_demo():
    """Create a simple animation."""
    print("\n=== Animation ===")
    print("Close the plot window to continue...")
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create data
    x = np.linspace(0, 2*np.pi, 100)
    line, = ax.plot(x, np.sin(x))
    
    # Set axis limits
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1.2, 1.2)
    
    # Add title and labels
    ax.set_title('Sine Wave Animation')
    ax.set_xlabel('x')
    ax.set_ylabel('sin(x)')
    ax.grid(True)
    
    # Define update function for animation
    def update(frame):
        line.set_ydata(np.sin(x + frame/10))
        return line,
    
    # Create animation
    ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
    
    # Show animation
    plt.tight_layout()
    plt.show()
    
    print("Animation demonstrated.")

def live_plotting_demo():
    """Demonstrate live plotting with manual updates."""
    print("\n=== Live Plotting ===")
    print("This will run for 5 seconds. Watch the plot update in real-time...")
    
    # Turn on interactive mode
    plt.ion()
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create initial plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    line, = ax.plot(x, y)
    
    # Set axis limits
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.5, 1.5)
    
    # Add title and labels
    ax.set_title('Live Plotting Demo')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    
    # Update plot in real-time
    start_time = time.time()
    while time.time() - start_time < 5:  # Run for 5 seconds
        # Update data
        phase = (time.time() - start_time) * 2
        y = np.sin(x + phase)
        
        # Update plot
        line.set_ydata(y)
        
        # Redraw plot
        fig.canvas.draw()
        fig.canvas.flush_events()
        
        # Small pause to control update rate
        plt.pause(0.05)
    
    # Turn off interactive mode
    plt.ioff()
    plt.close()
    
    print("Live plotting demonstrated.")

def customization_demo():
    """Demonstrate various plot customization options."""
    print("\n=== Plot Customization ===")
    
    # Create data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    # Create figure and axis with specific size
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Plot data with custom styles
    ax.plot(x, y1, 'b-', linewidth=2, label='sin(x)')
    ax.plot(x, y2, 'r--', linewidth=2, label='cos(x)')
    
    # Set title with custom font size
    ax.set_title('Customized Plot Example', fontsize=16, fontweight='bold')
    
    # Set axis labels with custom font size
    ax.set_xlabel('x-axis', fontsize=12)
    ax.set_ylabel('y-axis', fontsize=12)
    
    # Set custom axis limits
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.5, 1.5)
    
    # Add grid with custom style
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Customize tick marks
    ax.tick_params(axis='both', which='major', labelsize=10)
    
    # Add legend with custom location and style
    ax.legend(loc='upper right', fontsize=12, frameon=True, facecolor='white', edgecolor='gray')
    
    # Add text annotation
    ax.text(5, 1.2, 'Important Point', fontsize=12, 
            bbox=dict(facecolor='yellow', alpha=0.5))
    
    # Add arrow annotation
    ax.annotate('Local Maximum', xy=(1.5, 1), xytext=(3, 1.3),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))
    
    # Customize spines (the box around the plot)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    
    # Add a horizontal line
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    
    # Add a vertical line
    ax.axvline(x=5, color='k', linestyle='-', alpha=0.3)
    
    # Add a horizontal span
    ax.axhspan(0.5, 1, alpha=0.2, color='green')
    
    # Add a vertical span
    ax.axvspan(7, 8, alpha=0.2, color='red')
    
    # Show plot
    plt.tight_layout()
    plt.show()
    
    print("Plot customization demonstrated.")

def main():
    """Main function to run all demonstrations."""
    print("Matplotlib Demonstration Script")
    print("===============================")
    print("This script demonstrates various plotting capabilities of Matplotlib.")
    print("Close each plot window to proceed to the next demonstration.")
    
    # Run demonstrations
    basic_line_plot()
    multiple_lines()
    line_styles_and_markers()
    scatter_plot()
    bar_chart()
    histogram()
    pie_chart()
    subplots_demo()
    three_d_plot()
    customization_demo()
    animation_demo()
    live_plotting_demo()
    
    print("\nAll demonstrations completed!")

if __name__ == "__main__":
    main()