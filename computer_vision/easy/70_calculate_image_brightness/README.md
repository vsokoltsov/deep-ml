# Calculate Image Brightness

## Task: Image Brightness Calculator

In this task, you will implement a function `calculate_brightness(img)` that calculates the average brightness of a grayscale image.

The image is represented as a 2D matrix, where each element represents a pixel value between 0 (black) and 255 (white).

## Your Task:
Implement the function calculate_brightness(img) to:

1. Return the average brightness of the image rounded to two decimal places.
2. Handle edge cases:
    * If the image matrix is empty.
    * If the rows in the matrix have inconsistent lengths.
    * If any pixel values are outside the valid range (0-255).
  

For any of these edge cases, the function should return `-1`.

## Example

### Input

```python
img = [
    [100, 200],
    [50, 150]
]
print(calculate_brightness(img))
```

### Output

```
125.0
```

### Reasoning

The average brightness is calculated as (100 + 200 + 50 + 150) / 4 = 125.0


## Explanation

### Image Brightness Calculator

Consider a grayscale image represented as a 2D matrix where each element represents a pixel value between 0 (black) and 255 (white):

$$
\large Image = 
\begin{pmatrix}
p_{11} \quad p_{12} \\
P_{21} \quad p_{22}
2
\end{pmatrix}
$$


The average brightness is calculated as:

$$
\large Brightness = \frac{\sum_{i=1}^{m} \sum_{i=1}^{n} p_{ij} }{m x n}
$$

Where:

1. $\large p_{ij}$ is the pixl value at position $(i, j)$
2. $\large m$ is the number of rows
3. $\large n$ is the number of columns

#### Things to note

1. All pixel values must be between 0 and 255
2. The image matrix must be well-formed (all rows same length)
3. Empty or invalid images return -1