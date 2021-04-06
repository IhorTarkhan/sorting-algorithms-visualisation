import pygame as pg

from UI.Extract_results import Extract_Results
from UI.Visualization import MainVisual
from calculation.db.sorting_logs_connector import create_table_if_not_exist

create_table_if_not_exist()

results = Extract_Results()

pg.init()
ui = MainVisual(results)
ui.run()
pg.quit()

# ANDRUHUS, PLEASE FORMAT CODE - ctrl + l
# Bitte schön
