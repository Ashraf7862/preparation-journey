'''You are given an undirected tree with n nodes labeled 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an undirected edge between nodes ui and vi.

You are also given a string s of length n consisting of lowercase English letters, where s[i] represents the character assigned to node i.

You are also given a string array queries, where each queries[i] is either:

"update ui c": Change the character at node ui to c. Formally, update s[ui] = c.
"query ui vi": Determine whether the string formed by the characters on the unique path from ui to vi (inclusive) can be rearranged into a palindrome.
Return a boolean array answer, where answer[j] is true if the jth query of type "query ui vi"​​​​​​​ can be rearranged into a palindrome, and false otherwise.

 

Example 1:

Input: n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]

Output: [true,false]

Explanation:

"query 0 2": Path 0 → 1 → 2 gives "aac", which can be rearranged to form "aca", a palindrome. Thus, answer[0] = true.
"update 1 b": Update node 1 to 'b', now s = "abc".
"query 0 2": Path characters are "abc", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
Thus, answer = [true, false].

Example 2:

Input: n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]

Output: [false,false,true]

Explanation:

"query 1 2": Path 1 → 0 → 2 gives "bac", which cannot be rearranged to form a palindrome. Thus, answer[0] = false.
"update 0 b": Update node 0 to 'b', now s = "bbca".
"query 2 3": Path 2 → 0 → 3 gives "cba", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
"update 3 a": Update node 3 to 'a', s = "bbca".
"query 1 3": Path 1 → 0 → 3 gives "bba", which can be rearranged to form "bab", a palindrome. Thus, answer[2] = true.
Thus, answer = [false, false, true].'''

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        par = [0] * n
        tin = [0] * n
        tout = [0] * n
        order = []
        stack = [0]
        while stack:
            x = stack.pop()
            if x < 0:
                tout[~x] = len(order)
                continue
            tin[x] = len(order)
            order.append(x)
            stack.append(~x)
            for y in g[x]:
                if y != par[x]:
                    par[y] = x
                    stack.append(y)
        st = [[tin[par[x]] for x in order]]
        for k in range(1, n.bit_length()):
            prev = st[-1]
            st.append([
                min(prev[i], prev[i + (1 << (k - 1))])
                for i in range(n - (1 << k) + 1)
            ])
        def lca(u, v):
            if u == v:
                return u
            l, r = sorted((tin[u], tin[v]))
            k = (r - l).bit_length() - 1
            return order[min(
                st[k][l + 1],
                st[k][r - (1 << k) + 1]
            )]
        bits = [1 << (ord(c) - 97) for c in s]
        path = bits[:]
        for x in order[1:]:
            path[x] ^= path[par[x]]
        fw = [0] * (n + 1)
        def update(x, d):
            for i in (tin[x] + 1, tout[x] + 1):
                while i < len(fw):
                    fw[i] ^= d
                    i += i & -i
        def get(x):
            mask = path[x]
            i = tin[x] + 1
            while i:
                mask ^= fw[i]
                i -= i & -i
            return mask
        ans = []
        for q in queries:
            typ, a, b = q.split()
            a = int(a)
            if typ == "update":
                new_bit = 1 << (ord(b) - 97)
                update(a, bits[a] ^ new_bit)
                bits[a] = new_bit
            else:
                b = int(b)
                p = lca(a, b)
                mask = get(a) ^ get(b) ^ bits[p]
                ans.append(mask.bit_count() <= 1)
        return ans

object= Solution()
n = 3
edges = [[0,1],[1,2]]
s = "aac"
queries = ["query 0 2","update 1 b","query 02"]
print(object.palindromePath(n,edges,s,queries))