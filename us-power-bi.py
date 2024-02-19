#!/usr/bin/env python
# coding: utf-8

# source = 'https://ecos.fws.gov/ecp/report/table/critical-habitat.html#:~:text=A-,zip%20file,-containing%20two%20shapefiles' from here you should extract the shp file

# In[3]:


#!pip install  pandas geopandas requests 


# In[ ]:


import pandas as pd
import geopandas as gpd
import requests


# In[37]:


url = '/Users/andrei/Downloads/crithab_all_layers/crithab_poly.shp'

gdf = gpd.read_file(url)


# In[38]:


gdf.columns


# In[39]:


gdf.drop(columns=['unit', 'subunit', 'unitname', 'subunitnam','coopoffice', 'coopofmore', 'fedreg', 'effectdate',
       'vacatedate', 'accuracy','spcode', 'vipcode','leadoffice','source_id','objectid'],inplace = True)


# In[40]:


values_to_exclude = ['Chelonia mydas', 'Etheostoma phytophilum', 'Corvus kubaryi', 'Lepidomeda vittata', 'Catostomus warnerensis', 'Charadrius nivosus nivosus', 'Rana muscosa','Zosterops rotensis']

gdf = gdf[~gdf['sciname'].isin(values_to_exclude)]
gdf


# In[41]:


gdf.drop_duplicates(subset=None, keep='first', inplace=True)
gdf


# In[42]:


list_names = gdf['sciname'].to_list()


# In[29]:


