<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="AllStyleCategories" maxScale="0" hasScaleBasedVisibilityFlag="0" minScale="1e+08" version="3.16.1-Hannover">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal enabled="0" mode="0" fetchMode="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <customproperties>
    <property value="false" key="WMSBackgroundLayer"/>
    <property value="false" key="WMSPublishDataSourceUrl"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property value="Value" key="identify/format"/>
  </customproperties>
  <pipe>
    <provider>
      <resampling zoomedOutResamplingMethod="nearestNeighbour" enabled="false" zoomedInResamplingMethod="nearestNeighbour" maxOversampling="2"/>
    </provider>
    <rasterrenderer alphaBand="-1" band="1" opacity="1" type="singlebandpseudocolor" nodataColor="" classificationMin="2" classificationMax="17">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>MinMax</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader maximumValue="17" clip="0" classificationMode="1" labelPrecision="0" minimumValue="2" colorRampType="DISCRETE">
          <item value="1" alpha="255" label="1" color="#8c0000"/>
          <item value="2" alpha="255" label="2" color="#d10000"/>
          <item value="3" alpha="255" label="3" color="#fe0000"/>
          <item value="4" alpha="255" label="4" color="#be4d00"/>
          <item value="5" alpha="255" label="5" color="#ff6500"/>
          <item value="6" alpha="255" label="6" color="#ff9955"/>
          <item value="7" alpha="255" label="7" color="#faee05"/>
          <item value="8" alpha="255" label="8" color="#bcbcbc"/>
          <item value="9" alpha="255" label="9" color="#fecba9"/>
          <item value="10" alpha="255" label="10" color="#555555"/>
          <item value="11" alpha="255" label="11" color="#006900"/>
          <item value="12" alpha="255" label="12" color="#00aa00"/>
          <item value="13" alpha="255" label="13" color="#638424"/>
          <item value="14" alpha="255" label="14" color="#b8db78"/>
          <item value="15" alpha="255" label="15" color="#000000"/>
          <item value="16" alpha="255" label="16" color="#fbf8ae"/>
          <item value="17" alpha="255" label="17" color="#6969fe"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0" gamma="1"/>
    <huesaturation colorizeBlue="128" grayscaleMode="0" colorizeOn="0" colorizeRed="255" colorizeStrength="100" saturation="0" colorizeGreen="128"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
