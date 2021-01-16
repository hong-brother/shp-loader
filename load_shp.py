from qgis.core import (
    QgsVectorLayer
)

def load(path):
    try:
        layer = QgsVectorLayer(path, "LINKSHAPE_01", "ogr")
        print("layer name = " + layer.sourceName())
        print("layer count = " + str(layer.featureCount()))
        ## Create field
        # layer_provider = LINKSHAPE_01_Layer.dataProvider()
        # layer_provider.addAttributes([QgsField("Link_Cate", QVariant.String)])
        # layer.updateFields()
        for row in layer.getFeatures():
            print(row.attributes())
    except Exception as e:
        print(e)


