
def min_window(s: str, t: str) -> str:
    t_dict = {}
    for i in t:
        if i in t_dict:
            t_dict[i] += 1
        else:
            t_dict[i] = 1

    l, r, s_len = 0, 0, len(s)
    min_substring_len = s_len
    while r < s_len:
        if s[r] in t_dict:
            t_dict[s[r]] -= 1

        if max(list(t_dict.values())) <= 0:
            while l <= r:
                flag = t_dict.get(s[l], 1)
                if flag == 0:
                    substring_len = r - l
                    if substring_len < min_substring_len:
                        min_substring_len = substring_len
                        start = l
                        end = r
                        t_dict[s[l]] += 1
                        l += 1
                    break
                elif flag < 0:
                    t_dict[s[l]] += 1
                    l += 1
                else:
                    l += 1
        r += 1
    if min_substring_len == s_len:
        return ""
    else:
        return s[start: end+1]


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    ret = min_window(s, t)
    print(ret)