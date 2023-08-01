#9
"""
first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

if first > 0 and second > 0 and first < second:
    gcd = first
elif first > 0 and second > 0 and first > second:
    gcd = second
else:
    print(False)

while second % gcd != 0:
    gcd = gcd - 1
    while first % gcd != 0:
        gcd = gcd - 1
    print(gcd)
"""


#10
"""
num = int(input("Enter integer (0 for output): "))
sum = 0
while num !=0:
    for i in range(num):
        i = i + 1
        sum = sum + i
    print(sum)
    num = int(input("Enter integer (0 for output): "))
"""

#11
"""
sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    for i in range(num + 1):
        sum = sum + i
    print(sum)
"""

#12
"""
sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    for i in range(num + 1):
        if i % 2 == 1:
            continue
        sum = sum + i
    print(sum)

"""

#13
"""
message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ch.isupper():
        ch_unicode = ord(ch)
        ch_index = ord(ch) - ord("A")
        new_ch = (ch_index + offset) % 26
        new_unicode = new_ch + ord("A")
        new_message = chr(new_unicode)
        encoded_message = encoded_message + new_message
    elif ch.islower():
        ch_unicode = ord(ch)
        ch_index = ord(ch) - ord("a")
        new_ch = (ch_index + offset) % 26
        new_unicode = new_ch + ord("a")
        new_message = chr(new_unicode)
        encoded_message = encoded_message + new_message
    else:
        encoded_message += ch
    print(encoded_message)
"""

#14
"""
pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool // quantity
except ZeroDivisionError:
    print('Divide by zero completed!')
"""