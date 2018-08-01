'''
Author:Gnanika
Date:1 august 2018

'''
# Testing of comparing operators and if condition
varA=2
varB="gnani"
if type(varA) is str or type(varB) is str:
    print("string involved")
elif varA>varB:
	print("bigger")
elif varA==varB:
    print("equal")
else:
    print("smaller")

