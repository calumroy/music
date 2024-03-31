{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.youtube-dl
    pkgs.yt-dlp
    pkgs.ffmpeg  # Add the new package
    pkgs.python312  # pYthon version 3.12
  ];
}