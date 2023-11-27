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
	var mymachine,item;
	$("#nom_laverie").html(data.centrale_nom);
	var machinelist=data.machine_info_status.machine_list;
for (var i = 0;i<machinelist.length;i++){
	item=machinelist[i];
	mymachine=$("[data-machine-id=\""+String(item.selecteur_machine)+"\"]");
	if (mymachine.length > 0){
		mymachine.children("[data-selector='selecteur_machine']").html(item.selecteur_machine);
		mymachine.children("[data-selector='description']").html(item.nom_type);
		mymachine.children("[data-selector='status']").html(item.status);
		if (item.status === "libre"){
		mymachine.children("[data-selector='status']")[0].className="badge badge-success";
		}
	} else {
		mymodelrow.children("[data-selector='selecteur_machine']").html(item.selecteur_machine);
		mymodelrow.children("[data-selector='description']").html(item.nom_type);
		mymodelrow.children("[data-selector='status']").html(item.status);
		if (item.status === "libre"){
		mymodelrow.children("[data-selector='status']")[0].className="badge badge-success";
		}
		$("#list-machines").append(mymodelrow);
	}
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
