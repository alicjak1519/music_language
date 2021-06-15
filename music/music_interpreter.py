from typing import List

import pygame
from mingus.containers import MidiInstrument, Track, Bar, Composition
from mingus.midi import midi_file_out

from components.bar_list import BarList

TIMBRE_TO_NUMBER = {'FLute': 73, 'Piano': 0, 'Guitar': 24}


class MusicInterpreter:

    def __init__(self, bars_lists: List[BarList], timbre: str = 'Flute'):
        """
        MusicInterpreter class interprets lists of bars.
        :param bars_lists: single phrase of notes, each bar_list contains single melodic line
        """
        self.timbre = timbre
        self.bars_lists = bars_lists
        self.clock = pygame.time.Clock()

    def create_wave(self):
        instrument = MidiInstrument()
        instrument.instrument_nr = TIMBRE_TO_NUMBER[self.timbre]
        wave_composition = Composition()

        for bar_list in self.bars_lists:
            wave_track = Track(instrument)
            for bar in bar_list.bars:
                wave_bar = Bar(meter=bar.meter)
                for note in bar.notes:
                    wave_bar.place_notes(note.pitch, note.length)
                wave_track.add_bar(wave_bar)
            wave_composition.add_track(wave_track)
        midi_file_out.write_Composition('wololo.mid', wave_composition)
        self.clock.tick(30)

    def play_music_from_file(self, music_file):
        try:
            pygame.mixer.music.load(music_file)
        except pygame.error:
            print(f'File {music_file} not found! ({pygame.get_error()})')
            return
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            self.clock.tick(30)

    def play(self):
        self.create_wave()
        pygame.mixer.init()
        self.play_music_from_file('wololo.mid')
