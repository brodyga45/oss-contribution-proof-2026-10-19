# Commission a focused open-source fix

brodyga45 offers paid, AI-assisted work on public open-source software: reproducing a frontend regression, supplying a tested patch, or qualifying a public Rust/macOS build problem.

## Start with one concrete problem

Open an issue in this repository with the public upstream issue or repository, affected version, reproduction steps, and the outcome you need. Please include your budget and whether you need a tested patch, an accepted upstream PR, or an ongoing maintenance arrangement. Keep credentials, private code, personal data and payment details out of public issues.

A focused patch starts at **€150**, subject to a fixed quote after the scope is checked. A reasonable first package is one reproducible defect, one scoped fix, a regression check, and instructions to verify the result. There is no commitment or payment request until the scope, acceptance, timeline and payment terms are agreed.

For a dependency you use regularly, an initial accepted fix can lead to a separately scoped maintenance cycle covering the versions and checks you actually need. Recurring work has its own capacity, price and acceptance agreement.

## What acceptance means

Before implementation, we agree on the target revision, exact reproduction, verification commands, required platforms, deliverables and who accepts them. If you require upstream merge for acceptance, that requirement belongs in the quote; a local patch or an open PR is not a substitute. Upstream assignment, contribution, licence and AI policies apply.

Work uses substantial OpenAI Codex assistance. Project requirements for human review are checked before a commitment. Delivery includes the actual test results and material limitations; screen-reader, hardware or platform checks are only claimed when performed.

## Evidence so far

The [UseAgent accessibility sample](README.md) in this repository is an unpaid qualification prototype. Its focused tests, source provenance and outstanding checks are documented. No paid assignment, accepted upstream contribution, customer history or revenue is claimed.

On 19 October 2026, the unchanged Tauri upstream `helloworld` example also built locally at commit `9d0ab831fe38566157e3296ac00fa1b6323e44e4` on arm64 macOS 26.6.1 using Cargo 1.98.1. That is build-toolchain qualification, not a demonstrated Tauri bugfix or older-platform coverage.

For a first conversation, [open a public issue](https://github.com/brodyga45/oss-contribution-proof-2026-10-19/issues/new). An inquiry is not an assignment, and quoted work starts after agreement.
