import collections


def maximumBalloonNumber(text):
    if (type(text) != str):
        raise TypeError("Input must be a string")

    balloon = collections.Counter(text)

    if 'b' and 'a' and 'l' and 'o' and 'n' in balloon:

        for key in balloon:
            if (key != 'b' and key != 'a' and key != 'l' and key != 'o' and key != 'n'):
                balloon[key] = max(balloon.values())+1

        balloon['l'] = int(balloon['l']/2)
        balloon['o'] = int(balloon['o']/2)
        return min(balloon.values())
    else:
        return 0
