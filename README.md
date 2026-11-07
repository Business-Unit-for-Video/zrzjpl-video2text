# 政经鲁社长 Video2Text

This repository transcribes the public videos from [政经鲁社长](https://www.youtube.com/@zrzjpl) into Simplified Chinese text with timestamps.

The implementation is based on the shared `Video2Text` pipeline and the standalone `laowang-lai-le` channel workflow. Each GitHub Actions run handles one pending video, commits the transcript and durable state, and triggers the next run only when more work remains. This keeps the runner bounded and makes interrupted work resumable without re-transcribing completed videos.

## Outputs

- `youtube_channels/政经鲁社长/with_timestamps/`: timestamped transcripts.
- `youtube_channels/政经鲁社长/plain/`: plain text transcripts.
- `youtube_channels/政经鲁社长/_manifest.json`: discovered public-video metadata.
- `youtube_channels/政经鲁社长/_playlists.json`: snapshot of the channel's public playlists and their intersections with archived video IDs.
- `state_youtube/政经鲁社长/`: queue, progress, completed/failed IDs, and per-video errors.

Membership-only videos are excluded by default using YouTube availability metadata and conservative title matching. Set `include_members=true` only when the repository cookie is a valid Netscape cookie export and you are authorized to access that content. The workflow uses the repository Actions secret `YOUTUBE_SOURCE_COOKIE_FILE_VIDEO2TEXT`; cookies are written only to the ephemeral runner and are never committed. If the secret is a browser JSON export rather than a Netscape file, it is ignored for public-video runs instead of causing every download to fail.

## Channel playlists

The channel's public playlist page was captured on 2026-11-07. The snapshot in [`_playlists.json`](youtube_channels/政经鲁社长/_playlists.json) records the playlist titles, source URLs, and IDs of archived videos found in each playlist.

| Playlist | Archived videos matched |
|---|---:|
| 鲁-陶相对论 | 2 |
| 公开直播 | 60 |
| 核心会员线上会议 | 0 |
| 时事点评 | 6 |
| 习近平的家族故事 | 5 |
| 军队大乱斗丨政变谣言粉碎史：从苗华何卫东到张又侠 | 12 |
| 公开视频 | 81 |
| 会员直播 | 2 |
| 会员专享视频 | 0 |
| 每周高层人事动态点评 | 5 |
| 中纪委书记 | 4 |
| 中共白手套传奇 | 1 |

The playlist memberships overlap: 135 of the 152 videos in the archived manifest appear in at least one listed playlist, with 178 playlist-to-video matches in total. The remaining 17 archived IDs did not appear in the currently listed public playlists. “公开视频” and “公开直播” describe broad video formats rather than subject topics; playlist names are preserved as the channel presents them, not treated as an exhaustive or mutually exclusive taxonomy. Membership-only playlists are listed, but only IDs already present in the public archive are mapped.

## Run

Run **转写 YouTube 频道** manually from Actions to override the channel, output destination, Whisper model, or retry previously failed items. The scheduled workflow scans the channel every six hours. Each successful run processes one video and triggers the next one while pending items exist. A failed run stops the chain and records the error for manual inspection, so a platform authentication problem cannot create an unbounded Actions loop.

The current repository secret must contain a readable YouTube cookie export: a Netscape `cookies.txt`, a browser JSON export, JSON Lines, or a standard `Cookie:` request header containing YouTube cookies. An arbitrary token/string cannot authenticate yt-dlp; replace the secret with an export from the same signed-in YouTube account before retrying.

The source channel and any downloaded media must be used only where you have the necessary authorization or other lawful basis.
