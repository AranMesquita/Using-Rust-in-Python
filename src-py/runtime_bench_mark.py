import timeit
from benchmark_funcs import python_runtime_benchmark, rust_runtime_benchmark  # noqa: F401

# reason why we only have NTH_TERM = 94 as 93rd Fibonacci number is the largest that fits in a u64
# and 94th Fibonacci number is the first that exceeds u64::MAX
# the rust_runtime_benchmark & the python_runtime_benchmark functions
# will run from 0 to NTH_TERM - 1, so we set NTH_TERM to 94
# to benchmark calculating 0 --> 93rd Fibonacci number
NTH_TERM = 94
NUMBER_OF_CALLS = 100000

rust_time = timeit.timeit(
    stmt=f"rust_runtime_benchmark({NTH_TERM})",
    globals=globals(),
    number=NUMBER_OF_CALLS
)
python_time = timeit.timeit(
    stmt=f"python_runtime_benchmark({NTH_TERM})",
    globals=globals(),
    number=NUMBER_OF_CALLS
)

print(f"Rust avg: {rust_time * 1_000:.2f} µs, Python avg: {python_time * 1_000:.2f} µs (per call, over a total of {NTH_TERM * NUMBER_OF_CALLS:,} iterations)")