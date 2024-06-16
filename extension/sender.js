

let video_id;


let url = new URL(window.location);
if (url.searchParams.has("v")) {
	video_id = url.searchParams.get("v");
} else {
	let path = url.pathname;
	video_id = path.split("/").filter(p=>p).join("/");
}

let xhr = new XMLHttpRequest();
xhr.onload = function () { console.log(`sent to ffshell: ${video_id}`); };
xhr.onerror = function () { console.log(`couldn't send to ffshell: ${video_id}`); };

xhr.open("POST", "http://127.0.0.1:8765", true);
xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
xhr.responseType = "document";

let data = {
	url: url.toString(),
	video_id: video_id
}

xhr.send(JSON.stringify(data));

