def group_numbers_into_ranges(numbers, range_size=10):
    # Create a dictionary to hold the counts for each range
    ranges = {}
    
    # Determine the minimum and maximum values from the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Create ranges and initialize counts to zero
    for start in range(min_value, max_value + 1, range_size):
        end = start + range_size - 1
        ranges[f"{start}-{end}"] = 0
    
    # Count the numbers in each range
    for number in numbers:
        # Find the appropriate range for the number
        range_start = (number // range_size) * range_size
        range_end = range_start + range_size - 1
        
        # Update the count for the corresponding range
        ranges[f"{range_start}-{range_end}"] += 1
    
    return ranges

# Example usage
if __name__ == "__main__":
    numbers = [1, 5, 12, 15, 22, 25, 30, 35, 40, 45, 50]
    result = group_numbers_into_ranges(numbers)
    
    # Print the results
    for r_range, count in result.items():
        print(f"Range {r_range}: {count} elements")