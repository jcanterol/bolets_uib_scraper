#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

_MAP_ATTRIBUTES = {
    'nombre_comun_catalan': 'ca_common_name',
    'nombre_conmun_castellano': 'es_common_name',
    'descripcion': 'description',
    'observaciones': 'additional_info',
    'distribucion_por_islas': 'islands',
    'valor_alimentario': 'edibility',
}


def process_mushroom_df(df_mushrooms):
    """Process mushroom DataFrame"""

    # Modify attributes names
    df_mushrooms = df_mushrooms.rename(columns=_MAP_ATTRIBUTES)

    # Remove duplicate rows
    df_mushrooms.drop_duplicates(inplace=True)

    # Remove rows without scientific name, family or genre
    df_mushrooms.dropna(subset=['scientific_name', 'family', 'genre'], inplace=True)

    # Split multiple elements cells
    df_mushrooms['alternative_scientific_names'] = df_mushrooms['alternative_scientific_names'].str.split(r'\[sep\]')
    df_mushrooms['ca_common_name'] = df_mushrooms['ca_common_name'].str.split(r'\. ')
    df_mushrooms['es_common_name'] = df_mushrooms['es_common_name'].str.split(r'\. ')
    df_mushrooms['islands'] = df_mushrooms['islands'].str.split(r'\. ')
    df_mushrooms['habitat'] = df_mushrooms['habitat'].str.split(r'\. ')
    
    return df_mushrooms
