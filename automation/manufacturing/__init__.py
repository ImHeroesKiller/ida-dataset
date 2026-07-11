"""Continuous Knowledge Manufacturing intelligence.

Does not redesign architecture — observes datasets, estimates universe,
scores knowledge gaps, proposes missions, tracks economics & capacity.
"""

from .controller import ManufacturingController, run_manufacturing_cycle
from .targets import load_dynamic_targets, dataset_profile
from .enterprise_functions import (
    run_enterprise_generalization,
    build_enterprise_state,
)

__all__ = [
    "ManufacturingController",
    "run_manufacturing_cycle",
    "load_dynamic_targets",
    "dataset_profile",
    "run_enterprise_generalization",
    "build_enterprise_state",
]
