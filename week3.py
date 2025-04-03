class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        # Step 1: Find the middle using fast and slow pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Step 3: Compare both halves
        left, right = head, prev
        while right:  # Only need to check right half (reversed)
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
    
    def reorderList(self, head):
        
        if not head or not head.next:
            return
        
        # Step 1: Find the middle using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev, curr = None, slow.next
        slow.next = None  # Split the list into two halves
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
    def reorderList(self, head):
        
        if not head or not head.next:
            return
        
        # Step 1: Find the middle using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev, curr = None, slow.next
        slow.next = None  # Split the list into two halves
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
    def setZeroes(self,matrix):
        if not matrix:
            return
        
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # Mark rows and columns
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set matrix elements to zero based on marks
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
                    
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        # Set first row and first column to zero if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
                
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
            
