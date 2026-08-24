# 政经鲁社长 Video2Text

This repository transcribes the public videos from [政经鲁社长](https://www.youtube.com/@zrzjpl) into Simplified Chinese text with timestamps.

The implementation is based on the shared `Video2Text` pipeline and the standalone `laowang-lai-le` channel workflow. Each GitHub Actions run handles one pending video, commits the transcript and durable state, and triggers the next run only when more work remains. This keeps the runner bounded and makes interrupted work resumable without re-transcribing completed videos.

## Outputs

- `youtube_channels/政经鲁社长/with_timestamps/`: timestamped transcripts.
- `youtube_channels/政经鲁社长/plain/`: plain text transcripts.
- `youtube_channels/政经鲁社长/_manifest.json`: discovered public-video metadata.
- `state_youtube/政经鲁社长/`: queue, progress, completed/failed IDs, and per-video errors.

Membership-only videos are excluded by default using YouTube availability metadata and conservative title matching. Set `include_members=true` only when the organization cookie is a valid Netscape cookie export and you are authorized to access that content. The workflow uses the organization Actions secret `YOUTUBE_SOURCE_COOKIE_FILE_VIDEO2TEXT`; cookies are written only to the ephemeral runner and are never committed. If the secret is a browser JSON export rather than a Netscape file, it is ignored for public-video runs instead of causing every download to fail.

## Run

Run **转写 YouTube 频道** manually from Actions to override the channel, output destination, Whisper model, or retry previously failed items. The scheduled workflow scans the channel every six hours. Each successful run processes one video and triggers the next one while pending items exist. A failed run stops the chain and records the error for manual inspection, so a platform authentication problem cannot create an unbounded Actions loop.

The current organization secret must contain a readable YouTube cookie export: a Netscape `cookies.txt`, a browser JSON export, JSON Lines, or a standard `Cookie:` request header containing YouTube cookies. An arbitrary token/string cannot authenticate yt-dlp; replace the secret with an export from the same signed-in YouTube account before retrying.

The source channel and any downloaded media must be used only where you have the necessary authorization or other lawful basis.
