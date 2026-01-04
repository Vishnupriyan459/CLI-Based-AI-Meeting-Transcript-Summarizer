import sys
from groq_client import summarize_chunk,finalize_summary
from chunker import chunk_text
from file_loader import load_text


def summarize_transcript(file_path: str) -> str:
    # Load text from TXT or PDF
    text = load_text(file_path)

    chunks = chunk_text(text, max_chars=3000)
    print(f"🔹 Total chunks: {len(chunks)}")

    all_bullets = []

    for i, chunk in enumerate(chunks, start=1):
        print(f"Summarizing chunk {i}/{len(chunks)}...")
        summary = summarize_chunk(chunk)

        for line in summary.split("\n"):
            line = line.strip()
            if line.startswith(("-", "•")):
                all_bullets.append(line.lstrip("-• ").strip())
            elif line and len(line.split()) > 5:
                all_bullets.append(line)


    # Deduplicate bullets
    seen = set()
    final_bullets = []
    for b in all_bullets:
        if b not in seen:
            seen.add(b)
            final_bullets.append(b)

    print("\n🔄 Creating final consolidated summary...\n")
    return finalize_summary(final_bullets)


def main():
    if len(sys.argv) != 2:
        print("Usage: python summarize.py <file.txt | file.pdf>")
        sys.exit(1)

    file_path = sys.argv[1]
    summary = summarize_transcript(file_path)

    print("\n📝 FINAL SUMMARY\n")
    print(summary)


if __name__ == "__main__":
    main()
