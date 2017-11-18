
var can = document.getElementById("bar");
var wid = can.width;
var hei = can.height;
var context = can.getContext("2d");
context.fillStyle = "#eeeeee";
context.strokeStyle = "#999999";
context.fillRect(0,0,wid,hei);
var CHART_PADDING = 20;
context.font = "12pt Verdana, sans-serif";
context.fillStyle = "#999999";
context.moveTo(CHART_PADDING,CHART_PADDING);
context.lineTo(CHART_PADDING,hei-CHART_PADDING);
context.lineTo(wid-CHART_PADDING,hei-CHART_PADDING);
var stepSize = (hei - CHART_PADDING*2)/10;
for(var i=0; i<10; i++){
context.moveTo(CHART_PADDING, CHART_PADDING + i* stepSize);
context.lineTo(CHART_PADDING*1.3,CHART_PADDING + i*stepSize);
context.fillText((UB-Step*i).toFixed(0), CHART_PADDING*1.5, CHART_PADDING + i*stepSize + 6);
}
context.stroke();

var elementWidth =(wid-CHART_PADDING*2)/ data.length;
context.textAlign = "center";
for(i=0; i<data.length; i++){
context.fillStyle = data[i].style;
context.fillRect(CHART_PADDING +elementWidth*i ,(hei-CHART_PADDING)-((data[i].value-LB)*stepSize)/Step,elementWidth,((data[i].value-LB)*stepSize)/Step);
context.fillStyle = "rgba(255, 255, 225, 0.8)";
context.fillText(data[i].label, CHART_PADDING+elementWidth*(i+.5), hei-CHART_PADDING*1.5);
}

var can = document.getElementById("bar");
var wid = can.width;
var hei = can.height;
var context = can.getContext("2d");
var CHART_PADDING = 20;
var stepSize = (hei - CHART_PADDING*2)/10;
for(var i=0; i<10; i++){
}
/*
var elementWidth =(wid-CHART_PADDING*2)/ dataL.length;
context.textAlign = "center";
for(i=0; i<dataL.length; i++){
context.fillStyle = dataL[i].style;
context.fillRect(CHART_PADDING*3.4,(hei-CHART_PADDING)-((dataL[i].value-LB)*stepSize)/Step,wid-CHART_PADDING*6.2,5);
context.fillStyle = "rgba(255, 255, 225, 0.8)";
context.fillText(dataL[i].label, CHART_PADDING+elementWidth*(i+.5), hei-CHART_PADDING*1.5);
}
*/
function createBars(context,data){
var elementWidth =(wid-CHART_PADDING*2)/ data.length;
var startY = CHART_PADDING;
var endY = hei-CHART_PADDING;
var chartHeight = endY-startY;
var rangeLength = range.max-range.min;
var stepSize = chartHeight/rangeLength;
context.textAlign = "center";
for(i=0; i<data.length; i++){
context.fillStyle = data[i].style;
context.fillRect(CHART_PADDING +elementWidth*i ,hei-CHART_PADDING- data[i].value*stepSize,elementWidth,data[i].value*stepSize);
context.fillStyle = "rgba(255, 255, 225, 0.8)";
context.fillText(data[i].label, CHART_PADDING
+elementWidth*(i+.5), hei-CHART_PADDING*1.5);	
}	
}
/*
function createLine(context,dataL){
var elementWidth = dataL.length;
var startY = CHART_PADDING;
var endY = hei-CHART_PADDING;
var chartHeight = endY-startY;
var rangeLength = range.max-range.min;
var stepSize = chartHeight/rangeLength;
context.textAlign = "center";
for(i=0; i<dataL.length; i++){
context.fillStyle = dataL[i].style;
context.fillRect(CHART_PADDING +elementWidth*i ,hei-CHART_PADDING- dataL[i].value*stepSize,elementWidth,dataL[i].value*stepSize);
context.fillStyle = "rgba(255, 255, 225, 0.8)";
context.fillText(dataL[i].label, CHART_PADDING + elementWidth*(i+.5), hei-CHART_PADDING*1.5);	
}	
}
*/
