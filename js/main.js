$(function(){
const modelrow=$("[data-machine-id='0']");
var mymodelrowstring=modelrow[0].outerHTML;
var mymodelrow=$.parseHTML(mymodelrowstring);
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
	var mymachine,item,mydate,thisdate,hrs,minutes,seconds;
	$("#nom_laverie").html(data.centrale_nom);
	var machinelist=data.machine_info_status.machine_list;

for (var i = 0;i<machinelist.length;i++){
	item=machinelist[i];

	mymachine=$("[data-machine-id=\""+String(item.selecteur_machine)+"\"]");
	if (mymachine.length === 0){

                mymodelrow=$.parseHTML(mymodelrowstring.replace("data-machine-id=\"0\"","data-machine-id=\""+String(item.selecteur_machine)+"\""));
		$("#list-machines").append(mymodelrow);
	        mymachine=$("[data-machine-id=\""+String(item.selecteur_machine)+"\"]");


	}
	console.log(mymachine);
        mymachine.children().children("[data-selector='selecteur_machine']").html(item.selecteur_machine);
        mymachine.children().children().children("[data-selector='description']").html(item.nom_type);
        mymachine.children().children("[data-selector='status']").html(item.status);
	mydate=item.date_virtu_off.date;
	thisdate=new Date(new Date() - new Date(mydate));
	hrs=thisdate.getUTCHours();
	minutes=thisdate.getUTCMinutes();
	seconds=thisdate.getUTCSeconds();
        if (item.status === "hs"){
        mymachine.children().children("[data-selector='status']")[0].className="badge bg-danger";
        mymachine.children().children("[data-selector='status']").html("hs");
        mymachine.children().children().children("[data-selector='alert']").addClass("disabled");
	}else if ((hrs === 0 && minutes <= 0) || mydate === "None") {
        mymachine.children().children("[data-selector='status']")[0].className="badge bg-success";
        mymachine.children().children().children("[data-selector='alert']").addClass("disabled");
        mymachine.children().children("[data-selector='status']").html("libre");
	} else if (hrs === 0 && minutes <= 10 && minutes >= 1) {
        mymachine.children().children().children("[data-selector='alert']").removeClass("disabled");
        mymachine.children().children("[data-selector='status']")[0].className="badge bg-info";
        mymachine.children().children("[data-selector='status']").html(String(minutes)+"m"+String(seconds)+"s");
	} else if (hrs === 0 && minutes < 45 && minutes > 0) {
        mymachine.children().children("[data-selector='status']")[0].className="badge bg-warning";
        mymachine.children().children("[data-selector='status']").html("occupé");
        mymachine.children().children().children("[data-selector='alert']").removeClass("disabled");
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
