from dataclasses import dataclass
@dataclass(frozen=True)

class GlobeRect:
    lo_lat: float
    hi_lat: float
    west_long: float
    east_long: float

class Region:
    rect: GlobeRect
    name: str
    terrain: str # e.g. "ocean", "mountain", "forest", "other"

class RegionCondition:
    region: Region
    year: int
    pop: int
    ghg_rate: float # tons of CO2 per year
