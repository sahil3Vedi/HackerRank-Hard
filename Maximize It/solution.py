# nakuldev on the track

first_line = input().split(" ")
k = int(first_line[0])
m = int(first_line[1])

nis = []
k_lists = []

for i in range(k):
    ith_input = input().split(" ")
    int_ith_input = [int(x) for x in ith_input]
    jayZ = int_ith_input[0]
    nis.append(jayZ)
    int_ith_input.pop(0)
    k_lists.append(int_ith_input)


def findS(set_of_xis):
    if len(set_of_xis) == 1:
        tem1 = set_of_xis[0]
        return ((tem1 % m) ** 2) % m
    else:
        set_of_xs = [xi % m for xi in set_of_xis]
        set_of_psquares = [(p ** 2) % m for p in set_of_xs]
        # print(set_of_psquares)
        sum_of_squares = sum(set_of_psquares)
        return sum_of_squares % m


def productlist(alpha, beta):
    list_products = []
    for every_element in alpha:
        for every_other_element in beta:
            minilist = [every_element]
            if isinstance(every_other_element, int):
                minilist.append(every_other_element)
            else:
                minilist = minilist + every_other_element
            list_products.append(minilist)
    return list_products


def formTuples(klists):
    number_of_lists = len(klists)
    if number_of_lists == 1:
        superlist = []
        for each_number in klists[0]:
            sublist = [each_number]
            superlist.append(sublist)
        return superlist

    elif number_of_lists == 2:
        return productlist(klists[0], klists[1])
    else:
        temp = klists
        return productlist(klists[0], formTuples(temp[1:]))


table_of_Xs = formTuples(k_lists)
list_of_Ss = []

for each_row in table_of_Xs:
    S = findS(each_row)
    list_of_Ss.append(S)

# print(table_of_Xs)
print(max(list_of_Ss))
