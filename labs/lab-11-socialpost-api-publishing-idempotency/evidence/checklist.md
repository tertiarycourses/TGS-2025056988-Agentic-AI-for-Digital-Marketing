# Evidence checklist — Lab 11

- [ ] Workflow imported inactive and the manual execution ID is recorded
- [ ] Mock Excel data reviewed and metric `duplicate_rate = duplicate_attempts / publish_attempts` reproduced
- [ ] Expected terminal node `SocialPost Dry-Run Inspect` reached for the valid fixture
- [ ] Invalid/duplicate fixture reached the documented failure terminal where applicable
- [ ] Output keys and values match `solution/expected-output.json`
- [ ] Evidence saved as `publication-log.json` with an execution screenshot
- [ ] Acceptance check passed: The inspected request uses the documented SocialPost endpoint and Apikey credential pattern, remains approval-linked and idempotent, and sends nothing unless the trainer explicitly enables the sandbox node.
- [ ] Risk and control explained: Retries can publish the same approved content more than once or to an unapproved SocialPost profile
