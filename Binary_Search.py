'''
left middle Right
check if the middle is the target... if yes return the position
if not, check if the target is smaller than the middle 
if yes, then bring the target position to the middle and recalculate the middle position 
and check the target is smaller or greater than the middle position element...

repeate this and find the target element position...
'''

array = [4,7,8,12,45,99]
target = 45
pos = -1
l = 0
r = len(array) - 1
