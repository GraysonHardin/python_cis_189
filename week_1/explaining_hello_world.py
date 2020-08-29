# The print function will output any given text to the console. Programmers are essentially saying, "say this to the reader" and the code returns said value. Since the print functions are on separate lines, the code will output on separate lines.
print('Hello')
print('World')

# The built-in "help" function assists the programmer with documentation of classes, keywords, etc. It's like a helpdesk to aid the programmer with writing a proper print function.
help(print)

# The only difference between the code below and on lines 1 and 2, is that the "end=" command combines lines 9 and 10. While each print function is on a separate line, the "end=" wraps the text into one line.
print('Hello', end='')
print('World')
