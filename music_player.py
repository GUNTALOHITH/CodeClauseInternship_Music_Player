import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playlist = []
        self.current_song_index = 0

    def add_to_playlist(self, folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".mp3"):
                song_path = os.path.join(folder_path, filename)
                self.playlist.append(song_path)

    def play(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        pygame.mixer.music.load(self.playlist[self.current_song_index])
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

    def next_song(self):
        self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
        self.play()

# Example usage
player = MusicPlayer()
player.add_to_playlist("/path/to/your/music/folder")
player.play()
