opening_brackets=dict(zip(brackets[0::2],brackets[1::2]))
	closing_brackets=dict(zip(brackets[1::2],brackets[0::2]))

	bracket_stack=[]

	for chr in text:
		if chr in opening_brackets:
			bracket_stack.append(chr)
		elif chr in closing_brackets:
			if len(bracket_stack)==0 or bracket_stack[-1]!=closing_brackets[chr]:
				return False
			else:
				bracket_stack.pop()


	return len(bracket_stack)==0