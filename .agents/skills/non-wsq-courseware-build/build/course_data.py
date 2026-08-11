"""Single source of truth for the C926 AI-103 non-WSQ courseware."""

TITLE = "AI-103 Microsoft Certified Azure AI Apps and Agents Developer Associate (C926)"
SHORT_TITLE = "AI-103 Azure AI Apps and Agents Developer Associate (C926)"
COURSE_CODE = "C926"
VERSION = "v1.0"
VERSION_DATE = "11 August 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Tertiary Infotech Academy Trainer"
DAYS = 2
DAY_MINUTES = 480
INSTRUCTIONAL_MINUTES = 450
MODE = "Instructor-led, concept-first workshops and connected hands-on labs"
DAILY_TIMING = "9:30 am - 6:30 pm (1-hour lunch; two 15-minute tea breaks)"
DARK_THEME = False

LEARNING_OUTCOMES = [
    "LO1: Plan a secure, responsible and operable Microsoft Foundry solution by selecting suitable models, services, deployment patterns and controls.",
    "LO2: Build grounded generative applications with Microsoft Foundry, retrieval patterns, structured prompts and repeatable quality checks.",
    "LO3: Build and operationalize tool-using and multi-agent solutions with bounded roles, approval controls, tracing and error analysis.",
    "LO4: Implement multimodal computer-vision workflows for generation, understanding, accessibility and visual safety.",
    "LO5: Implement text, translation and speech workflows that return reliable structured outputs and handle language-specific limitations.",
    "LO6: Implement information-extraction and retrieval pipelines with OCR, Content Understanding, Azure AI Search and grounded outputs.",
]
LO_TITLES = ["Plan & Govern", "Generative Apps", "Agents", "Vision", "Text & Speech", "Extraction & Search"]


def concept(title, paragraphs, items, visual_title=None, visual_kicker="WORKING MODEL"):
    return dict(
        title=title,
        paragraphs=paragraphs,
        items=items,
        visual_title=visual_title or title,
        visual_kicker=visual_kicker,
    )


