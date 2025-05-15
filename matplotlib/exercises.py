#!/usr/bin/env python3
"""
Matplotlib Exercises

This file contains exercises to practice using Matplotlib.
Each exercise includes a problem statement and a solution.
"""

import matplotlib.pyplot as plt
import numpy as np

def exercise_1():
    """
    Exercise 1: Basic Line Plot
    
    Create a line plot of y = x^2 for x values from -10 to 10.
    Add appropriate title, labels, and grid.
    """
    print("\nExercise 1: Basic Line Plot")
    print("Problem: Create a line plot of y = x^2 for x values from -10 to 10.")
    
    # Your solution here
    
    # Solution
    x = np.linspace(-10, 10, 100)
    y = x**2
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2)
    plt.title('y = x²')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def exercise_2():
    """
    Exercise 2: Multiple Lines
    
    On the same plot, show the following functions:
    - y = x^2
    - y = x^3
    - y = x^4
    
    Use different colors and line styles, and add a legend.
    """
    print("\nExercise 2: Multiple Lines")
    print("Problem: Plot y = x^2, y = x^3, and y = x^4 on the same graph.")
    
    # Your solution here
    
    # Solution
    x = np.linspace(-2, 2, 100)
    y1 = x**2
    y2 = x**3
    y3 = x**4
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, 'b-', linewidth=2, label='y = x²')
    plt.plot(x, y2, 'r--', linewidth=2, label='y = x³')
    plt.plot(x, y3, 'g-.', linewidth=2, label='y = x⁴')
    plt.title('Polynomial Functions')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def exercise_3():
    """
    Exercise 3: Scatter Plot
    
    Create a scatter plot of 100 random points.
    The x and y coordinates should be normally distributed.
    Color the points based on their distance from the origin.
    """
    print("\nExercise 3: Scatter Plot")
    print("Problem: Create a scatter plot of 100 random points with color based on distance from origin.")
    
    # Your solution here
    
    # Solution
    # Generate random data
    np.random.seed(42)  # For reproducibility
    x = np.random.normal(0, 1, 100)
    y = np.random.normal(0, 1, 100)
    
    # Calculate distance from origin
    distance = np.sqrt(x**2 + y**2)
    
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(x, y, c=distance, cmap='viridis', 
                         s=100, alpha=0.7)
    plt.colorbar(scatter, label='Distance from Origin')
    plt.title('Scatter Plot with Color Mapping')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True, alpha=0.3)
    plt.axis('equal')  # Equal scaling
    plt.tight_layout()
    plt.show()

