# Count vowels in a string by Sampad Paul
def count_vowels(s):
    countn = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            countn += 1
    return countn


s = str(input("Enter a string: "))
print(count_vowels(s))
