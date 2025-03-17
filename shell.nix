{ pkgs ? import <nixpkgs> {} }:

let
  unstable = import (fetchTarball "https://nixos.org/channels/nixpkgs-unstable/nixexprs.tar.xz") {};
in

pkgs.mkShell {
  buildInputs = [
    pkgs.youtube-dl
    unstable.yt-dlp  # Use yt-dlp from unstable
    pkgs.ffmpeg
    pkgs.python312
  ];
}