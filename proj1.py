from dataclasses import dataclass
from math import sin

@dataclass(frozen=True)
class GlobeRect:
    lo_lat: float
    hi_lat: float
    west_long: float
    east_long: float

@dataclass(frozen=True)
class Region:
    rect: GlobeRect
    name: str
    terrain: str # e.g. "ocean", "mountain", "forest", "other"

@dataclass(frozen=True)
class RegionCondition:
    region: Region
    year: int
    pop: int
    ghg_rate: float # tons of CO2 per year

region_condition = [
    RegionCondition(Region(GlobeRect(40.4, 41.4, -74.0, -73.0), "New York Metro", "other"), 2025, 20000000, 50000000.0),
    RegionCondition(Region(GlobeRect(41.7, 42.1, 12.3, 12.7), "Rome Metro", "other"), 2025, 4000000, 10000000.0),
    RegionCondition(Region(GlobeRect(5.0, 35.0, 120.0, 150.0), "Ring of Fire", "ocean"), 2025, 1000000, 1000000.0),
    RegionCondition(Region(GlobeRect(35.0, 35.6, -120.9, -120.2), "San Luis Obispo", "other"), 2025, 300000, 500000.0)
]

def emissions_per_capita(rc: RegionCondition) -> float:
    if rc.pop == 0:
        return 0.0
    return rc.ghg_rate / rc.pop

def area(gr: GlobeRect) -> float:
    R = 6378.1
    lamda1, lamda2 = gr.west_long * (3.14159 / 180), gr.east_long * (3.14159 / 180)
    phi1, phi2 = gr.lo_lat * (3.14159 / 180), gr.hi_lat * (3.14159 / 180)
    return R**2 * abs(lamda2 - lamda1) * abs(sin(phi2) - sin(phi1))