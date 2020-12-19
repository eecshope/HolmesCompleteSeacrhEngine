from model import paragraph

class InvertedUnit:
	def __init__(self,arg_term: str ,arg_paragraph):
		self.chapter_index = arg_paragraph.chapter_index
		self.paragraph_index = arg_paragraph.index
		self.position = list()
	
		for i in range(len(arg_paragraph.lemmas)):
			if arg_term in arg_paragraph.lemmas[i]:
				self.position.append(i)


	
