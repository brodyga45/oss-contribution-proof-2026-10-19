"""Bounded feasibility probe; not a fix or the proposed funded corpus."""
import importlib.metadata as md
import json
import platform
from pathlib import Path
import warnings

from qiskit import QuantumCircuit, qasm3
from qiskit.circuit import Parameter
from qiskit.quantum_info import Operator

def run():
    cases = [("numeric_quarter", 0.25), ("symbolic_inverse", "inverse"),
             ("symbolic_inverse_square", "inverse_square")]
    rows = []
    for name, expression in cases:
        circuit = QuantumCircuit(1)
        theta = Parameter("theta")
        angle = 1 / theta if expression == "inverse" else (
            1 / (theta ** 2) if expression == "inverse_square" else expression)
        circuit.rx(angle, 0)
        source = qasm3.dumps(circuit)
        for importer_name in ["loads", "loads_experimental"]:
            row = {"case": name, "importer": importer_name, "qasm": source}
            try:
                with warnings.catch_warnings(record=True) as seen:
                    warnings.simplefilter("always")
                    restored = getattr(qasm3, importer_name)(source)
                row["warnings"] = [str(x.message) for x in seen]
                before = sorted(p.name for p in circuit.parameters)
                after = sorted(p.name for p in restored.parameters)
                row["parameters_before"] = before
                row["parameters_after"] = after
                row["parameter_names_preserved"] = before == after
                bound_original = circuit.assign_parameters(
                    {p: 2.0 for p in circuit.parameters})
                bound_restored = restored.assign_parameters(
                    {p: 2.0 for p in restored.parameters})
                row["equivalent_at_theta_2_up_to_global_phase"] = Operator(
                    bound_original).equiv(Operator(bound_restored))
                row["status"] = "imported"
            except Exception as exc:
                row["status"] = "error"
                row["error_type"] = type(exc).__name__
                row["error"] = str(exc)
            rows.append(row)
    report = {"scope": "three one-qubit RX cases; one numeric binding; no fix",
              "python": platform.python_version(), "platform": platform.platform(),
              "versions": {p: md.version(p) for p in [
                  "qiskit", "qiskit-qasm3-import", "openqasm3", "numpy"]},
              "rows": rows,
              "limits": ["not a comprehensive corpus", "no quantum hardware",
                         "no measurement or dynamic-control equivalence",
                         "no upstream submission or acceptance",
                         "one binding is not proof of symbolic equivalence"]}
    Path("reproduction-result.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    run()

