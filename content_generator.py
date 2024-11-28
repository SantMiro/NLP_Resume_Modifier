from openai import OpenAI
import os

API_KEY = os.getenv('OPENAI_API_KEY')

def rewrite_job_description(job_requirements):
    prompt = f'''The current user experience consists on these five bullet points:
                    1. Led the design and implementation of a Retrieval-Augmented Generation (RAG) model to enhance document interpretation and response generation at scale.
                    2. Developed and deployed deep learning models (LSTM, Transformer), achieving a 15% improvement in prediction accuracy for faster decision-making.
                    3. Optimized pre-trained LLMs for complex text analysis and RAG response generation, enhancing keyword detection and response accuracy.
                    4. Leveraged AWS services (EC2, S3, Lambda) for scalable, reliable model deployment, ensuring 99.9% uptime and efficient handling of large datasets.
                    5. Implemented end-to-end MLOps CI/CD pipelines using Jenkins and Docker, reducing model update times by 30%.
                The user will provide the requirements of a new job opportunity.
                You will have to rewrite the five user experience bullet points so that they match the requirements of the job opportunity.
                Most importantly the bullets should begin with a verb and contain a measurable quantity.
                Try to keep as much as you can from the original bullet points whilst including most of the job requirements. 
                You must not exceed five bullet points in your answer.
                Return the response as individual sentences. Do not add the numbers of each bullet.

            '''

    client = OpenAI(api_key=API_KEY)
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": prompt},
        {
            "role": "user", "content": f"This are the requirements for the job opportunity: {job_requirements}."
        }
    ]
)
    return completion.choices[0].message.content

