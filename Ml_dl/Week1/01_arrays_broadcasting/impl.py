def broadcast_shape(a, b):
    result = []

    # Step 1: Find the maximum number of dimensions
    max_dims = max(len(a), len(b))

    # Step 2: Compare dimesions from right to left
    for i in range(max_dims):

        # Step 3: Get dimensions; use 1 if missing
        if i < len(a):
            dim_a = a[-(i + 1)]
        else:
            dim_a = 1
        if i < len(b):
            dim_b = b[-(i + 1)]
        else:
            dim_b = 1

        # Step 4: Check compatibility
        if dim_a == dim_b:
            dim = dim_a
        elif dim_a == 1:
            dim = dim_b
        elif dim_b == 1:
            dim = dim_a
        else:
            raise ValueError (
                f"Shapes {a} and {b} are not compatible"
            )

        # Step 5: Store the resulting dimensions
        result.append(dim)

    return tuple(result[::-1])

"""

print(broadcast_shape((3, 1), (1, 4)))  # (3, 4)
print(broadcast_shape((5, 3), (3,)))    # (5, 3)
print(broadcast_shape((4, 1, 3), (2, 3)))  # (4, 2, 3)
print(broadcast_shape((), (2, 3)))      # (2, 3)

print(broadcast_shape((2, 3), (4, 3)))  # Raises ValueError

"""

    
