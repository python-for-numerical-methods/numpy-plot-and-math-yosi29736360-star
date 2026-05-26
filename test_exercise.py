import numpy as np

def normalized_array(input_array):
    arr = np.array(input_array, dtype=float)
    
    arr_min = np.min(arr)
    arr_max = np.max(arr)
    
    if arr_min == arr_max:
        return np.zeros_like(arr)
        
    new_array = (arr - arr_min) / (arr_max - arr_min)
    
    return new_array

def test_basic_normalization():
    data = np.array([10, 20, 30])
    result = normalized_array(data)
    expected = np.array([0.0, 0.5, 1.0])
    np.testing.assert_allclose(result, expected, atol=1e-5)

def test_all_same_values():
    # מקרה קצה - כל הערכים זהים
    data = np.array([5, 5, 5])
    result = normalized_array(data)
    expected = np.array([0.0, 0.0, 0.0])
    np.testing.assert_allclose(result, expected, atol=1e-5)

def test_negative_values():
    data = np.array([-10, 0, 10])
    result = normalized_array(data)
    expected = np.array([0.0, 0.5, 1.0])
    np.testing.assert_allclose(result, expected, atol=1e-5)
