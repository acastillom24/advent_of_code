"""Advent of Code 2015, day 7: Some Assembly Required
"""

from app.functions.helpers import read_file_txt

bitwise_operation = {
    "AND": "&",
    "OR": "|",
    "LSHIFT": "<<",
    "RSHIFT": ">>",
    "NOT": "~"
}

['~ hn -> ho', '1 & f -> hn', '1674 -> b', 'b >> 5 -> f', "c << 1 -> t", "0 -> c"]

bitwise_value = {}

rows = read_file_txt("app/2015/day_07/input.txt")
# rows = ['NOT hn -> ho', '1 AND f -> hn', '1674 -> b', 'b RSHIFT 5 -> f', "c LSHIFT 1 -> t", "0 -> c"]

_, search_value = rows[-1].split("->")

rows_clean = []
for row in rows:
    left, right = row.split("->")
    rows_clean += [right.strip() + " = " + " ".join(bitwise_operation.get(l, l) for l in left.split())]
rows_clean = sorted(rows_clean)

code = "; ".join(rows_clean)
exec(code, {}, bitwise_value)
print(bitwise_value.get(search_value))


# for row in rows:
#     left, right = row.split("->")
#     left = " ".join(bitwise_operation.get(l, l) for l in left.split())
#     right = " ".join(bitwise_operation.get(r, r) for r in right.split())
#     if left.isdigit():
#         bitwise_value[right] = str(left)
#     else:
#         bitwise_list.append((left, right))

# def evaluate_expression(expr):
#     for part in expr.split():
#         if part in bitwise_operation.values():
#             continue
#         if not part.isdigit():
#             return False
#     return True

# print(f"Initial bitwise_list size: {len(bitwise_list)}")
# while bitwise_list:
#     for idx, content in enumerate(bitwise_list):
#         left, right = content
#         left = " ".join(bitwise_value.get(l, l) for l in left.split())
#         if evaluate_expression(left):
#             bitwise_value[right] = str(eval(left))
#             bitwise_list.pop(idx)

#     if len(bitwise_list) % 100 == 0:
#         print(f"bitwise_list size: {len(bitwise_list)}")

# print(bitwise_value)
# print(bitwise_value.get(search_value))