## Siri-ously Leaky: Exploring Overlooked Attack Surfaces Across Apple's Ecosystem (DEF CON 33 / HOU.SEC.CON 2025)
**Author**: Richard Hyunho Im (@richeeta)

This repo contains my slide deck and demo videos for my [DEF CON 33 main stage presentation](https://infocondb.org/con/def-con/def-con-33/siri-ously-leaky-exploring-overlooked-attack-surfaces-across-apples-ecosystem) on overlooked attack surfaces across Apple's ecosystem. I will deliver an updated version of this talk at [HOU.SEC.CON 2025](https://web.cvent.com/event/9ba9c5ea-9502-44a2-922e-d026c047c9f3/websitePage:c95771fe-7a36-4da8-9150-389979ec788f?rp=7fc495f3-0ae2-4b86-a115-0ce784642a9f) on October 1, 2025 at 3 PM CT.

## TL;DR

- **Slides & all demos are attached to the [v2.02 release](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/tag/v2.02)**.
- **Talk recording (DEF CON 33 Main Stage, Track 4):**  
  - [Direct download (MP4)](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/SiriouslyLeakyTalk.mp4)
  - [Also viewable on YouTube](https://youtu.be/1d381JJPj7k?si=ksd-jiIltzU6SY8d)  

## Assets (v2.02)

_Direct download links below come from the [GitHub Release](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/tag/v2.02); checksums are shown on the release page._



| File                                                                                                                                            | What it shows                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **[SiriouslyLeakyTalk.mp4](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/SiriouslyLeakyTalk.mp4)** (Also on [YouTube](https://youtu.be/1d381JJPj7k?si=ksd-jiIltzU6SY8d)) | Full talk recording (DEF CON 33 main stage, Track 4) |
| [AppleSEEDBAC.MP4](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/AppleSEEDBAC.MP4)                               | Apple SEED BAC                                                             |
| [AudiobookLeak.mov](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/AudiobookLeak.mov)                             | Books Action Shortcut leaking last read audiobook title                    |
| [ChatGPTLeak.mp4](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/ChatGPTLeak.mp4)                                 | Siri→ChatGPT data exfil PoC (CVE-2024-44235 family)                        |
| [CVE-2025-24198-ChatGPT-Leak.mov](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/CVE-2025-24198-ChatGPT-Leak.mov) | ChatGPT conversation leak for CVE‑2025‑24198                               |
| [CVE-2025-24198-Safari-Leak.mov](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/CVE-2025-24198-Safari-Leak.mov)   | Safari browsing leak for CVE‑2025‑24198                                    |
| [CVE-2025-24225.mov](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/CVE-2025-24225.mov)                           | CVE‑2025‑24225 PoC                                                         |
| [FilesSpoofing.mov](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/FilesSpoofing.mov)                             | File spoofing in Files app                                                 |
| [getsupportIDOR.mp4](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/getsupportIDOR.mp4)                           | IDOR on getsupport.apple.com                                               |
| [HiddenPhotosLeakviaSiri.mp4](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/HiddenPhotosLeakviaSiri.mp4)         | Hidden Photos leakage via Siri                                             |
| [Im.Siriously.Leaky.v2.02.pptx](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/Im.Siriously.Leaky.v2.02.pptx)     | Slide deck (v2.02)                                                         |
| [PCCDataLeak.mp4](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/PCCDataLeak.mp4)                                 | Siri context confusion → Private Cloud Compute (PCC) data leak to ChatGPT  |
| [PhoneNumberSpoofing.mp4](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/PhoneNumberSpoofing.mp4)                 | Phone number spoofing in Notes                                             |
| [SafariPunycodeConfusion.mp4](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/SafariPunycodeConfusion.mp4)         | URL Punycode confusion in Safari                                           |
| [ShortcutsRaceCondition.mp4](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/ShortcutsRaceCondition.mp4)           | Shortcuts race condition (Face ID bypass path)                             |
| [SpeakScreenNotes.mov](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/SpeakScreenNotes.mov)                       | Speak Screen reading beyond visible content in Notes widget on Lock Screen |
| [StoreFrontBAC.mov](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/StoreFrontBAC.mov)                             | App Store storefront BAC #1 (initial access)                               |
| [StoreFrontBAC2.mov](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/download/v2.02/StoreFrontBAC2.mov)                           | App Store storefront BAC #2 (inside the app)                               |
| [StoreFrontBAC2.mov](https://github.com/richeeta/DEFCON33-Siriously-Leaky/idor.py)                           | PoC for IDOR in Apple's support portal                               |

## Repo structure

- `Im Siriously Leaky v2.02.pdf` – lightweight PDF copy of slides (kept in repo).
- Please see the [Releases](https://github.com/richeeta/DEFCON33-Siriously-Leaky/releases/tag/v2.02) page for all PoCs and the final `.pptx`. (Note: The PoC videos have been added individually, but the `.pptx` file also includes all PoC videos, screenshots, and diagrams.)
 
## Notes

- Most PoCs can only be reproduced on specific iOS/iPadOS versions (and certain app versions); please see slide notes for context.
- Please report issues via GitHub issues.


## License & Reuse

You're welcome to use, repurpose, and redistribute anything here for **personal use, research, and any non-commercial purposes**, but please cite/link back to this repo or the [v2.02 release](/richeeta/DEFCON33-Siriously-Leaky/releases/tag/v2.02).

If you want to use any of this for something commercial, please reach out to me at richeeta AT proton DOT me first to discuss.

This project is shared under the [Creative Commons Attribution–NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).


