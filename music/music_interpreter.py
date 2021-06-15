from typing import List

import pygame
from mingus.containers import MidiInstrument, Track, Bar, Composition
from mingus.midi import midi_file_out

from components.bar_list import BarList
from music.timbre_to_num import timbre_to_num


class MusicInterpreter:
    def __init__(self, bars_lists: List[BarList]):
        """
        MusicInterpreter class interprets lists of bars.
        :param bars_lists: single phrase of notes, each bar_list contains single melodic line
        """
        self.timbre = 'Flute'
        self.bars_lists = bars_lists

    def create_wave(self):
        instrument = MidiInstrument()
        instrument.instrument_nr = timbre_to_num(self.timbre)
        wave_composition = Composition()
        for bar_list in self.bars_lists:
            wave_track = Track(instrument)
            for bar in bar_list.bars:
                wave_bar = Bar(meter=bar.meter)
                for note in bar.notes:
                    wave_bar.place_notes(note.pitch, note.length)
                wave_track.add_bar(wave_bar)
            wave_composition.add_track(wave_track)
        midi_file_out.write_Composition("test.mid", wave_composition)

    @staticmethod
    def play_music_from_file(music_file):
        clock = pygame.time.Clock()
        try:
            pygame.mixer.music.load(music_file)
            print("Music file %s loaded!" % music_file)
        except pygame.error:
            print("File %s not found! (%s)" % (music_file, pygame.get_error()))
            return
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            clock.tick(30)

    def play(self):
        self.create_wave()
        pygame.mixer.init()
        self.play_music_from_file('test.mid')
