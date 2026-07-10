"""GitHub Actions / CI automation tools for the IDA Dataset repository.

Exit codes (shared contract):
  0 — Success
  1 — Validation error
  2 — Configuration error
  3 — Policy violation
  4 — Publisher blocked
"""

EXIT_SUCCESS = 0
EXIT_VALIDATION_ERROR = 1
EXIT_CONFIG_ERROR = 2
EXIT_POLICY_VIOLATION = 3
EXIT_PUBLISHER_BLOCKED = 4

__all__ = [
    "EXIT_SUCCESS",
    "EXIT_VALIDATION_ERROR",
    "EXIT_CONFIG_ERROR",
    "EXIT_POLICY_VIOLATION",
    "EXIT_PUBLISHER_BLOCKED",
]
