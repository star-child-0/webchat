$(document).ready(function(){
	msg_fit(document.getElementById("new-msg"));

	$("#overlay").hide();
});

function msg_fit(that){
	that.style.height = "1px";
	that.style.height = 5 + that.scrollHeight + "px";

	goto_last_msg();
}

function goto_last_msg(){
	if (mobileCheck())
		$("#messages").height($(window).height() - $("#textbox").height() - 50);
	else
		$("#messages").height($(window).height() - $("#textbox").height() - 48);
	document.querySelector(".message:last-child").scrollIntoView();
}

$("#attach-btn").click(function(){
	$("#new-msg-file").click();
});

$("#rem-file").on("click", function(){
	clear_img_preview();
});

function clear_img_preview(){
	$("#new-msg-file").val("");
	$("#file-preview").remove();
	$("#filearea").css({"display": "none"});
	goto_last_msg();
}

$("#new-msg-file").on("change", function(){
	if (!this.files[0])
		return ;

	$("#file-preview").remove();
	$("#filearea").css({"display": "flex"});
	var img = document.createElement("img");
	img.id = "file-preview";
	setAttributes(img, {"src": URL.createObjectURL(this.files[0])});
	$("#filearea").append(img);
	goto_last_msg();
});

$("#new-msg").on("keyup", function(){
	if (this.value)
		$("#send-btn").show();
	else
		$("#send-btn").hide();
});

$("#send-btn").click(function(){
	ajax_send_message();
});
