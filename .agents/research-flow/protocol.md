# Research Documentation Flow Protocol

Paths below are relative to the target project root. Read this protocol when using a `research-*` skill from this template.

## Scope and Evidence

Use the user's language for conversation and runtime notes. At a meaningful change of activity, briefly state what is being done, whether it is read-only or will write a research artifact, and whether it stays in the main session or is delegated. This is a coordination notice, not an extra approval gate.

Start from the research question and intended use. Establish the decision, reader, date boundary, jurisdiction or system boundary when relevant, and the needed confidence before expanding collection. A broad topic is not yet a researchable question; propose a narrower first question when necessary.

Keep three layers distinct:

- `source claim`: what a source actually states, with enough location context to re-find it.
- `analysis`: an interpretation, comparison, calculation, or inference based on stated evidence.
- `decision`: the user's or project's chosen action, preference, or open direction.

Use direct quotations only when their exact wording matters and preserve context. Otherwise paraphrase faithfully. Never invent a source, locator, access result, quotation, consensus, or citation. Mark missing, conflicting, stale, paywalled, second-hand, or unverified material explicitly. A link alone is often insufficient: record a page, section, figure, timestamp, commit, row range, or other useful locator when the source permits it.

## Researcher's Understanding

At the start of a new topic, first learn what the researcher can already explain. Ask one or two open questions about the central object, proposed method, or evidence before giving a full account when this helps calibrate depth. Basic questions are welcome. Use the user's answers and stated confidence to choose what to explain next; do not turn a request for immediate help into a mandatory quiz.

Treat the researcher's own restatement and explicit confidence as the primary evidence of their understanding. Source verification is separate: an agent reading a paper, inspecting code, or checking an experiment cannot mark the researcher as understanding it. If the user only states confidence, record it as self-reported; if they have not restated a claim, say so. Never invent a paraphrase or infer understanding from silence or agreement.

An early question such as "I cannot follow this conclusion" is already evidence of a specific understanding gap. Pause the explanation at that point, locate the relevant source, data transformation, or assumption, explain the smallest missing link, and invite the user to restate it in their own words when useful. Do this during ordinary research, not only during a later review. Correct their account against inspectable evidence without treating an elementary question as failure.

When a data choice, transformation, experiment result, key inference, or decision will constrain later work, keep a short understanding checkpoint: the claim and reason, evidence status, the user's actual restatement and self-reported confidence, and what would invalidate the claim. Record a specific gap when the user cannot yet explain a consequential link. Surface relevant gaps before relying on them; do not make all research wait for every gap to close.

For a long pause or a requested review, use active recall before explanation when useful. Select a few questions from the current research problem, evidence, and derivation chain, including basic object-level questions where appropriate. After the answer, correct using actual materials and update only the user's restatement, confidence, and remaining gap, not a quiz transcript.

## Activities and Sources

| Activity | Outcome |
| --- | --- |
| `orient` | A bounded question, known material, source priorities, and unknowns |
| `collect` | Candidate sources and explicit selection criteria |
| `capture` | Traceable claims, context, limitations, and relevance |
| `analyze` | Comparisons and tentative inferences with evidence boundaries |
| `synthesize` | A reader-appropriate answer, note, report, or draft |
| `review` | A check of traceability, scope, conflicts, and unsupported language |

Local project files, supplied documents, primary sources, datasets, official documentation, secondary reporting, and personal notes have different evidentiary roles. Identify what was actually read. Prefer the strongest source practical for a claim, but do not discard useful contextual material merely because it is not primary; describe its role instead.

Reading a source does not by itself authorize a network search, download, tool installation, new database, publication, or broad reproduction. Follow the current request and available capabilities. Preserve existing user materials and project conventions; do not reorganize a library merely to fit this template.

For a research tool connection, read [the tools guide](tools/README.md) and use `research-tool-connect` when the user wants setup, verification, or a reusable record. A previous tool note is evidence of an earlier check, not live availability. Keep tool access procedures separate from source evidence and from the researcher's understanding.

## Main Session and Branches

The main research conversation maintains `.agents/research-flow/understanding.md` when persistence is in scope. It records the current question and how it changed, evidence and unresolved claims, consequential decisions and their reasons, the researcher's own restatements and confidence, understanding gaps, and the derivation links that affect conclusions. It is a compact aid to understanding, not a transcript, issue tracker, or authority. Read the latest version before editing; actual sources and artifacts take precedence over its summaries. Do not copy Linear issues, task statuses, or session ownership into it; link to a relevant issue only when it helps locate work behind a claim.

For each consequential data or experiment node, record only enough lineage to trace `input/version -> operation and key configuration -> output -> validation -> downstream consumer`. Do not inventory every temporary file. Use stable IDs or paths to connect source cards, datasets, scripts, run records, figures, drafts, and decisions where they exist. A missing link is an explicit uncertainty, not a reason to reconstruct a plausible history.

For a substantial source, use [source.md](templates/source.md). For multi-source writing, use [synthesis.md](templates/synthesis.md). Trim fields that do not help the task. A separate conversation may investigate a source cluster or one bounded question, then return evidence and uncertainty to the main research conversation. It does not silently rewrite the shared understanding file.

The user opens separate conversations manually: a blank conversation or a fork of the main conversation, in the current workspace or a new worktree. The user or main conversation can formulate the question, source boundary, desired depth, and return shape. Research directions may split or merge as evidence changes; do not maintain a fixed session tree. A separate conversation reports negative findings and access limits as carefully as positive claims. Do not claim a conversation, file, source download, or external lookup exists without observing it.

On resume, verify old summaries and important derivation links against the actual source material and current artifact. Do not assume that an interrupted reader or unavailable source is complete. Preserve partial notes; distinguish them from checked evidence. Start with active recall when the user requests review or when a long gap makes their own understanding the priority.

## Synthesis and Completion

Tie material claims in a final artifact to source cards, citations, or an explicit explanation of why they are analytical judgment. Keep uncertainty near the conclusion it affects. When sources disagree, explain the disagreement, their scope or dates, and what evidence would change the conclusion rather than selecting a winner silently.

Before calling a research task complete, check the requested question and audience, claim traceability, important counterevidence, date/scope boundaries, known gaps, and any cognitive debt that materially qualifies the user's ability to rely on the result. Completion of a draft, a reading batch, a recommendation, and a published document are different delivery states. Do not imply later publication, citation-manager updates, or project decisions occurred unless they were observed.
