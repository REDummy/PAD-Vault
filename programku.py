def findSubsets(index, remaining, current, currentSum):
    if remaining == 0:
        print(current)
        return
    
    if index == n:
        return
    
    if w[index] <= remaining:
        current.append(w[index])
        findSubsets(index+1, remaining-w[index], current, currentSum+w[index])
        current.pop()
    
    findSubsets(index+1, remaining, current, currentSum)

n = 4
w = [3, 4, 5, 6]
M = 13
current = []
currentSum = 0

findSubsets(0, M, current, currentSum)
