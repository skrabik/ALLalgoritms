## Такс, закодим J

def sample_answer():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(input()))
    
    # первый флаг это чмы можем прийии слева, второй свурзу сверху
    dp = [[False for _ in range(m)] for _ in range(n)]
    dp[0][0] = True
    #! нам нужно что то эффективнее!!
    for i in range(1, n):
        if matrix[i][0] == '#':
            continue
        dp[i][0] = dp[i-1][0] 

    for j in range(1, m):
        if matrix[0][j] == '#':
            continue
        dp[0][j] = dp[0][j-1]
    
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == '#':
                continue
            dp[i][j] = dp[i-1][j] or dp[i][j-1]
    if dp[-1][-1] == False:
        print("NIE")
    else: 
        print("TAK")
        answers_way = []
        answers_rows = ["N" for _ in range(n)]
        answers_cols = ["N" for _ in range(m)]
        
        i = n-1
        j = m-1
        
        # если идём вверх, то меняем строку 
        # если влево - столбец 

        if matrix[-1][-1] == '@':
            answers_rows[-1] = 'T'
        
        while i > 0 or j > 0:
            if i > 0 and dp[i-1][j]:
                
                if matrix[i-1][j] == '@' and answers_cols[j] == 'N':
                    answers_rows[i-1] = 'T'
                if matrix[i-1][j] == 'O' and answers_cols[j] == 'T':
                    answers_rows[i-1] = 'T'
                                
                answers_way.append('D')
                i -= 1

            if j > 0 and dp[i][j-1]:
                
                if matrix[i][j-1] == '@' and answers_rows[i] == 'N':
                    answers_cols[j-1] = 'T'
                if matrix[i][j-1] == 'O' and answers_rows[i] == 'T':
                    answers_cols[j-1] = 'T'
                    
                answers_way.append('P')
                j -= 1
        answers = answers_way[::-1]

        print(''.join(answers_rows))
        print(''.join(answers_cols))
        print(''.join(answers))            
                           
t = int(input())

for _ in range(t):
    sample_answer()
    