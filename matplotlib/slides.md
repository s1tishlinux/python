# Matplotlib
## The Python Visualization Library

---

## What is Matplotlib?

- Comprehensive visualization library for Python
- Created by John Hunter in 2003
- Inspired by MATLAB's plotting capabilities
- Foundation for many other visualization libraries
- Publication-quality figures

---

## Basic Structure

```
Figure
  └── Axes (one or more)
       ├── Title
       ├── X-axis (label, ticks, scale)
       ├── Y-axis (label, ticks, scale)
       └── Plot elements (lines, markers, text, etc.)
```

---

## Two Interfaces

### Pyplot Interface (MATLAB-style)
```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
```

### Object-Oriented Interface
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4])
ax.set_ylabel('some numbers')
plt.show()
```

---

## Basic Line Plot

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()
```

---

## Multiple Lines

```python
plt.figure(figsize=(10, 6))
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.plot(x, np.sin(x+np.pi/4), label='sin(x+π/4)')
plt.title('Multiple Sine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
```

---

## Customizing Line Styles

```python
plt.figure(figsize=(10, 6))
plt.plot(x, np.sin(x), 'r-', linewidth=2, label='sin(x)')
plt.plot(x, np.cos(x), 'b--', linewidth=2, label='cos(x)')
plt.plot(x, np.sin(x+np.pi/4), 'g-.', linewidth=2, label='sin(x+π/4)')
plt.title('Customized Line Styles')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
```

---

## Scatter Plots

```python
plt.figure(figsize=(10, 6))
plt.scatter(x, np.sin(x), c=x, cmap='viridis', 
           s=100*np.random.rand(len(x)))
plt.colorbar(label='x value')
plt.title('Scatter Plot with Color Mapping')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()
```

---

## Bar Charts

```python
categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 2, 5, 9]

plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='skyblue', edgecolor='navy')
plt.title('Simple Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
```

---

## Histograms

```python
data = np.random.normal(0, 1, 1000)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, alpha=0.7, color='skyblue', 
        edgecolor='black')
plt.title('Histogram of Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.show()
```

---

## Subplots

```python
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# First subplot
axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title('Sine Wave')

# Second subplot
axs[0, 1].scatter(x, np.random.rand(len(x)))
axs[0, 1].set_title('Scatter Plot')

# Third subplot
axs[1, 0].bar(categories, values)
axs[1, 0].set_title('Bar Chart')

# Fourth subplot
axs[1, 1].hist(data, bins=20)
axs[1, 1].set_title('Histogram')

fig.tight_layout()
plt.show()
```

---

## 3D Plotting

```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Create data
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Plot surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_title('3D Surface Plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
fig.colorbar(surf)
plt.show()
```

---

## Animation

```python
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(0, 2*np.pi, 100)
line, = ax.plot(x, np.sin(x))
ax.set_ylim(-1.2, 1.2)

def animate(i):
    line.set_ydata(np.sin(x + i/10))
    return line,

ani = animation.FuncAnimation(
    fig, animate, frames=100, interval=50, blit=True)
plt.show()
```

---

## Saving Figures

```python
# Save as PNG with high resolution
plt.savefig('figure.png', dpi=300, bbox_inches='tight')

# Save as PDF (vector format)
plt.savefig('figure.pdf', format='pdf', bbox_inches='tight')

# Save as SVG (vector format)
plt.savefig('figure.svg', format='svg', bbox_inches='tight')
```

---

## Best Practices

- Use the object-oriented interface for complex plots
- Always label your axes and include a title
- Choose appropriate plot types for your data
- Use colormaps wisely (consider colorblind-friendly options)
- Keep plots simple and focused
- Use vectorized operations for better performance
- Consider figure size and aspect ratio

---

## Thank You!

### Questions?