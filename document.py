import argparse
from openai import OpenAI
import os

client = OpenAI()

def load_transcript(transcript_file):
    with open(transcript_file, 'r') as file:
        return file.read()

def generate_document(transcript, system_prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("The environment variable OPENAI_API_KEY is not set.")
    
    

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": transcript}
        ]
    )

    return response.choices[0].message.content

def main():
    parser = argparse.ArgumentParser(description="Generate a meeting summary from a transcript using GPT-4")
    parser.add_argument("transcript_file", type=str, help="Path to the transcript text file")
    parser.add_argument("output_file", type=str, help="Path to the output Markdown file")

    args = parser.parse_args()

    system_prompt = """
You are an AI assistant specialized in summarizing and analyzing meeting transcripts. Given the transcript below, please generate a markdown formatted document that includes the following sections:

1. **Meeting Summary**: A brief summary of the purpose of the meeting.
  - this should include the date, time, and participants involved.
    - if this can not be determined from the transcript, please use a placeholder.
  - this should also include the main topics discussed during the meeting.
  - this should also include any key decisions made during the meeting.
2. **Topics Discussed**: A detailed outline of the main topics spoken about during the meeting, including specific details about each topic.
3. **Key Products and Features**: A comprehensive description of the key products mentioned, including detailed information about each product and its features.
  - This section should be broken down into subsection for each project/product discussed.
  - Each section should include a brief overview of the product, its features, and any relevant details.
  - Each section should also include any action items or tasks related to the product. This should use markdown checkboxes to indicate completion.
  - Each section should include any deadlines or milestones related to the product.
  - Each section should include a subsection for features discussed, include a brief description of each feature.
  - If no products are mentioned, please skip this section
4. **Action Points**: List the action points or tasks assigned during the meeting.
  - This should include the responsible person, the task description, and the deadline.
    - Use markdown checkboxes to indicate completion.
5. **Meeting Evaluation**: Provide your opinion on the meeting's efficiency, usefulness, and the quality of communication among participants.
    - This should include any suggestions for improvement or follow-up actions.
    - This should also include any positive aspects of the meeting that should be highlighted.

Please ensure that each section is clearly labeled and well-structured in markdown format.
"""

    transcript = load_transcript(args.transcript_file)
    document = generate_document(transcript, system_prompt)

    with open(args.output_file, 'w') as file:
        file.write(document)

    print(f"Document saved to {args.output_file}")

if __name__ == "__main__":
    main()
