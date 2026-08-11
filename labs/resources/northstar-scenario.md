# Northstar Support Scenario

Northstar is a fictional regional services company. Its internal support team wants one application that answers staff questions from approved policies, prepares synthetic service-request drafts, summarizes support calls and extracts fields from supplier invoices.

The first release serves authenticated employees. It may:

- answer policy questions only from approved evidence and cite the source ID;
- look up synthetic request status;
- prepare an escalation draft after a person reviews the proposed fields;
- summarize synthetic images, calls and invoices;
- retrieve policy and extraction records that the caller is allowed to see.

It must not:

- change identity, entitlement, payroll, supplier or production ticket records;
- make financial commitments or send messages to real people;
- expose restricted documents or trace content;
- follow instructions embedded inside retrieved documents or images;
- invent a rule when evidence is absent or conflicting.

Success is measured with grounded-answer quality, correct citations, safe-unknown behavior, tool success, approval compliance, retrieval relevance, latency and operator-visible traces.
