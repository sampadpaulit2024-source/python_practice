# Reverse a String by Sampad Paul
def reverse_string(s):
    result = ""
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    return result


s = str(input("Enter a string: "))
print(reverse_string(s))
print("end of program")
