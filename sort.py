import midi.events "must have this repo https://github.com/vishnubob/python-midi"

def sort(pattern):
	lst = []
	for entry in pattern[1]:
		if type(entry) == midi.events.NoteOnEvent and entry.get_velocity() >= 0:
			lst.append([entry.get_pitch(), entry.tick])
	lst = mergesort(lst)
	print lst
	nwlst = [lst[0]]
	for i in range(1, len(lst)):
		j = 1
		if lst[i-j][1] != lst[i][1]:
			nwlst += [lst[i]]
		else:
			while lst[i-j][1] == lst[i][1]:
				if lst[i-j][0] == lst[i][0]:
					break
				elif i - j - 1 < 0 or lst[i - j - 1][1] != lst[i][1]:
					nwlst += [lst[i]]
					break
				else:
					j += 1
	return nwlst

def mergesort(lst):
	if len(lst) == 0:
		return []
	elif len(lst) == 1:
		return lst
	else:
		mid = len(lst) / 2;
		return merge(mergesort(lst[0:mid]), mergesort(lst[mid:]))

def merge(l1, l2):
	l = []
	c1, c2 = 0, 0
	while len(l1) != 0 and len(l2) != 0:
		if l1[0][1] < l2[0][1]:
			l += [l1[0]]
			l1 = l1[1:]
		else:
			l += [l2[0]]
			l2 = l2[1:]
	if len(l1) == 0:
		l1 = l2
	for x in l1:
		l += [x]
	return l
