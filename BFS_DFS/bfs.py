#Breadth-first search

Q.add(root)
M.add(root)

while not isempty(Q):
	cur = Q.pop()
	if cur == to_find:
    	return True #we have found what we were looking for
          
	V.append(cur)
	for child in cur.children:
		if child not in M:
	    	Q.add(child)	
			M.add(child)

return False #element is not in tree