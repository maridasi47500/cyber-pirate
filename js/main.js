$(function(){
$('.carousel').carousel("cycle");
$('#objet_message').keyup(function(){
$(".objetmonmessage").html($('#objet_message').val().replace(/\n/g,'<br/>'))

});
$('#message_content').keyup(function(){
$(".textemonmessage").html($('#message_content').val().replace(/\n/g,'<br/>'))
});
	$(".mylinks").click(function() {
		        var mylink=$(this)[0];
		        var mybegin=mylink.dataset.begin;
		        var myend=mylink.dataset.end;
		  var textarea=document.getElementById("message_content");
		    var start = textarea.selectionStart;

		  // Obtain the index of the last selected character
		     var finish = textarea.selectionEnd;
		
		         // Obtain the selected text
		             var sel = textarea.value.substring(start, finish);
		                   let first = textarea.value.slice(0, textarea.selectionStart);
		                     let rest = textarea.value.slice(textarea.selectionEnd, textarea.value.length);
		
		                       textarea.value = first + mybegin+myend + rest;
		
		                         // Bonus: place cursor behind replacement
		                                 textarea.focus();
		                                   textarea.selectionStart = (first + mybegin).length;
		                                     textarea.selectionEnd = (first + mybegin).length;
$(".textemonmessage").html($('#message_content').val().replace(/\n/g,'<br/>'))
		
		                                     });
	$(".mycssproprietes").click(function() {
		        var mylink=$(this)[0];
		        var mybegin=mylink.dataset.begin;
		        var myend=mylink.dataset.end;
		  var textarea=document.getElementById("message_content");
		    var start = textarea.selectionStart;

		  // Obtain the index of the last selected character
		     var finish = textarea.selectionEnd;
		
		         // Obtain the selected text
		             var sel = textarea.value.substring(start, finish);
		                   let first = textarea.value.slice(0, textarea.selectionStart);
		                     let rest = textarea.value.slice(textarea.selectionEnd, textarea.value.length);
		
		                       textarea.value = first + mybegin+"valeur"+myend + rest;
		
		                         // Bonus: place cursor behind replacement
		                                 textarea.focus();
		                                   textarea.selectionStart = (first + mybegin).length;
		                                     textarea.selectionEnd = (first + mybegin+"valeur").length;
$(".textemonmessage").html($('#message_content').val().replace(/\n/g,'<br/>'))
		
		                                     });
	$(".monlien").click(function() {
		        var mylink=$(this)[0];
		        var lien=mylink.dataset.lien;
		$.ajax({type:"post",url: lien,success:function(data){
			var mytext=data.text;
		  var textarea=document.getElementById("message_content");
		    var start = textarea.selectionStart;

		  // Obtain the index of the last selected character
		     var finish = textarea.selectionEnd;
		
		         // Obtain the selected text
		             var sel = textarea.value.substring(start, finish);
		                   let first = textarea.value.slice(0, textarea.selectionStart);
		                     let rest = textarea.value.slice(textarea.selectionEnd, textarea.value.length);
		
		                       textarea.value = first + mytext + rest;
		
		                         // Bonus: place cursor behind replacement
		                                 textarea.focus();
		                                   textarea.selectionStart = (first + mytext).length;
		                                     textarea.selectionEnd = (first + mytext).length;
$(".textemonmessage").html($('#message_content').val().replace(/\n/g,'<br/>'))
		}});
		return false;
		
		                                     });

});
