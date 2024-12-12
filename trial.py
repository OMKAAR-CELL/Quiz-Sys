import pandas as pd
id='Geography'
# Load the CSV file
df = pd.read_csv('question_content.csv')
section_question=df[df['Subject']==id]
print(section_question.sample(10).reset_index(drop=True))
