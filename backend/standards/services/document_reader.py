"""
Best-effort text extraction from an uploaded tender document.
Supports .txt, .docx and .pdf. Falls back to a clear error message rather
than silently returning empty text.
"""
from __future__ import annotations


class DocumentReadError(Exception):
    pass


def extract_text(django_file) -> str:
    name = (django_file.name or "").lower()
    data = django_file.read()

    if name.endswith(".txt") or name.endswith(".md"):
        try:
            return data.decode("utf-8", errors="ignore")
        except Exception as exc:  # pragma: no cover - defensive
            raise DocumentReadError(f"Could not read text file: {exc}") from exc

    if name.endswith(".docx"):
        try:
            import io
            from docx import Document
        except ImportError as exc:
            raise DocumentReadError(
                "python-docx is not installed on the server. Add it to requirements.txt."
            ) from exc
        try:
            doc = Document(io.BytesIO(data))
            return "\n".join(p.text for p in doc.paragraphs)
        except Exception as exc:
            raise DocumentReadError(f"Could not read .docx file: {exc}") from exc

    if name.endswith(".pdf"):
        try:
            import io
            import pdfplumber
        except ImportError as exc:
            raise DocumentReadError(
                "pdfplumber is not installed on the server. Add it to requirements.txt."
            ) from exc
        try:
            text_parts = []
            with pdfplumber.open(io.BytesIO(data)) as pdf:
                for page in pdf.pages:
                    text_parts.append(page.extract_text() or "")
            text = "\n".join(text_parts)
            if not text.strip():
                raise DocumentReadError(
                    "No selectable text found in this PDF. It may be a scanned image; "
                    "OCR is not included in this MVP."
                )
            return text
        except DocumentReadError:
            raise
        except Exception as exc:
            raise DocumentReadError(f"Could not read PDF file: {exc}") from exc

    raise DocumentReadError(f"Unsupported file type: {django_file.name}. Use .txt, .docx or .pdf.")
