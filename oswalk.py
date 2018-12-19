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
for a,b,c in os.walk("c:\\"):
	print a
	try:
		a=a.decode('gbk')
		
		for i in c:
			
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

	#file_count+=len(c)
	print file_size
print "origin:%d"%file_size
#print file_size/float(1024*1024*1024)
#print file_class
#print result_file

with open("D:\\coding\\ctestkind.txt",'wb+') as a:
	pickle.dump(file_class,a)
	
with open("D:\\coding\\cerrormovie.txt",'wb+') as b:
	pickle.dump(error_files,b)
	
with open("D:\\coding\\ctestsize.txt",'wb+') as c:
	pickle.dump(file_size,c)
	
	
with open("D:\\coding\\cresultmovie.txt",'wb+') as c:
	pickle.dump(result_file,c)	
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