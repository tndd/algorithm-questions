N = int(input())
A = list(map(int, input().split()))

ans_pos = ans_neg = 0

def simulate_operation(tgt_list):
  answer = 0
  N = len(tgt_list)
  previous_sum = tgt_list[0] # total to i - 1
  for i in range(1, N):
    # if prev_sum is plus and tgt_lis[i] is more minus than prev_sum, no action.
    # if prev_sum is plus and minus of tgt_lis[i] is larger than or equal to prev_sum.
    if previous_sum > 0 and previous_sum + tgt_list[i] >= 0:
      # the number that need to be subtracted to meet the requirements.
      require_subtraction = previous_sum + tgt_list[i] + 1
      # correcting the current number.
      tgt_list[i] -= require_subtraction
      answer += require_subtraction
    # if prev_sum is minus and tgt_lis[i] is more plus than prev_sum, no action.
    # if prev_sum is minus and minus of tgt_lis[i] is more smaller than or equal to prev_sum.
    elif previous_sum < 0 and previous_sum + tgt_list[i] <= 0:
      # the number that need to be added to meet the requirements.
      require_addition = -(previous_sum + tgt_list[i] - 1)
      # correcting the current number.
      tgt_list[i] += require_addition
      answer += require_addition
    previous_sum += tgt_list[i]
  return answer

# simulate two options of starting with a positive or negative.
# positive, the first item is 1.
A_pos = A[:]
init_cost = abs(A_pos[0] - 1)
ans_pos += init_cost
A_pos[0] -= init_cost
ans_pos += simulate_operation(A_pos)
# negative, the first item is -1.
A_neg = A[:]
init_cost = abs(A_neg[0] + 1)
ans_neg += init_cost
A_neg[0] -= init_cost
ans_neg += simulate_operation(A_neg)

print(min(ans_pos, ans_neg))