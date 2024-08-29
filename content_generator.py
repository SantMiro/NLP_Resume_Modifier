from openai import OpenAI
import os

API_KEY = os.getenv('OPENAI_API_KEY')

def rewrite_job_description(job_requirements):
    prompt = f'''The current user experience consists on these five bullet points:
                    1. Led the design and optimization of trigger software for the P-ONE detector, 
                    boosting detection capabilities by 25% and improving system precision.
                    2. Leveraged Python and SQL to streamline data processing workflows, 
                    reducing processing time by 40% and achieving a notable 90% efficiency rate.
                    3. Coordinated and communicated technical advancements to international stakeholders, 
                    resulting in a 30% increase in collaborative initiatives.
                    4. Harnessed machine learning and advanced statistical models to validate experimental data, 
                    achieving 95% accuracy in results.
                    5. Directed a data visualization project, 
                    reducing stakeholder decision-making time by 50% through effective transformation of complex datasets.
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

