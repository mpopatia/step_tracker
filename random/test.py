# def get_user_steps(user, date):
# 	return 1

# def one(users):
# 	date = "10-03-2016"
# 	for u in users:
# 		s = get_user_steps(u, date)
# 		if s is None:
# 			message = "User 1, you did not enter data for" + date + "."
# 			send_email("mpoatia@cmu.edu", message)
# 		else:
# 			if s.steps > 10000:
# 				message = "Congratualtions user 1, you completed your goal with a total of " + s.steps + "for" + date +"."
# 				send_email("mpoatia@cmu.edu", message)
# 			else:
# 				message = "Congratualtions user 1, you did not complete your goal with a total of just" + s.steps + "for" + date +"."
# 				send_email("mpoatia@cmu.edu", message)

def validate():
	ids = [101,102,103,104]
	for i in xrange(len(ids)-1):
		if ids[i]+1 != ids[i+1]:
			return False
	return True

def simple_pair():
	ans = []
	ids = [101,102,103,104, 105, 106]
	for i in xrange(0,len(ids),2):
		ans.append((ids[i], ids[i+1]))

	return ans

def test():
    ans = []
    ids = [101, 102, 103,106, 107]
    for i in xrange(len(ids)):
        elem = ids[i]
        if elem % 2 == 1:
        	if i != len(ids)-1:
	            elem2 = ids[i+1]
	            if elem+1 == elem2:
	                ans.append((elem, elem2))
	            else:
	                ans.append((elem, None))
	        else:
	        	ans.append((elem, None))
        else:
            if i != 0:
            	elem3 = ids[i-1]
            	if elem - 1 != elem3:
            		ans.append((None, elem))
            else:
            	ans.append((None, elem))


    print ans



test()

print validate()
print simple_pair()