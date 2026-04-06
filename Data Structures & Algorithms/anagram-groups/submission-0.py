class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output=[]
        visited = [False]*len(strs)
        for i in range(len(strs)):
            if visited[i]:
                continue
            if strs[i] not in output:

                temp = []
                temp.append(strs[i])
                for j in range(i+1,len(strs)):
                    if len(strs[i])==len(strs[j]):
                        if sorted(strs[i])==sorted(strs[j]):
                            temp.append(strs[j])
                            visited[j] = True
                output.append(temp)
        return output
