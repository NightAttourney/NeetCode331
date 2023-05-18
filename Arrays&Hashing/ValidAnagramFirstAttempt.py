# One solution to this problem is to create a set or dictionary make
# the word lowercase and then whenever you come across a new letter it is categoroized

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        letterSet = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in letterSet:
                letterSet[s[i]] += 1
            else:
                letterSet[s[i]] = 1
            if t[i] in letterSet:
                letterSet[t[i]] -= 1
            else:
                letterSet[t[i]] = -1
        if len(letterSet) != len(s):
            return False
        else:
            return True
        print(letterSet)

Solut = Solution()

print(Solut.isAnagram('car', 'rat'))
