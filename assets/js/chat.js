$(document).ready(function(){
	msg_fit(document.getElementById("new-msg"));
});

function msg_fit(that){
	that.style.height = "1px";
	that.style.height = 5 + that.scrollHeight + "px";
	if (mobileCheck())
		$("#messages").height($(window).height() - $("#textbox").height() - 70);
	else
		$("#messages").height($(window).height() - $("#textbox").height() - 48);
	document.querySelector(".message:last-child").scrollIntoView();
}
