generate-video.pyimport os
import time
from google import genai
from google.genai import types

# Connect to Google's AI video service
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

prompt = """
A photorealistic cinematic vertical video of two fictional Black adult
men sitting together on a rooftop at night, looking at the enormous
star-filled sky and Milky Way.

They have a natural conversation about the vastness of space.

The first man says:
"Have you ever really thought about how big the universe is?"

The second man looks at the stars and replies:
"Yeah. What we see is only a tiny part of what could actually exist."

The first man says:
"Billions of galaxies... and every galaxy can contain billions of stars."

They look at the sky with genuine wonder.

Natural facial expressions, realistic lip synchronization,
natural hand gestures, realistic body movement and blinking.
Realistic human voices and ambient nighttime sounds.

Cinematic lighting, realistic skin texture, detailed environment,
documentary-style photography.

Vertical 9:16 composition for an Instagram Reel.
No subtitles. No text. No logos.
Both characters are fictional adults.
"""

# Generate the video
operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt=prompt,
    config=types.GenerateVideosConfig(
        aspect_ratio="9:16",
        resolution="720p"
    )
)

print("Video generation started...")

# Wait for the video
while not operation.done:
    time.sleep(10)
    operation = client.operations.get(operation)
    print("Still generating...")

# Save the video
video = operation.response.generated_videos[0].video

client.files.download(
    file=video,
    destination="space_conversation.mp4"
)

print("DONE!")
print("Video saved as space_conversation.mp4")
