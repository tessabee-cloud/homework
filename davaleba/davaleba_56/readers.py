import os

from pypdf import PdfReader


def read_markdown(file_path: str) -> str:
    """
    Reads a Markdown file and returns its text.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def read_pdf(file_path: str) -> str:
    """
    Reads a PDF file and returns all extracted text
    as one string.
    """

    reader = PdfReader(file_path)

    pages = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n".join(pages)


def read_file(file_path: str) -> str:
    """
    Automatically chooses the correct reader based
    on the file extension.
    """

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".md":
        return read_markdown(file_path)

    elif extension == ".pdf":
        return read_pdf(file_path)

    else:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )