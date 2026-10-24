# Final fixes: holiday decks republish (2026-10-23)

| Finding | Action |
|---|---|
| Live decks were the old look / old slide set | All 60 private Claude Slides artifacts republished in place from split/<id>/project (deck.json plus slides). Stale slides (go, story, teachplan etc.) removed; new check and reflect slides added. |
| P5 L9 and L10 were empty shells | Populated for the first time at their existing URLs. |
| split/l1 deck.json cover pointed at removed slide "cover" | Changed to "l1-title". |
| Recording cues | Live in the tutor guides (levels/reccues.js), not in decks; decks carry time pill and timed speaker notes, spot-checked on published URLs. |
| outputs/deck_urls_all.json lacked P5 | P5 ids added. |
| outputs/deck_urls_p4_p6.md had stale "empty shell / not yet published" notes | Replaced with 2026-10-23 status. |
| split/l6s (60-minute trial deck) | Left unpublished at 7YVUJqZEsa3TKMPm5SXcBw; owner to decide. |

No rebuild needed: gen scripts reproduce split/ except timestamps. Nothing made public.
