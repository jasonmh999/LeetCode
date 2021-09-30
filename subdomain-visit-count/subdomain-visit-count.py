class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visited={}
        for domain in cpdomains:
            rep,subs=domain.split(' ')
            curr=None
            for sub in reversed(subs.split('.')):
                if curr:
                    curr=sub+'.'+curr
                else:
                    curr=sub
                visited[curr]=visited.get(curr,0)+int(rep)
        
        """ans=[]
        for key,value in visited.items():
            ans.append(str(value)+' '+key)"""
        return [str(value)+' '+key for key,value in visited.items()]
            
                
            