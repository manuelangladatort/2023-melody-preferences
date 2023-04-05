from flask import Markup

from dominate import tags

from psynet.modular_page import ModularPage, AudioPrompt
from psynet.timeline import CodeBlock, PageMaker, join, Event, Module

from psynet.js_synth import JSSynth, Note, HarmonicTimbre
from .melodies import convert_interval_sequence_to_absolute_pitches, sample_reference_pitch, sample_interval_sequence


def volume_calibration(timbre, note_duration, note_silence, time_estimate_per_trial=5):
    return ModularPage(
                "tone_js_volume_test",
                JSSynth(
                    Markup(
                        """
                        <h3>Volume calibration</h3>
                        <hr>
                        Set the volume in your laptop to a level in which you can hear each note properly.
                        <hr>
                        """
                    ),
                    sequence=[
                        Note(x)
                        for x in convert_interval_sequence_to_absolute_pitches(
                            intervals=sample_interval_sequence(
                                n_int=99,
                                max_interval_size=8.5,
                                max_melody_pitch_range=99,
                                discrete=False,
                                reference_mode="first_note",
                            ),
                            reference_pitch=sample_reference_pitch(55, 2.5),
                            reference_mode="first_note",
                        )
                    ],
                    timbre=timbre,
                    default_duration=note_duration,
                    default_silence=note_silence,
                ),
                time_estimate=time_estimate_per_trial
                )


def volume_calibration_page(audio, min_time=5, time_estimate=5.0):
    text = tags.div()
    with text:
        tags.p(
            """
            Please listen to the following melody and adjust your
            computer's output volume until it is at a comfortable level.
            """
        )
        tags.p(
            """
            If you can't hear anything, there may be a problem with your
            playback configuration or your internet connection.
            You can refresh the page to try loading the audio again.
            """
        )

    return ModularPage(
        "volume_calibration",
        AudioPrompt(audio, text, loop=True),
        events={
            "submitEnable": Event(is_triggered_by="trialStart", delay=min_time),
        },
        time_estimate=time_estimate,
    )
