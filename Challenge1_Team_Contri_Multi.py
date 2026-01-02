def team_contribution(contribution):    
    left = [1] * len(contribution)
    right = [1] * len(contribution)
    impact = [1] * len(contribution)

    for i in range(1, len(contribution)):
        left[i] = left[i-1] * contribution[i-1]

    for i in range(len(contribution)-2, -1, -1):
        right[i] = right[i+1] * contribution[i+1]

    for i in range(len(contribution)):
        impact[i] = left[i] * right[i]

    print(f"Contribution Array: {contribution}")
    print(f"Impact Array: {impact}")

team_contribution([3,5,2,7])