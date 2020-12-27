import _pickle as pkl
import json
import numpy as np

from model import chapter

raw_file = open('./data/caches/chapter_cache.pkl', 'rb')
dictlist = pkl.load(raw_file)
raw_file.close()
dictnum = len(dictlist)

raw_file = open('./data/caches/inverted_index_cache.pkl', 'rb')
inverted_index = pkl.load(raw_file)
raw_file.close()

raw_file = open('./data/caches/wordbag_cache.pkl', 'rb')
wordbag = pkl.load(raw_file)
raw_file.close()

raw_file = open('./data/caches/paragraph_cache.pkl', 'rb')
paralist = pkl.load(raw_file)
raw_file.close()

raw_file = open('./data/caches/wordnumber_cache.pkl', 'rb')
wordnumber = pkl.load(raw_file)
raw_file.close()

characters = list()

character0 = dict()
character0['id'] = 0
character0['name'] = 'Sherlock Holmes'
character0['subscribe'] = 'William Sherlock Scott Holmes (Benedict Cumberbatch) describes himself initially as "a consulting detective, the only one in the world",[1] helping out Scotland Yard when they are out of their depth with cases (usually homicides). He appears as a tall, thin man with dark, curly hair. Like the original character, Sherlock is highly intelligent and able to deduce or abduce information from the small details. According to Molly Hooper in the episode The Sign of Three, he is a graduate chemist.'
presented_chapters0 = set()
for i in range(len(inverted_index[wordnumber['sherlock']])):
	presented_chapters0.add(inverted_index[wordnumber['sherlock']][i].chapter_index)
presented_chapters0 = list(presented_chapters0)
chapters_name0 = list()
for index in presented_chapters0:
	chapters_name0.append(dictlist[index].story + " " + dictlist[index].part + " " + dictlist[index].chapter)
character0['chapters'] = list()
character0['chapters'].extend(chapters_name0)
characters.append(character0)

character1 = dict()
character1['id'] = 1
character1['name'] = 'John Watson'
character1['subscribe'] = 'John Hamish Watson (Martin Freeman) is Sherlock\'s best friend. He is often a foil to Sherlock in both appearance and personality. Unlike Sherlock, John is short with blond hair. He is friendly, compassionate, and patient, compared to Sherlock\'s aloof, cold-hearted tendencies. He gets on better with the police and takes care of practical matters at their flat, apparently doing most of the shopping. Sherlock has called him "the wisest, warmest human being [he] knows", and has stated that "the warmth and constancy of [John\'s] friendship" can redeem even a "rude, ignorant, all-around obnoxious arsehole like [Sherlock]".'
presented_chapters1 = set()
for i in range(len(inverted_index[wordnumber['watson']])):
	presented_chapters1.add(inverted_index[wordnumber['watson']][i].chapter_index)
presented_chapters1 = list(presented_chapters1)
chapters_name1 = list()
for index in presented_chapters1:
	chapters_name1.append(dictlist[index].story + " " + dictlist[index].part + " " + dictlist[index].chapter)
character1['chapters'] = list()
character1['chapters'].extend(chapters_name1)
characters.append(character1)

character2 = dict()
character2['id'] = 2
character2['name'] = 'D.I.Grag Lestrade'
character2['subscribe'] = 'Detective Inspector Greg Lestrade (Rupert Graves) works for Scotland Yard. He has a reluctant respect for Sherlock and often defends him from the other police officers\' animosity. He is often frustrated by Sherlock\'s cryptic deductions and habit of withholding evidence, but believes that he is a great man (hoping that one day, he can overcome his poorer qualities, and become a "good" man).'
presented_chapters2 = set()
for i in range(len(inverted_index[wordnumber['lestrade']])):
	presented_chapters2.add(inverted_index[wordnumber['lestrade']][i].chapter_index)
presented_chapters2 = list(presented_chapters2)
chapters_name2 = list()
for index in presented_chapters2:
	chapters_name2.append(dictlist[index].story + " " + dictlist[index].part + " " + dictlist[index].chapter)
character2['chapters'] = list()
character2['chapters'].extend(chapters_name2)
characters.append(character2)

