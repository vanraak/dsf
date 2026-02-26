# dsf/__init__.py
import warnings

warnings.warn(
    "The 'dsf' package is deprecated. Use 'datadepot' instead.",
    DeprecationWarning,
    stacklevel=2,
)

from datadepot import load, dataset_table

__all__ = ["load", "dataset_table"]
