import test_rust_in_python
from fibonacci_matrix_exponentiation import python_nth_fibonacci_using_matrix_exponentiation


RUST_FUNCTIONS = test_rust_in_python

rust_fibonacci_reuslt = RUST_FUNCTIONS.rust_nth_fibonacci_using_matrix_exponentiation(93) # type: ignore

print(f"Result from Rust: {rust_fibonacci_reuslt}")


python_fibonacci_reuslt = python_nth_fibonacci_using_matrix_exponentiation(93)
print(f"Result from Python: {python_fibonacci_reuslt}")