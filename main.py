import re
from content_generator import rewrite_job_description



def update_experience(latex_file, job_description):
    
    # Read the LaTeX file content
    with open(latex_file, 'r', encoding='utf-8') as file:
        content = file.read()


    # Extract the experience section using regex
    experience_section_pattern = re.compile(r'\\section\{\\textbf\{Experience\}\}(.+?)\\resumeSubHeadingListEnd', re.DOTALL)
    experience_section_match = experience_section_pattern.search(content)
    # Extract the experience section content
    experience_section = experience_section_match.group(1)
    # Extract resume items within the experience section
    resume_item_pattern = re.compile(r'\\resumeItem\{(.+?)\}', re.DOTALL)
    current_resume_items = resume_item_pattern.findall(experience_section)

    # Rewrite each resume item using OpenAI's API
    updated_resume_string = rewrite_job_description(job_description)
    updated_resume_string = updated_resume_string.replace('%',r'\%')
    sentences = [sentence.strip() for sentence in updated_resume_string.split('. ') if sentence]
    # If the sentences end with a period, make sure to add it back
    sentences = [sentence + '.' if not sentence.endswith('.') else sentence for sentence in sentences]
    
    for i, item in enumerate(current_resume_items):
            experience_section = experience_section.replace(item, sentences[i], 1)

        # Replace the old experience section in the document with the updated one
    content = content.replace(experience_section_match.group(1), experience_section)

    # Save the updated LaTeX document
    with open('updated_resume.tex', 'w', encoding='utf-8') as updated_file:
        updated_file.write(content)


latex_file = './resume_Santiago_Miro.tex'
job_description = '''Deep understanding and practical experience with NLP techniques and frameworks, including training and inference of large language models.

Deep understanding of any of retrieval, ranking, reinforcement learning, and agent-based systems and experience in how to build them for large systems.

Proficiency in Python and experience with ML libraries such as TensorFlow or PyTorch.

Excellent skills in data processing (SQL, ETL, data warehousing) and experience working with large-scale data systems.

Experience with machine learning model lifecycle management tools, and an understanding of MLOps principles and best practices.

Familiarity with cloud platforms like GCP or Azure.

Familiarity with the latest industry and academic trends in machine learning and AI, and the ability to apply this knowledge to practical projects.

Good understanding of software development principles, data structures, and algorithms.

Excellent problem-solving skills, attention to detail, and a strong capacity for logical thinking.

The ability to work collaboratively in an extremely fast-paced, startup environment.
'''

update_experience(latex_file, job_description)
