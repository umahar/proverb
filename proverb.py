def proverb(*words, qualifier):

    words = list(words)
    result = []

    for i, word in enumerate(words[:-1]):
        result.append(f"For want of a {word} the {words[i+1]} was lost.")

    if words:
        if qualifier:
            result.append(f"And all for the want of a {qualifier} {words[0]}.")
        else:
            result.append(f"And all for the want of a {words[0]}.")

    return result
