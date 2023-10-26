/*eslint no-console: "warn"*/
const path = require("path");

//library is saved locally in ../src
var img2gcode = require("img2gcode");

//progress bar in terminal 
const ProgressBar = require("progress");
var bar = new ProgressBar("Analyze: [:bar] :percent :etas", {
  complete: "#",
  incomplete: ".",
  width: 60,
  total: 100
});

// Path to input img
const imgFile = "/tests/img-and-gcode/woman.jpeg";


const options = {
  toolDiameter: 1.45, //(in mm) Playing with this value gives most interesting results (abstraction/complexity)
  sensitivity: 0.5, // intensity sensitivity (Eyeballing this shit)
  // scaleAxes: 400, // default: image.height equal mm
  feedrate: { work: 1200, idle: 3000 }, // Don't touch this
  deepStep: -1, // default: -1 (Would not touch this)
  // invest: {x:true, y: false},


  laser: {
    commandPowerOn: "M04",
    commandPowerOff: "M05"
  },
  whiteZ: 0, // default: 0
  blackZ: -3,
  safeZ: 2,
  info: "emitter", // ["none" | "console" | "emitter"] default: "none"
  dirImg: path.normalize(__dirname + imgFile)
};

function imgToGCode(options) {
  return new Promise(function (resolve, reject) {
    img2gcode
      .start(options)
      .on("log", str => console.log(str))
      .on("tick", data => bar.update(data))
      .on("error", reject)
      .on("complete", data => {
        // console.log(data.config);
        console.log(data.dirgcode);
        console.log("complete");
      })
      .then(data => {
        // console.log(data.config);
        console.log(data.dirgcode);
        resolve(data);
      });
  });
}
console.time("img2gcode");
// options.dirImg = path.normalize(__dirname + "/img-and-gcode/test.png");
imgToGCode(options).then(() => {
  console.timeEnd("img2gcode");
});
