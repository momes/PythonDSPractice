def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_counter = {}
    for ltr in phrase:
        letter_counter[ltr] = letter_counter.get(ltr,0) + 1
    return letter_counter

    # freqCount[char] = (freqCount[char] + 1) || 1;