# Author: Allen Anker
# Created by Allen Anker on 2019-05-29

a_poly = input().split()
b_poly = input().split()
exponents1, exponents2 = [int(a_poly[i]) for i in range(1, len(a_poly), 2)], \
                         [int(b_poly[i]) for i in range(1, len(b_poly), 2)]
coefficients1, coefficients2 = [float(a_poly[i]) for i in range(2, len(a_poly), 2)], \
                               [float(b_poly[i]) for i in range(2, len(b_poly), 2)]
dict1 = dict(zip(exponents1, coefficients1))
dict2 = dict(zip(exponents2, coefficients2))

non_common = set(exponents1) ^ set(exponents2)
common = set(exponents1).intersection(exponents2)

final_values = {}
for i in common:
    if dict1[i] + dict2[i]:
        final_values[i] = dict1[i] + dict2[i]
    dict1.pop(i)
    dict2.pop(i)
final_values.update(dict1)
final_values.update(dict2)
out = [str(len(final_values))]
final_keys = sorted(final_values, reverse=True)
for i in final_keys:
    out.append(str(i))
    out.append(str(round(final_values[i], 1)))
print(" ".join(out))
