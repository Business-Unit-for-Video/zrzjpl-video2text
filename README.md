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

## Political topic cross-reference

The following table links selected archived videos to their original channel playlists and related write-ups in the [Fudan alumni network repository](https://github.com/PeterKZhao/fudan-alumni-network/tree/main/topics/%E6%94%BF%E6%B2%BB%E4%B8%8E%E5%85%AC%E5%85%B1%E8%AE%AE%E9%A2%98). Playlist memberships are taken from the snapshot above and may overlap. This cross-reference is an index, not an endorsement of claims in the videos or write-ups.

| Video | Duration | Channel playlists in the 2026-11-07 snapshot | Related Fudan write-up(s) |
|---|---:|---|---|
| [許其亮：習近平的刀斧手](https://www.youtube.com/watch?v=dPtmJdDMlZY) (`dPtmJdDMlZY`) | 10:57 | 公开视频; 每周高层人事动态点评 | [许其亮视频内容与公开履历梳理](https://github.com/PeterKZhao/fudan-alumni-network/blob/main/topics/%E6%94%BF%E6%B2%BB%E4%B8%8E%E5%85%AC%E5%85%B1%E8%AE%AE%E9%A2%98/%E8%AE%B8%E5%85%B6%E4%BA%AE%E8%A7%86%E9%A2%91%E5%86%85%E5%AE%B9%E4%B8%8E%E5%85%AC%E5%BC%80%E5%B1%A5%E5%8E%86%E6%A2%B3%E7%90%86.md) |
| [栗戰書如何清洗中辦的令計劃勢力](https://www.youtube.com/watch?v=V6arqLM-9UQ) (`V6arqLM-9UQ`) | 14:43 | No match in listed public playlists | [令计划履历与关联人员核查](https://github.com/PeterKZhao/fudan-alumni-network/blob/main/topics/%E6%94%BF%E6%B2%BB%E4%B8%8E%E5%85%AC%E5%85%B1%E8%AE%AE%E9%A2%98/%E4%BB%A4%E8%AE%A1%E5%88%92%E5%B1%A5%E5%8E%86%E4%B8%8E%E5%85%B3%E8%81%94%E4%BA%BA%E5%91%98%E6%A0%B8%E6%9F%A5.md); [栗战书履历与关联关系核查](https://github.com/PeterKZhao/fudan-alumni-network/blob/main/topics/%E6%94%BF%E6%B2%BB%E4%B8%8E%E5%85%AC%E5%85%B1%E8%AE%AE%E9%A2%98/%E6%A0%97%E6%88%98%E4%B9%A6%E5%B1%A5%E5%8E%86%E4%B8%8E%E5%85%B3%E8%81%94%E5%85%B3%E7%B3%BB%E6%A0%B8%E6%9F%A5.md); [两人交集与比较](https://github.com/PeterKZhao/fudan-alumni-network/blob/main/topics/%E6%94%BF%E6%B2%BB%E4%B8%8E%E5%85%AC%E5%85%B1%E8%AE%AE%E9%A2%98/%E4%BB%A4%E8%AE%A1%E5%88%92%E4%B8%8E%E6%A0%97%E6%88%98%E4%B9%A6%E7%9A%84%E4%BA%A4%E9%9B%86%E5%92%8C%E5%AF%B9%E6%AF%94.md) |
| [6月30日的政治局会议：习近平被限权了吗](https://www.youtube.com/watch?v=GtzsCmJmIcc) (`GtzsCmJmIcc`) | 14:55 | 公开视频; 军队大乱斗丨政变谣言粉碎史：从苗华何卫东到张又侠 | [党中央决策议事协调机构与小组政治：权力协调、制度边界及治理影响](https://github.com/PeterKZhao/fudan-alumni-network/blob/main/topics/%E6%94%BF%E6%B2%BB%E4%B8%8E%E5%85%AC%E5%85%B1%E8%AE%AE%E9%A2%98/%E5%85%9A%E4%B8%AD%E5%A4%AE%E5%86%B3%E7%AD%96%E8%AE%AE%E4%BA%8B%E5%8D%8F%E8%B0%83%E6%9C%BA%E6%9E%84%E4%B8%8E%E5%B0%8F%E7%BB%84%E6%94%BF%E6%B2%BB%EF%BC%9A%E6%9D%83%E5%8A%9B%E5%8D%8F%E8%B0%83%E3%80%81%E5%88%B6%E5%BA%A6%E8%BE%B9%E7%95%8C%E5%8F%8A%E6%B2%BB%E7%90%86%E5%BD%B1%E5%93%8D.md) |
| [何卫东和秦刚：两个跳级生的悲惨命运](https://www.youtube.com/watch?v=YKXvrIxWrn0) (`YKXvrIxWrn0`) | 24:31 | 公开视频; 军队大乱斗丨政变谣言粉碎史：从苗华何卫东到张又侠 | [何卫东与秦刚：军队与外交系统中的两条独立人物线](https://github.com/PeterKZhao/fudan-alumni-network/blob/main/topics/%E6%94%BF%E6%B2%BB%E4%B8%8E%E5%85%AC%E5%85%B1%E8%AE%AE%E9%A2%98/%E4%BD%95%E5%8D%AB%E4%B8%9C%E4%B8%8E%E7%A7%A6%E5%88%9A%EF%BC%9A%E5%86%9B%E9%98%9F%E4%B8%8E%E5%A4%96%E4%BA%A4%E7%B3%BB%E7%BB%9F%E4%B8%AD%E7%9A%84%E4%B8%A4%E6%9D%A1%E7%8B%AC%E7%AB%8B%E4%BA%BA%E7%89%A9%E7%BA%BF.md) |
| [张又侠发动政变的四个条件；习近平是怎么夺权的](https://www.youtube.com/watch?v=QIgqP0mvzzg) (`QIgqP0mvzzg`) | 29:56 | 公开视频; 军队大乱斗丨政变谣言粉碎史：从苗华何卫东到张又侠 | [1949年以来中共高层权力斗争与权力更迭：事件性质、过程及制度影响](https://github.com/PeterKZhao/fudan-alumni-network/blob/main/topics/%E6%94%BF%E6%B2%BB%E4%B8%8E%E5%85%AC%E5%85%B1%E8%AE%AE%E9%A2%98/1949%E4%BB%A5%E6%9D%A5%E4%B8%AD%E5%85%B1%E9%AB%98%E5%B1%82%E6%9D%83%E5%8A%9B%E6%96%97%E4%BA%89%E4%B8%8E%E6%9D%83%E5%8A%9B%E6%9B%B4%E8%BF%AD%EF%BC%9A%E4%BA%8B%E4%BB%B6%E6%80%A7%E8%B4%A8%E3%80%81%E8%BF%87%E7%A8%8B%E5%8F%8A%E5%88%B6%E5%BA%A6%E5%BD%B1%E5%93%8D.md) |
| [决战四中全会：四中全会的召开时间？讨论哪些事项？](https://www.youtube.com/watch?v=usRDsxDAy54) (`usRDsxDAy54`) | 20:16 | 公开视频; 军队大乱斗丨政变谣言粉碎史：从苗华何卫东到张又侠 | [中国共产党会议制度与中央全会运行机制解读](https://github.com/PeterKZhao/fudan-alumni-network/blob/main/topics/%E6%94%BF%E6%B2%BB%E4%B8%8E%E5%85%AC%E5%85%B1%E8%AE%AE%E9%A2%98/%E4%B8%AD%E5%9B%BD%E5%85%B1%E4%BA%A7%E5%85%9A%E4%BC%9A%E8%AE%AE%E5%88%B6%E5%BA%A6%E4%B8%8E%E4%B8%AD%E5%A4%AE%E5%85%A8%E4%BC%9A%E8%BF%90%E8%A1%8C%E6%9C%BA%E5%88%B6%E8%A7%A3%E8%AF%BB.md) |
| [谁杀死了李克强和许其亮？保健医为什么没有用？](https://www.youtube.com/watch?v=Id7BpWuO3EU) (`Id7BpWuO3EU`) | 24:55 | 公开视频; 军队大乱斗丨政变谣言粉碎史：从苗华何卫东到张又侠 | [中共高层医疗保健制度：组织架构、保障层级与运行机制](https://github.com/PeterKZhao/fudan-alumni-network/blob/main/topics/%E6%94%BF%E6%B2%BB%E4%B8%8E%E5%85%AC%E5%85%B1%E8%AE%AE%E9%A2%98/%E4%B8%AD%E5%85%B1%E9%AB%98%E5%B1%82%E5%8C%BB%E7%96%97%E4%BF%9D%E5%81%A5%E5%88%B6%E5%BA%A6%EF%BC%9A%E7%BB%84%E7%BB%87%E6%9E%B6%E6%9E%84%E3%80%81%E4%BF%9D%E9%9A%9C%E5%B1%82%E7%BA%A7%E4%B8%8E%E8%BF%90%E8%A1%8C%E6%9C%BA%E5%88%B6.md) |

“No match” means the video ID is absent from the archived matches in the captured public-playlist snapshot; it does not rule out other channel classifications.

## Run

Run **转写 YouTube 频道** manually from Actions to override the channel, output destination, Whisper model, or retry previously failed items. The scheduled workflow scans the channel every six hours. Each successful run processes one video and triggers the next one while pending items exist. A failed run stops the chain and records the error for manual inspection, so a platform authentication problem cannot create an unbounded Actions loop.

The current repository secret must contain a readable YouTube cookie export: a Netscape `cookies.txt`, a browser JSON export, JSON Lines, or a standard `Cookie:` request header containing YouTube cookies. An arbitrary token/string cannot authenticate yt-dlp; replace the secret with an export from the same signed-in YouTube account before retrying.

The source channel and any downloaded media must be used only where you have the necessary authorization or other lawful basis.
