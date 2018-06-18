# -*- coding: utf-8 -*-
import sentencepiece as spm
import os
import codecs
import pythaipiece
templates_dir = os.path.dirname(pythaipiece.__file__)
template_file = os.path.join(templates_dir, 'thai1.model')
sp = spm.SentencePieceProcessor()
sp.Load(template_file)
def segment(text):
	listdata=[i for i in sp.EncodeAsPieces(text) if i!= '▁']
	listword=[]
	for i in listdata:
		if '▁' in i:
			listword.append('')
			listword.append(i.replace('▁',''))
		else:
			listword.append(i)
	return listword
