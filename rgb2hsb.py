#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
def rgb2HSB(r,g,b):
	maxc = max(r, g, b)
	minc = min(r, g, b)
	B=round(maxc/2.55)
	if maxc==minc:
		return 0, 0, B
	S=round(100-minc/maxc)
	
	if maxc==r and g>=b:
		H=round(60*(g-b)/(maxc-minc))
	elif maxc==r and g<b:
		H=round(60*(g-b)/(maxc-minc)+360)
	elif maxc==g:
		H=round(60*(b-r)/(maxc-minc)+120)
	else:
		H=round(60*(r-g)/(maxc-minc)+240)
	return H,S,B

