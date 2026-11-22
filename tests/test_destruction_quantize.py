import pytest
import gameplay.destruction_quantize as mod

CASES = [
    ("fixed_point", (0.001, 2)),
    ("keyframe_sync", (1, 2)),
    ("tolerance_converge", (0.01, 0.02)),
    ("float_drift", (1, 2)),
    ("server_authority", (1, 2)),
    ("replay_verify", (1, 2)),
    ("suspension_detect", (1, 2)),
    ("snapshot_interval", (10, 2)),
    ("quantize_scale", (1000, 2)),
    ("position_apply", (1, 2)),
    ("collision_resync", (1, 2)),
    ("desync_policy", (1, 2)),
    ("piece_id", (1, 2)),
    ("mass_inherit", (1, 2)),
    ("drift_metric", (1.0, 2.0)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
