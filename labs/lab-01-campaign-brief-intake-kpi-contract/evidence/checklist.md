# Evidence checklist — Lab 01

- [ ] Workflow imported inactive and the manual execution ID is recorded
- [ ] Mock Excel data reviewed and metric `brief_completeness = populated_required_fields / 8` reproduced
- [ ] Expected terminal node `Output Contract` reached for the valid fixture
- [ ] Invalid/duplicate fixture reached the documented failure terminal where applicable
- [ ] Output keys and values match `solution/expected-output.json`
- [ ] Evidence saved as `lab-01-evidence.json` with an execution screenshot
- [ ] Acceptance check passed: Output contains campaign_id CMP-NS-001, at least three KPI contracts, one owner per KPI and a human-review flag.
- [ ] Risk and control explained: Missing owner or budget can cause unbounded spend
