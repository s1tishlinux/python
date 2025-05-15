# Matplotlib Cheatsheet

## Basic Plot Creation
```python
import matplotlib.pyplot as plt
import numpy as np

# Simple line plot
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()

# Multiple plots on same figure
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.legend()
plt.show()
```

## Figure and Axes
```python
# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, np.sin(x))
ax.set_title('Sine Wave')
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')

# Multiple subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].plot(x, np.sin(x))
axs[0, 1].plot(x, np.cos(x))
axs[1, 0].plot(x, np.tan(x))
axs[1, 1].plot(x, np.exp(x))
fig.tight_layout()
```

## Plot Types
```python
# Scatter plot
plt.scatter(x, np.sin(x), c=x, cmap='viridis')
plt.colorbar()

# Bar plot
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]
plt.bar(categories, values)

# Histogram
data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=30)

# Pie chart
plt.pie([15, 30, 45, 10], labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%')

# Box plot
plt.boxplot([np.random.normal(0, 1, 100), np.random.normal(2, 1, 100)])

# Heatmap
data = np.random.rand(10, 10)
plt.imshow(data, cmap='hot')
plt.colorbar()
```

## Styling and Customization
```python
# Line styles and markers
plt.plot(x, np.sin(x), 'r--', linewidth=2, marker='o', markersize=5)

# Colors
plt.plot(x, np.sin(x), color='#FF8C00')  # Using hex color
plt.plot(x, np.cos(x), color=(0.2, 0.4, 0.6))  # Using RGB tuple

# Text and annotations
plt.plot(x, np.sin(x))
plt.annotate('Peak', xy=(np.pi/2, 1), xytext=(np.pi/2, 1.3),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Grids and spines
plt.grid(True, linestyle='--', alpha=0.7)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Using styles
plt.style.use('ggplot')  # Other options: 'seaborn', 'dark_background', etc.
```

## Live Plotting
```python
import matplotlib.animation as animation

# Method 1: Using FuncAnimation
fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_xlim(0, 100)
ax.set_ylim(-1, 1)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 10, 100)
    y = np.sin(x + i/10)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=100, interval=50, blit=True)
plt.show()

# Method 2: Manual updating with pause
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)
line, = ax.plot(x, np.sin(x))
ax.set_ylim(-1.5, 1.5)

for i in range(100):
    line.set_ydata(np.sin(x + i/10))
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.05)
```

## Saving Plots
```python
# Save as PNG
plt.savefig('plot.png', dpi=300, bbox_inches='tight')

# Save as PDF
plt.savefig('plot.pdf', format='pdf')

# Save as SVG (vector graphics)
plt.savefig('plot.svg', format='svg')
```

## 3D Plotting
```python
from mpl_toolkits.mplot3d import Axes3D

# 3D line plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
t = np.linspace(0, 20, 100)
x = np.cos(t)
y = np.sin(t)
z = t
ax.plot(x, y, z)

# 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
surf = ax.plot_surface(X, Y, Z, cmap='viridis')
fig.colorbar(surf)
```