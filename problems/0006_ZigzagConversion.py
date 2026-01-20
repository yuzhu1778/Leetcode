class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)<=numRows or numRows==1:
            return s

        else:
            rows=[[] for _ in range(numRows)]
            index=0
            d=1
            for char in s:
                rows[index].append(char)
                if index==0:
                    d=1
                elif index==numRows-1:
                    d=-1
                index+=d
        
            for i in range(numRows):
                rows[i]=''.join(rows[i])
            return ''.join(rows)