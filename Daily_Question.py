# 2264 Largest 3-Same-Digit Number in String

def largestGoodInteger(self, num):
	"""
	:type num: str
	:rtype: str
	"""
	last_num = num[0]
	count = 0
	current_best = ""
	
	for number in num[1:]:
			if number == last_num and number > current_best:
					count += 1
			else:
					count = 0
					last_num = number
			
			if count == 2:
					current_best = number
	
	return "" + current_best + current_best + current_best

# 1688 Count of Matches in Tournament
def numberOfMatches(self, n):
        return n-1

# 1662 Check If Two String Arrays are Equivalent
def arrayStringsAreEqual(self, word1, word2):
	word1ans = "".join(word1)
	
	word2ans = "".join(word2)
	    
	if word1ans == word2ans:
	    return True
	else:
	    return False
