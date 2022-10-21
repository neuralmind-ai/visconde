import json
from tqdm import tqdm
import spacy

nlp = spacy.blank("en")
nlp.add_pipe(nlp.create_pipe("sentencizer"))

stride = 4
max_length = 5

def window(document, stride=stride, max_length=max_length):
    doc = nlp(document[:10000])
    sentences = [sent.string.strip() for sent in doc.sents]
    if len(sentences) > max_length:
        new_documents = []
        for i in range(0, len(sentences), stride):
            segment = ' '.join(sentences[i:i + max_length])
            new_documents.append(segment)
        return new_documents
    return [document]


print("Creating strategyQA pyserin indices")

f = open("data/corpus-enwiki-20200511-cirrussearch-parasv2.jsonl",'r')
file_limit = 1000000
file_items_count = 0
file_number = 0

nf = open("data/strategyqa_pyserin_files/{0}.jsonl".format(file_number),"w")
id_ = 1
for l in tqdm(f):
    item = json.loads(l)
    docs = window(item['para'])
    # docs = [item['para']]
    for d in docs:    
        item['contents'] = "Title: {0}. Content: {1}".format(item["title"],d)
        item['m_id'] = item["title"]+"-"+str(item['para_id'])
        item['id'] = id_
        id_ += 1
        if "para" in item:
            del item['para']
        nf.write(json.dumps(item)+"\n")
        file_items_count = file_items_count + 1
    if file_items_count >= file_limit:
        file_number = file_number + 1
        nf.close()
        nf = open("data/strategyqa_pyserin_files/{0}.jsonl".format(file_number),"w")
        file_items_count = 0
    