$(document).ready(function(){
	msg_fit(document.getElementById("new-msg"));

	$("#overlay").hide();
});

function msg_fit(that){
	that.style.height = "1px";
	that.style.height = 5 + that.scrollHeight + "px";
	$("#messages").height($(window).height() - $("#textbox").height() - 70);
	document.querySelector(".message:last-child").scrollIntoView();
}