def chunk_text(text: str, max_chars: int = 3000) -> list[str]:
    chunks = []
    current_chunk = ""

    for paragraph in text.split("\n"):
        paragraph = paragraph.strip()

        if not paragraph:
            continue

        paragraph += "\n"

        while len(paragraph) > max_chars:
            chunks.append(paragraph[:max_chars].strip())
            paragraph = paragraph[max_chars:]

        if len(current_chunk) + len(paragraph) > max_chars:
            chunks.append(current_chunk.strip())
            current_chunk = paragraph
        else:
            current_chunk += paragraph

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks
