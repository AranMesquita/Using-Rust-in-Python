This repository explores the integration of Rust into Python applications, demonstrating how both languages can work together effectively. It includes examples and tests to assess real-world use cases and performance benefits.



### setup steps
##### to setup your own python-rust project

1. **python -m venv .venv**
2. activate the venv
3. **pip install maturin** (build system for building and publishing rust crates as python packages)
4. **maturin init** \& select --> pyo3
5. create the folder in the root directory where all the python files will be kept e.g. [src-py](https://github.com/AranMesquita/Using-Rust-in-Python/tree/main/src-py)
6. create a python file in the python directory e.g. [src-py\\example_import_rust_function.py](https://github.com/AranMesquita/Using-Rust-in-Python/blob/main/src-py/example_import_rust_function.py)
7. import the function, with the rust #\[pymodule] attribute, that is located in the [src\\lib.rs](https://github.com/AranMesquita/Using-Rust-in-Python/blob/main/src/lib.rs) file e.g. [example](https://github.com/AranMesquita/Using-Rust-in-Python/blob/main/src-py/example_import_rust_function.py)
8. then run **maturin develop --release** (which builds the lib.rs file and installs it as a package in the .venv)
9. then run the python file with the imported rust functions e.g. python [python file you created in step 6]
