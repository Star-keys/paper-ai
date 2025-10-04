"""
Mock Database
실제 MySQL 대신 사용할 가짜 데이터베이스
나중에 실제 DB로 교체 가능하도록 설계
"""

# Mock 논문 데이터
PAPERS = [
    {
        "id": 1,
        "title": "Attention Is All You Need",
        "authors": "Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N and Kaiser, Łukasz and Polosukhin, Illia",
        "year": 2017,
        "content": """
        Abstract

        The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature.

        Introduction

        Recurrent neural networks, long short-term memory and gated recurrent neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation. Numerous efforts have since continued to push the boundaries of recurrent language models and encoder-decoder architectures.

        Method

        The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder. The encoder is composed of a stack of N = 6 identical layers. Each layer has two sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, position-wise fully connected feed-forward network.

        Results

        On the WMT 2014 English-to-German translation task, the big transformer model outperforms the best previously reported models (including ensembles) by more than 2.0 BLEU, establishing a new state-of-the-art BLEU score of 28.4.
        """
    },
    {
        "id": 2,
        "title": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "authors": "Devlin, Jacob and Chang, Ming-Wei and Lee, Kenton and Toutanova, Kristina",
        "year": 2018,
        "content": """
        Abstract

        We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications.

        Introduction

        Language model pre-training has been shown to be effective for improving many natural language processing tasks. These include sentence-level tasks such as natural language inference and paraphrasing, which aim to predict the relationships between sentences by analyzing them holistically, as well as token-level tasks such as named entity recognition and question answering, where models are required to produce fine-grained output at the token level.

        Method

        BERT uses a multi-layer bidirectional Transformer encoder. We denote the number of layers (i.e., Transformer blocks) as L, the hidden size as H, and the number of self-attention heads as A. We primarily report results on two model sizes: BERT_BASE (L=12, H=768, A=12, Total Parameters=110M) and BERT_LARGE (L=24, H=1024, A=16, Total Parameters=340M).

        Results

        BERT obtains new state-of-the-art results on eleven natural language processing tasks. The pre-training approach also works extremely well for fine-tuning on downstream tasks.
        """
    },
    {
        "id": 3,
        "title": "Deep Residual Learning for Image Recognition",
        "authors": "He, Kaiming and Zhang, Xiangyu and Ren, Shaoqing and Sun, Jian",
        "year": 2015,
        "content": """
        Abstract

        Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions. We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. On the ImageNet dataset we evaluate residual nets with a depth of up to 152 layers—8× deeper than VGG nets but still having lower complexity.

        Introduction

        Deep convolutional neural networks have led to a series of breakthroughs for image classification. Deep networks naturally integrate low/mid/high-level features and classifiers in an end-to-end multi-layer fashion, and the "levels" of features can be enriched by the number of stacked layers (depth).

        Method

        We adopt residual learning to every few stacked layers. A building block is defined as: y = F(x, {Wi}) + x. The function F(x, {Wi}) represents the residual mapping to be learned. The operation F + x is performed by a shortcut connection and element-wise addition.

        Results

        We won the 1st place on the ILSVRC 2015 classification task. The method also won the 1st places on ImageNet detection, ImageNet localization, COCO detection, and COCO segmentation.
        """
    }
]


class MockDatabase:
    """Mock 데이터베이스 클래스"""

    def __init__(self):
        self.papers = PAPERS

    def get_all_papers(self):
        """모든 논문 반환"""
        return self.papers

    def get_paper_by_id(self, paper_id: int):
        """ID로 논문 조회"""
        for paper in self.papers:
            if paper["id"] == paper_id:
                return paper
        return None

    def get_papers_by_year(self, year: int):
        """연도별 논문 조회"""
        return [p for p in self.papers if p["year"] == year]


# 싱글톤 인스턴스
db = MockDatabase()
