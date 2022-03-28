# ab = input()
# ac = input()
# bc = input()
#
# def solve_task(self, ab, ac, bc):
#
#     if ab == '>':

ab = input()
ac = input()
bc = input()
result = ''
if ab == '<' and ac == '<':
    if bc == '>':
        result = 'acb'
    else:
        result = 'abc'
elif ab == '>' and ac == '>':
    if bc == '>':
        result = 'cba'
    else:
        result = 'bca'
elif ab == '<' and ac == '>':
    result = 'cab'
elif ab == '>' and ac == '<':
    result = 'bac'
elif ab == '=':
    if ac == '>':
        result = """cab \ncba"""
    else:
        result = """abc \nbac"""
elif ac == '=':
    if ab == '>':
        result = """bca \nbac"""
    else:
        result = """cab \nacb"""
elif bc == '=':
    if ab == '<':
        result = """abc \nacb"""
    else:
        result = """bca \ncba"""
print(result)