from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from model_bakery import baker

from .models import Bio, Education, Experience, Language, Project, Skill
from .views import projects, resume

# Create your tests here.


class BioModelTests(TestCase):
    def test_model_str_returns_name(self):
        new_bio = Bio(name='person')
        self.assertEqual(new_bio.__str__(), 'person')


class EducationModelTests(TestCase):
    def test_model_str_returns_award_discipline_institution(self):
        new_education = Education(
            award='BSc.', course='Economics', institution='UNILAG')
        self.assertEqual(new_education.__str__(), 'BSc. Economics from UNILAG')


class ExperienceModelTests(TestCase):
    def test_model_str_returns_position_company(self):
        new_experience = Experience(position='Developer', company='Freelance')
        self.assertEqual(new_experience.__str__(), 'Developer at Freelance')


class LanguageModelTests(TestCase):
    def test_model_str_returns_name(self):
        new_language = Language(name='python')
        self.assertEqual(new_language.__str__(), 'python')


class ProjectModelTests(TestCase):
    def test_model_str_returns_name(self):
        new_project = Project(name='tracker')
        self.assertEqual(new_project.__str__(), 'tracker')


class SkillModelTests(TestCase):
    def test_model_str_returns_name(self):
        new_skill = Skill(name='Communication')
        self.assertEqual(new_skill.__str__(), 'Communication')


class EmptyResumeViewTest(TestCase):
    def test_no_experiences(self):
        response = self.client.get(reverse("resume"))
        self.assertContains(response, "No experience has been uploaded")
    
    def test_no_education(self):
        response = self.client.get(reverse("resume"))
        self.assertContains(response, "No education has been uploaded")


class ProjectsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create some test projects
        self.project1 = baker.make(
            Project, name='Project 1', description='Description 1')
        self.project2 = baker.make(
            Project, name='Project 2', description='Description 2')

    def test_projects_view(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('resume/projects.html')
        self.assertQuerysetEqual(
            response.context['projects'], 
            [(self.project1), (self.project2)], 
            ordered=False)


class ResumeViewTest(TestCase):
    def setUp(self):
        # Create some test experiences
        self.experience1 = baker.make(Experience)
        self.experience2 = baker.make(Experience)
        # Create some test education entries
        self.education1 = baker.make(Education)
        self.education2 = baker.make(Education)
        # Create some test skills
        self.skill1 = baker.make(Skill)
        self.skill2 = baker.make(Skill)
        # Create some test languages
        self.language1 = baker.make(Language)
        self.language2 = baker.make(Language)

    def test_resume_view(self):
        response = self.client.get(reverse('resume'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resume/resume.html')
        self.assertQuerysetEqual(
            response.context['experiences'], 
            [(self.experience1), (self.experience2)], 
            ordered=False)
        self.assertQuerysetEqual(
            response.context['education_list'], 
            [(self.education1), (self.education2)], 
            ordered=False)
        self.assertQuerysetEqual(
            response.context['skill'], 
            [(self.skill1), (self.skill2)], 
            ordered=False)
        self.assertQuerysetEqual(
            response.context['languages'], 
            [(self.language1), (self.language2)], 
            ordered=False)
