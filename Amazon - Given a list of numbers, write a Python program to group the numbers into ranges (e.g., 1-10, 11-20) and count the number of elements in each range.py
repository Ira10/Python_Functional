def group_numbers_into_ranges(numbers, range_size):
    # Find the minimum and maximum of the numbers
    min_num = min(numbers)
    max_num = max(numbers)
    
    # Initialize a dictionary to store the range and counts
    range_counts = {}
    
    # Create ranges from min_num to max_num
    for start in range(min_num, max_num + 1, range_size):
        end = start + range_size - 1
        range_key = f"{start}-{end}"
        range_counts[range_key] = 0
    
    # Count how many numbers fall into each range
    for num in numbers:
        for start in range(min_num, max_num + 1, range_size):
            end = start + range_size - 1
            if start <= num <= end:
                range_key = f"{start}-{end}"
                range_counts[range_key] += 1
                break
    
    return range_counts

# Example usage
numbers = [5, 8, 15, 23, 17, 9, 35, 12, 44, 25]
range_size = 10
result = group_numbers_into_ranges(numbers, range_size)

# Display the result
for r, count in result.items():
    print(f"Range {r}: {count} numbers")
