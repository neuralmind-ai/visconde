# dataset download  

# iirc
wget https://iirc-dataset.s3.us-west-2.amazonaws.com/iirc_train_dev.tgz -P data
wget https://iirc-dataset.s3.us-west-2.amazonaws.com/context_articles.tar.gz -P data
wget https://iirc-dataset.s3.us-west-2.amazonaws.com/iirc_test.json -P data

cd data
tar -xf context_articles.tar.gz
tar -xf iirc_train_dev.tgz


# qasper

wget https://qasper-dataset.s3.us-west-2.amazonaws.com/qasper-test-and-evaluator-v0.3.tgz
tar -xf qasper-test-and-evaluator-v0.3.tgz
cd ..

wget https://storage.googleapis.com/ai2i/strategyqa/data/strategyqa_dataset.zip -P data
wget https://storage.googleapis.com/ai2i/strategyqa/data/corpus-enwiki-20200511-cirrussearch-parasv2.jsonl.gz -P data
