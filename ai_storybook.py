import streamlit as st

# Title of the app
st.title("AI Storybook")

# Function to generate the AI story (example, replace with your own)
def generate_story():
    return "Once upon a time, in a land powered by AI, amazing stories were told..."

# Display a button for generating the story
if st.button("Generate Story"):
    story = generate_story()
    st.write(story)

# Button to display the source code
if st.button("Show Source Code"):
    source_code = '''
import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
import textwrap
import json

# Load environment variables from .env file
load_dotenv()

# Setup OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if not client.api_key:
    st.error("Please set your OpenAI key in the environment variable 'OPENAI_API_KEY'.")
    st.stop()

def generate_story(prompt):
    """
    Generates a short story based on the user prompt using GPT-3.5-turbo.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative storyteller. Create a very short story in 3 sentences."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,  # Reduced token count for shorter stories
            temperature=0.7
        )
        story = response.choices[0].message.content.strip()
        return story
    except Exception as e:
        st.error(f"An error occurred while generating the story: {e}")
        return None

def generate_image(prompt):
    """Create an Image based on the prompt using DALL-E"""
    try:
        response = client.images.generate(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        image_url = response.data[0].url
        return image_url
    except Exception as e:
        st.error(f"An error occurred while generating the image: {e}")
        return None

# Set the title of the app
st.title('A.I. StoryBook (Limited Version)')

# Input of User
st.header("Create your own short story.")
story_prompt = st.text_input("Enter your story prompt:")

if not story_prompt:
    st.warning('Please enter a story prompt to proceed.')
    st.stop()

# Generate the story
story = generate_story(story_prompt)
if story:
    st.subheader('Your Generated Short Story:')
    st.write(story)
else:
    st.stop()

# Split the story into sentences
sentences = story.split('.')[:3]  # Ensure we have at most 3 sentences

# Display each sentence with a generated image
for idx, sentence in enumerate(sentences):
    if sentence.strip():  # Check if the sentence is not empty
        st.write(f'### Part {idx + 1}')
        st.write(sentence.strip() + '.')

        # Generate image for the sentence
        image_url = generate_image(sentence)

        if image_url:
            st.image(image_url, caption=f"Image for Part {idx + 1}")
        else:
            st.write("Image could not be generated.")

def save_story(story, filename="saved_short_story.json"):
    """
    Save the story to a json file.
    """
    try:
        with open(filename, 'w') as f:
            json.dump({'story': story}, f)
        st.success(f"Story saved to {filename}")
    except IOError as e:
        st.error(f'An error occurred while saving the story: {e}')

if st.button('Save Story'):
    save_story(story)
'''

    st.code(source_code, language='python')

# Footer
st.write("Enjoy generating your own AI-powered stories! 🚀")
