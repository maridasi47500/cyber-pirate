$(function(){
const modelrow=$("[data-machine-id='0']");
var mymodelrow=$.parseHTML(modelrow.html());
modelrow.hide();
setInterval(function(){ 
    //code goes here that will be run every 5 seconds.    
$.ajax({
type:"post",url:"/machinealaver",
success:function(data){
for (var i = 0;i<data.length;i++){
//hey
mymodelrow.children("").html("");
}
}
});
}, 1000);
});
