class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def push(self, x):
        self.in_stack.append(x)
    
    def pop(self):
        self._transfer()  # Move elements if out_stack is empty
        return self.out_stack.pop()
    
    def peek(self):
        self._transfer()
        return self.out_stack[-1]
    
    def empty(self):
        return not self.in_stack and not self.out_stack
    
    def _transfer(self):
        """Move elements from in_stack to out_stack if out_stack is empty."""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
def decodeString(s: str) -> str:
    stack = []
    current_string = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == "[":
            # Save context and reset
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif char == "]":
            prev_string, repeat_count = stack.pop()
            current_string = prev_string + current_string * repeat_count
        else:
            current_string += char

    return current_string

def peopleAwareOfSecret(n: int, delay: int, forget: int) -> int:
    MOD = 10**9 + 7
    dp = [0] * (n + 1)
    dp[1] = 1  # Day 1: one person knows the secret
    totalSharers = 0  # Running sum of sharers

    for day in range(2, n + 1):
        # People who can start sharing today
        if day - delay >= 1:
            totalSharers = (totalSharers + dp[day - delay]) % MOD
        # People who forgot the secret today
        if day - forget >= 1:
            totalSharers = (totalSharers - dp[day - forget]) % MOD
        dp[day] = totalSharers % MOD

    # Sum people who haven't forgotten the secret by day n
    result = sum(dp[n - forget + 1 : n + 1]) % MOD
    return result