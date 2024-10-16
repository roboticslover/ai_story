import streamlit as st
from openai import OpenAI
import textwrap
import json

st.header(Source-Code)
st.write(import streamlit as st
from openai import OpenAI
import textwrap
import json

# Initialize OpenAI client with the API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

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
            max_tokens=100,
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
    save_story(story))


# Initialize OpenAI client with the API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

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
            max_tokens=100,
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
