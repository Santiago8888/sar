var wid;
var hei;
var copyStyle = "#0000000000";
var radius = mod;
var radianOffset = Math.PI/2

function init(){
var can = document.getElementById("bar");
wid = can.width;
hei = can.height;
var context = can.getContext("2d");
createSpider(context,chartInfo,data);
}

function createSpider(context,chartInfo,data){
drawWeb(context,chartInfo,radius);
drawDataWeb(context,chartInfo,data,radius);
}

function drawWeb(context,chartInfo,radius){
chartInfo.stepSize = chartInfo.max/chartInfo.steps;
var hSteps = chartInfo.types.length;
var hStepSize = (Math.PI*2)/hSteps;
context.translate(wid/2,hei/2);
context.strokeStyle = "#aaaaaa";
context.textAlign="center";
for(var i=0; i<hSteps; i++){
context.moveTo(0,0);
context.lineTo(Math.cos(hStepSize*i + radianOffset)*(radius+20),Math.sin(hStepSize*i + radianOffset)*(radius+20));
context.fillText(chartInfo.types[i],Math.cos(radianOffset)*(radius+30),Math.sin( radianOffset)*(radius+30));
context.rotate(hStepSize);
}

var stepSize = radius/chartInfo.steps;
var cRad;
for(var i=1; i<=chartInfo.steps; i++){
cRad = i*stepSize;
context.moveTo(Math.cos(radianOffset)*cRad,
Math.sin(radianOffset)*cRad);
for(var j=0;j<hSteps; j++){
context.lineTo(Math.cos(hStepSize*j + radianOffset)*cRad,Math.sin(hStepSize*j + radianOffset)*cRad);
}
context.lineTo(Math.cos(radianOffset)*cRad,
Math.sin(radianOffset)*cRad);
}
context.lineWidth = 1;
context.stroke();
}

function drawDataWeb(context,chartInfo,data,radius){
var hSteps = chartInfo.types.length;
var hStepSize = (Math.PI*2)/hSteps;
for(i=0; i<data.length; i++){
context.beginPath();
context.strokeStyle = data[i].style;
context.lineWidth=3;
cRad =radius*(data[i][chartInfo.types[0]]/chartInfo.max);
context.moveTo(Math.cos(radianOffset)*cRad,Math.sin(radianOffset)*cRad);
for(var j=1;j<hSteps; j++){
cRad =radius*(data[i][chartInfo.types[j]]/chartInfo.max);
context.lineTo(Math.cos(hStepSize*j +radianOffset)*cRad,Math.sin(hStepSize*j +radianOffset)*cRad);
}
cRad =radius*(data[i][chartInfo.types[0]]/chartInfo.max);
context.lineTo(Math.cos(radianOffset)*cRad,Math.sin(radianOffset)*cRad);
context.stroke();
}
}


var c=document.getElementById("bar");
var context=c.getContext("2d");
context.beginPath();
context.lineWidth = 3;
context.arc(mad,mad,med,0,2*Math.PI);
context.strokeStyle = "#ffff00";
context.stroke()

