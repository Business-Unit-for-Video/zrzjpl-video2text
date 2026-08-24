from pathlib import Path


def test_transcription_pipeline_layout() -> None:
    assert Path("scripts/transcribe_youtube_channel.py").is_file()
    assert Path("scripts/transcription_integrity.py").is_file()
    assert Path(".github/workflows/transcribe_youtube_channel.yml").is_file()


def test_default_channel_is_zrzjpl() -> None:
    workflow = Path(".github/workflows/transcribe_youtube_channel.yml").read_text(encoding="utf-8")
    assert "https://www.youtube.com/@zrzjpl" in workflow
    assert "政经鲁社长" in workflow
    assert "YOUTUBE_SOURCE_COOKIE_FILE_VIDEO2TEXT" in workflow
