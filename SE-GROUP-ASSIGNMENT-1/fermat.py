def get_input_in_range(min_val, max_val):
    while True:
        try:
            input_value = int(input())
            if min_val <= input_value <= max_val:
                return input_value
            else:
                print(f"Invalid value. Please enter a value between {min_val} and {max_val}: ")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def find_relative_miss(x, y, z, n):
    z_val = z ** n
    xy_val = x ** n + y ** n
    return abs(1.0 - xy_val / z_val)

def find_actual_miss(x, y, z, n):
    z_val = z ** n
    xy_val = x ** n + y ** n
    return xy_val - z_val

def find_near_misses(k, n):
    global smallest_relative_miss  # Declare smallest_relative_miss as a global variable
    smallest_relative_miss = float('inf')

    for x in range(10, k + 1):
        for y in range(x, k + 1):
            close_val = float('inf')
            z = (x + y) // 2

            if z > k:
                z = k
                print_result_values(x, y, z, find_relative_miss(x, y, z, n), n)
                continue

            while z <= k:
                near = find_relative_miss(x, y, z, n)
                if near > close_val:
                    break

                close_val = near
                z += 1
            z -= 1

            print_result_values(x, y, z, close_val, n)
            if x != y:
                print_result_values(y, x, z, close_val, n)

def print_result_values(x, y, z, close_val, n):
    rel_miss = close_val

    global smallest_relative_miss
    if smallest_relative_miss > rel_miss:
        smallest_relative_miss = rel_miss
        print("\nNew Smallest Relative Miss:")
        print(f"x: {x}, y: {y}, z: {z}")
        print("Relative Miss (Ratio):", 1 + close_val)
        print("Actual Miss:", find_actual_miss(x, y, z, n))

if __name__ == "__main__":
    print("Finding Fermat's Last Theorem Near Misses")
    n = get_input_in_range(3, 11)
    k_upper_limit = 50
    print(f"Enter the value of k (should be greater than 10 and less than {k_upper_limit}):")
    k = get_input_in_range(11, k_upper_limit)

    find_near_misses(k, n)
