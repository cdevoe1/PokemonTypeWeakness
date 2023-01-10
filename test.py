def solution(s):
    # Your code here

    sol = ""

    brail = {'c': "100100", 'o': "101010", 'd': "100110", 'e': "100010"}


    for i in s:
        sol += brail.get(i)
        print(sol)

    return sol


print(solution("code") == "100100101010100110100010")