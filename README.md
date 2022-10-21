
# Visconde: Multi-document QA with GPT-3 and Neural Reranking

In this repository we maintain the code used in the paper Visconde: Multi-document QA with GPT-3 and Neural Reranking, submited to European Conference on Information Retrieval ECIR2023.

> **Abstract:** This paper discusses a question-answering system that can answer questions whose supporting evidence is spread over multiple (potentially long) documents. The system, called Visconde, uses a three-step pipeline to perform the task: decompose, retrieve, and aggregate. The first step decomposes the question into simpler questions using a few-shot large language model (LLM). Then, a state-of-the-art search engine is used to retrieve candidate passages from a large collection for each decomposed question. In the final step, we use the LLM in a few-shot setting to aggregate the contents of the passages into the final answer. The system is evaluated on three datasets: IIRC, Qasper, and StrategyQA. Results suggest that current retrievers are the main bottleneck and that readers are already performing at the human level as long as relevant passages are provided. The system is also shown to be more effective when the model is induced to give explanations before.

We evaluated our proposal on three datasets: [IIRC](https://allenai.org/data/iirc), [QASPER](https://allenai.org/data/qasper) and [StrategyQA](https://allenai.org/data/strategyqa).

## Reproducing
Download datasets

    sh setup.sh

### IIRC

 1. [Decompose test questions](https://anonymous.4open.science/r/visconde-4592/iirc_generate_explanations.ipynb)
 2. [Create Indices](https://anonymous.4open.science/r/visconde-4592/iirc_create_indices.ipynb)
 3. [Create list for reranking](https://anonymous.4open.science/r/visconde-4592/iirc_prepare_to_rerank.ipynb)
 4. [Rerank items (GPU required)](https://anonymous.4open.science/r/visconde-4592/iirc_rerank.ipynb)
 5. [Generate explanation for training examples](https://anonymous.4open.science/r/visconde-4592/iirc_generate_explanations.ipynb)
 6. [Testing](https://anonymous.4open.science/r/visconde-4592/iirc_generate_and_evaluate.ipynb)

### QASPER

 1. [Rerank paragraphs by question](https://anonymous.4open.science/r/visconde-4592/qasper_rerank.ipynb)
 2. [Testing](https://anonymous.4open.science/r/visconde-4592/qasper_generate.ipynb)
 3. Compute metrics
	For computing metrics download run:
	
  ```python qasper_evaluator.py --predictions PREDICTIONS_FILE --gold data/qasper-test-v0.3.json --text_evidence_only```

### StrategyQA

 1. [Create indices](https://anonymous.4open.science/r/visconde-4592/strategyqa_create_indices.py)
 2. [Decompose questions](https://anonymous.4open.science/r/visconde-4592/strategyqa_decompose_query.ipynb)
 3. [Create lists for reranking](https://anonymous.4open.science/r/visconde-4592/strategyqa_create_rerankable.py)
 4. [Rerank items (GPU required)](https://anonymous.4open.science/r/visconde-4592/strategyqa_rerank.ipynb)
 5. [Testing](https://anonymous.4open.science/r/visconde-4592/strategyqa_generate.ipynb)
 6. Compute metrics
	 For computing metrics clone [this repository](https://github.com/allenai/strategyqa-evaluator.git) and run the evaluator.

