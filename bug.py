def function_with_unclosed_file(filename):
    f = open(filename, 'r')
    # ... some code that processes the file ... 
    return

# The file f remains open, consuming system resources and potentially preventing other processes from accessing it.