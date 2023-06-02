from django.test import Client, TestCase

from .models import Bio, Education, Experience, Language, Project, Skill

# Create your tests here.


class BioModelTests(TestCase):
    def test_model_str_returns_name(self):
        new_bio = Bio(name='person')
        self.assertEqual(new_bio.__str__(), 'person')


class EducationModelTests(TestCase):
    def test_model_str_returns_award_discipline_institution(self):
        new_education = Education(
            award='BSc.', discipline='Economics', institution='UNILAG')
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



class ResumeViewTest(TestCase):

    def test_resume_view(self):
        response = self.client.get(reverse("resume:resume"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dowload Resume")
        self.assertTemplateUsed(response, 'resume/resume.html')

    def test_no_experiences(self):
        response = self.client.get(reverse("resume:resume"))
        self.assertContains(response, "No experience has been uploaded")
    
    def test_no_education(self):
        response = self.client.get(reverse("resume:resume"))
        self.assertContains(response, "No education has been uploaded")


class ProjectViewTest(TestCase):

    def test_projects_view(self):
        response = self.client.get(reverse("resume:projects"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resume/projects.html')