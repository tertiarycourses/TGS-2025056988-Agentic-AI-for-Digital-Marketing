# Evidence checklist — Lab 09

- [ ] Workflow imported inactive and the manual execution ID is recorded
- [ ] Mock Excel data reviewed and metric `qa_pass_rate = passed_rules / applicable_rules` reproduced
- [ ] Expected terminal node `Reject Queue` reached for the valid fixture
- [ ] Invalid/duplicate fixture reached the documented failure terminal where applicable
- [ ] Output keys and values match `solution/expected-output.json`
- [ ] Evidence saved as `lab-09-evidence.json` with an execution screenshot
- [ ] Acceptance check passed: No high-severity asset reaches approval; every medium-risk finding has category, evidence, owner and disposition.
- [ ] Risk and control explained: An AI self-review can miss the same hallucination made during generation
