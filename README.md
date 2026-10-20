# UseAgent running-footer accessibility prototype

A narrow contribution sample for [UseAgent issue #338](https://github.com/useagenthq/useagent/issues/338), prepared with substantial Codex assistance by brodyga45 on 19 October 2026. This is an unpaid local prototype, not an accepted upstream contribution. It has not been tested with VoiceOver or NVDA.

The original footer puts a self-updating elapsed timer inside `role="status"`. The patch moves that role onto the phase/step sentence, preserving the phase in a visually hidden span. The timer, run-details trigger and Stop control remain accessible outside the announcement region.

## Reproduce

Use the public upstream repository at commit `9be3a7f96699feb9a83b7cd6179d326d27567d20`. Follow its root/frontend AGENTS and CONTRIBUTING instructions. Bun is pinned to 1.3.14; install the frontend and linked `packages/agent-client` dependencies separately.

From the upstream repository root, apply this patch and run:

```sh
git apply /path/to/running-footer-live-region.patch
cd frontend
bun test components/pro/running-footer.test.tsx components/pro/running-phase.test.ts
bun run typecheck
bun run lint
```

The two complete modified source files are included for review. Copy them into `frontend/components/pro/` only in a checkout of the stated upstream commit. This bundle is not a standalone application.

## Checks performed

- Two new regression tests fail on the original component, then pass with the patch. The focused footer/phase set has 30 passing tests.
- Frontend TypeScript and lint pass; lint reports existing repository warnings.
- Full frontend test suite: 1,695 pass and one Ghostty/WASM URL failure. That failure also reproduces with the original production component restored.
- In the actual upstream session component lab, the timer advanced from 1m 57s to 2m 29s while live text stayed `Working. Editing gateway/routes.ts`. The status region contained no timer or buttons. The lab used synthetic upstream fixtures and a local fixture API, without real account data or model calls.
- Full root checks, a successful production build, a signed-in agent run and manual screen-reader verification remain outstanding. Production build attempts encountered Google Fonts connectivity and a Turbopack worker port permission error.

The upstream issue requires VoiceOver/NVDA verification, so structural tests and browser DOM observations alone do not establish completion. No paid assignment, merge, customer history or revenue is claimed.

## License and provenance

AGPL-3.0-only, inherited from UseAgent. See LICENSE and NOTICE. Source changes and test assertions are in `running-footer-live-region.patch`; the source snapshot is pinned above. No unrelated upstream assets, private correspondence, account details or credentials are included.

## Additional independent proposal evidence

[OpenQASM round-trip feasibility probe and video proposal](unitary-qasm3/README.md): three original local cases across two importers. This is an unfunded microgrant proposal; no completed fix or upstream acceptance is claimed. The independent files have their own MIT license; the UseAgent-derived material above retains its AGPL license.

[Panel Tabulator streaming reproduction](panel-tabulator-streaming/README.md): four synthetic controls with a real local-server browser observation on Panel 1.9.4. Remote streaming on the same page stays stale while the local and page-boundary controls update. This is reproduction evidence, not a fix, accepted contribution or paid delivery. These original files are separately MIT-licensed.
