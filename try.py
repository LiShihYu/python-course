def position(string):
    final_answer = -1
    for num, s in enumerate(string):
        if s == s.upper():
            final_answer = (s, num)
    return final_answer


print(position("abCD"))
