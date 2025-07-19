import test_rust_in_python
from fibonacci_matrix_exponentiation import python_nth_fibonacci_using_matrix_exponentiation

def python_runtime_benchmark(nth_term: int):
    for n in range(nth_term):
        python_nth_fibonacci_using_matrix_exponentiation(n)


def rust_runtime_benchmark(nth_term: int):
    test_rust_in_python.rust_runtime_benchmark(nth_term)  # type: ignore