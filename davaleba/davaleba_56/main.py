import os

from dotenv import load_dotenv

from readers import read_file
from chunking import create_chunks
from database import (
    create_table,
    insert_chunk,
    similarity_search
)


load_dotenv()



CHUNK_SIZE = 5

MAX_DISTANCE = 0.7




def ingest_file(file_path: str):

    print(f"\nReading: {file_path}")


    text = read_file(file_path)

    print(
        f"Extracted {len(text)} characters."
    )


    chunks = create_chunks(
        text,
        sentences_per_chunk=CHUNK_SIZE
    )

    print(
        f"Created {len(chunks)} chunks."
    )

    file_name = os.path.basename(file_path)


    for index, chunk in enumerate(chunks):

        insert_chunk(
            content=chunk,
            file_name=file_name,
            chunk_index=index
        )

        print(
            f"Saved chunk {index}: "
            f"{file_name}"
        )




if __name__ == "_main_":


    create_table()



    ingest_file("company_handbook.md")



    ingest_file("handbook.pdf")



    query = input(
        "\nEnter your search question: "
    )

    results = similarity_search(
        query=query,
        top_k=3,
        max_distance=MAX_DISTANCE
    )

    print("\nTop 3 similar documents:")

    if not results:
        print(
            "No relevant documents found "
            "within the distance threshold."
        )

    else:

        for i, (
            document_id,
            content,
            file_name,
            chunk_index,
            distance
        ) in enumerate(
            results,
            start=1
        ):

            print(
                f"{i}. [id={document_id}] "
                f"distance={distance:.4f} | "
                f"content: {content}"
            )

            print(
                f"   file: {file_name} | "
                f"chunk: {chunk_index}"
            )