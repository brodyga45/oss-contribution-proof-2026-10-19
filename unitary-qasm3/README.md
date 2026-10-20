# OpenQASM round-trip feasibility probe

**Proposal evidence, not a funded or completed project.** Codex prepared this material with the account owner's authorization. No quantum research background, paid quantum delivery history, maintainer endorsement, accepted fix or guaranteed adoption is claimed.

The related report is [qiskit-qasm3-import #58](https://github.com/Qiskit/qiskit-qasm3-import/issues/58). This folder contains only three original one-qubit RX examples and two importer calls per example, not the proposed thirty-case corpus.

## Actual local result

Environment: Qiskit 2.6.0, qiskit-qasm3-import 0.6.0, OpenQASM3 1.0.1, Python 3.14.8, macOS arm64.

| Example | Standard importer | Experimental native importer |
| --- | --- | --- |
| Numeric RX(0.25) | Imports | Imports |
| Symbolic RX(1/theta) | Imports | Rejects input declaration |
| Symbolic RX(1/(theta**2)) | Rejects unsupported binary operation | Parsing error |

Imported cases preserve the parameter-name list and are equivalent in the SDK's operator comparison at theta=2.0, up to global phase. **One binding is not proof of general symbolic equivalence.** There is no claim about measurements, dynamic control, larger circuits or quantum hardware.

Run from this directory in an isolated environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python reproduce.py
```

The probe catches importer exceptions to write a diagnostic report; exit code zero does not mean all examples imported successfully. See [reproduction-result.json](reproduction-result.json).

## Video proposal

[Watch the 110-second proposal](proposal-video.mp4) or read the [transcript](transcript.txt). Speech is synthetic; no human appearance or interview is represented. The video describes a conditional USD4,000, three-month microgrant proposal.

If funded and agreed, the planned scope is up to thirty original fixtures, two version targets, a CPU-only runner/CI, an explicit supported/unsupported matrix, two further compatibility runs, and handover. A targeted upstream patch depends on maintainer agreement and any required owner-reviewed CLA. This is not another parser and no patch has been implemented.

[render_video.py](render_video.py) documents generation using Pillow, FFmpeg, system fonts and the built-in macOS Samantha voice; those binaries/font files are not redistributed. [video-verification.json](video-verification.json) records media metadata.

This independently authored preflight is MIT-licensed under its own LICENSE file. The repository root license is retained for the other material; no UseAgent source is used here. The funded corpus was proposed under Apache-2.0; it has not been commissioned or delivered. No cloud account, wallet, paid resource or quantum hardware was used for this probe.

