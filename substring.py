
def substring(string, pattern=None):
    print('ORIGINAL:           {}'.format(string))
    chars = {}
    if pattern is None:
        for char in string:
            if chars.get(char):
                chars[char] += 1
            else:
                chars[char] = 0
        pattern = list(chars.keys())
        pattern = ''.join(pattern)
    print('NON EXACT PATTERN:  {}'.format(pattern))

    start = 0
    shortest_substring = ''
    shortest_substring_len = 100000
    for end in range(0, len(string) + 1):
        tmp = string[start:end]
        if len(tmp) >= len(pattern):
            if len(tmp) < shortest_substring_len and is_valid(tmp, pattern):
                shortest_substring = tmp
                shortest_substring_len = len(tmp)
                while True:
                    start += 1
                    tmp = string[start:end]
                    if is_valid(tmp, pattern):
                        if len(tmp) < shortest_substring_len:
                            shortest_substring = tmp
                            shortest_substring_len = len(tmp)
                        else:
                            break
                    else:
                        break

    print('SHORTEST SUBSTRING: {}\n\n'.format(shortest_substring))
    if not shortest_substring:
        print('Invalid string!')

def is_valid(tmp, pattern):
    for i in pattern:
        if i not in tmp:
            return False
    return True


if __name__ == '__main__':
    substring('I am a test or am I', 'at')
    substring('I am a test or am I not a test')