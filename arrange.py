import random



with open('problems.txt') as f1, open('answers.txt') as f2:
    s1 = f1.readlines()
    s2 = f2.readlines()
    
    s = [[i,j] for i,j in zip(s1,s2)]
    random.shuffle(s)
    for i,_ in s:
        print("\item \\begin{align*}")
        print("  "+i,end='')
        print("\end{align*}")
        print()

    for i,j in s:
        print("\item \\begin{align*}")
        print("  &"+i[:-1]+"\\\\",end='\n')
        print("  &"+j,end='')
        print("\end{align*}")
        print()