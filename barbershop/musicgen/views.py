from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse

from .models import MusicScoreRecord, MusicScoreRating

from .generator import RandomMusicGenerator, ABCtoMusicConverter

# Create your views here.

class MusicScoreListView( ListView ):
    model = MusicScoreRecord
    ordering = "-id"
    
class MusicScoreDetailView( DetailView ):
    model = MusicScoreRecord    
    
    
class MusicScoreMusicXMLDownloadView( DetailView ):
    model = MusicScoreRecord
    
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        
        headers = {
            'Content-Type': 'application/xml',
            'Content-Disposition': f'attachment; filename={obj.name}.musicxml'
            }
        
        response = HttpResponse(
            headers=headers,
            content=obj.musicxml
        )
        return response
    
class MusicScoreMIDIDownloadView( DetailView ):
    model = MusicScoreRecord
    
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        
        headers = {
            'Content-Type': 'audio/midi',
            'Content-Disposition': f'attachment; filename={obj.name}.midi'
            }
        
        # Generate the MIDI file
        converter = ABCtoMusicConverter()
        midi_bytes = converter.generateMusicMIDIbytes( obj.abcnotation )
        
        response = HttpResponse(
            headers=headers,
            content=midi_bytes
        )
        return response
    
        
class MusicScoreCreateView( CreateView ):
    model = MusicScoreRecord
    fields = ()
    
    def get_success_url(self):
        return reverse_lazy("score-detail", kwargs={"pk": self.object.id})
    
    def form_valid(self, form):
        self.object = form.save(False)
        
        # Set the owner to whomever is logged in
        self.object.owner = self.request.user
        
        # Generate the ABCNotation
        generator = RandomMusicGenerator()
        abcmusic = generator.generateABC()
        # print(abcmusic)
        self.object.abcnotation = abcmusic
        self.object.name = generator.name
        self.object.slug = generator.name
        
        # Create the MusicXML version of the ABCNotation
        converter = ABCtoMusicConverter()
        musicxml = converter.generateMusicXML(abcmusic)
        # print(musicxml)
        self.object.musicxml = musicxml
        
        self.object.save()
        
        return super().form_valid(form)
    
# Method to handle ajax request to update a rating for a score
def update_rating(request, pk):
    rating = request.POST.get('rating', None)   
    
    # Any user who wants to rate something - we know the users by logged in user
    user = request.user
    score = MusicScoreRecord.objects.get(pk=pk)
    
    # Get existing score, or create a new one if there isn't one.
    score_rating, created = MusicScoreRating.objects.get_or_create(user=user, score=score)

    # Update and save.
    score_rating.rating = rating
    score_rating.save()
    
    # Return some value which might be helpful or useful. But not 100% required.
    data = {
        'value': rating,
        'created': created
    }
    
    return JsonResponse(data)
    