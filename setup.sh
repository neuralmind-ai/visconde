# dataset download  
cd data
# iirc
wget https://iirc-dataset.s3.us-west-2.amazonaws.com/iirc_train_dev.tgz 
wget https://iirc-dataset.s3.us-west-2.amazonaws.com/context_articles.tar.gz 
wget https://iirc-dataset.s3.us-west-2.amazonaws.com/iirc_test.json 

tar -xf context_articles.tar.gz
tar -xf iirc_train_dev.tgz

# qasper

wget https://qasper-dataset.s3.us-west-2.amazonaws.com/qasper-test-and-evaluator-v0.3.tgz
tar -xf qasper-test-and-evaluator-v0.3.tgz

#strategy qa
wget https://storage.googleapis.com/ai2i/strategyqa/data/strategyqa_dataset.zip 
wget https://storage.googleapis.com/ai2i/strategyqa/data/corpus-enwiki-20200511-cirrussearch-parasv2.jsonl.gz 

unzip strategyqa_dataset.zip
corpus-enwiki-20200511-cirrussearch-parasv2.jsonl.gz 
gzip -dv corpus-enwiki-20200511-cirrussearch-parasv2.jsonl.gz
