# class Solution(object):
#     def compress(self, chars):
#         """
#         :type chars: List[str]
#         :rtype: int
#         """
#         # from collections import Counter
#         # counter = Counter(chars)
#         index = 0
#         len_string = len(chars)
#         answer = ""
#         while index < len_string:
#         	start = chars[index]
#         	count = 0
#         	while index < len_string and start == chars[index]:
#         		count = count+1
#         		index = index+1
#         	print "C", count
#         	print "A", answer
#         	answer = answer+start
#         	print answer
#         	if count > 1:
#         		answer = answer+str(count)
#         	print answer

#         return answer



# sol = Solution()
# print sol.compress("aaabbb")
# print sol.compress("abbbbbbbbbb")
# print sol.compress(["a","a","b","b","c","c","c"])



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
        chars = []
        while index < len_string:
        	start = temp[index]
        	count = 0
        	while index < len_string and start == temp[index]:
        		count = count+1
        		index = index+1
        	chars.append(start)
        	if count > 1:
        		chars.append(str(count))
        # chars = answer
        # print chars
        del temp
        return len(chars)

sol = Solution()
print sol.compress("aaabbb")
print sol.compress("abbbbbbbbbb")
print sol.compress(["a","a","b","b","c","c","c"])
