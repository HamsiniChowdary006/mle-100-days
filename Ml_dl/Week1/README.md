# Task 1: Arrays, dtype and broadcasting 

## Step 1
- Set up your folder
```powershell

python -m venv .venv
.\.venv\Scripts\activate

python -m pip install numpy pytest

```

- Create these three files:
    - impl.py
    - test_impl.py


## Step 2
- Implement broadcasting from scratch
- The first requirement is to write broadcast_shape(a, b)
- Numpy compare dimensions from right to left. Two dimensions are compatible when:
    - They are equal or,
    - One of them is 1
- If dimensions are incompatible, raises ValueError
- Return the resulting shape as a tuple


## Step 3
- Test the implementation
- Write tests in test_impl.py using pytest
- Test normal broadcasting
- Test shapes with different number of dimensions
- Test scalar shapes and zero-sized dimensions
- Test incompatible shapes
- Comapre the implementation against NumPy on random shape pairs

```py

pythom -m pytest -v

```


## Step 4
- Variation and Experiments
- Demonstrate the difference between NumPy array views and copies




# Task 2: 