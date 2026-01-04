import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_chunk(chunk: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert assistant that summarizes meeting transcripts "
                    "clearly and concisely into bullet points."
                )
            },
            {
                "role": "user",
                "content": (
                    "Summarize the following meeting transcript chunk "
                    "into concise bullet points (max 5–6 bullets):\n\n"
                    f"{chunk}"
                )
            }
        ],
        temperature=0.3,
        max_tokens=250
    )

    return response.choices[0].message.content.strip()

def finalize_summary(bullets: list[str]) -> str:
    joined = "\n".join(f"- {b}" for b in bullets)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional analyst who writes clean, "
                    "executive-ready summaries."
                )
            },
            {
                "role": "user",
                "content": (
                    "Create a FINAL executive summary from the points below.\n\n"
                    "STRICT RULES:\n"
                    "- Output EXACTLY 8–10 bullet points\n"
                    "- Use plain bullet points (•)\n"
                    "- Do NOT use numbering\n"
                    "- Do NOT add headings or introductions\n"
                    "- Do NOT repeat points\n"
                    "- Every bullet must be a complete sentence\n"
                    "- Do NOT cut off mid-sentence\n\n"
                    f"{joined}"
                )
            }
        ],
        temperature=0.15,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()
