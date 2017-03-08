#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.dont_write_bytecode = True

import random
from data.dataLoader import *
from data.musicData import *
from models.unigramModel import *
from models.bigramModel import *
from models.trigramModel import *

###############################################################################
# Helpers
###############################################################################

def sentenceTooLong(desiredLength, currentLength):
    """
    Requires: nothing
    Modifies: nothing
    Effects:  returns a bool indicating whether or not this sentence should
              be ended based on its length. This function has been done for
              you.
    """
    STDEV = 1
    val = random.gauss(currentLength, STDEV)
    return val > desiredLength

def printSongLyrics(verseOne, verseTwo, chorus):
    """
    Requires: verseOne, verseTwo, and chorus are lists of lists of strings
    Modifies: nothing
    Effects:  prints the song. This function is done for you.
    """
    verses = [verseOne, chorus, verseTwo, chorus]
    print
    for verse in verses:
        for line in verse:
            print (' '.join(line)).capitalize()
        print

###############################################################################
# Core
###############################################################################

def trainModels(dataDirectory):
    """
    Requires: nothing
    Modifies: nothing
    Effects:  loads data from the data/lyrics/<lyricsDirectory> folder
              using the pre-written DataLoader class, then creates an
              instance of each of the NGramModel child classes and trains
              them using the text loaded from the data loader. The list
              should be in tri-, then bi-, then unigramModel order.

              Returns the list of trained models.
    """
    models = [TrigramModel(), BigramModel(), UnigramModel()]
    for lyricdir in LYRICSDIRS:
        lyrics = dataLoader.loadLyrics(lyricdir)
        for model in models:
            model.trainModel(lyrics)
    return models

def selectNGramModel(models, sentence):
    """
    Requires: models is a list of NGramModel objects sorted by descending
              priority: tri-, then bi-, then unigrams.
    Modifies: nothing
    Effects:  returns the best possible model that can be used for the
              current sentence based on the n-grams that the models know.
              (Remember that you wrote a function that checks if a model can
              be used to pick a word for a sentence!)
    """
    pass

def generateSentence(models, desiredLength):
    """
    Requires: models is a list of trained NGramModel objects sorted by
              descending priority: tri-, then bi-, then unigrams.
              desiredLength is the desired length of the sentence.
    Modifies: nothing
    Effects:  returns a list of strings where each string is a word in the
              generated sentence. The returned list should NOT include
              any of the special starting or ending symbols.

              For more details about generating a sentence using the
              NGramModels, see the spec.
    """
    sentence = ['^::^', '^:::^']
    pass

def runGenerator(models):
    """
    Requires: models is a list of a trained models
    Modifies: nothing
    Effects:  generates a song using models
    """
    pass

###############################################################################
# Reach
###############################################################################

PROMPT = """
(1) Generate song lyrics by The Beatles
(2) Generate a song using data from Nintendo Gamecube
(3) Quit the music generator
> """
TEAM = '[NAME HERE]'
LYRICSDIRS = ['the_beatles']
MUSICDIRS = ['gamecube']
WAVDIR = 'wav/'

def main():
    """
    Requires: Nothing
    Modifies: Nothing
    Effects:  This is your main function, which is done for you. It runs the
              entire generator program for both the reach and the core.

              It prompts the user to choose to generate either lyrics or music.
    """

    # TODO only load when requested
    # print 'Starting program and loading data...'
    # lyricsModels = trainLyricsModels(lyricsDirectory)
    # musicModels = trainMusicModels(musicDirectory)
    # print 'Data successfully loaded\n'

    print 'Welcome to the ', TEAM, ' music generator!'
    while True:
        try:
            userInput = int(raw_input(PROMPT))
            if userInput == 1:
                # runLyricsGenerator(lyricsModels)
                print("Under construction")
            elif userInput == 2:
                print("Under construction")
                # songName = raw_input('What would you like to name your song? ')
                # runMusicGenerator(musicModels, WAVDIR + songName + '.wav')
            elif userInput == 3:
                print 'Thank you for using the ', TEAM, ' music generator!'
                sys.exit()
            else:
                print("Invalid option!")
        except ValueError:
            print("Please enter a number")

if __name__ == '__main__':
    main()
    # note that if you want to individually test functions from this file,
    # you can comment out main() and call those functions here. Just make
    # sure to call main() in your final submission of the project!
