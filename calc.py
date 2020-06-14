def neuron(x, w, b):
    y = x * w + b
    y = max(0, y)
    return y

if __name__ == "__main__":
    print(f"neuron(4, 1, 3):{neuron(4, 1, 3)}")

