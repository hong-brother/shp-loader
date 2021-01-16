# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import load_shp
from qgis.core import *

# TODO - https://gis.stackexchange.com/questions/279874/using-qgis3-processing-algorithms-from-standalone-pyqgis-scripts-outside-of-gui/279937
# qgs = QgsApplication([], False)
# QgsApplication.setPrefixPath("C:\OSGEO4~1\apps\qgis", True)
# QgsApplication.initQgis()
# for alg in QgsApplication.processingRegistry().algorithms():
#         print(alg.id(), "->", alg.displayName())

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    load_shp.load('/Users/hsnam/Downloads/CTPRVN_202101/TL_SCCO_CTPRVN.shp')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


