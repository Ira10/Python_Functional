import threading
import time

# This is like a helper that counts numbers
def count_numbers():
    for i in range(1, 6):  # Count from 1 to 5
        print(f"Counting: {i}")
        time.sleep(1)  # Wait for 1 second

# This is another helper that prints letters
def print_letters():
    for letter in 'ABCDE':  # Print letters A to E
        print(f"Letter: {letter}")
        time.sleep(1)  # Wait for 1 second

# Making two helpers
count_thread = threading.Thread(target=count_numbers)  # Helper for counting
letter_thread = threading.Thread(target=print_letters)  # Helper for letters

# Start the helpers working
count_thread.start()
letter_thread.start()

# Wait for both helpers to finish
count_thread.join()
letter_thread.join()

print("All done!")



# Counting: 1
# Letter: A
# Counting: 2
# Letter: B
# Counting: 3
# Letter: C
# Letter: D
# Counting: 4
# Counting: 5
# Letter: E
# All done!

## Notice there is no order.