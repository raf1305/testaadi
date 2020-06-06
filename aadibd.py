import copy
def task_1(your_data):
    rev_data=copy.copy(your_data[::-1])
    return True if rev_data==your_data else False
 
def task_2(N):
    for i in range(1,N):
        print (str(i)*i)
   
def task_3():
        SELECT
        d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
    FROM
        Employee e1
            JOIN
        Department d ON e1.DepartmentId = d.Id
    WHERE
        3 > (SELECT
                COUNT(DISTINCT e2.Salary)
            FROM
                Employee e2
            WHERE
                e2.Salary > e1.Salary
                    AND e1.DepartmentId = e2.DepartmentId
            )
    ; 
    
def task_4():
    def maxSum(arr, i, n): 
            
        if (i >= n): 
            return 0

            
        if (v[i]): 
            return dp[i] 
        v[i] = 1

            
        dp[i] = max(maxSum(arr, i + 1, n), 
                arr[i] + maxSum(arr, i + 2, n)) 

            
        return dp[i]







    maxLen = 10000
    dp = [0 for i in range(maxLen)] 
    v = [0 for i in range(maxLen)]
    n=int(input())
    arr=[int(x) for x in input().split(' ')]
    print(maxSum(arr, 0, n))
    


