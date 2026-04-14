<<<<<<< HEAD
import librosa
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import random

def create_synced_video(audio_path, video_paths, output_path="final_reel.mp4"):
    # 1. Analyse de la musique
    print("Analyse de l'audio...")
    y, sr = librosa.load(audio_path)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    
    # On définit les points de coupe (on peut sauter des beats pour que ce soit moins épasmodique)
    # Ici, on coupe tous les 4 beats (une mesure en 4/4)
    cut_points = beat_times[::4] 
    
    clips = []
    current_time = 0
    
    print(f"Tempo détecté : {tempo:.2f} BPM")
    print("Montage en cours...")

    # 2. Création des segments vidéo
    for i in range(len(cut_points) - 1):
        start_t = cut_points[i]
        end_t = cut_points[i+1]
        duration = end_t - start_t
        
        # Sélection aléatoire d'une vidéo source (utilisateur ou défaut)
        source_video = random.choice(video_paths)
        
        with VideoFileClip(source_video) as v_clip:
            # On prend un segment aléatoire dans la vidéo source qui fit la durée du beat
            if v_clip.duration > duration:
                start_extract = random.uniform(0, v_clip.duration - duration)
                sub_clip = v_clip.subclip(start_extract, start_extract + duration)
            else:
                sub_clip = v_clip.loop(duration=duration) # Si la vidéo est trop courte
                
            clips.append(sub_clip.set_fps(30))

    # 3. Assemblage final
    final_video = concatenate_videoclips(clips, method="compose")
    final_audio = AudioFileClip(audio_path)
    
    final_video = final_video.set_audio(final_audio.set_duration(final_video.duration))
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")
    print("Terminé !")

# Utilisation
# video_list = ["user_vid1.mp4", "default_vid1.mp4", "default_vid2.mp4"]
=======
import librosa
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import random

def create_synced_video(audio_path, video_paths, output_path="final_reel.mp4"):
    # 1. Analyse de la musique
    print("Analyse de l'audio...")
    y, sr = librosa.load(audio_path)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    
    # On définit les points de coupe (on peut sauter des beats pour que ce soit moins épasmodique)
    # Ici, on coupe tous les 4 beats (une mesure en 4/4)
    cut_points = beat_times[::4] 
    
    clips = []
    current_time = 0
    
    print(f"Tempo détecté : {tempo:.2f} BPM")
    print("Montage en cours...")

    # 2. Création des segments vidéo
    for i in range(len(cut_points) - 1):
        start_t = cut_points[i]
        end_t = cut_points[i+1]
        duration = end_t - start_t
        
        # Sélection aléatoire d'une vidéo source (utilisateur ou défaut)
        source_video = random.choice(video_paths)
        
        with VideoFileClip(source_video) as v_clip:
            # On prend un segment aléatoire dans la vidéo source qui fit la durée du beat
            if v_clip.duration > duration:
                start_extract = random.uniform(0, v_clip.duration - duration)
                sub_clip = v_clip.subclip(start_extract, start_extract + duration)
            else:
                sub_clip = v_clip.loop(duration=duration) # Si la vidéo est trop courte
                
            clips.append(sub_clip.set_fps(30))

    # 3. Assemblage final
    final_video = concatenate_videoclips(clips, method="compose")
    final_audio = AudioFileClip(audio_path)
    
    final_video = final_video.set_audio(final_audio.set_duration(final_video.duration))
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")
    print("Terminé !")

# Utilisation
# video_list = ["user_vid1.mp4", "default_vid1.mp4", "default_vid2.mp4"]
>>>>>>> initial
# create_synced_video("ma_musique.mp3", video_list)