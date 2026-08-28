# Evidence checklist — Lab 12

- [ ] Workflow imported inactive and the manual execution ID is recorded
- [ ] Mock Excel data reviewed and metric `stage_success_rate = successful_stages / attempted_stages` reproduced
- [ ] Expected terminal node `Run Ledger` reached for the valid fixture
- [ ] Invalid/duplicate fixture reached the documented failure terminal where applicable
- [ ] Output keys and values match `solution/expected-output.json`
- [ ] Evidence saved as `run-ledger.json` with an execution screenshot
- [ ] Acceptance check passed: A successful run reaches SOCIALPOST_REQUEST_INSPECTED only after research, strategy, content, QA and approval succeed; failures stop downstream execution.
- [ ] Risk and control explained: A parent agent may continue after a failed or unapproved stage
