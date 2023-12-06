$(function(){
$('.carousel').carousel("cycle");
$('#message_content').keyup(function(){
$(".textemonmessage").html($('#message_content').val().replace(/\n/g,'<br/>'))
});
	$(".mylinks").click(function() {
		        var mylink=$(this)[0];
		        var mybegin=mylink.dataset.begin;
		        var myend=mylink.dataset.end;
		  var textarea=document.getElementById("message_content");
		  var mytext=document.getElementById("mytext");
		    var start = textarea.selectionStart;

		  // Obtain the index of the last selected character
		     var finish = textarea.selectionEnd;
		
		         // Obtain the selected text
		             var sel = textarea.value.substring(start, finish);
		                 var othertext = mytext.innerHTML;
		                   let first = textarea.value.slice(0, textarea.selectionStart);
		                     let rest = textarea.value.slice(textarea.selectionEnd, textarea.value.length);
		
		                       textarea.value = first + mybegin+myend + rest;
		
		                         // Bonus: place cursor behind replacement
		                                 textarea.focus();
		                                   textarea.selectionStart = (first + mybegin).length;
		                                     textarea.selectionEnd = (first + mybegin).length;
		
		                                     });
	$(".mycssproprietes").click(function() {
		        var mylink=$(this)[0];
		        var mybegin=mylink.dataset.begin;
		        var myend=mylink.dataset.end;
		  var textarea=document.getElementById("mytextarea");
		  var mytext=document.getElementById("mytext");
		    var start = textarea.selectionStart;

		  // Obtain the index of the last selected character
		     var finish = textarea.selectionEnd;
		
		         // Obtain the selected text
		             var sel = textarea.value.substring(start, finish);
		                 var othertext = mytext.innerHTML;
		                   let first = textarea.value.slice(0, textarea.selectionStart);
		                     let rest = textarea.value.slice(textarea.selectionEnd, textarea.value.length);
		
		                       textarea.value = first + mybegin+"valeur"+myend + rest;
		
		                         // Bonus: place cursor behind replacement
		                                 textarea.focus();
		                                   textarea.selectionStart = (first + mybegin).length;
		                                     textarea.selectionEnd = (first + mybegin+"valeur").length;
		
		                                     });

});
