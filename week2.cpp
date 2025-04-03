#include <string>
#include <vector>
#include <iostream>

using namespace std;
class Solution {
    public:
        int myAtoi(string s) {
            int i = 0, sign = 1;
        long result = 0; // Use long to handle overflow before clamping
        
        // 1. Ignore leading whitespace
        while (i < s.length() && s[i] == ' ') {
            i++;
        }
    
        // 2. Check for '+' or '-' sign
        if (i < s.length() && (s[i] == '+' || s[i] == '-')) {
            sign = (s[i] == '-') ? -1 : 1;
            i++;
        }
    
        // 3. Read the number and stop at non-digit character
        while (i < s.length() && isdigit(s[i])) {
            result = result * 10 + (s[i] - '0');
            
            // 4. Handle overflow by clamping to INT_MIN or INT_MAX
            if (sign * result < INT_MIN) return INT_MIN;
            if (sign * result > INT_MAX) return INT_MAX;
            
            i++;
        }
    
        return sign * result;
    }
    };

    /*
    from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        result = []
        p_count = Counter(p)  # Frequency map of p
        window_size = len(p)
        s_count = Counter(s[:window_size])  # Initial window

        if s_count == p_count:
            result.append(0)

        # Slide the window across the string
        for i in range(len(s) - window_size):
            left_char, right_char = s[i], s[i + window_size]
            
            s_count[left_char] -= 1
            if s_count[left_char] == 0:
                del s_count[left_char]  # Remove character if count becomes zero
            
            s_count[right_char] += 1  # Add the new right character

            if s_count == p_count:
                result.append(i + 1)  # Append the starting index

        return result*/

        /*
        class Solution(object):
    def reverseWords(self, s):
        strinnger = ""
        arr = [i for i in s.split()]
        for i in range(len(arr)-1,0,-1):
            strinnger+=arr[i] + " "
        strinnger += arr[0]
        return strinnger*/