TOPICS = [
    dict(
        num=1,
        code="01",
        title="Plan and Manage an Azure AI Solution",
        subtitle="25-30% objective coverage · models · Foundry services · infrastructure · security · operations · responsible AI",
        weighting="25-30%",
        concepts=[
            "Choose models and Foundry services from the task, modality, grounding, agency and operational constraints.",
            "Treat deployment topology, quotas, cost, identity, networking and CI/CD as part of the AI design.",
            "Monitor model quality, retrieval health, latency, tokens, safety events and business outcomes together.",
            "Apply guardrails, provenance, approval and tool-access controls according to impact and reversibility.",
        ],
        concept_sections=[
            concept(
                "Choose Models and Foundry Services",
                [
                    "Start with the workload contract: modalities, output, latency, quality, data boundary and permitted actions. Select a model by task fit, not size alone.",
                    "A Foundry project groups deployments, connections, agents, evaluation and observability. Use Azure AI Search or Foundry IQ for grounding and Foundry Tools for specialist services such as Content Understanding, Translator and Speech.",
                ],
                [
                    ("Task fit", "Match reasoning, modality, context and structured-output needs."),
                    ("Grounding", "Choose retrieval and indexing for evidence-bound answers."),
                    ("Agency", "Choose tools, memory and orchestration only when actions need them."),
                    ("Operations", "Check region, quota, latency, cost, lifecycle and support status."),
                ],
            ),
            concept(
                "Infrastructure and Deployment",
                [
                    "Separate development, validation and production environments. Use repeatable infrastructure definitions, named model deployments and environment-specific configuration so a release can be reproduced and rolled back.",
                    "Capacity is shaped by tokens, requests, concurrency and downstream limits. Rate-limit handling should use bounded retries and backoff; cost controls should combine quotas, budgets, model routing, caching and output limits rather than relying on a single alert.",
                ],
                [
                    ("Project", "Own models, agents, connections, evaluations and traces as one boundary."),
                    ("Deployment", "Name a model version and capacity configuration used by applications."),
                    ("Pipeline", "Promote tested code, prompts and configuration through environments."),
                    ("Capacity", "Model token, request and downstream-service constraints explicitly."),
                ],
            ),
            concept(
                "Identity, Network and Secrets",
                [
                    "Prefer Microsoft Entra identities and role-based access over copied service keys. Distinguish the developer identity, application managed identity and end-user identity because each may be authorized to different project connections or data sources.",
                    "Private endpoints and network controls reduce exposure but add DNS, routing and build-agent dependencies. Keep secrets in managed stores or environment settings and never place credentials in prompts, notebooks, screenshots or source control.",
                ],
                [
                    ("Authenticate", "Prove which workload or user is calling."),
                    ("Authorize", "Grant the minimum project, model, search and data roles."),
                    ("Isolate", "Use approved public or private network paths and test DNS."),
                    ("Protect", "Use keyless credentials where supported and rotate unavoidable keys."),
                ],
            ),
            concept(
                "Responsible AI and Operations",
                [
                    "Responsible AI is a lifecycle practice. Define intended use, affected users, excluded behavior, content filtering, groundedness expectations, human oversight, disclosure and incident response before release.",
                    "Trace evidence should connect user input, retrieval, model call, tool call and final response. Observe quality, drift, retrieval relevance, safety signals, token use, latency and errors without collecting more personal or confidential data than operations require.",
                ],
                [
                    ("Prevent", "Use instructions, filters, schemas, least privilege and tool boundaries."),
                    ("Detect", "Evaluate quality and safety; monitor traces and unusual behavior."),
                    ("Respond", "Pause actions, route to people and preserve a useful correlation ID."),
                    ("Improve", "Change the component supported by evidence, then rerun regression tests."),
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="Implement Generative AI and Agentic Solutions",
        subtitle="30-35% objective coverage · Responses API · RAG · tools · memory · multi-agent · evaluation · observability",
        weighting="30-35%",
        concepts=[
            "A generative application is a controlled system of instructions, context, model parameters, validation and evaluation.",
            "RAG quality depends on ingestion, chunking, retrieval, evidence selection and faithful generation.",
            "Agents add tool selection, state and delegation; each capability needs a bounded contract and failure path.",
            "Evaluation and tracing turn fluent behavior into measurable evidence for release and improvement.",
        ],
        concept_sections=[
            concept(
                "Generative Application Contract",
                [
                    "Separate system instructions, user input, trusted context and output schema. The model should be told what to do when evidence is absent or conflicting, not merely what a good answer looks like.",
                    "Generation parameters trade determinism, diversity, length, latency and cost. Structured outputs reduce brittle parsing, but the application must still validate types, required fields and allowed values before using the result.",
                ],
                [
                    ("Instruction", "Role, task, evidence boundary and prohibited behavior."),
                    ("Context", "Retrieved or supplied facts that may support the answer."),
                    ("Generation", "Model and parameters selected for the task."),
                    ("Validation", "Schema, policy and business-rule checks before use."),
                ],
            ),
            concept(
                "Retrieval-Augmented Generation",
                [
                    "RAG retrieves candidate evidence before generation. Diagnose the stages separately: ingestion quality, index freshness, query representation, retrieval relevance, context selection and answer faithfulness.",
                    "Keyword search is precise for exact terms; vector search retrieves semantic similarity; hybrid search combines both and can add semantic ranking. Access filters and source metadata must travel with the evidence so grounding does not become an authorization bypass.",
                ],
                [
                    ("Ingest", "Extract, clean, segment and enrich approved content."),
                    ("Retrieve", "Use keyword, vector, hybrid or agentic retrieval deliberately."),
                    ("Ground", "Supply relevant evidence with identifiers and provenance."),
                    ("Answer", "Stay faithful, cite sources and decline unsupported claims."),
                ],
            ),
            concept(
                "Agent Roles, Tools and Memory",
                [
                    "An agent combines a model with instructions, conversation state and tools. Tool names, descriptions and schemas are routing signals; narrow typed tools are safer and easier to evaluate than a generic function that can do anything.",
                    "Use conversation state for current-turn continuity and long-term memory only for durable user facts with an explicit scope and retention policy. Require human confirmation before consequential or hard-to-reverse tool calls.",
                ],
                [
                    ("Role", "One bounded outcome and clear exclusions."),
                    ("Tool", "A typed capability with least privilege and safe errors."),
                    ("State", "Conversation history needed for the current task."),
                    ("Memory", "Durable facts isolated by user or business scope."),
                ],
            ),
            concept(
                "Multi-Agent Orchestration",
                [
                    "Multiple agents are justified when capabilities have different expertise, identities, data boundaries, ownership or release cadences. They also add latency, cost, routing uncertainty and more failure states.",
                    "Give each specialist a non-overlapping capability description and a predictable result contract. Bound delegation depth, context sharing, timeouts and retries; preserve one correlation identifier across all hops.",
                ],
                [
                    ("Route", "Choose a specialist from distinct capability descriptions."),
                    ("Delegate", "Pass the minimum task, context and constraints."),
                    ("Return", "Use a stable status, result, evidence and error shape."),
                    ("Control", "Limit depth, time, tools, context and consequential actions."),
                ],
            ),
            concept(
                "Evaluate and Operationalize",
                [
                    "Use representative datasets for core, boundary, adversarial and regression scenarios. Measure relevance, groundedness, retrieval quality, task completion, tool selection, tool-input accuracy, latency, token use and safety according to the application risk.",
                    "Tracing exposes the path from input through retrieval, model and tool spans. Error analysis should identify whether to change data, retrieval, instructions, model, tool schema or infrastructure rather than repeatedly editing the prompt by instinct.",
                ],
                [
                    ("Dataset", "Representative queries, expected behavior and risk cases."),
                    ("Evaluator", "A defined metric, threshold and explanation."),
                    ("Trace", "Ordered spans for retrieval, model, tools and errors."),
                    ("Decision", "Release, hold or improve based on evidence and guardrails."),
                ],
            ),
        ],
    ),
    dict(
        num=3,
        code="03",
        title="Implement Computer Vision Solutions",
        subtitle="10-15% objective coverage · image and video generation · editing · multimodal understanding · accessibility · visual safety",
        weighting="10-15%",
        concepts=[
            "Generation prompts specify subject, composition, style, constraints and intended use; editing adds source images and masks.",
            "Multimodal understanding grounds answers in pixels, embedded text, temporal segments and extracted regions.",
            "Accessible descriptions prioritize purpose and relevant evidence rather than listing every visual detail.",
            "Visual inputs can contain unsafe content or indirect prompt injection and require content and policy controls.",
        ],
        concept_sections=[
            concept(
                "Generate and Edit Images or Video",
                [
                    "Select a generation model by supported modality, region, quality, latency, cost and control surface. A useful prompt defines subject, setting, composition, visual treatment, text requirements and exclusions; reference media and masks constrain edits.",
                    "Generation is iterative but should remain traceable. Save prompt versions, model deployment, parameters, content-filter outcomes and human decisions when outputs feed a business process.",
                ],
                [
                    ("Prompt", "Subject, composition, treatment, constraints and exclusions."),
                    ("Reference", "Source media that preserves identity, layout or style."),
                    ("Mask", "Region eligible for inpainting or replacement."),
                    ("Review", "Safety, accuracy, rights, brand and accessibility checks."),
                ],
            ),
            concept(
                "Multimodal Understanding",
                [
                    "A multimodal model can answer questions about images and selected video frames, while Content Understanding can extract descriptions, fields, timing, segments and structured representations from several media types.",
                    "Ask for observations before interpretations, cite the visual region or time segment when possible, and state uncertainty. Optical text can be untrusted input; embedded instructions should never override the application policy.",
                ],
                [
                    ("Observe", "Objects, text, layout, action and scene evidence."),
                    ("Locate", "Region, page, frame, timestamp or segment."),
                    ("Reason", "Answer only what the visible evidence supports."),
                    ("Represent", "Return captions, markdown, fields or structured JSON."),
                ],
            ),
            concept(
                "Accessible Visual Descriptions",
                [
                    "Alt text communicates the image's purpose in context. Decorative images can use empty alt text; informative images need concise meaning; complex charts or diagrams need a short label plus a nearby extended description.",
                    "Generated descriptions require human review for names, sensitive attributes, inferred emotion and domain-specific claims. Do not guess protected or personal characteristics that are not needed for the task.",
                ],
                [
                    ("Purpose", "Explain why the image matters in this context."),
                    ("Evidence", "Describe visible facts before interpretation."),
                    ("Length", "Use concise alt text plus an extended description when needed."),
                    ("Review", "Check names, numbers, bias, privacy and unsupported inference."),
                ],
            ),
            concept(
                "Responsible Multimodal Controls",
                [
                    "Apply input and output content policies, provenance or watermark rules, permitted-brand constraints and a review path for ambiguous or high-impact content. A safe text prompt does not guarantee a safe visual result.",
                    "Indirect prompt injection can be hidden in signs, screenshots or documents. Treat extracted visual text as data, keep system instructions authoritative and restrict tool access even when the image asks the model to take action.",
                ],
                [
                    ("Classify", "Detect unsafe or disallowed visual content."),
                    ("Resist", "Treat embedded instructions as untrusted data."),
                    ("Constrain", "Apply brand, provenance, watermark and tool policies."),
                    ("Escalate", "Route uncertain or consequential content to a person."),
                ],
            ),
        ],
    ),
    dict(
        num=4,
        code="04",
        title="Implement Text Analysis Solutions",
        subtitle="10-15% objective coverage · entities · topics · summaries · structured JSON · sentiment · translation · speech",
        weighting="10-15%",
        concepts=[
            "Generative text analysis can combine extraction, classification, summarization and structured output in one controlled prompt.",
            "Sentiment and safety signals are probabilistic evidence, not facts about a person's intent or character.",
            "Translation quality depends on locale, terminology, context and a review path for high-impact content.",
            "Speech pipelines add audio quality, language, speaker, timing, voice and latency decisions.",
        ],
        concept_sections=[
            concept(
                "Structured Text Analysis",
                [
                    "Define the field schema before prompting. Entity extraction identifies spans or values, classification assigns allowed labels, summarization compresses information, and structured output makes downstream validation possible.",
                    "Keep source text alongside extracted values and record confidence or evidence spans where the service supports them. Missing information should remain null or explicitly unknown rather than being fabricated to complete a schema.",
                ],
                [
                    ("Extract", "Entities, facts, topics and domain fields."),
                    ("Classify", "Sentiment, tone, safety or business category."),
                    ("Summarize", "Compress while retaining decisions and exceptions."),
                    ("Structure", "Validate allowed keys, types and values."),
                ],
            ),
            concept(
                "Sentiment, Tone and Safety",
                [
                    "Sentiment services return labels and confidence scores at document or sentence level. Opinion mining can connect an evaluated target to the words that describe it, making the signal more actionable than a single overall label.",
                    "Use these signals for routing or prioritization with safeguards, not as unquestioned truth. Sarcasm, dialect, mixed sentiment, domain language and short text can reduce reliability.",
                ],
                [
                    ("Label", "A supported category such as positive, neutral or negative."),
                    ("Confidence", "Model certainty, not correctness probability for every use."),
                    ("Target", "The product, feature or issue being discussed."),
                    ("Safeguard", "Threshold, human review and representative monitoring."),
                ],
            ),
            concept(
                "Translation and Domain Adaptation",
                [
                    "Translation requires a source language, one or more target languages, terminology decisions and a fallback for unsupported language or ambiguous input. Preserve proper nouns, numbers, links and regulated terms deliberately.",
                    "A generative model can adapt tone or format, while Azure Translator offers a dedicated translation contract. High-impact or customer-facing content should use terminology resources and bilingual review.",
                ],
                [
                    ("Detect", "Identify or confirm the source language."),
                    ("Translate", "Select target locale and dedicated or generative method."),
                    ("Adapt", "Apply domain terminology, tone and formatting."),
                    ("Verify", "Back-translate samples and review critical terms."),
                ],
            ),
            concept(
                "Speech and Audio Workflows",
                [
                    "Speech to text converts audio into time-aligned language; text to speech renders text with a selected voice; speech translation combines recognition and translation. Choose real-time, fast-file or batch transcription by latency and media length.",
                    "Audio quality, microphone placement, accents, overlap and domain terms affect accuracy. Custom speech models may improve specialist vocabulary but add data, evaluation and lifecycle responsibilities.",
                ],
                [
                    ("Capture", "Microphone, stream or audio file with known format."),
                    ("Recognize", "Language, timing, speakers and confidence."),
                    ("Reason", "Summarize or extract from the transcript with evidence."),
                    ("Respond", "Translate or synthesize an accessible voice output."),
                ],
            ),
        ],
    ),
    dict(
        num=5,
        code="05",
        title="Implement Information Extraction Solutions",
        subtitle="10-15% objective coverage · ingestion · OCR · layout · Content Understanding · semantic, hybrid and vector search · grounding",
        weighting="10-15%",
        concepts=[
            "Information extraction converts unstructured multimodal content into evidence-bearing fields and representations.",
            "OCR finds text; layout finds structure; field extraction maps evidence to a business schema.",
            "Search index design controls what can be retrieved, filtered, ranked, cited and secured.",
            "A trustworthy pipeline monitors ingestion completeness, index freshness, retrieval relevance and grounded output quality.",
        ],
        concept_sections=[
            concept(
                "The Extraction Pipeline",
                [
                    "Ingest approved documents, images, audio or video; normalize and segment the content; enrich it with OCR, layout, descriptions or custom skills; then map evidence to a stable field schema.",
                    "Keep source identifiers, pages, spans, regions or timestamps so downstream users can inspect the evidence. Confidence thresholds and validation rules should route uncertain fields for review rather than silently accepting them.",
                ],
                [
                    ("Ingest", "Acquire approved content and preserve source identity."),
                    ("Understand", "OCR, layout, segments, descriptions and fields."),
                    ("Validate", "Schema, type, confidence and business-rule checks."),
                    ("Publish", "Clean markdown, JSON, index documents and provenance."),
                ],
            ),
            concept(
                "Content Understanding Analyzers",
                [
                    "An analyzer defines the content types, segmentation and fields that Content Understanding should return. Prebuilt analyzers accelerate common documents and media; custom analyzers express a domain-specific schema and extraction instructions.",
                    "Single-task pipelines optimize one outcome, while pro-mode or richer pipelines combine multiple extraction and reasoning tasks. Model availability, regional support, latency and cost remain deployment decisions.",
                ],
                [
                    ("Prebuilt", "A ready analyzer for common document or media types."),
                    ("Custom", "A reusable domain schema with extraction instructions."),
                    ("Content", "Markdown, transcript, figures, segments and fields."),
                    ("Evidence", "Page, span, region, timestamp and confidence metadata."),
                ],
            ),
            concept(
                "Search for Grounding",
                [
                    "An Azure AI Search index separates retrievable content from vector fields and filterable metadata. Keyword, vector and hybrid queries serve different needs; hybrid results use reciprocal rank fusion and can be reranked semantically.",
                    "Use integrated vectorization or precomputed embeddings consistently. Vector dimensions must match the embedding model, and security filters must be applied before evidence is returned to the application or agent.",
                ],
                [
                    ("Schema", "Key, content, vector, filter, source and security fields."),
                    ("Query", "Keyword, vector, hybrid or agentic retrieval."),
                    ("Rank", "Similarity, reciprocal rank fusion and semantic reranking."),
                    ("Filter", "Tenant, user, source, category, date and permission boundary."),
                ],
            ),
            concept(
                "Grounded Representations and Quality",
                [
                    "The retrieval pipeline should return compact evidence with stable source identifiers. The generation layer should cite that evidence, state uncertainty and decline questions the retrieved content cannot answer.",
                    "Monitor document counts, failed ingestion, stale sources, empty queries, retrieval precision, citation coverage and groundedness. A strong model cannot compensate for missing or unauthorized evidence.",
                ],
                [
                    ("Completeness", "Expected content was ingested and indexed."),
                    ("Relevance", "Retrieved passages address the actual query."),
                    ("Faithfulness", "The response stays within returned evidence."),
                    ("Provenance", "A user or operator can locate the supporting source."),
                ],
            ),
        ],
    ),
]

DAY_THEMES = {
    1: "Foundry Planning, Grounded Generation and Agents",
    2: "Multimodal, Text, Extraction and Retrieval Solutions",
}


def SCHEDULE(lab_titles, lab_minutes):
    return {
        1: (DAY_THEMES[1], [
            ("9:30", "9:45", 15, "admin", "Welcome, solution scenario, setup expectations and learning outcomes"),
            ("9:45", "10:30", 45, "topic", "Topic 1 - " + TOPICS[0]["title"] + " (concepts and demonstration)"),
            ("10:30", "11:15", lab_minutes[1], "lab", "Hands-on: " + lab_titles([1])),
            ("11:15", "11:30", 15, "break", "Tea break"),
            ("11:30", "12:30", lab_minutes[2], "lab", "Hands-on: " + lab_titles([2])),
            ("12:30", "13:30", 60, "lunch", "Lunch break"),
            ("13:30", "14:15", 45, "topic", "Topic 2 - " + TOPICS[1]["title"] + " (concepts and demonstration)"),
            ("14:15", "15:30", lab_minutes[3], "lab", "Hands-on: " + lab_titles([3])),
            ("15:30", "15:45", 15, "break", "Tea break"),
            ("15:45", "17:15", lab_minutes[4], "lab", "Hands-on: " + lab_titles([4])),
            ("17:15", "18:15", lab_minutes[5], "lab", "Hands-on: " + lab_titles([5])),
            ("18:15", "18:30", 15, "recap", "Day 1 recap, troubleshooting clinic and learning-outcome review"),
        ]),
        2: (DAY_THEMES[2], [
            ("9:30", "9:45", 15, "admin", "Day 2 orientation, prior-learning recap and solution checkpoint"),
            ("9:45", "10:15", 30, "topic", "Topic 3 - " + TOPICS[2]["title"] + " (concepts and demonstration)"),
            ("10:15", "11:30", lab_minutes[6], "lab", "Hands-on: " + lab_titles([6])),
            ("11:30", "11:45", 15, "break", "Tea break"),
            ("11:45", "12:15", 30, "topic", "Topic 4 - " + TOPICS[3]["title"] + " (concepts and demonstration)"),
            ("12:15", "13:30", lab_minutes[7], "lab", "Hands-on: " + lab_titles([7])),
            ("13:30", "14:30", 60, "lunch", "Lunch break"),
            ("14:30", "15:00", 30, "topic", "Topic 5 - " + TOPICS[4]["title"] + " (concepts and demonstration)"),
            ("15:00", "16:30", lab_minutes[8], "lab", "Hands-on: " + lab_titles([8])),
            ("16:30", "16:45", 15, "break", "Tea break"),
            ("16:45", "18:15", lab_minutes[9], "lab", "Hands-on: " + lab_titles([9])),
            ("18:15", "18:30", 15, "recap", "Course recap, operational next steps and learning-outcome review"),
        ]),
    }


COURSE_OVERVIEW = dict(
    section_title="Build Azure AI Apps and Agents as Operable Systems",
    concepts_title="The AI Solution Stack",
    concepts=[
        ("Experience", "User inputs, multimodal interactions and accessible outputs."),
        ("Models", "Task-fit language, code, image, audio and multimodal deployments."),
        ("Knowledge", "Extraction, indexes, retrieval and evidence-bound generation."),
        ("Agents", "Roles, tools, memory, delegation and approval controls."),
        ("Guardrails", "Identity, filters, policy, provenance and human oversight."),
        ("Operations", "Evaluation, traces, capacity, cost, CI/CD and incident response."),
    ],
    framework_title="The GROUND Solution Framework",
    framework=[
        ("Goal", "Define the user outcome, system boundary and quality threshold."),
        ("Resources", "Choose Foundry models, tools, retrieval and deployment pattern."),
        ("Ownership", "Assign identities, data owners, operators and review authority."),
        ("Understanding", "Extract, retrieve and preserve evidence across modalities."),
        ("Navigation", "Route prompts, tools and specialist agents through bounded contracts."),
        ("Defence", "Evaluate, trace, guard, recover and continuously improve."),
    ],
    statement=dict(
        headline="Production AI is an evidence-and-control system, not a single model call.",
        body="Reliable outcomes come from task-fit models, grounded context, bounded tools, explicit identities, measurable quality and disciplined operations.",
        kicker="CORE IDEA",
    ),
    pillars_title="One Connected Northstar Support Solution",
    pillars=[
        ("Plan", ["Architecture and service-selection record", "Identity, cost, safety and monitoring controls"]),
        ("Build", ["Grounded generative app", "Tool-using and multi-agent workflow"]),
        ("Extend", ["Vision, text, speech and extraction", "Hybrid search grounding pipeline"]),
    ],
    arc_title="How Every Lab Progresses",
    arc=[
        "Start from the prior checkpoint.",
        "Apply the topic concept to synthetic Northstar evidence.",
        "Build with placeholder configuration and least privilege.",
        "Verify a visible output, trace, file or query result.",
        "Save the named checkpoint for the next lab.",
    ],
)

LG_INTRO = (
    "This Learner Guide is the self-contained study text for AI-103 Microsoft Certified Azure AI Apps and Agents Developer Associate (C926). "
    "It follows the five official skills domains published for AI-103 as of 16 April 2026 and teaches each concept before the related practice."
)
LG_INTRO2 = (
    "Nine connected labs grow one synthetic Northstar Support solution from an architecture decision record into a grounded, tool-using and multimodal application with extraction, retrieval, evaluation and operational controls. "
    "Detailed verification, troubleshooting and rejoin checkpoints keep the practical work executable without replacing the conceptual coverage."
)
LG_SETUP = dict(
    needs=[
        "A Windows or macOS laptop with a current Microsoft Edge or Google Chrome browser.",
        "Python 3.10 or later, Visual Studio Code and Git.",
        "Azure CLI signed in to an instructor-provided subscription or sandbox with access to a Microsoft Foundry project.",
        "A deployed language model in the Foundry project and, where enabled, an image model, Azure AI Search service and Content Understanding resource.",
        "Permission to read project deployments, call the selected model, view traces and use the instructor-provided search index and analyzers.",
        "The values named in labs/resources/instructor-readiness-manifest.md; use the documented rejoin path when a regional or optional feature is unavailable.",
    ],
    verify_text="Open the Microsoft Foundry project, confirm the project endpoint and model deployment name, run az account show, and ask the instructor to show PASS evidence for the readiness manifest before starting a dependent lab.",
    verify_code="python --version\naz --version\naz account show --query '{subscription:name, tenant:tenantId}' -o table\n# Never paste tokens or keys into this record.",
    conventions=[
        "Replace angle-bracket placeholders such as <FOUNDRY_PROJECT_ENDPOINT> with instructor-provided training values.",
        "Store real values only in environment variables or managed connections; never in prompts, screenshots or source control.",
        "Portal navigation changes over time; follow the named resource and intent when a menu label has moved.",
        "Save every named checkpoint because later labs reuse the architecture record, policy corpus, traces or extracted fields.",
    ],
)
LAB_NOTE = "Use only the synthetic Northstar data supplied with this course. Keep credentials in managed identities, environment variables or approved secret stores, never in prompts, lab files or source control."

LG_WRAPUP = dict(
    title="Wrap-Up - From Prototype to Operated AI Service",
    intro="A production Azure AI solution remains trustworthy only while its data, models, tools, identities and owners remain current.",
    sections=[
        dict(title="Before release", bullets=[
            "Review task boundaries, identities, network paths and consequential tool controls.",
            "Run representative quality, retrieval, safety and failure-path checks.",
            "Confirm trace collection, sensitive-data handling, support ownership and rollback evidence.",
        ]),
        dict(title="After release", bullets=[
            "Monitor user outcomes, retrieval health, groundedness, tool reliability, latency, tokens and safety signals.",
            "Triage evidence before changing data, prompts, models, tools or capacity.",
            "Retire stale sources, unused deployments, orphaned agents and unowned connections.",
        ]),
    ],
)
LG_NEXT_STEPS = [
    "Rebuild the Northstar solution in a separate development project using your own approved sandbox resources.",
    "Replace one synthetic integration with an authorized organisational dataset and define its identity and freshness controls.",
    "Convert the course quality rubric, trace review and release checklist into reusable engineering templates.",
    "Review the current Microsoft Learn AI-103 study guide and product documentation before implementing features in a live environment.",
]
LG_GLOSSARY = [
    ("Agent", "A model-directed system with instructions, state and tools for a bounded outcome."),
    ("Content Understanding", "A Foundry Tool that extracts multimodal content, structure and fields through analyzers."),
    ("Embedding", "A numeric representation used to compare semantic similarity."),
    ("Foundry project", "A project boundary for models, agents, connections, data, evaluations and observability."),
    ("Groundedness", "The extent to which a response is supported by the provided context or retrieved evidence."),
    ("Hybrid search", "Keyword and vector search executed together, with results fused into one ranking."),
    ("Managed identity", "An Azure-managed workload identity that avoids application-managed credentials."),
    ("RAG", "Retrieval-augmented generation: retrieve evidence, then generate an answer constrained by it."),
    ("Semantic ranker", "A language-understanding stage that reranks search results for relevance."),
    ("Tool schema", "The typed name, description, inputs and outputs an agent uses to select and call a capability."),
    ("Trace", "An ordered record of model, retrieval, tool and application spans for one interaction."),
    ("Vector search", "Similarity search over embedding vectors rather than exact terms alone."),
]

REFERENCES = [
    ("AI-103 study guide", "https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103"),
    ("Azure AI Projects Python library", "https://learn.microsoft.com/en-us/python/api/overview/azure/ai-projects-readme?view=azure-python"),
    ("Microsoft Foundry quickstarts", "https://learn.microsoft.com/en-us/azure/foundry/quickstarts/quickstarts"),
    ("Responses API agents", "https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/responses-api"),
    ("Function tools and approval", "https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval"),
    ("Agent tracing", "https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-framework"),
    ("Generative AI evaluation", "https://learn.microsoft.com/en-us/azure/ai-studio/how-to/evaluate-generative-ai-app"),
    ("RAG evaluators", "https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators"),
    ("Azure AI Search vector quickstart", "https://learn.microsoft.com/en-us/azure/search/search-get-started-vector?pivots=python"),
    ("Azure AI Search hybrid queries", "https://learn.microsoft.com/en-us/azure/search/hybrid-search-how-to-query"),
    ("Content Understanding quickstart", "https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/quickstart/use-rest-api"),
    ("Content Understanding analyzer reference", "https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/concepts/analyzer-reference"),
    ("Speech to text quickstart", "https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-to-text"),
    ("Translator SDK quickstart", "https://learn.microsoft.com/en-us/azure/ai-services/translator/text-translation/quickstart/client-library-sdk"),
    ("Image generation tool", "https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/image-generation"),
]
NEXT_STEPS = dict(title="Continue Building", items=LG_NEXT_STEPS)
THANK_YOU = dict(body="You have planned, built, grounded, extended and operationalized one connected Azure AI apps and agents solution.")
LAB_SHOTS = {}
VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial aligned release of slides, Learner Guide, Lesson Plan and nine connected labs.", TRAINER),
]
