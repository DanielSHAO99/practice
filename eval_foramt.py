
flag=[chr(i) for i in range(65,92)]
temp=["flag"+"["+str(i)+"]" for i in range(26)]
temp_str=",".join(temp)

temp_t=tuple(temp)
result_pre="'"+"{}-"*26+"'"
#print "temp_str is {}".format(temp_str)
#print "result_pre is {}".format(result_pre)
#print eval(temp_str)
#print result_pre.format(eval(temp_str))
#print "{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{
# }-{}-{}-{}-{}-{}-{}-{}-{}-{}-".format(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'))
#print "type(eval(temp_str)) is {}".format(type(eval(temp_str)))

result_all=result_pre+".format("+temp_str+")"
#print eval(result_all)
'''
print ">>{}".format(result_all)
print "{}".format(eval("flag[0],flag[1]"))
print eval("flag[0],flag[1]")
'''
print "result_all is {}".format(result_all)
#print "Final>>>>>"
print eval(result_all)

