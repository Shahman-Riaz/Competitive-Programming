n = int(input())
arr = map(int, input().split())
real_arr = []
for i in arr:
    real_arr.append(i)
if (n == len(real_arr)):
    max_num = max(real_arr)
    real_arr.remove(max_num)
    runner_up = max(real_arr)
    print(runner_up) 
