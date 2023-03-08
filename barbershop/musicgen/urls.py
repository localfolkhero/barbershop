# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', MusicScoreListView.as_view(), name='score-list'),
    path('scores/create/', MusicScoreCreateView.as_view(), name='score-create'),
    path('scores/<pk>/', MusicScoreDetailView.as_view(), name='score-detail'),

    path('scores/<pk>/musicxml/', MusicScoreMusicXMLDownloadView.as_view(), name='score-musicxml'),
    path('scores/<pk>/midi/', MusicScoreMIDIDownloadView.as_view(), name='score-midi'),
]