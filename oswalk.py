#coding:utf-8
import os 
import sys
import pickle
file_count=0
file_size=0
#print os.system("dir")
file_class=[]
result_file=[]
error_files=[]
max=0
max_temp=""
too_long=[]
max_in=0
re="re"
re_flag=0
for a,b,c in os.walk("I:\\self"):
		#print "start>"
		print a
		#print len(a)
		flag=0
		
		for i in b:
			'''
			if len(i)>100:
				print ">>>>"+i
				print "i[-3:] is "+i[0:10]
				print i[5:7]
				flag=1
				break
			'''
			if len(i)>100:
				print "before is {}".format(os.path.join(a,i))
				os.rename(os.path.join(a,i),os.path.join(a,re+str(re_flag)))
				flag=1
				print "after is {}".format(os.path.join(a,re+str(re_flag)))
				re_flag+=1
				#break
				too_long.append(a+i)
				max=len(i)+len(a)
				b.remove(i)
				print "afeer"
		if flag==1:
			break
			
		try:
			a=a.decode('gbk')
			for i in c:
				if len(a)+len(i)>258:
					too_long.append(a+i)
					max=len(a)+len(i)
					c.remove(i)
			
			for i in c:
				if len(i)+len(a)>max_in:
					max_in=len(i)+len(a)
				
				#print "typei:%s"%type(i)
				#print i
				#i=unicode(i,"utf-8")
				i=i.decode('gbk')
				temp=i.split('.')
				temp=temp[-1]
				if temp not in file_class:
					file_class.append(temp)
				#print i 
				#i=i.decode('utf8').encode('gbk')
				if i.lower().endswith(('.mp4','.mkv','.rmvb','.avi')):
					
					#print i
					try:
						file_temp=os.path.join(a,i)
						result_file.append(file_temp)
						file_size+=os.path.getsize(file_temp)
					except:
						error_files.append(os.path.join(a,i))
						continue
		except:
			for j in c:
				error_files.append(a)
				error_files.append(j)
			continue
		#print ">>"
		#print max
		#print "max in is {}".format(max_in)
		#		print too_long
		#file_count+=len(c)
		#print file_size
		#print "too long : {}".format(too_long)
		print "<<end"

print "origin:%d"%file_size
#print file_size/float(1024*1024*1024)
#print file_class
#print result_file

with open("D:\\coding\\newtestkind.txt",'wb+') as a:
	pickle.dump(file_class,a)
	
with open("D:\\coding\\newerrormovie.txt",'wb+') as b:
	pickle.dump(error_files,b)
	
with open("D:\\coding\\newtestsize.txt",'wb+') as c:
	pickle.dump(file_size,c)
	
	
with open("D:\\coding\\newresultmovie.txt",'wb+') as c:
	pickle.dump(result_file,c)	
with open("D:\\coding\\newtoolong.txt",'wb+') as c:
	pickle.dump(too_long,c)		
'''
with open("D:\\coding\\testtest.txt",'wb+') as a:
	a.write('[')
	for i in file_class:
		a.write(i)
		a.write(',')
		
	a.write(']')
	a.write("wrong files:\n")
	for i in error_files:
		a.write(i)
		a.wriet('\n')
with open("D:\\coding\\testmovie.txt",'wb+') as b:
	b.write('total size:')
	b.write(str(file_size))
	b.write("\ntotal amount:")
	b.write(str(len(result_file))+"\n")
	
	for i in result_file:
		b.write(i)
		b.write('\n')

'''
