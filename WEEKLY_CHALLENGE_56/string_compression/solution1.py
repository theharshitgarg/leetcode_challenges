class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        index = 0
        temp = chars
        len_string = len(chars)
        answer = []
        while index < len(chars):
            start = temp[index]
            s_index = index
            count = 0
            while index < len and start == temp[index]:
                count = count+1
                index = index+1
            h_i = index
            if count > 1:
                chars[s_index: h_i] = [start, str(count)]
            else:
                chars[s_index: h_i] = [start]
        print chars
        return len(chars)

sol = Solution()
print sol.compress(["a","a","b","b","c","c","c"])
print sol.compress(["a","a","a","b","b","a","a"])
