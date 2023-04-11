from zemberek import (
    TurkishTokenizer,
    TurkishMorphology,
    TurkishSentenceNormalizer,
    TurkishSentenceExtractor,
)


class TurkishNLP:
    def __init__(self):
        self

    def __repr__(self):
        pass

    def tokenizer(self, word: str):
        tokenizer = TurkishTokenizer.DEFAULT
        tokens = tokenizer.tokenize(word)
        for token in tokens:
            print("Content = ", token.content)
            print("Type = ", token.type_.name)
            print("Start = ", token.start)
            print("Stop = ", token.end, "\n")

    def morphology_correction(self, sentences: str) -> str:
        morphology = TurkishMorphology.create_with_defaults()
        normalizer = TurkishSentenceNormalizer(morphology)
        return normalizer.normalize(sentences)

    def sentences_extractor(self, sentence: tuple) -> tuple:
        extractor = TurkishSentenceExtractor()
        sentences = extractor.from_paragraph(sentence)
        return sentences
