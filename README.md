# sample-library

Scripts for generating a structured sample library with Python

Requires Docker

## about

Samples are written to wave files in `lib/`.

Different collections are written in folders `lib/foo_collection/*.wav`.

Currently generates collections of basic waveforms for a list of notes `data/notes.json`.

## how-to

Run `make it` to build the Dockerized environment and open an interactive shell, then run `make main` to generate samples in `lib/`.

## requirements

Generate samples of audio

Write audio as a wav file in `$PWD/lib/foo.wav`

## resources

https://pythonaudio.blogspot.com/2014/04/4-writing-wav-file-1.html
