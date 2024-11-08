import pandas as pd
from django.conf import settings
import os


def load_experience_data():
    file_path_en = os.path.join(settings.BASE_DIR, 'main', 'static',
                             'texts', 'resume_texts_en.xlsx')
    print("File path:", file_path_en)

    file_path_es = os.path.join(settings.BASE_DIR, 'main', 'static',
                             'texts', 'resume_texts_es.xlsx')
    print("File path:", file_path_es)

    pitch_resume_en_df = pd.read_excel(file_path_en, sheet_name='Pitch')
    pitch_resume_en_df = pitch_resume_en_df.iloc[0, 0]
    pitch_resume_es_df = pd.read_excel(file_path_es, sheet_name='Pitch')
    pitch_resume_es_df = pitch_resume_es_df.iloc[0, 0]

    experience_resume_en_df = pd.read_excel(file_path_en, sheet_name='Experience')
    experience_resume_en_df.columns = ['JobTitle', 'Company', 'JobDescription', 'Date']
    experience_resume_en_df = experience_resume_en_df.to_dict(orient='records')

    experience_resume_es_df = pd.read_excel(file_path_es, sheet_name='Experience')
    experience_resume_es_df.columns = ['JobTitle', 'Company', 'JobDescription', 'Date']
    experience_resume_es_df = experience_resume_es_df.to_dict(orient='records')

    projects_resume_en_df = pd.read_excel(file_path_en, sheet_name='Projects')
    projects_resume_en_df.columns = ['Name', 'Title', 'Role', 'Summary', 'Responsibilities', 'WebPage','GitHub','Image','Date']
    projects_resume_en_df = projects_resume_en_df.to_dict(orient='records')

    projects_resume_es_df = pd.read_excel(file_path_es, sheet_name='Projects')
    projects_resume_es_df.columns = ['Name', 'Title', 'Rol', 'Resumen', 'Responsabilidades', 'WebPage','GitHub','Image','Date']
    projects_resume_es_df = projects_resume_es_df.to_dict(orient='records')
    
    education_resume_en_df = pd.read_excel(file_path_en, sheet_name='Education')
    education_resume_en_df.columns = ['Degree', 'Completion', 'Institute', 'Date']
    education_resume_en_df = education_resume_en_df.to_dict(orient='records')

    education_resume_es_df = pd.read_excel(file_path_es, sheet_name='Education')
    education_resume_es_df.columns = ['Degree', 'Completion', 'Institute', 'Date']
    education_resume_es_df = education_resume_es_df.to_dict(orient='records')

    skills_resume_en_df = pd.read_excel(file_path_en, sheet_name='Skills')
    skills_resume_en_df.columns = ['ComputerKnowledge', 'LanguageKnowledge']
    skills_resume_en_df = skills_resume_en_df.to_dict(orient='records')

    skills_resume_es_df = pd.read_excel(file_path_es, sheet_name='Skills')
    skills_resume_es_df.columns = ['ComputerKnowledge', 'LanguageKnowledge']
    skills_resume_es_df = skills_resume_es_df.to_dict(orient='records')

    icons_resume_en_df = pd.read_excel(file_path_en, sheet_name='Icons')
    icons_resume_en_df.columns = ['Icons']
    icons_resume_en_df = icons_resume_en_df.to_dict(orient='records')

    icons_resume_es_df = pd.read_excel(file_path_es, sheet_name='Icons')
    icons_resume_es_df.columns = ['Icons']
    icons_resume_es_df = icons_resume_es_df.to_dict(orient='records')

    interests_resume_en_df = pd.read_excel(file_path_en, sheet_name='Interests')
    interests_resume_en_df = interests_resume_en_df.iloc[0, 0]

    interests_resume_es_df = pd.read_excel(file_path_es, sheet_name='Interests')
    interests_resume_es_df = interests_resume_es_df.iloc[0, 0]

    certifications_resume_en_df = pd.read_excel(file_path_en, sheet_name='Certifications')
    certifications_resume_en_df.columns = ['Certifications', 'Institute', 'Link', 'Date']
    certifications_resume_en_df['Link'] = certifications_resume_en_df['Link'].fillna('')
    certifications_resume_en_df = certifications_resume_en_df.to_dict(orient='records')

    certifications_resume_es_df = pd.read_excel(file_path_es, sheet_name='Certifications')
    certifications_resume_es_df.columns = ['Certifications', 'Institute', 'Link', 'Date']
    certifications_resume_es_df['Link'] = certifications_resume_es_df['Link'].fillna('')
    certifications_resume_es_df = certifications_resume_es_df.to_dict(orient='records')

    OtherFactsOfInterests_resume_en_df = pd.read_excel(file_path_en, sheet_name='OtherFactsOfInterests')
    OtherFactsOfInterests_resume_en_df.columns = ['OtherFactsOfInterests']
    OtherFactsOfInterests_resume_en_df = OtherFactsOfInterests_resume_en_df.to_dict(orient='records')

    OtherFactsOfInterests_resume_es_df = pd.read_excel(file_path_es, sheet_name='OtherFactsOfInterests')
    OtherFactsOfInterests_resume_es_df.columns = ['OtherFactsOfInterests']
    OtherFactsOfInterests_resume_es_df = OtherFactsOfInterests_resume_es_df.to_dict(orient='records')

    return {
        'pitch_resume_en_df': pitch_resume_en_df,
        'pitch_resume_es_df': pitch_resume_es_df,
        'experience_resume_en_df': experience_resume_en_df,
        'experience_resume_es_df': experience_resume_es_df,
        'projects_resume_en_df': projects_resume_en_df,
        'projects_resume_es_df': projects_resume_es_df,
        'education_resume_en_df': education_resume_en_df,
        'education_resume_es_df': education_resume_es_df,
        'skills_resume_en_df': skills_resume_en_df,
        'skills_resume_es_df': skills_resume_es_df,
        'icons_resume_en_df': icons_resume_en_df,
        'icons_resume_es_df': icons_resume_es_df,
        'interests_resume_en_df': interests_resume_en_df,
        'interests_resume_es_df': interests_resume_es_df,
        'certifications_resume_en_df': certifications_resume_en_df,
        'certifications_resume_es_df': certifications_resume_es_df,
        'OtherFactsOfInterests_resume_en_df': OtherFactsOfInterests_resume_en_df,
        'OtherFactsOfInterests_resume_es_df': OtherFactsOfInterests_resume_es_df,
    }