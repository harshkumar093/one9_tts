from pydub import AudioSegment
import numpy as np

def change_pitch(input_file, output_file, semitones=-4):
    """
    Shifts the pitch of an audio file without affecting the speed.
    - `semitones`: Negative values lower the pitch (female voice), positive values raise it (male voice).
    """
    # Load the audio file
    audio = AudioSegment.from_file(input_file)
    
    # Calculate pitch adjustment factor
    pitch_factor = 2 ** (semitones / 12.0)
    
    # Adjust sample rate for pitch change
    new_sample_rate = int(audio.frame_rate / pitch_factor)
    
    # Resample audio to match the adjusted pitch
    audio = audio._spawn(audio.raw_data, overrides={"frame_rate": new_sample_rate})
    
    # Reset the frame rate back to the original for correct playback speed
    audio = audio.set_frame_rate(audio.frame_rate)
    
    # Export the modified audio
    audio.export(output_file, format="mp3")
    print(f"Converted audio saved to: {output_file}")
