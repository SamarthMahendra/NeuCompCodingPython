class TV:
    def turn_on(self):
        print("TV is turned ON")

    def switch_to_hdmi(self):
        print("TV switched to HDMI mode")

class SoundSystem:
    def turn_on(self):
        print("Sound system is turned ON")

    def set_volume(self, level):
        print(f"Volume set to {level}")

class StreamingService:
    def load_movie(self, movie):
        print(f"Loading {movie} on streaming service...")

    def play(self):
        print("Movie is now playing 🎬")



class HomeTheaterFacade:
    def __init__(self, tv, sound, streaming):
        self.tv = tv
        self.sound = sound
        self.streaming = streaming

    def watch_movie(self, movie):
        print("\n🎬 Setting up your Home Theater...")
        self.tv.turn_on()
        self.tv.switch_to_hdmi()
        self.sound.turn_on()
        self.sound.set_volume(50)
        self.streaming.load_movie(movie)
        self.streaming.play()
        print("🍿 Enjoy your movie!\n")

# Using the Facade
tv = TV()
sound = SoundSystem()
streaming = StreamingService()

home_theater = HomeTheaterFacade(tv, sound, streaming)
home_theater.watch_movie("Inception")  # One call does it all!