character3 = dict()
character3['id'] = 3
character3['name'] = 'Martha Louise Hudson'
character3['subscribe'] = 'Martha Louise Hudson, née Sissons (Una Stubbs) is the landlady of 221B Baker Street. Sherlock won his way into her good graces after ensuring her husband, who ran a drug cartel, was executed for a double murder in Florida.'
presented_chapters3 = set()
for i in range(len(inverted_index[wordnumber['hudson']])):
	presented_chapters3.add(inverted_index[wordnumber['hudson']][i].chapter_index)
presented_chapters3 = list(presented_chapters3)
chapters_name3 = list()
for index in presented_chapters3:
	chapters_name3.append(dictlist[index].story + " " + dictlist[index].part + " " + dictlist[index].chapter)
character3['chapters'] = list()
character3['chapters'].extend(chapters_name3)
characters.append(character3)

character4 = dict()
character4['id'] = 4
character4['name'] = 'Mycroft Holmes'
character4['subscribe'] = 'Mycroft Holmes (played by the show\'s executive producer, co-creator, and writer Mark Gatiss) is first introduced when he abducts John and offers to pay him to spy on Sherlock. He is Sherlock\'s older brother and engages in sibling rivalry with Sherlock. Mycroft is frequently mocked by Sherlock for “putting on weight”. He occupies a "minor position in the British government"; however, as with many Holmes-based works, it is heavily hinted that he has a much bigger role than he claims – on one occasion, Sherlock sarcastically remarks that Mycroft is the British government "when he’s not too busy being the British Secret Services, or the CIA on a freelance basis". He is driven around in a private car with his personal assistant who goes by the name of "Anthea".'
presented_chapters4 = set()
for i in range(len(inverted_index[wordnumber['mycroft']])):
	presented_chapters4.add(inverted_index[wordnumber['mycroft']][i].chapter_index)
presented_chapters4 = list(presented_chapters4)
chapters_name4 = list()
for index in presented_chapters4:
	chapters_name4.append(dictlist[index].story + " " + dictlist[index].part + " " + dictlist[index].chapter)
character4['chapters'] = list()
character4['chapters'].extend(chapters_name4)
characters.append(character4)

character5 = dict()
character5['id'] = 5
character5['name'] = 'Jim Moriarty'
character5['subscribe'] = 'James "Jim" Moriarty (Andrew Scott) is a "consulting criminal", a counterpoint to Sherlock\'s similarly unrivaled "consulting detective". He is responsible for the criminals and crimes in all three episodes of the first series, acting as a sponsor, an informant, or a mastermind. His interest in Sherlock borders on obsession, though he does not hesitate trying to kill him when he loses interest. Like Sherlock, he possesses a genius level intellect and appears to be motivated by boredom rather than money or power.'
presented_chapters5 = set()
for i in range(len(inverted_index[wordnumber['moriarty']])):
	presented_chapters5.add(inverted_index[wordnumber['moriarty']][i].chapter_index)
presented_chapters5 = list(presented_chapters5)
chapters_name5 = list()
for index in presented_chapters5:
	chapters_name5.append(dictlist[index].story + " " + dictlist[index].part + " " + dictlist[index].chapter)
character5['chapters'] = list()
character5['chapters'].extend(chapters_name5)
characters.append(character5)

character6 = dict()
character6['id'] = 6
character6['name'] = 'Irene Adler'
character6['subscribe'] = 'Irene Adler (Lara Pulver) is featured in "A Scandal in Belgravia" as a dominatrix, known professionally as "The Woman". She takes pictures of her clients during her job as "protection" to make sure her clients don\'t do anything unfavourable to her. Irene is brilliant enough to impress Sherlock, and managed to deceive him; however, she also ends up falling in love with him, which proves to be her downfall. She sends Sherlock a series of flirtatious texts, repeatedly requesting to "have dinner" with him.'
presented_chapters6 = set()
for i in range(len(inverted_index[wordnumber['adler']])):
	presented_chapters6.add(inverted_index[wordnumber['adler']][i].chapter_index)
presented_chapters6 = list(presented_chapters6)
chapters_name6 = list()
for index in presented_chapters6:
	chapters_name6.append(dictlist[index].story + " " + dictlist[index].part + " " + dictlist[index].chapter)
character6['chapters'] = list()
character6['chapters'].extend(chapters_name6)
characters.append(character6)

#print(character0)
filepath = './data/caches/main_character.json'
json_file = open(filepath,'w+')
jsonArr = json.dump(characters,json_file,ensure_ascii=True,indent=4)





