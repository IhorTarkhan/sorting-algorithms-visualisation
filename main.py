import pygame as pg
from UI.Visualization import MainVisual
from UI.Extract_results import Extract_Results

results = Extract_Results()

pg.init()
ui = MainVisual(results)
ui.run()
pg.quit()

# ANDRUHUS, PLEASE FORMAT CODE - ctrl + l
# Bitte schön
