import pygame
import os
import random
import sys
import multiprocessing as mp


# Initialize the pygame  
pygame.init()

# Music Folder Path
MUSIC_FOLDER = "W music"
WINDOW_TITLE = "Music Player"
WINDOW_WIDTH = pygame.display.Info().current_w 
WINDOW_HEIGHT = pygame.display.Info().current_h
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)
fullscreen = False

# Make the record player screen f11 full screen
def toggle_fullscreen():
    global fullscreen, screen
    if fullscreen:
        # Switch to windowed mode
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        fullscreen = False
    else:
        # Switch to fullscreen mode
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        fullscreen = True

# Loads the music folder
def load_music_files(folder):
    # Supported formats
    # Load Music Files
    SUPPORTED_FORMATS = (".mp3", ".wav", ".ogg")
    if not os.path.exists(folder):
          print(f"Error: '{folder}' directory not found!")
          return
    music_files = [f for f in os.listdir(folder) if f.endswith(SUPPORTED_FORMATS)]
    return music_files

# Play the selected song
def play_song(song_path):
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

# Function to display available songs
def display_songs(song_list):
    print("\nAvailable Songs:")
    for idx, song in enumerate(song_list):
        print(f"{idx + 1}. {song}")

def music_player():
     global fullscreen
     angle = 0
     clock = pygame.time.Clock()
     record = pygame.image.load("record.png").convert_alpha() # Path to record.png on your computer which will be in "Image assets"
     background = pygame.image.load("background.jpg").convert() # Path to background.jpg on your computer, also in "Image assets"
     record_rect = record.get_rect()
     running = True
 
     songs = load_music_files(MUSIC_FOLDER)

     if not songs:
          print("No music files found in the folder!")
          return
     
     current_index = 0
     display_songs(songs)

     playing = False
     toggle_fullscreen()

     while running:  
          screen.blit(background, (0, 0))
          
          rotated_record = pygame.transform.rotate(record, angle)
          record_rect = rotated_record.get_rect(center=record_rect.center)

          screen.blit(rotated_record, record_rect.topleft)

          pygame.display.flip()
          
          if playing == True:
               angle -= 1

          else: 
               angle -= 0

          angle %= 360 
          
          clock.tick(110)

          for event in pygame.event.get():

               if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_r:
                         current_index = random.randint(0, len(songs) - 1)
                         song_path = os.path.join(MUSIC_FOLDER, songs[current_index])
                         play_song(song_path)
                         playing = True
                         print(f"Now Playing: {songs[current_index]} 🎶")

                    elif event.key == pygame.K_SPACE:
                         if playing == True:
                              pygame.mixer.music.pause()
                              print("Music paused.")
                              playing = False
 
                         elif playing == False:
                              pygame.mixer.music.unpause()
                              print("Music resumed.")
                              playing = True

                    elif event.key == pygame.K_1:
                         pygame.mixer.music.rewind()
                         print("Music rewinded to the beginning.")

                    elif event.key == pygame.K_RIGHT:
                         current_index = (current_index + 1) % len(songs)
                         song_path = os.path.join(MUSIC_FOLDER, songs[current_index])
                         play_song(song_path)
                         print(f"Skipped to: {songs[current_index]}")

                    elif event.key == pygame.K_LEFT:
                         current_index = (current_index - 1) % len(songs)
                         song_path = os.path.join(MUSIC_FOLDER, songs[current_index])
                         play_song(song_path)
                         print(f"Previous song: {songs[current_index]}")

                    else:
                         print("Invalid command. Please try again.")


if __name__ == "__main__":
     music_player()
     


