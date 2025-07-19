use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// A Python module implemented in Rust.
#[pymodule]
fn test_rust_in_python(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(rust_nth_fibonacci_using_matrix_exponentiation, m)?)?;
    m.add_function(wrap_pyfunction!(rust_runtime_benchmark, m)?)?;
    Ok(())
}

// Calculates the nth Fibonacci number using matrix exponentiation.
// The Fibonacci sequence is defined as:
// F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n >= 2
// The nth Fibonacci number can be computed using matrix exponentiation in O(log n) time.
#[pyfunction]
fn rust_nth_fibonacci_using_matrix_exponentiation(n: u64) -> u64 {
    if n == 0 {
        0
    } else {
        let base: [u64; 4] = [1, 1, 1, 0];
        let result: [u64; 4] = _power(base, n - 1);
        result[0]
    }
}

fn _power(mut m: [u64; 4], mut n: u64) -> [u64; 4] {
        let mut result: [u64; 4] = [1, 0, 0, 1];
        while n > 0 {
            if n % 2 == 1 {
                result = _multiply(result, m);
            }
            m = _multiply(m, m);
            n /= 2;
        }
        result
}

fn _multiply(a: [u64; 4], b: [u64; 4]) -> [u64; 4] {
        [
            a[0] * b[0] + a[1] * b[2],
            a[0] * b[1] + a[1] * b[3],
            a[2] * b[0] + a[3] * b[2],
            a[2] * b[1] + a[3] * b[3],
        ]
}

#[pyfunction]
fn rust_runtime_benchmark(nth_term: u64) {
    for n in 0..nth_term {
        rust_nth_fibonacci_using_matrix_exponentiation(n);
    }
}

