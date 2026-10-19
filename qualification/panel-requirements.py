import io
import json
import hashlib
import inspect
import platform
import panel as pn
from panel.io.mime_render import find_requirements
from panel.io.convert import collect_python_requirements

cases = {
    "namespace_imports": "import plaidcloud.rpc\nimport plaidcloud.utilities",
    "namespace_from": "from plaidcloud.rpc import api\nfrom plaidcloud.utilities import helpers",
    "stdlib_control": "import sys\nimport json",
    "ignored_pil_control": "from PIL import Image",
    "known_alias_control": "import sklearn",
}
results = [{"case": name, "input_code": code, "inferred": find_requirements(code)} for name, code in cases.items()]
explicit = collect_python_requirements(io.StringIO(cases["namespace_imports"]), requirements=["plaidcloud-rpc", "plaidcloud-utilities"])
print(json.dumps({"panel": pn.__version__, "python": platform.python_version(), "scope": "Dependency inference only; imported namespace code is parsed but never executed; no PlaidCloud app, credentials, converter output or browser runtime tested; no patch", "find_requirements_source_sha256": hashlib.sha256(inspect.getsource(find_requirements).encode()).hexdigest(), "cases": results, "explicit_requirements_result": explicit}, indent=2))
