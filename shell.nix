{ pkgs ? import <nixpkgs> {} }:

let
  unstable = import (fetchTarball "https://nixos.org/channels/nixpkgs-unstable/nixexprs.tar.xz") {};
in

pkgs.mkShell {
  buildInputs = [
    unstable.yt-dlp  # Use yt-dlp from unstable instead of youtube-dl
    pkgs.ffmpeg
    pkgs.python312
  ];
}