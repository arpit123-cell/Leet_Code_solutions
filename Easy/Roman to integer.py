"""

Problem: 9. Roman to Integer
Difficulty: Easy

Approach:

1. Create a hash map (dictionary) mapping each Roman numeral to its integer value.

2. Iterate through the string character by character. For each numeral
compare its value to the value of the next numeral (if it exists).

3. If the current value is greater than or equal to the next value, add it to the total.

4. If the current value is less than the next value
subtract it from the total (this handles cases like IV, IX, XL, etc.).

5. The sum after processing all characters is the final integer value.

"""

def Roman_to_integer(s):
    hashmap = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0

    for i in range(len(s)- 1):
        if hashmap[s[i]] < hashmap[s[i+1]]:
            total -= hashmap[s[i]]
        else:
            total += hashmap[s[i]]
    total += hashmap[s[-1]]