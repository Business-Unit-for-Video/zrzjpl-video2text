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


def test_cookie_normalizer_converts_browser_json(tmp_path) -> None:
    from scripts.normalize_youtube_cookies import normalize

    cookie_file = tmp_path / "cookies.txt"
    cookie_file.write_text(
        '[{"domain":"youtube.com","name":"SID","value":"redacted",'
        '"path":"/","secure":true,"expirationDate":1700000000}]',
        encoding="utf-8",
    )

    assert normalize(cookie_file) == "converted-json:1"
    lines = cookie_file.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "# Netscape HTTP Cookie File"
    assert lines[2].startswith(".youtube.com\tTRUE\t/\tTRUE\t1700000000\tSID\t")


def test_cookie_normalizer_converts_request_header(tmp_path) -> None:
    from scripts.normalize_youtube_cookies import normalize

    cookie_file = tmp_path / "cookies.txt"
    cookie_file.write_text("Cookie: SID=redacted; SAPISID=also-redacted", encoding="utf-8")

    assert normalize(cookie_file) == "converted-header:2"
    assert "\tSID\tredacted" in cookie_file.read_text(encoding="utf-8")
