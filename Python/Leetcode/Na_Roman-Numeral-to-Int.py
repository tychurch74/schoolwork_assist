def roman_to_int(s):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(s):
        curr_value = roman_dict[char]
        if curr_value >= prev_value:
            total += curr_value  # Add the current value if it's greater or equal to the previous one
        else:
            total -= curr_value  # Subtract the current value if it's less than the previous one
        prev_value = curr_value

    return total


def roman_to_int_no_reverse(s):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    i = 0

    while i < len(s):
        # If this is the last character or the current character's value is greater or equal to the next character's
        if i + 1 == len(s) or roman_dict[s[i]] >= roman_dict[s[i + 1]]:
            total += roman_dict[s[i]]
        else:
            # Subtract the current character's value from the total
            total -= roman_dict[s[i]]
        i += 1

    return total


