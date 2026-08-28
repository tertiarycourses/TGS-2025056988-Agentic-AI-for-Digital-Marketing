# Evidence checklist — Lab 07

- [ ] Workflow imported inactive and the manual execution ID is recorded
- [ ] Mock Excel data reviewed and metric `contract_valid = required_fields_present AND evidence_ids_resolved` reproduced
- [ ] Expected terminal node `Brief Approval` reached for the valid fixture
- [ ] Invalid/duplicate fixture reached the documented failure terminal where applicable
- [ ] Output keys and values match `solution/expected-output.json`
- [ ] Evidence saved as `lab-07-evidence.json` with an execution screenshot
- [ ] Acceptance check passed: The approved contract includes evidence IDs, approved claims, prohibited terms, CTA, version and contract hash.
- [ ] Risk and control explained: Unbounded prompts can invent claims or leak confidential context
