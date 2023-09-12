#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" --- Learn to Code - Validator --- """

import os
import subprocess

repo_path = "/Users/jmetrikat/Code/jmetrikat/learn-to-code"
timeout_in_seconds = 10
err_msg_file_not_found = "File not found."
err_msg_timeout = f" timed out after {timeout_in_seconds} seconds."
err_msg_invalid_literal = "Invalid literal for int() with base 10."

languages = ["C", "Cpp", "Go", "Java", "Python", "Rust"]
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
        10: 3628800,
        20: 2432902008176640000, # limit for java, c, c++, go and rust
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
        10: 55,
        92: 7540113804746346429, # limit for java, c, c++, go and rust
    },
    "gcd": {
        (10, 25): 5,
        (14, 28): 14,
        (21, 14): 7,
        (18, 24): 6,
        (35, 49): 7,
        (12, 30): 6,
        (16, 24): 8,
        (-27, 36): 9,
        (8, -12): 4,
        (-9, -15): 3
    },
    "lcm": {
        (10, 25): 50,
        (14, 28): 28,
        (21, 14): 42,
        (18, 24): 72,
        (35, 49): 245,
        (12, 30): 60,
        (16, 24): 48,
        (-27, 36): 108,
        (8, -12): 24,
        (-9, -15): 45
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
# def run_c_solution(problem: str, key: int) -> str:
#     try:
#         os.chdir(f"{repo_path}/c")
#         if problem == "gcd" or problem == "lcm":
#             output = subprocess.check_output([f"./{problem}", f"{key[0]}", f"{key[1]}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)
#         else:
#             output = subprocess.check_output([f"./{problem}", f"{key}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)

#         if problem == "primefactors" or problem == "primes":
#             return output.decode("utf-8").strip()
#         else:
#             return int(output.decode("utf-8").strip())

#     except subprocess.TimeoutExpired:
#         return f" \033[3m{problem}.c\033[0m" + err_msg_timeout

#     except subprocess.CalledProcessError as e:
#         if "be positive" in e.output.decode("utf-8") or "be greater than" in e.output.decode("utf-8"):
#             return e.output.decode("utf-8").strip()
#         elif "no such file or directory" in e.output.decode("utf-8"):
#             return err_msg_file_not_found
#         else:
#             print(f"Error running {problem}:")
#             print(e.output.decode("utf-8"))
#             return None


# run solution for a given problem in C++ and return the output
# def run_cpp_solution(problem: str, key: int) -> str:
#     try:
#         os.chdir(f"{repo_path}/cpp")
#         if problem == "gcd" or problem == "lcm":
#             output = subprocess.check_output(
#                 [f"./{problem}", f"{key[0]}", f"{key[1]}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)
#         else:
#             output = subprocess.check_output(
#                 [f"./{problem}", f"{key}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)

#         if problem == "primefactors" or problem == "primes":
#             return output.decode("utf-8").strip()
#         else:
#             return int(output.decode("utf-8").strip())

#     except subprocess.TimeoutExpired:
#         return f" \033[3m{problem}.c\033[0m" + err_msg_timeout

#     except subprocess.CalledProcessError as e:
#         if "be positive" in e.output.decode("utf-8") or "be greater than" in e.output.decode("utf-8"):
#             return e.output.decode("utf-8").strip()
#         elif "no such file or directory" in e.output.decode("utf-8"):
#             return err_msg_file_not_found
#         else:
#             print(f"Error running {problem}:")
#             print(e.output.decode("utf-8"))
#             return None


# run solution for a given problem in Go and return the output
# def run_go_solution(problem: str, key: int) -> str:
#     try:
#         os.chdir(f"{repo_path}/go")
#         if problem == "gcd" or problem == "lcm":
#             output = subprocess.check_output(["go", "run", f"{problem}.go", f"{key[0]}", f"{key[1]}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)
#         else:
#             output = subprocess.check_output(["go", "run", f"{problem}.go", f"{key}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)

#         if problem == "primefactors" or problem == "primes":
#             return output.decode("utf-8").strip()
#         else:
#             return int(output.decode("utf-8").strip())

#     except subprocess.TimeoutExpired:
#         return f" \033[3m{problem}.go\033[0m" + err_msg_timeout

#     except subprocess.CalledProcessError as e:
#         if "be positive" in e.output.decode("utf-8") or "be greater than" in e.output.decode("utf-8"):
#             return e.output.decode("utf-8").strip().replace("\nexit status 1", "")
#         elif "no such file or directory" in e.output.decode("utf-8"):
#             return err_msg_file_not_found
#         else:
#             print(f"Error running {problem}:")
#             print(e.output.decode("utf-8"))
#             return None


# run solution for a given problem in Java and return the output
# def run_java_solution(problem: str, key: int) -> str:
#     try:
#         if problem == "gcd" or problem == "lcm":
#             output = subprocess.check_output(["java", f"{problem[0].upper() + problem[1:]}", f"{key[0]}", f"{key[1]}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)
#         else:
#             output = subprocess.check_output(["java", f"{problem[0].upper() + problem[1:]}", f"{key}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)

#         if problem == "primefactors" or problem == "primes":
#             return output.decode("utf-8").strip()
#         else:
#             return int(output.decode("utf-8").strip())

#     except subprocess.TimeoutExpired:
#         return f" \033[3m{problem}.java\033[0m" + err_msg_timeout

#     except subprocess.CalledProcessError as e:
#         if "be positive" in e.output.decode("utf-8") or "be greater than" in e.output.decode("utf-8"):
#             return e.output.decode("utf-8").strip()
#         elif "file not found" in e.output.decode("utf-8"):
#             return err_msg_file_not_found
#         else:
#             print(f"Error running {problem}:")
#             print(e.output.decode("utf-8"))
#             return None


# run solution for a given problem in Python and return the output
# def run_python_solution(problem: str, key: int) -> str:
#     try:
#         os.chdir(f"{repo_path}/python")
#         if problem == "gcd" or problem == "lcm":
#             output = subprocess.check_output(["/opt/homebrew/bin/python3.11", f"{problem}.py", f"{key[0]}", f"{key[1]}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)
#         else:
#             output = subprocess.check_output(["/opt/homebrew/bin/python3.11", f"{problem}.py", f"{key}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)

#         if problem == "primefactors" or problem == "primes":
#             return output.decode("utf-8").strip()
#         else:
#             return int(output.decode("utf-8").strip())

#     except subprocess.TimeoutExpired:
#         return f" \033[3m{problem}.py\033[0m" + err_msg_timeout

#     except subprocess.CalledProcessError as e:
#         if "be positive" in e.output.decode("utf-8") or "be greater than" in e.output.decode("utf-8"):
#             return e.output.decode("utf-8").strip()
#         elif "no such file or directory" in e.output.decode("utf-8"):
#             return err_msg_file_not_found
#         else:
#             print(f"Error running {problem}:")
#             print(e.output.decode("utf-8"))
#             return None


# run solution for a given problem in Rust and return the output
# def run_rust_solution(problem: str, key: int) -> str:
#     try:
#         os.chdir(f"{repo_path}/rust")
#         if problem == "gcd" or problem == "lcm":
#             output = subprocess.check_output([f"./{problem}", f"{key[0]}", f"{key[1]}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)
#         else:
#             output = subprocess.check_output([f"./{problem}", f"{key}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)

#         if problem == "primefactors" or problem == "primes":
#             return output.decode("utf-8").strip()
#         else:
#             return int(output.decode("utf-8").strip())

#     except subprocess.TimeoutExpired:
#         return f" \033[3m{problem}.rust\033[0m" + err_msg_timeout

#     except subprocess.CalledProcessError as e:
#         if "be positive" in e.output.decode("utf-8") or "be greater than" in e.output.decode("utf-8"):
#             return e.output.decode("utf-8").strip()
#         elif "No such file or directory" in e.output.decode("utf-8"):
#             return err_msg_file_not_found
#         else:
#             print(f"Error running {problem}:")
#             print(e.output.decode("utf-8"))
#             return None


def run_solution(lang: str, problem: str, key: int) -> str:
    try:
        os.chdir(f"{repo_path}/{lang.lower()}")
        if problem == "gcd" or problem == "lcm":
            if lang == "C" or lang == "Cpp" or lang == "Rust":
                output = subprocess.check_output(
                    [f"./{problem}", f"{key[0]}", f"{key[1]}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)
            elif lang == "Go":
                output = subprocess.check_output(
                    ["go", "run", f"{problem}.go", f"{key[0]}", f"{key[1]}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)
            elif lang == "Java":
                output = subprocess.check_output(
                    ["java", f"{problem[0].upper() + problem[1:]}", f"{key[0]}", f"{key[1]}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)
            elif lang == "Python":
                output = subprocess.check_output(
                    ["/opt/homebrew/bin/python3.11", f"{problem}.py", f"{key[0]}", f"{key[1]}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)
            else:
                return "Language not supported."

        else:
            if lang == "C" or lang == "Cpp" or lang == "Rust":
                output = subprocess.check_output(
                    [f"./{problem}", f"{key}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)
            elif lang == "Go":
                output = subprocess.check_output(
                    ["go", "run", f"{problem}.go", f"{key}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)
            elif lang == "Java":
                output = subprocess.check_output(
                    ["java", f"{problem[0].upper() + problem[1:]}", f"{key}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)
            elif lang == "Python":
                output = subprocess.check_output(
                    ["/opt/homebrew/bin/python3.11", f"{problem}.py", f"{key}"], stderr=subprocess.STDOUT, timeout=timeout_in_seconds)
            else:
                return "Language not supported."
        try:
            decoded_output = output.decode("utf-8").strip()
            if problem == "primefactors" or problem == "primes":
                return decoded_output
            else:
                return int(decoded_output)
        except ValueError as e:
            if "invalid literal for int() with base 10" in str(e):
                return err_msg_invalid_literal
            else:
                print(f"Error running {problem}:")
                print(e)
                return None

    except subprocess.TimeoutExpired:
        return f" \033[3m{problem}.c\033[0m" + err_msg_timeout

    except subprocess.CalledProcessError as e:
        if "be positive" in e.output.decode("utf-8") or "be greater than" in e.output.decode("utf-8"):
            return e.output.decode("utf-8").strip().replace("\nexit status 1", "")
        elif "no such file or directory" in e.output.decode("utf-8"):
            return err_msg_file_not_found
        else:
            print(f"Error running {problem}:")
            print(e.output.decode("utf-8"))
            return None


# validate each problem for a given language
def validate_solution(lang: str, problem: str, verbose: bool) -> int:
    prob_output = expected_outputs[problem]

    for key, value in prob_output.items():
        actual_output = run_solution(lang, problem, key)
        expected_output = value

        if err_msg_file_not_found in str(actual_output) or err_msg_timeout in str(actual_output) or err_msg_invalid_literal in str(actual_output):
            if verbose:
                print(f"Test failed for \033[3m{problem}\033[0m: {actual_output}")
            return 1
        elif actual_output != expected_output:
            if verbose:
                print(f"Test failed for \033[3m{problem}\033[0m. Expected '{expected_output}', got '{actual_output}'.")
            return 1

    if verbose:
        print(f"Test passed for \033[3m{problem}\033[0m.")

    return 0


# main entry point: ask user to choose between c and python
print("Choose a language:")
print(" 1) C")
print(" 2) C++")
print(" 3) Go")
print(" 4) Java")
print(" 5) Python")
print(" 6) Rust")
print(" 7) All")
choice = input("Your choice: ")

# run c solutions
if choice == "1":
    correct = 0
    verbose = True
    lang = "C"

    print(f"Validating {lang} solutions...")

    os.chdir(f"{repo_path}/{lang.lower()}")
    subprocess.run(["make", "clean"], check=True)
    subprocess.run(["make", "all"], check=True, stderr=subprocess.DEVNULL)

    for problem in problems:
        if validate_solution(lang, problem, verbose) == 0:
            correct += 1

    os.chdir(f"{repo_path}/{lang.lower()}")
    subprocess.run(["make", "clean"], check=True)
    print('\033[1m' + f"{correct}/{len(problems)} problems correct in {lang}." + '\033[0m')


# run cpp solutions
elif choice == "2":
    correct = 0
    verbose = True
    lang = "Cpp"

    print(f"Validating {lang} solutions...")

    os.chdir(f"{repo_path}/{lang.lower()}")
    subprocess.run(["make", "clean"], check=True)
    subprocess.run(["make", "all"], check=True, stderr=subprocess.DEVNULL)

    for problem in problems:
        if validate_solution(lang, problem, verbose) == 0:
            correct += 1

    os.chdir(f"{repo_path}/{lang.lower()}")
    subprocess.run(["make", "clean"], check=True)
    print('\033[1m' + f"{correct}/{len(problems)} problems correct in {lang}." + '\033[0m')


# run go solutions
elif choice == "3":
    correct = 0
    verbose = True
    lang = "Go"

    print(f"Validating {lang} solutions...")

    os.chdir(f"{repo_path}/{lang.lower()}")
    for problem in problems:
        if validate_solution(lang, problem, verbose) == 0:
            correct += 1

    print('\033[1m' + f"{correct}/{len(problems)} problems correct in {lang}." + '\033[0m')


# run java solutions
elif choice == "4":
    correct = 0
    verbose = True
    lang = "Java"

    print(f"Validating {lang} solutions...")

    os.chdir(f"{repo_path}/{lang.lower()}")
    java_files = subprocess.check_output(["find", f"{repo_path}/{lang.lower()}", "-name", "*.java"], stderr=subprocess.STDOUT).decode().splitlines()
    subprocess.check_output(["javac"] + java_files, stderr=subprocess.STDOUT)

    for problem in problems:
        if validate_solution(lang, problem, verbose) == 0:
            correct += 1
            subprocess.run(["rm", f"{problem}.class"], check=True)

    print('\033[1m' + f"{correct}/{len(problems)} problems correct in {lang}." + '\033[0m')


# run python solutions
elif choice == "5":
    correct = 0
    verbose = True
    lang = "Python"
    os.chdir(f"{repo_path}/{lang.lower()}")

    print(f"Validating {lang} solutions...")

    for problem in problems:
        if validate_solution(lang, problem, verbose) == 0:
            correct += 1

    print('\033[1m' + f"{correct}/{len(problems)} problems correct in {lang}." + '\033[0m')


# run rust solutions
elif choice == "6":
    correct = 0
    verbose = True
    lang = "Rust"

    print(f"Validating {lang} solutions...")

    os.chdir(f"{repo_path}/{lang.lower()}")
    rust_files = subprocess.check_output(["find", f"{repo_path}/{lang.lower()}", "-name", "*.rs"], stderr=subprocess.STDOUT).decode().splitlines()
    for rust_file in rust_files:
        subprocess.check_output(["rustc", rust_file], stderr=subprocess.STDOUT)

    for problem in problems:
        if validate_solution(lang, problem, verbose) == 0:
            correct += 1
            subprocess.run(["rm", f"{problem}"], check=True)

    print('\033[1m' + f"{correct}/{len(problems)} problems correct in {lang}." + '\033[0m')


# run all solutions
elif choice == "7":
    for lang in languages:
        correct = 0
        verbose = False

        print (f"Validating {lang} solutions...")

        os.chdir(f"{repo_path}/{lang.lower()}")

        if lang == "C" or lang == "Cpp":
            subprocess.run(["make", "clean"], check=True)
            subprocess.run(["make", "all"], check=True, stderr=subprocess.DEVNULL)

        elif lang == "Java":
            java_files = subprocess.check_output(["find", f"{repo_path}/{lang.lower()}", "-name", "*.java"], stderr=subprocess.STDOUT).decode().splitlines()
            subprocess.check_output(["javac"] + java_files, stderr=subprocess.STDOUT)

        elif lang == "Rust":
            rust_files = subprocess.check_output(
                ["find", f"{repo_path}/{lang.lower()}", "-name", "*.rs"], stderr=subprocess.STDOUT).decode().splitlines()
            for rust_file in rust_files:
                subprocess.check_output(["rustc", rust_file], stderr=subprocess.STDOUT)

        for problem in problems:
            if validate_solution(lang, problem, verbose) == 0:
                correct += 1

        if lang == "C" or lang == "Cpp":
            subprocess.run(["make", "clean"], check=True)

        if lang == "Java":
            for problem in problems:
                subprocess.run(["rm", f"{problem}.class"], check=True)

        if lang == "Rust":
            for problem in problems:
                subprocess.run(["rm", f"{problem}"], check=True)

        print('\033[1m' + f"{correct}/{len(problems)} problems correct in {lang.replace('pp', '++')}." + '\033[0m')


else:
    print("Invalid choice")
    exit(1)
