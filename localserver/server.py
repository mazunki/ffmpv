#!/usr/bin/env python

from flask import Flask, request
import socket, json

app = Flask(__name__)
MPV_SOCKET = "/home/mazunki/.local/state/mpv/socket"


def launch_with_mpv(video_url):
    print("launching")
    command = ["loadfile", f"https://youtube.com/watch?v={video_url}"]
    msg = {"command": command}
    print(msg)
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
        client.connect(MPV_SOCKET)
        client.sendall(json.dumps(msg).encode() + b"\n")
    print("done")


@app.route("/", methods=["POST"])
def run_script():
    try:
        data = request.get_json()
        video_id = data["video_id"]
        print(f"Found path: {video_id}")
        launch_with_mpv(video_id)
        return "OK!"
    except Exception:
        return "Failed to process request", 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8765)
