def balanced_performance_score(scoresA, scoresB):
    total = len(scoresA) + len(scoresB)
    mid1 = (total - 1) // 2   
    mid2 = total // 2         
    indexA = 0
    indexB = 0
    seen = -1
    first_value = 0
    second_value = 0
    while indexA < len(scoresA) or indexB < len(scoresB):
        if indexA < len(scoresA) and (indexB >= len(scoresB) or scoresA[indexA] <= scoresB[indexB]):
            current = scoresA[indexA]
            indexA += 1
        else:
            current = scoresB[indexB]
            indexB += 1
        seen += 1
        if seen == mid1:
            first_value = current
        if seen == mid2:
            second_value = current
            break   
    if total % 2 == 1:
        return float(second_value)
    return (first_value + second_value) / 2

print(balanced_performance_score([1, 3], [2]))        
print(balanced_performance_score([1, 2], [3, 4]))     
