function formatToPercent(val){
 val*=10000;
 val = parseInt(val);
 val/=100;
 return val + "%"
}
var copyStyle = "#0000000000";

function init(){
 var can = document.getElementById("bar");
 wid = can.width;
 hei = can.height;
 var context = can.getContext("2d");
 context.translate(wid/2,hei/2);
 context.shadowOffsetX = 0;
 context.shadowOffsetY = 0;
 context.shadowBlur = 2;
 context.shadowColor = 'rgba(0, 0, 0, 0.5)';
 createPie(context,data1,rad);
 createHole(context,hol);
 context.shadowBlur = 1;
 context.shadowColor = 'rgba(0, 0, 0, 1)';
 context.translate(-35,-55);
 createLegend(context,data1);
}


function createPie(context,data,radius){
 var total=0;
 for(var i=0; i<data.length;i++) total+=data[i].value;
 var rad360 = Math.PI*2;
 var currentTotal=0;
 var midRadian;
 var offset=0;
 for(i=0; i<data.length; i++){
  context.beginPath();
  context.moveTo(0,0);
  context.fillStyle = data[i].style;
  context.stroke();
  context.arc( 0,0,radius,currentTotal/total*rad360,(currentTotal+data[i].value)/total*rad360,false);
  context.lineTo(0,0);
  context.closePath();
  context.fill();
  context.strokeStype = context.fillStyle = copyStyle; 
  midRadian = (currentTotal+data[i].value/2)/total*rad360; 
  context.textAlign = "center"; 
  context.fillStyle = "#000000";
  if(data[i].value/total!=0){
  context.fillText(formatToPercent(data[i].value/total),Math.cos(midRadian)*(radius-35),Math.sin(midRadian)*(radius-35));}
  currentTotal+=data[i].value;
  context.stroke();
 }
}

function createHole(context,radius){
 context.beginPath();
 context.moveTo(0,0);
 context.fillStyle = "#ffffff";
 context.arc( 0,0,radius,0,Math.PI*2,false);
 context.stroke()
 context.closePath();
 context.fill();
}

function createLegend(context,data){
 context.textAlign="left";
 for(var i=0;i<data.length;i++){
 context.fillStyle=data[i].style;
 context.fillText(data[i].label,20,i*20+8);
 }
}

new init();

