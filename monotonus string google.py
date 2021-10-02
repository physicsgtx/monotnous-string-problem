# Function to return final result
def minReqSubstring(s, n):
     
    # Initialize variable to keep
    # track of ongoing sequence
    ongoing = 'N'
    count, l = 0, len(s)
     
    for i in range(1, l):
         
        # If current sequence is neither
        # increasing nor decreasing
        if ongoing == 'N':
             
            # If prev char is greater
            if s[i] < s[i - 1]:
                ongoing = 'D'
                 
            # If prev char is same
            elif s[i] == s[i - 1]:
                ongoing = 'N'
                 
            # Otherwise
            else:
                ongoing = 'I'
                 
        # If current sequence
        # is Non-Decreasing
        elif ongoing == 'I':
             
            # If prev char is smaller
            if s[i] > s[i - 1]:
                ongoing = 'I'
                 
            # If prev char is same
            elif s[i] == s[i - 1]:
                 
                # Update ongoing
                ongoing = 'I'
             
            # Otherwise
            else:
                 
                # Update ongoing
                ongoing = 'N'
                 
                # Increase count
                count += 1
             
        # If current sequence
        # is Non-Increasing
        else:
             
            # If prev char is greater,
            # then update ongoing with D
            if s[i] < s[i - 1]:
                ongoing = 'D'
                 
            # If prev char is equal, then
            # update current with D
            elif s[i] == s[i - 1]:
                ongoing = 'D'
                 
            # Otherwise, update ongoing
            # with N and increment count
            else:
                ongoing = 'N'
                count += 1
                 
    # Return count + 1
    return count + 1
 
# Driver code
S = "aeccdhba"
n = len(S)
 
print(minReqSubstring(S, n))
