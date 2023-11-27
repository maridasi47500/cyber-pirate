$(function(){
const modelrow=$("[data-machine-id='0']");
var mymodelrow=$.parseHTML(modelrow.html());
modelrow.hide();
setInterval(function(){ 
    //code goes here that will be run every 5 seconds.    
	var formData = new FormData(); // Formulaire vide à cet instant
	formData.append("myid", $("#myid").html());
$.ajax({
type:"post",url:"/machinealaver",
	data:formData,
	   cache: false,
	    contentType: false,
	    processData: false,

success:function(data){
for (var i = 0;i<data.length;i++){
//hey
//mymodelrow.children("").html("");
/*
 * si le temps est inférieur à 10 minutes
 * afficher le temps avec badge-info
 * si la machine a laver est libre
 * afficher le temps avec badge-success
 * si la machine a laver est occupee
 * afficher le temps avec badge-warning
 * si la machine a laver est hs
 * afficher le temps avec badge-dager
 */
}
}
});
}, 1000);
});
