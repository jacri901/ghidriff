__version__ = '0.4.0'
__author__ = 'clearbluejar'

# Expose API
from .ghidra_diff_engine import GhidraDiffEngine
from .version_tracking_diff import VersionTrackingDiff
from .simple_diff import SimpleDiff
from .structural_graph_diff import StructualGraphDiff
from .__main__ import get_parser, get_engine_classes

__all__ = [
    "GhidraDiffEngine", "SimpleDiff", "StructualGraphDiff", "VersionTrackingDiff", "get_parser", "get_engine_classes"
]
