from conversational_sentence_encoder.vectorizers import SentenceEncoder
from jina import Executor, requests
from docarray import DocumentArray

class ConveRTFeaturizer(Executor):
    def __init__(self, **kwargs):
        super(ConveRTFeaturizer, self).__init__(**kwargs)
        self.sentence_encoder = SentenceEncoder(multiple_contexts=False)

    @requests
    def featurize(self, docs: DocumentArray, **kwargs) -> DocumentArray:
        docs.embeddings = self.sentence_encoder.encode_sentences(docs.texts)
        return docs
