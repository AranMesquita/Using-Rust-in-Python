A repo where I use rust in python and vice versa to test the capabilities of using rust and python code together



\[setup steps]

1. python -m venv .venv
2. activate the venv
3. pip install maturin (build system for building and publishing rust crates as python packages)
4. maturin init \& select --> pyo3
5. create the folder in the root directory where all the python files will be kept e.g. mkdir src-py
6. create a python file in the python directory
7. import and run the functions, with the rust #\[pymodule] attribute, that is located in the .\\src\\lib.rs file
8. then run maturin develop --release (which builds the lib.rs file and installs it as a package in the .venv)
9. then run the python file with the imported rust functions 
