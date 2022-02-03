stu_ans = input()
ans = input()
correct = 0
if(len(stu_ans) != len(ans)):
    print("Incomplete answer")
else:
    for i, j in zip(stu_ans, ans):
        if i == j:
            correct += 1
    print(correct)