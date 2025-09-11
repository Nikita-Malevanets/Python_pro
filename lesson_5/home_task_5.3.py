import importlib
import inspect


def analyze_module(module_name: str):
    """
    Analyzes a Python module and prints all its functions (including built-in)
    and classes with their signatures.

    Args:
        module_name (str): Name of the module to analyze (e.g., "math").

    Example:
        analyze_module("math")
    """
    try:
        # Dynamically import the module by name
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Module '{module_name}' not found.")
        return

    # Get all regular Python functions from the module
    functions = inspect.getmembers(module, inspect.isfunction)
    # Get all built-in functions (like math module functions)
    builtins = inspect.getmembers(module, inspect.isbuiltin)
    # Combine both lists
    all_functions = functions + builtins

    print("Functions:")
    if all_functions:
        for name, func in all_functions:
            try:
                # Try to get the function signature (arguments)
                sig = inspect.signature(func)
                print(f"- {name}{sig}")
            except ValueError:
                # For some built-in functions, signature cannot be obtained
                print(f"- {name}(...)")
    else:
        print("- <no functions in this module>")

    # Get all classes from the module
    classes = [(name, cls) for name, cls in inspect.getmembers(module, inspect.isclass) if not name.startswith("__")]

    print("\nClasses:")
    if classes:
        for name, cls in classes:
            print(f"- {name}")
    else:
        print("- <no classes in this module>")


# Example usage
analyze_module("math")

analyze_module("math")
