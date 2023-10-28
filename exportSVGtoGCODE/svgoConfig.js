const pluginConfig = [
    { "cleanupAttrs": false },
    { "removeDoctype": false },
    { "removeXMLProcInst": false },
    { "removeComments": false },
    { "removeMetadata": false },
    { "removeTitle": false },
    { "removeDesc": false },
    { "removeUselessDefs": false },
    { "removeEditorsNSData": false },
    { "removeEmptyAttrs": false },
    { "removeHiddenElems": false },
    { "removeEmptyText": false },
    { "removeEmptyContainers": false },
    { "removeViewBox": false },
    { "cleanupEnableBackground": false },
    { "convertStyleToAttrs": false },
    { "convertColors": false },
    { "convertPathData": false },
    { "convertTransform": true },
    { "removeUnknownsAndDefaults": true },
    { "removeNonInheritableGroupAttrs": false },
    { "removeUselessStrokeAndFill": true },
    { "removeUnusedNS": false },
    { "cleanupIDs": false },
    { "cleanupNumericValues": false },
    { "moveElemsAttrsToGroup": false },
    { "moveGroupAttrsToElems": false },
    { "collapseGroups": false },
    { "removeRasterImages": false },
    { "mergePaths": false },
    { "convertShapeToPath": true },
    { "sortAttrs": false },
    { "removeDimensions": false },
    { "removeAttrs": false }
]

module.exports = { svgoConfig: pluginConfig }