def exercise_4():
    """
    Exercise 4: Bar Chart
    
    Create a bar chart showing the following data:
    - Python: 35%
    - Java: 25%
    - JavaScript: 20%
    - C++: 15%
    - Other: 5%
    
    Add value labels on top of each bar.
    """
    print("\nExercise 4: Bar Chart")
    print("Problem: Create a bar chart showing programming language popularity.")
    
    # Your solution here
    
    # Solution
    languages = ['Python', 'Java', 'JavaScript', 'C++', 'Other']
    percentages = [35, 25, 20, 15, 5]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(languages, percentages, color='skyblue', edgecolor='navy')
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height}%', ha='center', va='bottom')
    
    plt.title('Programming Language Popularity')
    plt.xlabel('Language')
    plt.ylabel('Percentage (%)')
    plt.ylim(0, max(percentages) + 5)  # Add some space for labels
    plt.grid(True, axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()

def exercise_5():
    """
    Exercise 5: Subplots
    
    Create a 2x2 grid of subplots showing:
    1. A line plot of sin(x)
    2. A scatter plot of random data
    3. A bar chart
    4. A histogram
    """
    print("\nExercise 5: Subplots")
    print("Problem: Create a 2x2 grid of different plot types.")
    
    # Your solution here
    
    # Solution
    # Create figure and subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. Line plot
    x = np.linspace(0, 10, 100)
    axs[0, 0].plot(x, np.sin(x), 'b-')
    axs[0, 0].set_title('Sine Wave')
    axs[0, 0].set_xlabel('x')
    axs[0, 0].set_ylabel('sin(x)')
    axs[0, 0].grid(True)
    
    # 2. Scatter plot
    np.random.seed(42)
    x_scatter = np.random.rand(50)
    y_scatter = np.random.rand(50)
    axs[0, 1].scatter(x_scatter, y_scatter, c=np.random.rand(50), cmap='plasma')
    axs[0, 1].set_title('Random Scatter')
    axs[0, 1].set_xlabel('x')
    axs[0, 1].set_ylabel('y')
    
    # 3. Bar chart
    categories = ['A', 'B', 'C', 'D']
    values = [3, 7, 2, 5]
    axs[1, 0].bar(categories, values, color='lightgreen')
    axs[1, 0].set_title('Bar Chart')
    axs[1, 0].set_xlabel('Category')
    axs[1, 0].set_ylabel('Value')
    
    # 4. Histogram
    data = np.random.normal(0, 1, 1000)
    axs[1, 1].hist(data, bins=30, color='lightblue', edgecolor='blue')
    axs[1, 1].set_title('Histogram')
    axs[1, 1].set_xlabel('Value')
    axs[1, 1].set_ylabel('Frequency')
    
    # Adjust layout
    fig.tight_layout()
    plt.show()

def exercise_6():
    """
    Exercise 6: 3D Plot
    
    Create a 3D surface plot of the function:
    z = sin(sqrt(x^2 + y^2))
    """
    print("\nExercise 6: 3D Plot")
    print("Problem: Create a 3D surface plot of z = sin(sqrt(x^2 + y^2)).")
    
    # Your solution here
    
    # Solution
    from mpl_toolkits.mplot3d import Axes3D
    
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
    ax.set_title('z = sin(sqrt(x^2 + y^2))')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # Add colorbar
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    
    plt.tight_layout()
    plt.show()

def exercise_7():
    """
    Exercise 7: Customization
    
    Create a highly customized plot with:
    - Custom colors and line styles
    - Text annotations
    - Custom tick marks
    - A legend
    - Modified spines
    """
    print("\nExercise 7: Customization")
    print("Problem: Create a highly customized plot.")
    
    # Your solution here
    
    # Solution
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Plot with custom styles
    ax.plot(x, y1, color='#8A2BE2', linestyle='-', linewidth=2, 
           marker='o', markevery=10, markersize=8, label='sin(x)')
    ax.plot(x, y2, color='#FF8C00', linestyle='--', linewidth=2, 
           marker='s', markevery=10, markersize=8, label='cos(x)')
    
    # Set title and labels with custom fonts
    ax.set_title('Customized Trigonometric Functions', fontsize=16, fontweight='bold')
    ax.set_xlabel('Angle (radians)', fontsize=12)
    ax.set_ylabel('Value', fontsize=12)
    
    # Set custom tick marks
    ax.set_xticks(np.arange(0, 11, np.pi/2))
    ax.set_xticklabels(['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$', r'$5\pi/2$'])
    
    # Add grid with custom style
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Add text annotations
    ax.text(np.pi/2, 1.1, 'sin(x) = 1', fontsize=10, 
           bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))
    ax.text(np.pi, -1.1, 'cos(x) = -1', fontsize=10, 
           bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))
    
    # Add arrow annotations
    ax.annotate('Local Maximum', xy=(np.pi/2, 1), xytext=(np.pi/2 - 1, 1.3),
               arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))
    
    # Customize spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    
    # Add horizontal and vertical lines
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=np.pi, color='k', linestyle='-', alpha=0.3)
    
    # Add legend
    ax.legend(loc='upper right', fontsize=12, frameon=True, 
             facecolor='white', edgecolor='gray')
    
    plt.tight_layout()
    plt.show()

def main():
    """Run all exercises."""
    print("Matplotlib Exercises")
    print("===================")
    
    # List of exercises
    exercises = [
        exercise_1,
        exercise_2,
        exercise_3,
        exercise_4,
        exercise_5,
        exercise_6,
        exercise_7
    ]
    
    # Run each exercise
    for i, exercise in enumerate(exercises, 1):
        input(f"\nPress Enter to run Exercise {i}...")
        exercise()
    
    print("\nAll exercises completed!")

if __name__ == "__main__":
    main()