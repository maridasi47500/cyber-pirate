
	function myFunc(mydiv) {
		// Get the snackbar DIV
		var nom_machine=mydiv.parentElement.parentElement.parentElement.children[1].children[0].children[0].innerHTML;
		myFunction('vous avez activé l\'alerte pour '+nom_machine);
		mydiv.dataset.myalert='on';
		           }
	function myFunction(sometext) {
		// Get the snackbar DIV
		   var x = document.getElementById("snackbar");
		x.innerHTML=sometext;
		
		     // Add the "show" class to DIV
		       x.className = "show";
		
		         // After 3 seconds, remove the show class from DIV
		           setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
		           }

$(function(){
	function secondsToMinutesAndSeconds(totalSeconds) {
		  var minutes = Math.floor(totalSeconds / 60);
		  var seconds = totalSeconds % 60;

		  return {
			      minutes: minutes,
			      seconds: seconds
			    };
	}
	function montempsrestant(min,sec) {
		var temps=45*60;
		  var seconds = temps - (min*60 + sec);

		  return seconds;
	}


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
	var mymachine,item,mydate,thisdate,hrs,minutes,seconds,alertitem,statusitem,selecteurmachinenum;
	var tempsrestant;
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
        selecteurmachinenum=mymachine.children().children("[data-selector='selecteur_machine']");
	selecteurmachinenum.html(item.selecteur_machine);
        mymachine.children().children().children("[data-selector='description']").html(item.nom_type);
        mymachine.children().children("[data-selector='status']").html(item.status);
	mydate=item.date_virtu_off.date;
	thisdate=new Date(new Date() - new Date(mydate));
	hrs=thisdate.getUTCHours();
	minutes=thisdate.getUTCMinutes();
	seconds=thisdate.getUTCSeconds();
	console.log(hrs,minutes,seconds);
	statusitem=mymachine.children().children("[data-selector='status']");
        alertitem=mymachine.children().children().children("[data-selector='alert']");
        if (item.status === "hs"){
        statusitem[0].className="badge bg-danger";
        statusitem.html("hs");
        statusalert.addClass("disabled");
	}else if ((hrs >= 1) || (minutes >= 45 && hrs === 0) || (hrs > 0 && minutes >= 0) || mydate === "None") {

	statusitem[0].className="badge bg-success";
        alertitem.addClass("disabled");
        statusitem.html("libre");
        if (alertitem[0].dataset.myalert==="on") {
        alertitem[0].dataset.myalert="off";
	myFunction("la machine a laver n°"+String(selecteurmachinenum.html())+" a fini son cycle");
	}
	} else if (hrs === 0 && minutes >= 35 && minutes <= 44) {
        alertitem.removeClass("disabled");
        statusitem[0].className="badge bg-info";
        tempsrestant=secondsToMinutesAndSeconds(montempsrestant(minutes, seconds));
        statusitem.html(String(tempsrestant.minutes)+"m"+String(tempsrestant.seconds)+"s");
	} else if (hrs === 0 && minutes < 45 && minutes > 0) {
        statusitem[0].className="badge bg-warning";
        statusitem.html("occupé");
        alertitem.removeClass("disabled");
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
