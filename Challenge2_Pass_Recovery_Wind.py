def recover_password(log, pattern):
    if len(pattern) > len(log):
        return ""
    needed_chars = {}
    for ch in pattern:
        if ch in needed_chars:
            needed_chars[ch] += 1
        else:
            needed_chars[ch] = 1
    current_window = {}
    total_required = len(needed_chars)
    matched = 0
    start = 0
    smallest_length = float('inf')
    answer = ""
    for end in range(len(log)):
        letter = log[end]
        current_window[letter] = current_window.get(letter, 0) + 1
        if letter in needed_chars and current_window[letter] == needed_chars[letter]:
            matched += 1
        while matched == total_required:
            window_size = end - start + 1
            if window_size < smallest_length:
                smallest_length = window_size
                answer = log[start:end+1]
            remove_char = log[start]
            current_window[remove_char] -= 1
            if remove_char in needed_chars and current_window[remove_char] < needed_chars[remove_char]:
                matched -= 1
            start += 1
    return answer

print(recover_password("ADOBECODEBANC", "ABC"))  
print(recover_password("a", "a"))              
print(recover_password("a", "aa"))              
