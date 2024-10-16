class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        temp_stack = []
        while len(pushed)>0:
            elem = pushed.pop(0)
            temp_stack.append(elem)
            while len(temp_stack)>0 and temp_stack[-1] == popped[0]:
                temp_stack.pop()
                popped.pop(0)
        # print(pushed, popped,temp_stack)
        if temp_stack == popped[::-1]:
            return True
        else:
            return False
