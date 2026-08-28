# Evidence checklist — Lab 10

- [ ] Workflow imported inactive and the manual execution ID is recorded
- [ ] Mock Excel data reviewed and metric `approval_integrity = decision_hash == current_payload_hash` reproduced
- [ ] Expected terminal node `Approved` reached for the valid fixture
- [ ] Invalid/duplicate fixture reached the documented failure terminal where applicable
- [ ] Output keys and values match `solution/expected-output.json`
- [ ] Evidence saved as `approval-record.json` with an execution screenshot
- [ ] Acceptance check passed: Only APPROVED records with a matching SocialPost payload hash proceed; rejected, retargeted or changed payloads cannot publish.
- [ ] Risk and control explained: A reviewer may approve one version while a changed payload is later published
