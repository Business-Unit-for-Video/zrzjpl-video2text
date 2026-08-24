# 政经鲁社长 Video2Text

This repository transcribes the public videos from [政经鲁社长](https://www.youtube.com/@zrzjpl) into Simplified Chinese text with timestamps.

The implementation is based on the shared `Video2Text` pipeline and the standalone `laowang-lai-le` channel workflow. Each GitHub Actions run handles one pending video, commits the transcript and durable state, and triggers the next run only when more work remains. This keeps the runner bounded and makes interrupted work resumable without re-transcribing completed videos.

## Outputs

- `youtube_channels/政经鲁社长/with_timestamps/`: timestamped transcripts.
- `youtube_channels/政经鲁社长/plain/`: plain text transcripts.
- `youtube_channels/政经鲁社长/_manifest.json`: discovered public-video metadata.
- `state_youtube/政经鲁社长/`: queue, progress, completed/failed IDs, and per-video errors.

Membership-only videos are excluded by default. The workflow uses the organization Actions secret `YOUTUBE_SOURCE_COOKIE_FILE_VIDEO2TEXT`; cookies are written only to the ephemeral runner and are never committed.

## Run

Run **转写 YouTube 频道** manually from Actions to override the channel, output destination, Whisper model, or force-retranscribe setting. The scheduled workflow scans the channel every six hours. The first run processes one video and then continues serially while pending items exist.

The source channel and any downloaded media must be used only where you have the necessary authorization or other lawful basis.
