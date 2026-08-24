# Music Downloader

Download audio from a YouTube URL into `~/Music`.

## Prerequisites

Install [Nix](https://nixos.org/download/) with the official multi-user installer:
From the nix OS page (linux install one line installer):
```bash
sudo curl --proto '=https' --tlsv1.2 -L https://nixos.org/nix/install | sh -s -- --daemon
```

Open a new shell after it finishes. Nix needs flakes enabled for this project: `nix run`, `nix develop`, and `./get_music` all depend on them. Check first:

```bash
nix config show experimental-features
```

If that already lists `flakes` and `nix-command`, you are done. If it does not (or the command fails), enable them:

```bash
mkdir -p ~/.config/nix
echo 'experimental-features = nix-command flakes' >> ~/.config/nix/nix.conf
```

The [Determinate Nix installer](https://docs.determinate.systems/determinate-nix) turns flakes on for you. The official installer does not.

You also need Git.

You do **not** need to install `yt-dlp`, `ffmpeg`, or Python yourself. Nix pulls those in when you run the app.

## Run With Modern Nix

Use the wrapper:

```bash
./get_music "https://www.youtube.com/watch?v=6Dh-RL__uN4"
```

It runs this for you:

```bash
nix run . -- -u "https://www.youtube.com/watch?v=6Dh-RL__uN4"
```

The `--` means "send the rest of this command to the script". The wrapper hides that ugly bit.

Note: because this is a Git repo, Nix only sees flake files that are tracked or staged. If `nix run` or `nix develop` cannot see the flake, run:

```bash
git add flake.nix flake.lock
```

## Dev Shell

Use `nix develop` if you want a shell with `yt-dlp`, `ffmpeg`, and Python loaded:

```bash
nix develop
./music_finder.py -u "https://www.youtube.com/watch?v=6Dh-RL__uN4"
exit
```

## Old `nix-shell` Way

This still works, but flakes are the modern Nix style:

```bash
nix-shell --run './music_finder.py -u "https://www.youtube.com/watch?v=6Dh-RL__uN4"'
```

## Difference

`nix run` runs the app. `nix develop` opens a dev shell. `nix-shell` is the older version of that idea.

## YouTube 403 Forbidden

If a download finds the video, then fails with:

```text
ERROR: unable to download video data: HTTP Error 403: Forbidden
```

the URL is fine. YouTube blocked the stream because the `yt-dlp` in this flake is too old. Update the lock and retry:

```bash
nix flake update
./get_music "https://www.youtube.com/watch?v=WGj2RBRltEM"
```

Commit `flake.lock` after it works, or the next clone will keep the old `yt-dlp`. If it still 403s, nixpkgs may not have a new enough `yt-dlp` yet.
