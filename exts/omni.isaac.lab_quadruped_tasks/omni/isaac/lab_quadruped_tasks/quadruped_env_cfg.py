from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class MotorGains:
    kp: float = 20.0
    kd: float = 0.5

@dataclass
class QuadrupedRobotCfg:
    usd_path: str | None = None
    urdf_path: str | None = None
    base_link: str = "base"
    foot_links: List[str] = field(default_factory=lambda: ["FL_foot", "FR_foot", "RL_foot", "RR_foot"])
    default_gains: MotorGains = field(default_factory=MotorGains)
    friction: float = 0.9
    restitution: float = 0.0

@dataclass
class LocomotionTaskCfg:
    episode_length_s: float = 20.0
    control_dt_s: float = 0.02
    target_forward_velocity_mps: float = 0.5
    reward_weights: Dict[str, float] = field(default_factory=lambda: {
        "forward": 1.0, "energy": 0.01, "stability": 0.5
    })
    use_flat_ground: bool = True
    ground_friction: float = 1.0