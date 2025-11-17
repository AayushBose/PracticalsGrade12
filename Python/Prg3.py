#WAP to create a text file word.txt with content
file = open("C:\\Users\\aayus\\OneDrive\\Documents\\GitHub\\PRACTICALS\\Python\\File3.txt", 'w+')
file.write("A text file is a computer file that only contains text and has no special formatting such as bold text, italic text,\nimages, etc. \nWith Microsoft Windows computers text files are identified with the. txt file extension.")
file.seek(0)
content = file.read()
print("File content is:\n"+content)
file.seek(0)
lines = len(file.readlines())
vowels = 0
for i in content:
    if i.lower() in ('a','e','i','o','u'):
        vowels = vowels+1
words = len(content.split())

print("Total number of lines:",lines)
print("Total number of vowels:",vowels)
print("Total number of words is:",words)