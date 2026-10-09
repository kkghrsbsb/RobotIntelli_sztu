---
name: research-tool-connect
description: Verify access to a research tool or local literature source and record a reproducible connection note in the project's research-flow tools directory. Use when adding, reconnecting, or documenting an integration such as Zotero; ordinary source reading does not require it.
---

# Research Tool Connect

Read [the shared protocol](../../research-flow/protocol.md) and [the tools guide](../../research-flow/tools/README.md). This skill records how a tool was actually reached in the current research project. Existing notes are leads, not proof that a connection still works.

Identify the tool, intended research use, current host or workspace, available connector or local API, and whether this is an initial setup or a recheck. Inspect an existing `tools/<tool>.md` before updating it. Use the smallest read-only check that confirms the needed capability: for a literature library, a successful API status alone does not prove that items can be listed or searched. Report separately whether metadata, attachments, and full text were each tested.

Prefer an already available skill, connector, or documented helper. For Zotero, follow [the Zotero note](../../research-flow/tools/zotero.md) and use the installed Zotero skill when available. If a sandbox blocks loopback access, identify that as an environment restriction and retry through an authorized route; do not label Zotero unavailable from that error alone. Do not install software, change app preferences, restart the app, import items, or export a library just to document a connection unless those actions are part of the user's request.

After a real check, write or update only the relevant `tools/<tool>.md` in the target research project. Keep the purpose, access prerequisites, tested read-only commands or routes, observed outcome and date, limits, and recovery hints. Separate portable instructions from host-specific observations. Do not store credentials, private profile paths, library inventories, or document contents in a reusable note. If the user requested a check without persistence, report in chat and leave files unchanged.

When a project note is later brought back to the template repository, review and merge the reusable method without replacing other tool notes or carrying over a project's private details. Tool connection notes do not replace source cards: cite the Zotero item and inspect the actual source when making research claims.
