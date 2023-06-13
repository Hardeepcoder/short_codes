def fun(numbers):
    # print(numbers)
    seen=set()
    duplicates = []

    for n in numbers:
        if n in seen and n not in duplicates:
            duplicates.append(n)
        else:
            seen.add(n)
    return duplicates



numbers = [1,4,2,4,4,5,56,3,2,2,3,2,1,5,1]

duplicates = fun(numbers)

print(duplicates)
