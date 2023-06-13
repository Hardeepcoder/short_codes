def find(group1, group2):
    common_chick = []
    for g in group1:
        if g in group2 and g not in common_chick:
            common_chick.append(g)
    return common_chick


group1 = ["kylie", "kendle", "gigi", "bella"]
group2 = ["julia", "kendra", "kylie", "mia", "bella"]

common = find(group1, group2)
print(common)
