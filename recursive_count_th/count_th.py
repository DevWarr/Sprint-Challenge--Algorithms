'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # casing matters, so no need to .lower() or .upper()
    if len(word) < 2:
        # We can't have "th" if the string length is less than 2
        return 0

    for i in range(len(word)-1):
        if word[i] + word[i+1] == "th":
            # If we find a 'th', return 1 plus our recursive result.
            # Make sure to pass in a shallower word that doesn't include 
            # the 'th' we just found
            return 1 + count_th(word[i+2:])
    
    # If we make it through the whole word 
    # and we haven't returned yet, there are no
    # more 'th' letter pairs. Return 0.
    return 0
