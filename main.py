import re
from content_generator import rewrite_job_description

def generated_sentences(job_description):
    # Ensure each job description is rewritten by OpenAI's API
    updated_resume_string = rewrite_job_description(job_description)
    
    updated_resume_string = updated_resume_string.replace('%', r'\%')

    # Split updated resume string into sentences
    sentences = [sentence.strip() for sentence in updated_resume_string.split('. ') if sentence]
    # If the sentences end with a period, make sure to add it back
    sentences = [sentence + '.' if not sentence.endswith('.') else sentence for sentence in sentences]

    return sentences


def update_experience(latex_file, job_description):
    
    # Read the LaTeX file content
    with open(latex_file, 'r', encoding='utf-8') as file:
        content = file.read()


        # Extract the experience section using regex
    sentences = generated_sentences(job_description)
    #print(sentences)
    experience_section_pattern = re.compile(r'\\textbf\{Machine Learning Engineer\}.*?\\end\{itemize\}', re.DOTALL)
    experience_section_match = experience_section_pattern.search(content)

    experience_section = experience_section_match.group(0)  # The full section

    # Extract the resume items
    resume_item_pattern = re.compile(r'\\item\s*(.+?)(?=\n|\\item|$)', re.DOTALL)  # More robust regex for whitespace handling
    current_resume_items = resume_item_pattern.findall(experience_section)
    #print(current_resume_items)
    # Replace the first 5 items with the new sentences
    for i, item in enumerate(current_resume_items[:5]):
        experience_section = experience_section.replace(item, sentences[i], 1)

    # Replace the old experience section with the updated one
    content = content.replace(experience_section_match.group(0), experience_section)


    # Save the updated LaTeX document
    with open('test_resume.tex', 'w', encoding='utf-8') as updated_file:
        updated_file.write(content)


latex_file = './Santiago_Miro_resume.tex'
job_description = '''
3-5 years hands-on experience working on AWS technologies for data processing and analytics

 3+ years experience with AWS Glue for ETL, Glue Catalog, Glue Data Quality, AWS Step Functions, AWS Lambda, AWS Athena

Experience in AWS CLI, Identity & Access Management (IAM) and BI Tools like Tableau and Quicksight is a definite plus.

3 years experience in Python, Pyspark and SQL

Demonstrated experience in performance tuning of Spark jobs

5 years hands-on experience with relational database systems, relational models, dimensional models, and analytical models

3-5 years experience with engineering data products as input to various analytical models

3-5 years building feedback loops between model deployment and its data – i.e. tune & tweak data products to achieve scale, optimization, etc.

Sound understanding of Data Management principles (data warehousing, data quality, master data management, etc.) and Data Governance principles. Sound understanding of data modelling and a passion for analytics

Proven ability to leverage knowledge of data engineering to extract, conform and integrate a variety of operational data sources into production-grade data products

Experience of popular data formats like Parquet, Iceberg is a definite plus.

Excellent verbal and written communication skills; have executive presence and proven ability to partner with Data Scientists to articulate insights gleaned from the model and the underlying data
Understand and Embrace Agile Operating Model 

Proven Experienced working as Product Owner in Scrum or Service Request Manager in Kanban projects

Experience working in a large financial services organization

Knowledge of fundamental statistical models & techniques
'''

update_experience(latex_file, job_description)
