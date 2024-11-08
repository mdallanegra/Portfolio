from django.shortcuts import render
from .utils import load_experience_data


def home(request):
    experience_data = load_experience_data()
    return render(request, 'home.html', {
        'pitch_resume_es_df': experience_data['pitch_resume_es_df'],
        'experience_resume_es_df': experience_data['experience_resume_es_df'],
        'projects_resume_es_df': experience_data['projects_resume_es_df'],
        'education_resume_es_df': experience_data['education_resume_es_df'],
        'skills_resume_es_df': experience_data['skills_resume_es_df'],
        'icons_resume_es_df': experience_data['icons_resume_es_df'],
        'interests_resume_es_df': experience_data['interests_resume_es_df'],
        'certifications_resume_es_df': experience_data['certifications_resume_es_df'],
        'OtherFactsOfInterests_resume_es_df': experience_data['OtherFactsOfInterests_resume_es_df'],
    })

def home_en(request):
    experience_data = load_experience_data()
    return render(request, 'home_en.html', {
        'pitch_resume_en_df': experience_data['pitch_resume_en_df'],
        'experience_resume_en_df': experience_data['experience_resume_en_df'],
        'projects_resume_en_df': experience_data['projects_resume_en_df'],
        'education_resume_en_df': experience_data['education_resume_en_df'],
        'skills_resume_en_df': experience_data['skills_resume_en_df'],
        'icons_resume_en_df': experience_data['icons_resume_en_df'],
        'interests_resume_en_df': experience_data['interests_resume_en_df'],
        'certifications_resume_en_df': experience_data['certifications_resume_en_df'],
        'OtherFactsOfInterests_resume_en_df': experience_data['OtherFactsOfInterests_resume_en_df'],
    })