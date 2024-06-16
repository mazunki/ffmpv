
# ffmpv

view youtube in mpv instead of through the browser.

steps:
- install extension by loading the manifest through about:debugging. it POSTs to 127.0.0.1:8765
- set up mpv to accept input on an ipc socket
    - `mkdir ${XDG_STATE_HOME}/mpv`
    - launch mpv with `--input-ipc-server=${XDG_STATE_HOME}/mpv/socket`, OR
    - add `input-ipc-server=~~state/socket` in your `${XDG_CONFIG_HOME}/mpv/mpv.conf`, to apply it to all your mpvs
- run the python server locally (it listens to 127.0.0.1:8765 and communicates to mpv ipc socket)

<!-- vim: set sts=4 sw=4 ts=4 expandtab-->

