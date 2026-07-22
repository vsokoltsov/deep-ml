import math

def sigmoid(z: float) -> float:
    
    return (1 / (1 + math.exp(-z)))

if __name__ == '__main__':
    print(sigmoid(0), 0.5)