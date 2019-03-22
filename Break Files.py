import os
import hashlib
import pickle

def save(path):
	def allPatches(path):
		tree = os.walk(path)
		Patches = []
		for i in tree:
			Path = i[0]
			Files = i[2]
			for File in Files:
				 Patches.append(Path + "/" + File)
		return Patches

	dic = {}
	all = allPatches(path)
	for index, i in enumerate(all):
		print (index * 1.0 / len(all)) * 100, "%"
		dic[i] = hashlib.md5(open(i,'rb').read()).hexdigest()

	filename = path.replace("/", "->") + ".bd"
	file = open(filename,'wr')
	pickle.dump(dic,file)
	file.close()

def test(path):
	def load(path):
		filename = path.replace("/", "->") + ".bd"
		file = open(filename, "rb")
		dic = pickle.load(file)
		file.close()
		return dic

	def main_test(dic):
		Eror = False
		index = 0
		for file, hash in dic.iteritems():
			print (index * 1.0 / len(dic)) * 100, "%"
			byte = None
			try:
				byte = open(file,'rb').read()
			except IOError:
				Eror = True
				print "No such file", file

			if not byte is None:
				if hashlib.md5(byte).hexdigest() != hash:
					Eror = True
					print "File ", file," damaged"
			index += 1
		if Eror:
			print "Completed with errors"
		else:
			print "Completed without errors"
		

	dic = load(path)
	main_test(dic)


path = "" # You path
#save(path) # for save hash all files
#test(path) # for check hask sum




























