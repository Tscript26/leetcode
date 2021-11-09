"""
Suppose you are at a party with n people (labeled from 0 to n - 1), and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her, but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

 

Example 1:


Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
Example 2:


Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.
 

Constraints:

n == graph.length
n == graph[i].length
2 <= n <= 100
graph[i][j] is 0 or 1.
graph[i][i] == 1
 

Follow up: If the maximum number of allowed calls to the API knows is 3 * n, could you find a solution without exceeding the maximum number of calls?

"""

# The knows API is already defined for you.
# return a bool, whether a knows b

def knows(a: int, b: int) -> bool:
    global called, persons
    called += 1
    if called > 3 * persons:
        print("over maximum")
    return graph[a][b] == 1
class Solution:
    def findCelebrity(self, n: int) -> int:
        off = set()
        def temp(candidates):
            print(candidates)
            i = 0
            if len(candidates) == 1:
                if all(knows(i, candidates[0]) for i in range(n)) and all(not knows(candidates[0], i) for i in range(n) if i != candidates[0]):
                    return candidates[0]
                return -1

            rest = []
            total = len(candidates)
            while i < total:
                a = candidates[i % total]
                b = candidates[(i + 1) % total]
                if knows(a, b):
                    if b not in off:
                        rest.append(b)
                    off.update({a})
                    try:
                        rest.remove(a)
                    except:
                        pass
                i += 1
            if rest:
                return temp(rest)
            return -1
        return temp([i for i in range(n)])


if __name__ == '__main__':
    called = 0
    # persons = 3
    # graph = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
    # graph = [[1,1,0],[0,1,0],[1,1,1]] # 1
    persons = 4
    graph = [[1,1,1,0],[1,1,0,1],[0,1,1,0],[1,1,1,1]]
    S = Solution()
    print(S.findCelebrity(persons))