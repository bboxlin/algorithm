class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # [-2,-2,1,-2]
        stack = []
        for asteriod in asteroids:
            if asteriod > 0:
                stack.append(asteriod)
            else:             
                while stack and stack[-1] > 0 and stack[-1] < abs(asteriod):
                    stack.pop() 
                    
                if not stack or stack[-1] < 0:
                    stack.append(asteriod) 
  
                if stack[-1] == abs(asteriod):
                    stack.pop()
        return stack
    
    
 