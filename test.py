values = """

58
52
68
86
72
66
97
89
84
91
91
92
66
68
87
86
73
61
70
75
72
73
85
84
90
57
77
76
84
93
58
47"""

sorted_value = sorted([int(x) for x in values.split()])
stems_leave = {}
for x in sorted_value:
    x = int(x)
    print(x)
    stem = x // 10
    leave = x % 10
    if stem in stems_leave:
        stems_leave[stem].append(leave)
    else:
        stems_leave[stem] = [leave]

from pprint import pprint
pprint(stems_leave)
# total = 0
# avg = 0
# for x in sorted_value:
#     total += x
#
# avg = total/len(sorted_value)
#
# print("total: ", total)
# print("avg: ", avg)
# print(sorted_value)
