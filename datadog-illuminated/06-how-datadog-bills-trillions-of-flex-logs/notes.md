# Standard Indexing vs Flex Logs

**Standard Indexing**
- Pay Up Front
- Unlimited query
- Count at ingest

**Flex Logs**
- cheaper storage
- infrequent query
- longer retention
- Count "now"

---

# PROBLEM — Billing for Flex Logs was generally bad

- Querying ALL logs at once is hard & slow
- Number of Logs Changes → no usage + attribution
- Lose money on outages — we can't bill what we can't count

**SLIDING WINDOW**
- smaller queries
- Can recover from outages
- fast & reliable

---

# The Solution: THE CACHE LAYER

Hourly Count → logs (1h) → [H][H][H][H][H][H][H][H][H] → logs expire

DAY aggregations feed into TOTAL

**Counting Job** (Finds Holes)
- reads cache
- queries new logs
- writes to cache
- counts by groups for attribution tags
- computes totals

**BILLING JOB**
- reads total from cache
- Sends to billing
- just grabs pre-computed numbers

**BACKFILLING**
- Reason: Querying or BILLING can go down, etc
- part of counting job
- Notices "holes" & fills them in w counts & attribution
- Suspends computation of totals until there's no holes

**AGGREGATION LAYER**
- Bounded cardinality
- Logs Roll up
- usage attribution
