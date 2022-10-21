from pyserini.search import SimpleSearcher
import json
from tqdm import tqdm

searcher = SimpleSearcher('./data/strategyqa_index_all')

test_set = json.load(open("data/decomposed_dev_dynamic.json",'r'))

to_rerank = []

k = 1000

for item in tqdm(test_set):

    decompositions = []

    for d in item['decompositions']:
        hits = searcher.search(item['question'],k=k)

        hits = [json.loads(hit.raw) for hit in hits]
        decompositions.append({
            "question": d,
            "documents": hits
        })
    to_rerank.append({
        "qid": item['qid'],
        "question": item['question'],
        "decompositions": decompositions
    })

json.dump(to_rerank, open("./data/strategyqa_torerank.json", 'w'))
