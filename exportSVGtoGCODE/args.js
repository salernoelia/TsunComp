
const settingsGcode = require('./settingsGcode').getSettings()
const yargs = require('yargs')
const args = yargs
    .usage(`Usage: node main.js -f myFile.svg\nInput Folder: ${settingsGcode.inputFolder}\nOutput Folder: ${settingsGcode.exportFolder}`)
    .option('file', {
        alias: 'f',
        description: 'give me a svg file to convert (required)',
        type: 'string',
    })
    .option('travelSpeed', {
        alias: 't',
        description: 'travel speed (no printing)',
        type: 'number',
        default: 3000
    })
    .option('printingSpeed', {
        alias: 'p',
        description: 'speed during printing',
        type: 'number',
        default: 3000
    })
    .option('output', {
        alias: 'o',
        description: 'where to output the converted .gcode file ?',
        type: 'string',
        default: 'output.gcode'
    })
    .option('zOffset', {
        alias: 'z',
        description: 'elevation of the pen when moving (note: during printing Z=0 always)',
        type: 'number',
        default: 10
    })
    .option('useSvgo', {
        alias: 's',
        description: 'use svgo lib to make optimizations, can break some things',
        type: 'boolean',
    })
    .demandOption(['f'])
    .help()
    .alias('help', 'h')
    .argv



module.exports = {
    args: args
}