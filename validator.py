#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" --- Learn to Code - Validator --- """

import os
import subprocess
import inspect

repo_path = "/Users/jmetrikat/Code/jmetrikat/learn-to-code"
timeout_in_seconds = 10
problems = ["factorial", "fibonacci", "gcd", "lcm", "primes", "primefactors"]
expected_outputs = {
    "factorial": {
        -1: "Number must be positive.",
        0: 1,
        1: 1,
        2: 2,
        3: 6,
        4: 24,
        5: 120,
        6: 720,
        7: 5040,
        8: 40320,
        9: 362880,
        10: 3628800
    },
    "fibonacci": {
        -1: "Number must be positive.",
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        4: 3,
        5: 5,
        6: 8,
        7: 13,
        8: 21,
        9: 34,
        10: 55
    },
    "gcd": {
        (10, 25): 5,
        (14, 28): 14,
        (21, 14): 7,
        (18, 24): 6,
        (35, 49): 7,
        (12, 30): 6,
        (16, 24): 8,
        (27, 36): 9,
        (8, 12): 4,
        (9, 15): 3
    },
    "lcm": {
        (10, 25): 50,
        (14, 28): 28,
        (21, 14): 42,
        (18, 24): 72,
        (35, 49): 245,
        (12, 30): 60,
        (16, 24): 48,
        (27, 36): 108,
        (8, 12): 24,
        (9, 15): 45
    },
    "primefactors": {
        -1: "Number must be greater than 1.",
        0: "Number must be greater than 1.",
        1: "Number must be greater than 1.",
        2: "2 is prime.",
        3: "3 is prime.",
        4: "2",
        5: "5 is prime.",
        6: "2\n3",
        7: "7 is prime.",
        8: "2",
        9: "3",
        10: "2\n5"
    },
    "primes": {
        -1: "Number must be greater than 1.",
        0: "Number must be greater than 1.",
        1: "Number must be greater than 1.",
        2: "2",
        3: "2\n3",
        4: "2\n3",
        5: "2\n3\n5",
        6: "2\n3\n5",
        7: "2\n3\n5\n7",
        8: "2\n3\n5\n7",
        9: "2\n3\n5\n7",
        10: "2\n3\n5\n7"
    }
}


# run solution for a given problem in C and return the output
def run_c_solution(problem, key) -> str:
    try:
        os.chdir(f"{repo_path}/c")
        if problem == "gcd" or problem == "lcm":
            output = subprocess.check_output([f"./{problem}", f"{key[0]}", f"{key[1]}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)
        else:
            output = subprocess.check_output([f"./{problem}", f"{key}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)

        if problem == "primefactors" or problem == "primes":
            return output.decode("utf-8").strip()
        else:
            return int(output.decode("utf-8").strip())

    except subprocess.TimeoutExpired:
        return f" {problem} timed out after {timeout_in_seconds} seconds."

    except subprocess.CalledProcessError as e:
        if "be positive" in e.output.decode("utf-8") or "be greater than" in e.output.decode("utf-8"):
            return e.output.decode("utf-8").strip()
        else:
            print(f"Error running {problem}:")
            print(e.output.decode("utf-8"))
            return None


# run solution for a given problem in C++ and return the output
def run_cpp_solution(problem, key) -> str:
    pass


# run solution for a given problem in Go and return the output
def run_go_solution(problem, key) -> str:
    pass


# run solution for a given problem in Java and return the output
def run_java_solution(problem, key) -> str:
    pass


# run solution for a given problem in Python and return the output
def run_python_solution(problem, key) -> int:
    try:
        os.chdir(f"{repo_path}/python")
        if problem == "gcd" or problem == "lcm":
            output = subprocess.check_output(["/opt/homebrew/bin/python3.11", f"{problem}.py", f"{key[0]}", f"{key[1]}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)
        else:
            output = subprocess.check_output(["/opt/homebrew/bin/python3.11", f"{problem}.py", f"{key}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)

        if problem == "primefactors" or problem == "primes":
            return output.decode("utf-8").strip()
        else:
            return int(output.decode("utf-8").strip())

    except subprocess.TimeoutExpired:
        return f" {problem} timed out after {timeout_in_seconds} seconds."

    except subprocess.CalledProcessError as e:
        if "be positive" in e.output.decode("utf-8") or "be greater than" in e.output.decode("utf-8"):
            return e.output.decode("utf-8").strip()
        else:
            print(f"Error running {problem}:")
            print(e.output.decode("utf-8"))
            return None


# run solution for a given problem in Rust and return the output
def run_rust_solution(problem, key) -> str:
    pass


# validate each problem for a given language
def validate_solution(lang, problem) -> None:
    prob_output = expected_outputs[problem]

    module = inspect.getmodule(run_python_solution)
    func_name = f"run_{lang.lower()}_solution"
    run_func = getattr(module, func_name)

    for key, value in prob_output.items():
        actual_output = run_func(problem, key)
        expected_output = value

        if actual_output != expected_output:
            print(f"Test failed. Expected {expected_output}, got {actual_output}")
            exit(1)

    print(f"Test passed for {problem}.")
    return 0


# main entry point: ask user to choose between c and python
print("Choose a language:")
print(" 1) C")
print(" 2) C++")
print(" 3) Go")
print(" 4) Java")
print(" 5) Python")
print(" 6) Rust")
choice = input("Your choice: ")

# run c solutions
if choice == "1":
    correct = 0
    lang = "C"

    os.chdir(f"{repo_path}/{lang}")
    subprocess.run(["make", "clean"], check=True)
    subprocess.run(["make", "all"], check=True, stderr=subprocess.DEVNULL)

    for problem in problems:
        if validate_solution(lang, problem) == 0:
            correct += 1

    os.chdir(f"{repo_path}/{lang}")
    subprocess.run(["make", "clean"], check=True)
    print('\033[1m' + f"{correct}/{len(problems)} problems correct in {lang}." + '\033[0m')

# run cpp solutions
elif choice == "2":
    print("C++ not implemented yet")
    exit(1)

elif choice == "3":
    print("Go not implemented yet")
    exit(1)

elif choice == "4":
    print("Java not implemented yet")
    exit(1)

elif choice == "5":
    correct = 0
    lang = "Python"
    os.chdir(f"{repo_path}/{lang}")

    for problem in problems:
        if validate_solution(lang, problem) == 0:
            correct += 1

    print('\033[1m' + f"{correct}/{len(problems)} problems correct in {lang}." + '\033[0m')


elif choice == "6":
    print("Rust not implemented yet")
    exit(1)

else:
    print("Invalid choice")
    exit(1)
