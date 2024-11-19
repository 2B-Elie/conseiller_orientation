from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from google.cloud import dialogflow
import uuid

class IndexView(TemplateView):
    template_name = 'orientation/index.html'

class BlogView(TemplateView):
    template_name = 'orientation/blog.html'

class AboutView(TemplateView):
    template_name = 'orientation/about.html'

class VirtualAdvisorView(TemplateView):
    template_name = 'orientation/virtual_advisor.html'

def detect_intent(request):
    user_text = request.GET.get('user_text', '')
    project_id = "elevated-codex-431816-b0"  # Remplace par ton Project ID Google Cloud
    session_client = dialogflow.SessionsClient()
    session_id = str(uuid.uuid4())  # Génère une session ID unique
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=user_text, language_code="fr")
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(request={"session": session, "query_input": query_input})

    return JsonResponse({"response": response.query_result.fulfillment_text})


def prompt(request):
    welcom_message = """
                Bonjour, je suis Mme Ruth, votre conseillère d'orientation virtuelle, je suis 
                disponible pour échanger avec vous et vous aider à répondre 
                à toutes vos préoccupations éducatives ou professionnelles
            """
    return render(request, "orientation/chatgpt.html", locals())