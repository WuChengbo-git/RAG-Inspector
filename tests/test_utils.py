import textwrap
from pathlib import Path
from backend.app.utils import extract_text, chunk_text


def test_extract_text_txt(tmp_path: Path) -> None:
    p = tmp_path / "sample.txt"
    p.write_text("Hello world", encoding="utf-8")
    assert extract_text(p) == "Hello world"


def test_extract_text_html(tmp_path: Path) -> None:
    p = tmp_path / "sample.html"
    p.write_text("<html><body><p>Hello <b>world</b></p></body></html>")
    assert extract_text(p) == "Hello world"


def test_chunk_text() -> None:
    text = "abcdefghijklmno"
    chunks = chunk_text(text, window_size=10, stride=5)
    assert chunks == [
        (0, "abcdefghij"),
        (1, "fghijklmno"),
        (2, "klmno"),
    ]
