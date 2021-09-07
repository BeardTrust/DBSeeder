#!/usr/bin/python3


streets = """Seacoast Lane
Crystal Lane
Stone Street
Green Avenue
Gray Lane
Wetland Street
Tower Street
Hill Street
Union Street
Rosemary Lane
Boulder Lane
Sycamore Lane
Paradise Avenue
Nightingale Way
Brown Street
Parkside Route
Bell Avenue
Harbor Route
Brewer Way
Pioneer Lane
Auburn Row
Railway Passage
Coral Lane
Cliff Street
Pebble Way
Arch Boulevard
Moon Row
Anchor Avenue
Temple Row
Smith Route
Farmer Way
Lilypad Passage
Acorn Avenue
Granite Street
Quarry Row
Mandarin Boulevard
Barley Way
Poplar Avenue
Aviation Avenue
Greenfield Boulevard
"""

cities = ['Winchester', 'Vernon', 'Smithville', 'Davis', 'Waltham',
          'Maryville', 'Hampton', "Aachen", "Rome", 'Carthage']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA',
          'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK',
          'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']


def get_cities():
    return cities


def get_states():
    return states


def get_streets():
    return streets.replace('\n    ', '').split('\n')
