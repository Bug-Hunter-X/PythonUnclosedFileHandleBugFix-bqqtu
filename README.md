# Unclosed File Handle Bug in Python

This repository demonstrates a common error in Python: forgetting to close file handles after use.  Leaving files open can lead to resource exhaustion and other issues. The `bug.py` file shows the problem, and `bugSolution.py` provides a corrected version.

## Problem

The `function_with_unclosed_file` in `bug.py` opens a file but fails to close it using `f.close()`.  This means the file remains locked and resources associated with it are not released until the program terminates.

## Solution

The `bugSolution.py` file corrects this by using a `with` statement.  The `with` statement ensures the file is automatically closed even if errors occur within the block.