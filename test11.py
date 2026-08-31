#This code snippet takes a phone number as input and converts each digit into its corresponding word representation using a dictionary mapping. If a character in the input is not a digit, it will be replaced with an exclamation mark ("!"). The final output is a string of words representing the digits in the phone number.
phone = input("Phone")
digits_mapping  = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)


