def team_contribution(contribution):
    left = []
    right = []
    impact = []
    for i in range(len(contribution)):
        if i == 0 :
            left.append(1)
        left_temp = 1
        if i != 0 :
            for j in range(i):
                left_temp *= contribution[j]
            left.append(left_temp)
    for i in range(len(contribution)):
        if i == len(contribution) - 1:
            right.append(1)
        right_temp = 1
        if i != len(contribution) - 1:
            for j in range(i+1,len(contribution)):
                right_temp *= contribution[j]
            right.append(right_temp)

    for i in range(len(left)):
        for j in range(len(right)):
            if i == j:
                impact.append(left[i]*right[j])
    print(f"Contribution Array: {contribution}")
    print(f"Impact Array: {impact}")

team_contribution([1,2,3,4])