# Finding and vetting free resources

Goal: for every daily target, point the learner to the best free material, with working links where possible. Many search results are paid courses and test series, so the work is filtering and verifying, not just collecting.

## Where to look (by usefulness)
1. **Official sources**: the exam body's syllabus, notices, sample and previous papers, answer keys.
2. **Public and government textbooks**: national and state textbook boards publish PDFs free (for example NCERT; state boards and their research councils). Prefer the medium (language) of the exam.
3. **Open courseware and free platforms**: MIT OpenCourseWare, NPTEL and SWAYAM, Khan Academy, OpenStax, university lecture notes, free MOOC audit tracks.
4. **Free video**: YouTube channels and playlists. Look for complete playlists matched to the syllabus, in the exam's language, from consistent, recognised teachers. Check recency for exams that change.
5. **Past-paper archives and free mock tests**: aggregator sites and public quiz sites; check that questions match the current pattern.
6. **Daily practice material**: newspaper e-papers, government bulletins, official magazines (current affairs, writing practice).
7. **Community**: forums, subreddits and Telegram groups can lead to material but are never the final source.

## How to search
Search the topic and the exam name with words like "free", "PDF", "playlist", "previous year paper", "syllabus", plus the language. Run separate searches per paper or subject. Prefer fetching the actual page to confirm it contains what the snippet claims.

## Vetting rules (every resource)
- **Free**: opens without payment or a login wall; if it is a paid product with a free sample, say so or skip it.
- **Relevant**: matches the syllabus section, level and language.
- **Current**: for exams, check the year; for science, check the edition.
- **Legitimate**: never link to pirated copies of paid books or leaked papers; use official or openly licensed copies.
- **Verified**: only produce a clickable link for a URL you saw in a search result or fetched this session. If you know a resource exists but have not seen its URL, name it in plain text and mark it "find and verify" rather than inventing a link. Never guess chapter numbers, unit names or playlist titles.
- **Dated**: record the check date in `verifiedOn`.

## Mapping resources to the daily target
Each lesson gets one primary resource (study it) and one practice resource (do problems, a past paper or a mock). Put the primary in order of how a learner should use it. Use the task `hint` for the module-level list and the lesson resources for the specific chapter, video or paper. Write links as `[Label](https://...)`.

## Report honestly
Tell the user which resources are verified links and which are named but unverified, which tasks still lack lessons, and where free material is thin (for example, descriptive-writing evaluation has few free options; suggest self-evaluation against past-paper answer keys or a peer).
