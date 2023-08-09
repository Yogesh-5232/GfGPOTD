class Solution:
    def largestPrimeFactor (self, N):
        # code here
        max_prime = -1
        
        while N % 2 == 0:
            max_prime = 2
            N //= 2
        
        for i in range(3, int(N**0.5) + 1, 2):
            while N % i == 0:
                max_prime = i
                N //= i
    
        if N > 2:
            max_prime = N
        
        return max_prime
