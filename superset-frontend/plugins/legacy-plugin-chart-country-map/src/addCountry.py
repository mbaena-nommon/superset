#!/usr/bin/python

"""
 Module description:
"""

__author__ = 'mbaena'
__copyright__ = '(c) Nommon 2023'

import pandas as pd
import geojson
import geopandas as gpd
import json
import os

def run():
    zoning_path = r"C:\Users\mbaena\PycharmProjects\travelint-visualisation\data\study_zoning\study_zoning_4326.geojson"
    study_zoning = 'palma_municipios'

    study_zoning_gdf = read_geojson(zoning_path)

    iso_column = 'ID'
    name_column = 'ID'

    save_geojson(study_zoning, study_zoning_gdf,iso_column,name_column)

def read_geojson(zoning_path):
    study_zoning_gdf = gpd.read_file(zoning_path)
    study_zoning_gdf = study_zoning_gdf[['ID', 'geometry']]

    return study_zoning_gdf


def save_geojson(study_zoning, study_zoning_gdf, iso_column, name_column):
    useful_columns = ["ISO", "NAME_1", "geometry"]

    # For backward compatibility
    study_zoning_gdf["ISO"] = study_zoning_gdf[iso_column]
    study_zoning_gdf["NAME_1"] = study_zoning_gdf[name_column]

    print(f'Saving geojson for {study_zoning}...')
    study_zoning_gdf[useful_columns].to_file(f"countries/{study_zoning}.geojson",
                                             driver="GeoJSON")

def modify_countruies_file(study_zoning):
    with open('countries.ts', 'r') as file:
        data = file.read()

    add_line = "import {} from './countries/{}.geojson';".format(study_zoning)

    add_after_line = "export const countries = {"

if __name__ == '__main__':
    run()
