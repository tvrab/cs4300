import numpy as np

# Function to calculate the mean and standard deviation of a list using NumPy
def calculate_statistics(numbers):
    
    # Check to see if the input is empty and raise an error if so
    if not numbers:
        raise ValueError("Input list cannot be empty.")

    # Return the mean and std using numpy
    return {
        "mean": float(np.mean(numbers)),
        "std": float(np.std(numbers))
    }

if __name__ == "__main__":
    sample_data = [10, 20, 30, 40, 50]
    print(calculate_statistics(sample_data))