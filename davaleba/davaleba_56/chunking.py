import re


def split_into_sentences(text: str) -> list[str]:
    """
    Splits text into sentences using . ! and ?
    """

    text = re.sub(r"\s+", " ", text).strip()


    sentences = re.split(r"(?<=[.!?])\s+", text)

    sentences = [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]

    return sentences


def create_chunks(
    text: str,
    sentences_per_chunk: int = 5
) -> list[str]:
    """
    Groups consecutive sentences into chunks.

    Example:
    5 sentences -> 1 chunk
    next 5 sentences -> another chunk
    """

    sentences = split_into_sentences(text)

    chunks = []

    for i in range(
        0,
        len(sentences),
        sentences_per_chunk
    ):

        chunk_sentences = sentences[
            i:i + sentences_per_chunk
        ]

        chunk = " ".join(chunk_sentences)

        if chunk:
            chunks.append(chunk)

    return chunks