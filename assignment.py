# File Read & Write challenge
f1 = open('myDataFile.txt','r')
with open("output.txt", "w") as f1: f1.write("Hello, Python!We are writing a modified version to a new file")

# Error Handling Lab
file = input("Enter Name of File:")
try:
    with open(file, "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found. Please check the filename.")