url_img_list = []
for i,row in enumerate(list_names):
    page_title = list_names[i]

    url = 'https://en.wikipedia.org/w/api.php'
    params = {
    'action': 'query',
    'format': 'json',
    'redirects': '1',
    'titles': page_title
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Check if there are redirects
    if 'redirects' in data['query']:
        page_title = redirected_title = data['query']['redirects'][0]['to']

        url = 'https://en.wikipedia.org/w/api.php'
        params = {
        'action': 'query',
        'format': 'json',
        'prop': 'pageimages',
        'piprop': 'original',
        'titles': page_title
        }
        response = requests.get(url, params=params)
        data = response.json()

        page_id = list(data['query']['pages'].keys())[0]
        image_url = data['query']['pages'][page_id].get('original', {}).get('source', None)

        url_img_list.append(image_url)
    elif 'redirects' not in data['query']:
        page_id = list(data['query']['pages'].keys())[0]
        image_url = data['query']['pages'][page_id].get('original', {}).get('source', None)
        url_img_list.append(image_url)
url_img_list


# In[43]:


url_img_list = [None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/8/87/CoquiLlanero.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/2/2f/Noturus_flavipinnis.jpg',
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/7/7e/Gila_intermedia_Gratwicke.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/6/6f/Kiwikiu_perched_in_the_Waikamoi_Forest_Preserve.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/e/ed/Antrobia_culveri.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/f/f5/-conservationlands15_Social_Media_Takeover%2C_July_15th%2C_Wild_and_Scenic_Rivers_%2819701741428%29.jpg',
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/8/87/USFWSOregonSpottedFrogPhoto.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/4/40/Sunflower_sky_backdrop.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/0/0b/Charadrius-melodus-004_edit.jpg',
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/3/35/4803_white_sturgeon_swart_odfw_%284455050144%29.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/b/b5/Woundfin_%28Plagopterus_argentissimus%29.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Marbled_murrelet.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/d/db/Chiricahua_leopard_frog_01.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/4/40/Rio_Grande_silvery_minnow_2.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/b/bc/Notropis_girardi.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/c/ce/California_Tiger_Salamander.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/4/47/Desert_Bighorn_Barna_Cropped.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/6/60/Xyrauchen_texanus.jpg',
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/1/11/California-condor-gymnogyps-californianus-078_%2821196759264%29.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/c/ce/California_Tiger_Salamander.jpg',
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/1/1a/Canada_lynx_by_Michael_Zahra_%28cropped%29.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/0/05/Sierra_Nevada_bighorn_ewes_and_lambs.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/0/0a/Standing_jaguar.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/8/83/Fenders_blue_butterfly_Oregon.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/8/8e/Catostomus_santaanae.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/0/0b/Lasmigona_decorata.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/d/dd/Epioblasma_capsaeformis.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/1/14/Naturalis_Biodiversity_Center_-_ZMA.MOLL.418104_-_Simpsonaias_ambigua_%28Say%2C_1825%29_-_Unionidae_-_Mollusc_shell.jpeg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/5/51/Steller%27s_Eider_%28Polysticta_stelleri%29_%2813667966664%29.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/3/32/Eurycea_waterlooensis.png',
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/e/e1/Haleakalasilversword.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/3/3e/Xylosma_crenatum_%288403048555%29.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/f/f0/Noturus_munitus.jpg',
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/3/31/Male_female_mecularius.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/5/5f/Carolina_Madtom_chilling.jpg',
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/2/2e/Etheostoma_trisella.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/8/82/Bull_trout_fish_salvelinus_confluentus.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/7/71/Necturus_lewisi.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/4/4e/Humpback_chub_-_upper_Colorado_River_cropped.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/e/e7/Arenariaursina.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/f/f8/Florida_bonneted_bat_%28Eumops_floridanus%29.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/3/3a/Northern_red-bellied_cooter_in_Long_Pond.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/9/99/Starr_050407-6232_Vigna_o-wahuensis.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/d/de/Rana_sierrae01.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/9/95/Platanthera_yadonii_146515368.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/0/01/Kadua_st.-johnii_%285490647063%29.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/b/bb/Batrachoseps_relictus.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/4/44/Neostapfia.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/3/39/Spruce_Fir_Moss_Spider.jpg',
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/b/ba/Stygoparnus_comalensis.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/e/eb/Boechera_perstellata.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/2/27/FMIB_34234_Sucker_%28Chasmistes_horus%29.jpeg',
 'https://upload.wikimedia.org/wikipedia/commons/1/1b/Hermes_copper_butterfly_%285559012176%29.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/f/f4/Gopherus_agassizii.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/0/02/Sea_Otter_%28Enhydra_lutris%29_%2825169790524%29_crop.jpg',
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/c/ce/California_Tiger_Salamander.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/9/95/Astragalus_montii.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/6/65/Banded_Dune_Snail_%282647329862%29.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/0/07/CSSS1.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/1/1a/Pacific_marten_Martes_caurina.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/f/f8/Spectacled_Eider_pair.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/b/b8/Anaxyrus_canorus_2.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/8/8a/Threatened_kincaids_lupine_flower.jpg',
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/2/26/Schiedea_trinervis_%285311705034%29.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/0/06/Schiedea_obovata_%286220849808%29.jpg',
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/5/55/Diamond_darter_%28Crystallaria_cincotta%29.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/f/f8/Etheostoma_chermocki.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/b/be/Federally_endangered_Morro_bay_kangaroo_rat%2C_last_documented_in_the_wild_in_1986._%2831045316021%29.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/3/38/Mt._Graham_Red_Squirrel.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/5/59/Tidewater_Goby_-_USFWS4.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/0/0e/Dusky_Gopher_Frog-a.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/6/66/Polar_Bear_-_Alaska_%28cropped%29.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/3/3f/ALbeachmouse1.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/0/03/Sorex_ornatus_relictus.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/2/25/Yellow-shouldered_Blackbird_5_Mike_Morel.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/b/bc/Coastal_California_Gnatcatcher_%285912318877%29.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/8/84/LoxioidesBailleuiKeulemans.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/d/d0/Northern_Spotted_Owl.USFWS.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/d/d0/Northern_Spotted_Owl.USFWS.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/1/13/Eleutherodactylus_jasperi.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/b/bd/Coachella_Valley_Fringe-toed_Lizard.JPG',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/b/bf/San_Marcos_salamander.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/9/9f/Female_guajon_frog_on_tree.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/9/9e/Slender_chub_fish_erimystax_cahni.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/d/d1/Oryzomys_palustris_in_vegetation.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/e/e1/Beautiful_Shiner%2C_juvenile%2C_Cyprinella_formosa.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/a/a1/Salt_Creek_Tiger_Beetle.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/en/5/56/PVBlue.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/9/9c/Bay_Checkerspot_f1.JPG',
 'https://upload.wikimedia.org/wikipedia/commons/c/c5/Branchinecta_conservatio.jpg',
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/8/83/Kentucky_cave_shrimp_%28Palaemonias_ganteri%29_%2812434722624%29.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/7/71/Rana_aurora.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/b/bf/Indiana_Bat_FWS.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/f/f0/Alasmidonta_raveneliana.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/5/51/Erinna_newcombi_color.png',
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/7/74/Crenichthys_baileyi_moapae.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/1/12/Yellowcheek_darter.jpg',
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/c/c5/Adelocosa_anops.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/e/e1/Oahu_Elepaio_%289-19-2017%29_Aiea_Loop_trail%2C_Keaiwa_Heiau_recreation_area%2C_Honolulu_co%2C_Hawaii_-02_%2823717988448%29.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/e/e5/Casey%27s_June_Beetle.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/5/5a/Loxops_caeruleirostris1.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/2/24/Oreomystis_bairdi.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/0/04/Centrocercus_minimus.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/7/7c/Valley_elderberry_longhorn_beetle_FWS.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/f/fb/Percina_jenkinsi.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/1/12/Dipodomys_nitratoides.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/d/da/Houston_toad.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/3/3b/Bonytail_chub_or_bonytail%2C_Gila_elegans.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/d/dc/Arroyo_toad.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/7/7d/Sonora_Chub_imported_from_iNaturalist_photo_32212215_on_21_April_2022.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/2/21/Etheostoma_fonticola.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/b/b7/Gila_purpurea.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/1/17/Ambdrtr.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/5/5d/Percina_pantherina.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/6/66/Dionda_diaboli.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/8/8c/Delistes_luxatus_usgs.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/b/b2/Etheostoma_boschungi.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/4/4c/Capefear1.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/3/3a/Hypomesus_transpacificus.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/1/12/Shortnose_sucker_usgs.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/b/bb/Ameiva_polops_St._Croix_Ground_Lizard.JPG',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/7/74/Crenichthys_baileyi_moapae.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/a/a4/Iguana_sitting_down_looking_to_the_left.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/3/39/Salmo_salar.jpg',
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/9/90/Male_spring_pygmy_Sunfish.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/a/ad/Eurycea_tonkawae_IMG_3631.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/b/ba/Centaurium_namophilum.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/9/9c/Georgetown_salamander.jpg',
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/d/d3/Zapus_hudsonius.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/2/2c/Elfin-woods_warbler_perched_on_a_tree_branch.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/3/34/Coccyzus-americanus-001.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/9/9e/AlabamaCavefish.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/8/8a/Hine%27s_Emerald_Dragonfly_%2841092633930%29.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/9/9c/Chlorogalum_purpureum_var_purpureum_1.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/6/6d/Naturalis_Biodiversity_Center_-_ZMA.MOLL.418089_-_Elliptio_lanceolata_%28Lea%2C_1828%29_-_Unionidae_-_Mollusc_shell.jpeg',
 'https://upload.wikimedia.org/wikipedia/commons/9/99/PinesnakeSaenz_nr-page.jpg',
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/1/15/Vestiaria_coccinea_-Hawaii_-adult-8_%283%29.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/9/98/Fisher_cat_tree.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/f/f9/Etheostoma_nianguae.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/0/0b/Charadrius-melodus-004_edit.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/f/f2/Crocodylus_acutus_mexico_02-edit1.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/b/be/%C4%80kohekohe_%28crested_honeycreeper%29%2C_Haleakala_National_Park_%28bf2b729b-af5a-44ea-b068-c09e166e4bda%29.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/9/99/Manatee_with_calf.PD_-_colour_corrected.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/8/8e/Loggerhead_sea_turtle.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/f/fc/Leatherback_sea_turtle_Tinglar%2C_USVI_%285839996547%29.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/b/b0/Eretmochelys-imbricata-K%C3%A9lonia-2.JPG',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/d/df/Peromyscus_polionotus_ammobates.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/8/84/Peromyscus_polionotus_trissyllepsis.jpg',
 None,
 'https://upload.wikimedia.org/wikipedia/commons/4/4b/Ambystoma_cingulatum_USGS.jpg',
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/2/2b/Mezonevron_kauaiense_%284822011505%29_%282%29.jpg',
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/7/7f/Grus_americana_Sasata.jpg',
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 None,
 'https://upload.wikimedia.org/wikipedia/commons/6/68/Eurasian_wolf_2.jpg',
 'https://upload.wikimedia.org/wikipedia/commons/e/e2/Micronesian_Kingfisher_1644.jpg']


# In[44]:


gdf['url_img'] = url_img_list


# In[45]:


gdf = gdf[gdf['url_img'].notnull()]


# In[46]:


gdf


# In[47]:


#set here the path to geojson wuth states file
states_file = '/Users/andrei/Desktop/DATA ANALISYS/us animals/us_states.json'
states_gdf = gpd.read_file(states_file)
df1 = gdf[['entity_id','sciname','geometry',]]
intersection_gdf = gpd.sjoin(df1, states_gdf, how="inner", predicate='intersects')
#intersection_gdf = intersection_gdf[['sciname','NAME','SHORT','CENSUSAREA']]
#intersection_gdf.rename(columns={'name':'State'},inplace=True)

intersection_gdf.reset_index(inplace=True)
intersection_gdf.drop(columns=['index','geometry','GEO_ID','index_right','LSAD'], inplace=True)
intersection_gdf.drop_duplicates(subset=None, keep='first', inplace=True)
intersection_gdf


# In[48]:


gdf.drop(columns=['geometry','singlmulti','status'], inplace=True)
gdf


# In[51]:


output_file_path = '/Users/andrei/Desktop/DATA ANALISYS/us power bi/main.csv'

# Save the DataFrame to a geojson file
gdf.to_csv(output_file_path)


# In[52]:


output_file_path = '/Users/andrei/Desktop/DATA ANALISYS/us power bi/intersection.csv'

# Save the DataFrame to a geojson file
intersection_gdf.to_csv(output_file_path)


# In[ ]:




