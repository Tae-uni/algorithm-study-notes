import timeit
import tracemalloc
from functools import partial

from valid_palindrome_slicing import isPalindrome_slicing
from valid_palindrome_two_pointers import isPalindrome_two_pointers
# Test Data
s = "A man, a plan, a canal: Panama" * 10000
# Check Time Complexity.
execution_time_slicing = min(timeit.repeat(partial(isPalindrome_slicing, s), repeat=20, number=10))
execution_time_pointers = min(timeit.repeat(partial(isPalindrome_two_pointers, s), repeat=20, number=10))
# func Space Complexity.
def memory_usage(func, s):
    tracemalloc.start()
    func(s)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return current / 1024, peak / 1024

memory_slicing = memory_usage(isPalindrome_slicing, s)
memory_pointers = memory_usage(isPalindrome_two_pointers, s)

print(f"Slicing Method: {execution_time_slicing:.6f} sec (min avg)")
print(f"Two Pointers Method: {execution_time_pointers:.6f} sec (min avg)")
print(f"Slicing Memory Usage: {memory_slicing[0]:.6f} KB (current), {memory_slicing[1]:.4f} KB (peak)")
print(f"Two Pointers Memory Usage: {memory_pointers[0]:.6f} KB (current), {memory_pointers[1]:.4f} KB (peak)")
