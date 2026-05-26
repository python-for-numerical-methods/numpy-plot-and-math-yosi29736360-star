import numpy as np
import pytest
from normalized_array import normalized_array  # מייבא את הפונקציה מהקובץ של הסטודנט

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
