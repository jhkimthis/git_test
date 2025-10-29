# from pytube import YouTube
# from pydub import AudioSegment
# import os

# def download_youtube_audio(url, output_folder="downloads"):
#     try:
#         # 유튜브 동영상 다운로드
#         yt = YouTube(url)
#         audio_stream = yt.streams.filter(only_audio=True).first()
        
#         if not os.path.exists(output_folder):
#             os.makedirs(output_folder)
        
#         print(f"Downloading: {yt.title}")
#         audio_file = audio_stream.download(output_folder)
        
#         # 파일 확장자 변환 (mp4/webm -> mp3)
#         base, ext = os.path.splitext(audio_file)
#         mp3_file = base + ".mp3"
        
#         audio = AudioSegment.from_file(audio_file)
#         audio.export(mp3_file, format="mp3")
        
#         # 원본 오디오 파일 삭제
#         os.remove(audio_file)
        
#         print(f"Converted to MP3: {mp3_file}")
#         return mp3_file
    
#     except Exception as e:
#         print(f"Error: {e}")
#         return None

# if __name__ == "__main__":
#     # video_url = input("Enter YouTube URL: ")
#     video_url = 'www.youtube.com/watch?v=XGxGAjsG0Pg'
#     download_youtube_audio(video_url)


from pytube import YouTube
import os
# from moviepy.editor import *
# from moviepy import *

def download_youtube_audio(url, output_path="."):
    # YouTube 객체 생성
    yt = YouTube(url)
    
    # 가장 높은 품질의 오디오 스트림 선택
    audio_stream = yt.streams.filter(only_audio=True).first()
    
    # 오디오 다운로드
    print(f"Downloading: {yt.title}...")
    audio_file = audio_stream.download(output_path=output_path)
    
    # 파일 확장자를 mp3로 변경
    base, ext = os.path.splitext(audio_file)
    new_file = base + '.mp3'
    os.rename(audio_file, new_file)
    
    print(f"Download complete: {new_file}")
    return new_file

# YouTube 동영상 URL
youtube_url = input("Enter YouTube URL: ")

youtube_url = input("Enter YouTube URL2: ")

# 여기에 추가로 변경함
yt = YouTube(url)
print(f"Download complete: {new_file}")

print(f"Download complete: {new_file}")
print(f"Download complete: {new_file}")
