$(function(){
$('.carousel').carousel();
	  function readFile() {
		        if (this.files && this.files[0]) {
				        var FR= new FileReader();
				        FR.onload = function(e) {
						          document.getElementById("mycardpic").src = e.target.result;

						        };
				        FR.readAsDataURL( this.files[0] );
				      }
		      }

	    document.getElementById("addpic").addEventListener("change", readFile, false);

$('form').on('submit', function () {
  if (window.filesize > 1024*5) {
    alert('max upload size is 5k');
return false;
  }
  $.ajax({
    // Your server script to process the upload
    url: $(this).attr("action"),
    type: 'POST',

    // Form data
    data: new FormData($(this)[0]),

    // Tell jQuery not to process data or worry about content-type
    // You *must* include these options!
    cache: false,
    contentType: false,
    processData: false,

    // Custom XMLHttpRequest
    success: function (data) {
	    console.log(JSON.stringify(data))
	    console.log(JSON.stringify(data.redirect))
	    if (data.redirect){
	    window.location=data.redirect;
	    }
},
    error: function (data,error) {
	    console.log(JSON.stringify(data))
},
    xhr: function () {
      var myXhr = $.ajaxSettings.xhr();
      if (myXhr.upload) {
        // For handling the progress of the upload
        myXhr.upload.addEventListener('progress', function (e) {
          if (e.lengthComputable) {
            $('progress').attr({
              value: e.loaded,
              max: e.total,
            });
          }
        }, false);
      }
      return myXhr;
    }
  });
	return false;
  });
  
});
