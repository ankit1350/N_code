import os

def convert(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0  # Move outside the return

def file_size(file_path):
    if os.path.isfile(file_path):  # Ensure it's a file, not a folder
        file_info = os.stat(file_path)
        return convert(file_info.st_size)
    else:
        return "File not found or incorrect path."

file_path = r"C:\Users\Ankit\OneDrive\initial pages pdf.pdf" # Correct path format
print(file_size(file_path))
