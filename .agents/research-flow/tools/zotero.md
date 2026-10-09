# Zotero: Local Literature Library

## Purpose and Route

Use the user's running Zotero Desktop as a personal literature library for finding item metadata. The local API base used in this check was `http://127.0.0.1:23119`. Zotero's Settings > Advanced > Miscellaneous had "Allow other applications on this computer to communicate with Zotero" enabled. The Zotero application must be running for the local API to answer.

If the Zotero skill and its helper are installed, locate that installation's `scripts/zotero.py` and run:

```bash
python3 <path-to-zotero.py> status --json
python3 <path-to-zotero.py> inventory --json
python3 <path-to-zotero.py> search "<known-title-or-keyword>" --json
```

The first command checks the local preference and API; the latter two confirm that this session can read and search item metadata. Use a relevant known title or keyword in the target library. Do not infer PDF access, indexed full text, or citation quality from a metadata search.

Without that helper, the local HTTP route can be checked directly when a command-line HTTP client is already available:

```bash
curl --fail --silent --show-error --max-time 3 http://127.0.0.1:23119/api/
curl --fail --silent --show-error --max-time 3 'http://127.0.0.1:23119/api/users/0/items/top?limit=1'
```

These requests read API metadata. A `200` from the second route confirms endpoint access; inspect its response to confirm the returned items are useful for the current library. Querying or reading an item still requires checking the actual source before using it as research evidence.

## Observed Check

- Checked on 2026-10-02 (Asia/Shanghai), on the template maintainer's local machine.
- Zotero Desktop `10.0.3`; local API version `3`.
- Local API `/api/` and Connector `/connector/ping` both returned HTTP `200`.
- Direct HTTP GET to `/api/` and `/api/users/0/items/top?limit=1` also returned HTTP `200`.
- `inventory --json` returned an item; `search` by that item's title returned the same item key. The title and key are omitted because they do not help reproduce the connection.
- Attachment paths, PDFs, indexed full text, Zotero writes, and operation from another host were not tested.

## Recheck and Limits

The observed result belongs to that machine and date. Re-run the checks in each research environment before reporting the tool as available. A command sandbox may deny loopback access with `Operation not permitted` even when Zotero is running; retry through an authorized local route before diagnosing the app. If the preference is off, enable it in Zotero's Advanced settings, then check again. Do not record credentials or a private Zotero profile path.

For research claims, find the item in Zotero, then inspect the source itself and record a useful locator in a source card. Item metadata alone does not establish what the paper says.
