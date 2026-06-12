class Solution(object):
    def hIndex(self, citations):
        # first we sort the number 
        citations.sort()
        count = 0 # assign count

        for i in range(len(citations)):
            # now we have to find if index + 1 <= citation[i] than count += 1
            # as we know it sort in asending order for maintaining that we have to use this 
            h = len(citations) - i
            
            if citations[i] >= h:
                count += 1
        return count
        
        