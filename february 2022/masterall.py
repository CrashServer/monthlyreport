### FoxDot function masterAll() ### 
### One function to rule them all !!! ###

valueDict = {}

def masterAll(args = "dur", value=1):
	global valueDict
	if args != "reset":
		for p in Clock.playing:
			if p in valueDict:
				if args in valueDict[p]:
					pass
				else:
					try:
						valueDict[p][args] = p.__getitem__(args)
					except:
						valueDict[p][args] = 0
			else:
				valueDict[p] = {}
				try:
					valueDict[p][args] = p.__getitem__(args)
				except:
					valueDict[p][args] = 0
			p.__setattr__(args, value)
	else:
		for k,v in valueDict.items():
			for l, w in v.items():
				try:
					k.__setattr__(l, w)
				except:
					pass
		valueDict = {}

'''
- add a lots of players with different dur.
- masterAll("dur", 4)
- masterAll("reset")
'''