import sys
import asyncio
import subprocess
import time
from typing import Optional

from core.assistant import JarvisAssistant
from add_modules import ConversationHandler
from modules.vocalize.async_edgetts import textToSpeechBytes, AudioPlayer
from modules.sqlqueue import SqlQueue
from util.jarvis.main import process, JFunction, codeBrew, historyDb
from modules.prompt.base import Role

# Constants
IMPORTS_SOUND = r"data\audio\imports.wav"
AFTER_IMPORTS_SOUND = r"data\audio\after_imports.wav"
SR = "async_js_sr"
SR_DATABASE = rf"data\tmp\{SR}.queue.db"

# Initialize Audio Player
audioPlayer = AudioPlayer()
audioPlayer.setVolume(0.2)
audioPlayer.play(open(IMPORTS_SOUND, 'rb').read())

# Start Speech Recognition Process
SR_PROCESS = subprocess.Popen([f"{sys.executable}", f"modules/vocalize/{SR}.py"])
SR_QUEUE = SqlQueue(SR_DATABASE)

# Play post-import sound
audioPlayer.play(open(AFTER_IMPORTS_SOUND, 'rb').read())
audioPlayer.setVolume(1)

# Function to convert text to audio and print
def textToAudioPrint(*args, **kwargs):
    string = " ".join([str(x) for x in args])
    print(f"{string = }")
    
    historyDb.addMessage(
        role=Role.assistant.value,
        content=string
    )

    print(f"{string = }")
    audioPlayer.play(
        asyncio.run(
            textToSpeechBytes(string)
        ),
    )
    while audioPlayer.isPlaying() and kwargs.get('block', False):
        time.sleep(0.1)

# Async version of textToAudioPrint
async def asyncTextToAudioPrint(*args, **kwargs):
    string = " ".join([str(x) for x in args])
    print(f"{string = }")
    
    historyDb.addMessage(
        role=Role.assistant.value,
        content=string
    )

    print(f"{string = }")
    audioPlayer.play(await textToSpeechBytes(string))
    
    while audioPlayer.isPlaying() and kwargs.get('block', False):
        time.sleep(0.1)

# Function to vocalize input
def vocalizeInput(prompt: Optional[str] = "", ignoreThreshold: float = 0.3) -> str:
    if prompt:
        textToAudioPrint(prompt, block=True)
    SR_QUEUE.clear()
    
    # ignoreThreshold is the time to wait for the user to speak
    SR_QUEUE.get(timeout=ignoreThreshold)
    
    recordedAudio: str = SR_QUEUE.get()
    historyDb.addMessage(
        role=Role.user.value,
        content=recordedAudio
    )
    return recordedAudio

# Override print and input functions
codeBrew.print = textToAudioPrint
codeBrew.input = vocalizeInput

# Function to evaluate JFunctions asynchronously
async def jFunctionEval(jFunctions: list[JFunction]) -> list[str | None]:
    taskList = []
    for jFunction in jFunctions:
        taskList.append(asyncio.to_thread(jFunction.function))
    return await asyncio.gather(*taskList)

# Main async function
async def main():
    audioPlayer.play(await textToSpeechBytes("Jarvis Online!, Hello. How can I help you?"))
    while True:
        query = vocalizeInput()
        result = await process(query)
        dmm = result['dmm']
        edmm = result['edmm']
        ndmm = result['ndmm']
        timeTaken = result['timeTaken']
        
        print(f"""{dmm = }\n{edmm = }\n{ndmm = }\n{timeTaken = }""")

        await asyncio.gather(
            jFunctionEval(ndmm),
            jFunctionEval(edmm)
        )

        dmmResult = await jFunctionEval(dmm)
        strOnlyDmmResult = list(filter(lambda x: isinstance(x, str), dmmResult))
        if len(strOnlyDmmResult) == 0:
            continue
        await asyncTextToAudioPrint(*strOnlyDmmResult, block=True)

# Jarvis Class
class Jarvis:
    def __init__(self):
        print("Initializing Jarvis...")
        self.assistant = JarvisAssistant()
        self.conversation_handler = ConversationHandler(self.assistant)
        self.input_mode = "text"  # Default input mode is text

    def start(self):
        self.run_interactive_mode()

    def run_interactive_mode(self):
        print("\nJarvis is ready! Commands available:")
        print("- 'exit' to quit")
        print("- 'clear' to start a new conversation (preserves history)")
        print("- 'new' to start fresh (clears all history)")
        print("- 'switch input mode' to toggle between text and voice input")
        
        while True:
            try:
                if self.input_mode == "text":
                    user_input = input("\nYou: ").strip()
                else:
                    user_input = vocalizeInput()

                if user_input.lower() == 'exit':
                    print("Goodbye!")
                    break
                elif user_input.lower() == 'clear':
                    self.assistant.clear_history()
                    print("Started new conversation (previous conversations preserved).")
                    continue
                elif user_input.lower() == 'new':
                    self.assistant._history_manager.save_conversations([])
                    self.assistant._history_manager.load_or_create_conversation()
                    print("All conversation history cleared.")
                    continue
                elif user_input.lower() == 'switch input mode':
                    self.input_mode = "voice" if self.input_mode == "text" else "text"
                    print(f"Input mode switched to {self.input_mode}.")
                    continue
                if user_input:
                    response = self.process_command(user_input)
                    print("\nJarvis:", response)
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    def process_command(self, command: str):
        return self.conversation_handler.handle_conversation(command)

if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.start()
    asyncio.run(main())