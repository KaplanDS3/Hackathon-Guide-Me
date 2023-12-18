from gtts import gTTS
import os


def read_file_out_loud(file_path):
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Create a gTTS object
        tts = gTTS(text=file_content, lang='en')

        # Save the audio file
        audio_file_path = 'output.mp3'
        tts.save(audio_file_path)

        # Play the audio file using the default audio player
        os.system(f'start {audio_file_path}')

    except Exception as e:
        print(f'An error occurred: {e}')

def red_alart_area():
    file_path = 'red_alart'
    read_file_out_loud(file_path)

def no_red_alart():
    file_path = 'no_red_alart'
    read_file_out_loud(file_path)

def no_shelter_around():
    file_path = 'no_shelter_around_txt'
    read_file_out_loud(file_path)
if __name__ == '__main__':
    # Replace 'your_file.txt' with the path to your text file
    file_path = 'no_shelter_around_txt'
    read_file_out_loud(file_path)

