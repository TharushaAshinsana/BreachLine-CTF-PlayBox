# How to Apply Content in CTFd (S1–S3)

This folder contains player-facing text/hints/pages that must be pasted into CTFd Admin UI.

## 1) Pages (Admin Panel → Pages → New Page)
Create these pages (Route values are WITHOUT a leading slash):

1. Route: start
   - Paste: pages/start.md
   - Format: Markdown

2. Route: forum
   - Paste: pages/forum.md
   - Format: Markdown

3. Route: forum/thread-17
   - Paste: pages/forum-thread-17.md
   - Format: Markdown

4. Route: internal-landing
   - Paste: pages/internal-landing.html
   - Format: Markdown (HTML content is acceptable)

## 2) Challenges (Admin Panel → Challenges)
### S1 - First Footprint
- Description: challenges/s1.md
- Flag: NOVATECH{S1_FIRST_FOOTPRINT_FLAG}
- Hints: hints/s1.md
- Requirements: none

### S2 - Planning Notes
- Description: challenges/s2.md
- Flag: NOVATECH{S2_PLANNING_NOTES_FLAG}
- Requirements: S1
- Attachment: planning_notes.jpg (upload via Files tab)
- Hints: hints/s2.md

### S3 - Point of Entry
- Description: challenges/s3.md
- Flag: NOVATECH{S3_ADMIN_DB_FLAG}
- Requirements: S2
- Hints: hints/s3.md

## 3) Sequential gating
Set Requirements so the player sees:
S1 → S2 → S3

(Use 'Behavior if not unlocked = Hidden' for a strict linear pathway.)
