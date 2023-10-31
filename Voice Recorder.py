import tkinter as tk
import sounddevice as sd
import numpy as np
import wave
import os

class VoiceRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Recorder")

        self.is_recording = False
        self.frames = []

        self.record_button = tk.Button(root, text="Start Recording", width=20, command=self.toggle_recording)
        self.record_button.pack(pady=10)

        self.save_button = tk.Button(root, text="Save Recording", state="disabled", width=20, command=self.save_recording)
        self.save_button.pack(pady=10)

    def toggle_recording(self):
        if not self.is_recording:
            self.is_recording = True
            self.record_button.config(text="Stop Recording")
            self.frames = []
            sd.stream(callback=self.audio_callback)
        else:
            self.is_recording = False
            self.record_button.config(text="Start Recording")
            sd.stop()

            self.save_button.config(state="normal")

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(status, flush=True)
        if self.is_recording:
            self.frames.append(indata.copy())

    def save_recording(self):
        filename = "recorded_audio.wav"
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(44100)
            wf.writeframes(b''.join(self.frames))

        self.save_button.config(state="disabled")
        self.frames = []
        print(f"Recording saved as {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceRecorder(root)
    root.mainloop()
