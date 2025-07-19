def _power(m: list[int], n: int) -> list[int]:
    result = [1, 0, 0, 1]
    while n > 0:
        if n % 2 == 1:
            result = _multiply(result, m)

        m = _multiply(m, m)
        n //= 2

    return result


def _multiply(a: list[int], b: list[int]) -> list[int]:
    return [
        a[0] * b[0] + a[1] * b[2],
        a[0] * b[1] + a[1] * b[3],
        a[2] * b[0] + a[3] * b[2],
        a[2] * b[1] + a[3] * b[3],
    ]


def python_nth_fibonacci_using_matrix_exponentiation(n: int) -> int:
    if n == 0:
        return 0
    else:
        base = [1, 1, 1, 0]
        result = _power(base, n - 1)
        return result[0]
