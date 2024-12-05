def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some code that processes the file ...
            contents = f.read()
            # Process the contents
            return contents
    except FileNotFoundError:
        return "File not found"

# The 'with' statement ensures the file is automatically closed, even if exceptions occur.