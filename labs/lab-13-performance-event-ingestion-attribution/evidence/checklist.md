# Evidence checklist — Lab 13

- [ ] Workflow imported inactive and the manual execution ID is recorded
- [ ] Mock Excel data reviewed and metric `data_quality = valid_unique_events / received_events` reproduced
- [ ] Expected terminal node `Performance Facts` reached for the valid fixture
- [ ] Invalid/duplicate fixture reached the documented failure terminal where applicable
- [ ] Output keys and values match `solution/expected-output.json`
- [ ] Evidence saved as `performance-facts.csv` with an execution screenshot
- [ ] Acceptance check passed: All facts have unique event_id, valid campaign_id, normalised time and an explicit attribution rule or quarantine reason.
- [ ] Risk and control explained: Inconsistent IDs and time zones can misattribute outcomes
