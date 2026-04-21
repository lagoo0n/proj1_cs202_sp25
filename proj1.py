from dataclasses import dataclass
import math

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

region_conditions = [
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
    lambda1, lambda2 = gr.west_long * (math.pi / 180), gr.east_long * (math.pi / 180)
    phi1, phi2 = gr.lo_lat * (math.pi / 180), gr.hi_lat * (math.pi / 180)

    diff_lambda = lambda2 - lambda1
    if diff_lambda < 0:
        diff_lambda += 2 * math.pi
    return R**2 * abs(diff_lambda) * abs(math.sin(phi2) - math.sin(phi1))

def emissions_per_square_km(rc: RegionCondition) -> float:
    return rc.ghg_rate / area(rc.region.rect)

def densest_helper(rc: list[RegionCondition]) -> RegionCondition:
    if len(rc) == 1:
        return rc[0]
    
    first = rc[0]
    rest = densest_helper(rc[1:])

    first_dens = first.pop / area(first.region.rect)
    res_dens = rest.pop / area(rest.region.rect)  

    if first_dens > res_dens:
        return first
    else:
        return rest

def densest(rc: list[RegionCondition]) -> str:
    if len(rc) == 0:
        return ""
    return densest_helper(rc).region.name

def project_condition(rc: RegionCondition, years: int) -> RegionCondition:
    year = rc.year + years

    if rc.region.terrain == "ocean":
        growth = 1.0001 

    elif rc.region.terrain == "mountains":
        growth = 1.0005 

    elif rc.region.terrain == "forest":
        growth = 0.99999

    else:
        growth = 1.0003 

    return RegionCondition(rc.region, year, int(rc.pop * growth ** years), rc.ghg_rate * growth ** years)